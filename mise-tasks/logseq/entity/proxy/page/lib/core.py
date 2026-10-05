"""Plan and safely apply page proxy imports (standard library only)."""
from __future__ import annotations

import base64
from dataclasses import dataclass, field
from datetime import datetime
import fcntl
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
from urllib.parse import parse_qs, quote, unquote, urlparse
from zoneinfo import ZoneInfo

PROXY_KEYS = ('logseq-proxy-url', 'logseq-proxy-codeforge-url', 'logseq-proxy-last-sync-date')
TRANSACTION = '.logseq-proxy-transaction'
PROPERTY = re.compile(r'^([^\s:]+):: (.*?)(?:\r?\n)?$')


class SyncError(ValueError):
    """A conflict or unsafe import; no writes should be made."""


@dataclass
class Plan:
    source_root: Path
    destination_root: Path
    page: str
    writes: dict[str, bytes] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    expected: dict[str, bytes | None] = field(default_factory=dict)
    modes: dict[str, int] = field(default_factory=dict)
    pages: set[str] = field(default_factory=set)
    codeforge_url: str | None = None
    expected_modes: dict[str, int | None] = field(default_factory=dict)
    source_expected: dict[Path, bytes] = field(default_factory=dict)
    source_modes: dict[Path, int] = field(default_factory=dict)


def safe_path(root: Path, relative: str) -> Path:
    """Reject traversal and symlinks, including ancestor directories."""
    part = PurePosixPath(relative)
    if not relative or part.is_absolute() or '..' in part.parts or '\\' in relative or '\x00' in relative:
        raise SyncError(f'Unsafe relative path: {relative}')
    root = Path(root).absolute()
    for parent in (root, *root.parents):
        if parent.is_symlink():
            raise SyncError(f'Symlink path: {parent}')
    result = root.joinpath(*part.parts)
    current = root
    for component in part.parts:
        current = current / component
        if current.is_symlink():
            raise SyncError(f'Symlink path: {current}')
    if result.exists() and not result.is_file():
        raise SyncError(f'Expected a regular file: {result}')
    return result


def validate_graph(root: Path) -> Path:
    root = Path(root).absolute()
    # macOS standard temporary directories are system aliases.
    if sys.platform == 'darwin' and root.parts[1:2] in (('tmp',), ('var',)):
        root = Path('/private').joinpath(*root.parts[1:])
    safe_path(root, 'pages/.proxy-validation')
    if not (root / 'pages').is_dir() or not (root / 'logseq').is_dir():
        raise SyncError(f'Graph must contain pages/ and logseq/: {root}')
    return root


def property_lines(text: str) -> tuple[list[str], str]:
    lines = text.splitlines(keepends=True)
    stop = 0
    while stop < len(lines) and PROPERTY.match(lines[stop]):
        stop += 1
    return lines[:stop], ''.join(lines[stop:])


def parse_properties(text: str) -> tuple[dict[str, str], str]:
    lines, body = property_lines(text)
    props = {}
    for line in lines:
        match = PROPERTY.match(line)
        key, value = match.groups()
        if key in props:
            raise SyncError(f'Duplicate property: {key}')
        props[key] = value
    return props, body


def page_filename(page: str) -> str:
    if not page or page.startswith('/') or any(x in ('', '.', '..') for x in page.split('/')) or '\\' in page:
        raise SyncError(f'Unsafe page name: {page}')
    return quote(page.replace('/', '___'), safe=' _-.,()[]') + '.md'


def resolve_page(root: Path, page: str) -> Path:
    encoded = page_filename(page)
    raw = page.replace('/', '___') + '.md'
    candidates = {safe_path(root, 'pages/' + name) for name in (encoded, raw)}
    # Logseq escapes reserved punctuation but leaves common Unicode names readable.
    for p in (Path(root) / 'pages').glob('*.md'):
        if unquote(p.stem).replace('___', '/') == page:
            safe_path(root, str(p.relative_to(root)))
            candidates.add(p)
    existing = [p for p in candidates if p.exists()]
    if len(existing) > 1:
        raise SyncError(f'Ambiguous page filename for {page}: {existing}')
    return existing[0] if existing else safe_path(root, 'pages/' + encoded)


def graph_url(root: Path, page: str) -> str:
    return f'logseq://graph/{quote(root.name, safe="")}?page={quote(page, safe="")}'


def proxy_identity(url: str) -> tuple[str, str]:
    parsed = urlparse(url)
    values = parse_qs(parsed.query)
    if parsed.scheme != 'logseq' or parsed.netloc != 'graph' or len(values.get('page', [])) != 1:
        raise SyncError(f'Invalid proxy URL: {url}')
    return unquote(parsed.path.lstrip('/')), values['page'][0]


def run_local(*args: str, cwd: Path | None = None) -> str:
    try:
        return subprocess.check_output(args, cwd=cwd, text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return ''


def infer_codeforge(root: Path, source: Path) -> str | None:
    repo = run_local('git', 'rev-parse', '--show-toplevel', cwd=root)
    remote = run_local('git', 'remote', 'get-url', 'origin', cwd=root)
    if not repo or not remote:
        return None
    if remote.startswith('git@'):
        remote = 'https://' + remote[4:].replace(':', '/', 1)
    elif remote.startswith('ssh://'):
        p = urlparse(remote)
        remote = 'https://' + (p.hostname or '') + p.path
    parsed_remote = urlparse(remote)
    if parsed_remote.scheme != 'https' or not parsed_remote.netloc:
        return None
    remote = parsed_remote._replace(
        netloc=parsed_remote.netloc.rsplit('@', 1)[-1], query='', fragment=''
    ).geturl().removesuffix('.git').rstrip('/')
    branch = run_local('git', 'symbolic-ref', '--short', 'refs/remotes/origin/HEAD', cwd=root).removeprefix('origin/') or 'main'
    relative = source.relative_to(Path(repo))
    marker = '/-/blob/' if 'gitlab' in urlparse(remote).netloc else '/blob/'
    return remote + marker + quote(branch, safe='') + '/' + quote(relative.as_posix(), safe='/')


def validate_codeforge(url: str, root: Path, source: Path) -> None:
    parsed = urlparse(url)
    if parsed.username is not None or parsed.password is not None:
        raise SyncError('Code forge URLs must omit embedded credentials')
    parts = parsed.path.split('/')
    if parsed.scheme != 'https' or not parsed.netloc or 'blob' not in parts or unquote(parts[-1]) != source.name or parts[-2:-1] != ['pages']:
        raise SyncError(f'Code forge URL names a different source file: {url}')
    expected = infer_codeforge(root, source)
    if expected:
        expected_url = urlparse(expected)
        marker = parts.index('blob')
        expected_parts = expected_url.path.split('/')
        expected_marker = expected_parts.index('blob')
        repo = run_local('git', 'rev-parse', '--show-toplevel', cwd=root)
        relative = quote(source.relative_to(Path(repo)).as_posix(), safe='/')
        if (parsed.netloc != expected_url.netloc or parts[:marker] != expected_parts[:expected_marker]
                or not parsed.path.endswith('/' + relative)):
            raise SyncError(f'Code forge source ownership conflict: {url}')


def resolve_source(destination: Path, page: str, registry: Path | None = None) -> Path:
    target = resolve_page(destination, page)
    if not target.exists():
        raise SyncError('Initial import requires --source')
    props, _ = parse_properties(target.read_text())
    graph, original_page = proxy_identity(props.get('logseq-proxy-url', ''))
    if original_page != page:
        raise SyncError(f'Proxy names a different page: {original_page}')
    forge = props.get('logseq-proxy-codeforge-url')
    if forge:
        parsed = urlparse(forge)
        path = parsed.path.split('/')
        try:
            marker = path.index('blob')
            repo_parts = path[1:marker]
            if repo_parts[-1:] == ['-']:
                repo_parts.pop()
            address = parsed.netloc + '/' + '/'.join(repo_parts)
            clones = run_local('ghq', 'list', '--full-path', '--exact', address).splitlines()
            if len(clones) != 1:
                raise SyncError(f'Expected one ghq clone for {address}; found {len(clones)}')
            # pages/ disambiguates a branch containing slashes from the nested graph.
            pages_index = path.index('pages', marker + 2)
            clone = Path(clones[0])
            candidates = []
            for start in range(marker + 2, pages_index + 1):
                relative = '/'.join(unquote(x) for x in path[start:pages_index])
                candidate = clone / relative
                if (candidate / 'pages').is_dir() and (candidate / 'logseq').is_dir() and candidate.name == graph:
                    candidates.append(candidate)
            if len(candidates) != 1:
                raise SyncError(f'Cannot uniquely resolve graph {graph} in {clone}')
            root = validate_graph(candidates[0])
            actual = safe_path(root, 'pages/' + unquote(path[pages_index + 1]))
            if actual != resolve_page(root, page):
                raise SyncError('Code forge URL names a different source file')
            return root
        except (ValueError, IndexError) as error:
            if isinstance(error, SyncError):
                raise
            raise SyncError(f'Invalid code forge source URL: {forge}') from error
    registry = registry or Path.home() / '.logseq/graphs'
    matches = []
    if registry.is_dir():
        for record in registry.iterdir():
            name = record.name
            if name.startswith('logseq_local_'):
                decoded = name.removeprefix('logseq_local_').removesuffix('.transit').replace('++', '/')
                root = Path(decoded)
                if root.name == graph and (root / 'pages').is_dir() and (root / 'logseq').is_dir():
                    matches.append(root)
    matches = list(set(matches))
    if len(matches) != 1:
        raise SyncError(f'Expected one registered graph named {graph}; found {len(matches)}; use --source')
    return validate_graph(matches[0])


def add_write(plan: Plan, relative: str, data: bytes, mode: int | None = None) -> None:
    target = safe_path(plan.destination_root, relative)
    if relative in plan.writes and plan.writes[relative] != data:
        raise SyncError(f'Conflicting planned writes: {relative}')
    if relative not in plan.expected:
        plan.expected[relative] = target.read_bytes() if target.exists() else None
        plan.expected_modes[relative] = target.stat().st_mode & 0o777 if target.exists() else None
    plan.writes[relative] = data
    plan.modes[relative] = mode if mode is not None else (plan.expected_modes[relative] or 0o644)


def add_page(plan: Plan, page: str) -> None:
    if page in plan.pages:
        return
    source = resolve_page(plan.source_root, page)
    if not source.exists():
        raise SyncError(f'Missing source page: {source}')
    target = resolve_page(plan.destination_root, page)
    src_data = source.read_bytes()
    plan.source_expected[source] = src_data
    text = src_data.decode('utf-8')
    source_props, body = parse_properties(text)
    source_lines, _ = property_lines(text)
    if plan.codeforge_url and page == plan.page:
        validate_codeforge(plan.codeforge_url, plan.source_root, source)
    first = not target.exists()
    if first:
        target = safe_path(plan.destination_root, 'pages/' + source.name)
    if not first:
        old_text = target.read_bytes().decode('utf-8')
        props, _ = parse_properties(old_text)
        if 'logseq-proxy-url' not in props:
            raise SyncError(f'Page collision: {target} is not a proxy')
        if proxy_identity(props['logseq-proxy-url']) != (plan.source_root.name, page):
            raise SyncError(f'Proxy source conflict: {target}')
        if props.get('logseq-proxy-codeforge-url'):
            validate_codeforge(props['logseq-proxy-codeforge-url'], plan.source_root, source)
        lines, _ = property_lines(old_text)
    else:
        lines = source_lines
        if 'logseq-entity' in source_props:
            lines = [line.rstrip('\r\n') + ', [[Logseq/Entity/Proxy/Page]]\n' if PROPERTY.match(line).group(1) == 'logseq-entity' and '[[Logseq/Entity/Proxy/Page]]' not in source_props['logseq-entity'] else line for line in lines]
        else:
            lines = ['logseq-entity:: [[Logseq/Entity/Proxy/Page]]\n'] + lines
    retained = [line for line in lines if PROPERTY.match(line).group(1) not in PROXY_KEYS]
    # A final property without a newline still needs to remain a separate property.
    retained = [line if line.endswith('\n') else line + '\n' for line in retained]
    metadata = {'logseq-proxy-url': graph_url(plan.source_root, page)}
    forge = plan.codeforge_url if page == plan.page and plan.codeforge_url else infer_codeforge(plan.source_root, source)
    if forge:
        metadata['logseq-proxy-codeforge-url'] = forge
    metadata['logseq-proxy-last-sync-date'] = '[[' + datetime.now(ZoneInfo('America/New_York')).date().isoformat() + ']]'
    data = ''.join(retained) + ''.join(f'{key}:: {value}\n' for key, value in metadata.items()) + body
    relative = str(target.relative_to(plan.destination_root))
    add_write(plan, relative, data.encode())
    plan.pages.add(page)
    plan.details.append(f'{"Create" if first else "Re-sync"} {source} -> {target}')
    plan.details.extend(f'  {key}:: {value}' for key, value in metadata.items())
    # Capture Markdown link targets, allowing <...> around paths with literal spaces.
    assets = re.findall(r'\]\(\s*(?:<([^>]+)>|([^\s)]+))', body)
    for a, b in assets:
        url = a or b
        if not url.startswith('../assets/'):
            continue
        relative = unquote(url.split('#', 1)[0]).removeprefix('../')
        asset = safe_path(plan.source_root, relative)
        safe_path(plan.destination_root, relative)
        if not asset.exists():
            plan.warnings.append(f'Missing asset: {asset}')
            continue
        asset_data = asset.read_bytes()
        plan.source_expected[asset] = asset_data
        add_write(plan, relative, asset_data)
        plan.details.append(f'Asset {asset} -> {plan.destination_root / relative}')


def build_page_plan(source: Path | None, destination: Path, page: str, codeforge_url: str | None = None) -> Plan:
    destination = validate_graph(destination)
    source = validate_graph(source if source is not None else resolve_source(destination, page))
    if source == destination:
        raise SyncError('Source and destination must be different graphs')
    plan = Plan(source, destination, page, codeforge_url=codeforge_url)
    add_page(plan, page)
    return plan


def _remove_empty_dirs(root: Path, directories: list[str]) -> None:
    for relative in sorted(directories, key=lambda p: len(PurePosixPath(p).parts), reverse=True):
        try:
            (root / relative).rmdir()
        except OSError:
            pass


def _recover(destination: Path) -> None:
    txn = destination / TRANSACTION
    if not txn.exists():
        return
    if txn.is_symlink():
        raise SyncError(f'Symlink transaction: {txn}')
    journal_file = safe_path(destination, TRANSACTION + '/journal.json')
    if journal_file.exists():
        journal = json.loads(journal_file.read_text())
        if not isinstance(journal, dict) or not isinstance(journal.get('files'), list) or not isinstance(journal.get('directories'), list):
            raise SyncError(f'Invalid recovery journal: {journal_file}')
        restored = []
        for item in journal['files']:
            if not isinstance(item, dict) or not {'path', 'original', 'mode'} <= item.keys():
                raise SyncError(f'Invalid recovery entry: {journal_file}')
            target = safe_path(destination, item['path'])
            original = item['original']
            if original is not None:
                if not isinstance(item['mode'], int):
                    raise SyncError(f'Invalid recovery mode: {journal_file}')
                original = base64.b64decode(original, validate=True)
            restored.append((target, original, item['mode']))
        for relative in journal['directories']:
            safe_path(destination, relative + '/.recovery-validation')
        for target, original, mode in restored:
            if original is None:
                target.unlink(missing_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(original)
                target.chmod(mode)
        _remove_empty_dirs(destination, journal['directories'])
    shutil.rmtree(txn)


def recover_transaction(destination: Path) -> None:
    destination = validate_graph(destination)
    lock_fd = os.open(destination, os.O_RDONLY)
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX)
        _recover(destination)
    finally:
        os.close(lock_fd)


def apply_plan(plan: Plan) -> None:
    root = plan.destination_root
    lock_fd = os.open(root, os.O_RDONLY)
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX)
        if (root / TRANSACTION).exists():
            raise SyncError('Interrupted import exists; run --destination <graph> --recover, then preview again')
        for source, expected in plan.source_expected.items():
            safe_path(source.parent, source.name)
            if not source.exists() or source.read_bytes() != expected or (source in plan.source_modes and source.stat().st_mode & 0o777 != plan.source_modes[source]):
                raise SyncError(f'Source changed since preview: {source}')
        changes = {}
        for relative, data in plan.writes.items():
            target = safe_path(root, relative)
            actual = target.read_bytes() if target.exists() else None
            mode = target.stat().st_mode & 0o777 if target.exists() else None
            if actual != plan.expected[relative] or mode != plan.expected_modes[relative]:
                raise SyncError(f'Destination changed since preview: {relative}')
            if actual != data or mode != plan.modes[relative]:
                changes[relative] = data
        if not changes:
            return
        directories = set()
        for relative in changes:
            parent = (root / relative).parent
            while parent != root and not parent.exists():
                directories.add(str(parent.relative_to(root)))
                parent = parent.parent
        txn = root / TRANSACTION
        txn.mkdir()
        journal = {'directories': sorted(directories), 'files': [
            {'path': p, 'original': base64.b64encode(plan.expected[p]).decode() if plan.expected[p] is not None else None, 'mode': plan.expected_modes[p]}
            for p in changes]}
        try:
            # Persist rollback information before replacing any destination file.
            with (txn / 'journal.json').open('w') as handle:
                json.dump(journal, handle)
                handle.flush()
                os.fsync(handle.fileno())
            staged = []
            for index, (relative, data) in enumerate(changes.items()):
                stage = txn / str(index)
                with stage.open('wb') as handle:
                    handle.write(data)
                    handle.flush()
                    os.fsync(handle.fileno())
                stage.chmod(plan.modes[relative])
                staged.append((stage, safe_path(root, relative)))
            for stage, target in staged:
                safe_path(root, str(target.relative_to(root)))
                target.parent.mkdir(parents=True, exist_ok=True)
                os.replace(stage, target)
        except BaseException:
            _recover(root)
            raise
        shutil.rmtree(txn)
    finally:
        os.close(lock_fd)
