"""Plan imports of entity definitions, task references, and executable task files.

Follow logseq-entity, entity-tasks, and task-dependencies links from the pages
already selected for sync. Read each task reference's task-files mapping to
locate the entrypoint and helpers, and add their copies to the page-sync plan.
Before replacing imported task files, check the destination manifest's source
ownership, last-imported content hashes, and file modes. Update the manifest
in the same plan so later syncs can distinguish upstream changes from local
edits. core.apply_plan writes the completed plan as one recoverable update.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
from urllib.parse import urlsplit
import tomllib

import core
import records as record_store

MANIFEST = record_store.LEGACY


def refs(value):
    return re.findall(r'\[\[([^\]]+)\]\]', value or '')


def repository(graph):
    for parent in (graph, *graph.parents):
        if (parent / '.git').exists():
            return parent
    return graph


def repository_identity(repo):
    result = subprocess.run(['git', '-C', str(repo), 'remote', 'get-url', 'origin'], capture_output=True, text=True)
    if result.returncode == 0:
        remote = result.stdout.strip()
        if '://' in remote:
            parsed = urlsplit(remote)
            address = (parsed.hostname or '') + '/' + parsed.path.lstrip('/')
        elif ':' in remote and not remote.startswith('/'):
            host, path = remote.split(':', 1)
            address = host.split('@')[-1] + '/' + path
        else:
            address = remote
        return address.removesuffix('.git').rstrip('/')
    return str(repo.resolve())


def relative(value, label):
    path = PurePosixPath(value)
    if not value or path == PurePosixPath('.') or path.is_absolute() or '..' in path.parts or '\\' in value or path.as_posix() != value:
        raise ValueError(f'{label}: expected a normalized repository-relative path: {value}')
    return path


def safe_file(root, value, label):
    path = relative(value, label)
    current = root
    for part in path.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f'{label}: symlink is unsupported: {value}')
    return current


def digest(data):
    return hashlib.sha256(data).hexdigest()


def compatible_config(root):
    """Check that the destination Mise config can discover imported file tasks.

    Read mise.toml or .mise.toml at the graph root. When task_config.includes
    is set, require mise-tasks (with an optional ./ prefix or trailing slash).
    An absent includes setting uses Mise's default file-task discovery.
    Reject an explicit list that excludes mise-tasks before planning writes;
    malformed TOML also stops the import.
    """
    for filename in ('mise.toml', '.mise.toml'):
        config = root / filename
        if config.exists():
            parsed = tomllib.loads(config.read_text())
            includes = parsed.get('task_config', {}).get('includes')
            if includes is not None and not any(str(value).rstrip('/') in ('mise-tasks', './mise-tasks') for value in includes):
                raise ValueError(f'{config}: task_config.includes must include mise-tasks to discover imported tasks')
            return


def load_manifest(data, label):
    """Validate a legacy aggregate for compatibility with older callers."""
    try:
        return record_store.validate_aggregate(json.loads(data), label)
    except (ValueError, AttributeError) as exc:
        raise ValueError(f'{label}: invalid import manifest: {exc}') from exc


def source_manifest(plan):
    if plan.source_record_store is None:
        plan.source_record_store = record_store.load_store(plan.source_root, source_plan=plan)
    return plan.source_record_store


def declarations(props):
    return {key: value for key, value in props.items()
            if key in ('logseq-entity', 'entity-tasks', 'source-link') or key.startswith('task-')}


def source_properties(plan, page, file):
    props, _ = core.parse_properties(file.read_text())
    if props.get('logseq-proxy-url'):
        latest = source_manifest(plan).get('declarations', {}).get(page)
        if latest is not None:
            for key in list(props):
                if key in ('logseq-entity', 'entity-tasks', 'source-link') or key.startswith('task-'):
                    del props[key]
            props.update(latest)
    return props


def task_spec(plan, page, props):
    required = ('task-owner', 'task-config-root', 'task-name', 'source-link', 'task-entrypoint', 'task-files')
    for key in required:
        if not props.get(key):
            raise ValueError(f'{page}: missing {key}')
    repo = repository(plan.source_root)
    scope = props['task-config-root']
    if scope != '.':
        relative(scope, f'{page} task-config-root')
    entry = relative(props['task-entrypoint'], f'{page} task-entrypoint')
    name = props['task-name']
    name_path = PurePosixPath(*name.split(':'))
    if not name or '/' in name or '\\' in name or any(not part or part in ('.', '..') for part in name.split(':')):
        raise ValueError(f'{page}: invalid task-name {name}')
    try:
        mapping = json.loads(props['task-files'])
    except json.JSONDecodeError as exc:
        raise ValueError(f'{page}: task-files must be a JSON object') from exc
    if not isinstance(mapping, dict) or not mapping or not all(isinstance(k, str) and isinstance(v, str) for k, v in mapping.items()):
        raise ValueError(f'{page}: task-files must map source paths to destination paths')
    if mapping.get(str(entry)) != str(PurePosixPath('mise-tasks') / name_path):
        raise ValueError(f'{page}: task-files must map the entrypoint to mise-tasks/{name_path}')
    imported = source_manifest(plan).get('tasks', {}).get(page, {})
    identity = [repository_identity(repo), plan.source_root.relative_to(repo).as_posix(), props['task-owner'], scope, name]
    files = []
    for source, destination in mapping.items():
        dest = relative(destination, f'{page} destination')
        if dest.parts[0] != 'mise-tasks' or len(dest.parts) < 2:
            raise ValueError(f'{page}: task destinations must be implementation files under mise-tasks: {destination}')
        if any(part in ('.git', '.logseq-proxy') for part in dest.parts):
            raise ValueError(f'{page}: reserved destination {destination}')
        actual_source = imported.get('mapping', {}).get(source, source)
        if imported and relative(actual_source, f'{page} imported source').parts[0] != 'mise-tasks':
            raise ValueError(f'{page}: imported source must be under mise-tasks')
        actual_root = plan.source_root if imported else repo
        if any(part in ('.git', '.logseq-proxy') for part in relative(actual_source, f'{page} source').parts):
            raise ValueError(f'{page}: reserved implementation source {actual_source}')
        file = safe_file(actual_root, actual_source, f'{page} source')
        safe_file(plan.destination_root, destination, f'{page} destination')
        if not file.is_file():
            raise ValueError(f'{page}: missing implementation file {source}')
        mode = stat.S_IMODE(file.stat().st_mode)
        if source == str(entry) and not mode & 0o111:
            raise ValueError(f'{page}: entrypoint is not executable: {source}')
        data = file.read_bytes()
        if imported:
            claim = source_manifest(plan).get('files', {}).get(actual_source)
            if (not claim or claim['source'][:2] != imported['identity'][:2]
                    or digest(data) != claim.get('sha256') or mode != claim.get('mode')):
                raise ValueError(f'{page}: forwarded implementation was edited locally or lacks ownership: {actual_source}')
        plan.source_expected[file] = data
        plan.source_modes[file] = mode
        source_relative = file.relative_to(repo).as_posix()
        files.append((source_relative, destination, data, mode))
    return identity, files


def extend_plan(plan, *, migrate=False):
    """Extend the page plan without writing to either garden."""
    compatible_config(plan.destination_root)
    if plan.record_store is None:
        plan.record_store = record_store.load_store(plan.destination_root, destination_plan=plan)
    manifest = plan.record_store
    if manifest.get('_legacy') and not migrate:
        raise core.SyncError('Legacy proxy manifest requires --migrate-records before applying new syncs')
    records = manifest['files']
    queue = list(plan.pages)
    visited = set()
    claims = {}
    required_tasks = set()
    contents = {}
    while queue:
        page = queue.pop()
        if page in visited:
            continue
        visited.add(page)
        file = core.resolve_page(plan.source_root, page)
        if file is None or not file.is_file():
            plan.warnings.append(f'Entity definition {page} has no source file; no companion declaration can be read')
            continue
        props = source_properties(plan, page, file)
        manifest.setdefault('declarations', {})[page] = declarations(props)
        for entity in refs(props.get('logseq-entity')):
            entity_file = core.resolve_page(plan.source_root, entity)
            if entity_file is None or not entity_file.is_file():
                plan.warnings.append(f'Entity definition {entity} has no source file; no companion declaration can be read')
                continue
            core.add_page(plan, entity)
            queue.append(entity)
        task_refs = refs(props.get('entity-tasks')) + refs(props.get('task-dependencies'))
        for task in task_refs:
            task_file = core.resolve_page(plan.source_root, task)
            if task_file is None or not task_file.is_file():
                raise ValueError(f'{page}: missing required task reference {task}')
            task_props = source_properties(plan, task, task_file)
            task_spec(plan, task, task_props)
            required_tasks.add(task)
            core.add_page(plan, task)
            queue.append(task)
        if page not in required_tasks and not props.get('task-files'):
            if props.get('task-entrypoint'):
                raise ValueError(f'{page}: missing task-files')
            continue
        identity, files = task_spec(plan, page, props)
        manifest.setdefault('tasks', {})[page] = {'identity': identity, 'mapping': json.loads(props['task-files'])}
        for source, destination, data, mode in files:
            source_identity = [identity[0], identity[1], source]
            claim = {'source': source_identity, 'sha256': digest(data), 'mode': mode}
            if destination in claims and claims[destination]['source'] != source_identity:
                raise ValueError(f'Competing source files claim {destination}')
            claims[destination] = claim
            contents[destination] = data
    repo = repository(plan.source_root)
    page_records = manifest.setdefault('pages', {})
    for page in plan.pages:
        identity = [repository_identity(repo), plan.source_root.relative_to(repo).as_posix(), page]
        previous = page_records.get(page)
        if previous and previous != identity:
            raise ValueError(f'{page}: page already imported from a different source graph')
        page_records[page] = identity
    for destination, claim in claims.items():
        path = safe_file(plan.destination_root, destination, 'task destination')
        previous = records.get(destination)
        if previous and previous.get('source') != claim['source']:
            raise ValueError(f'{destination}: already claimed by a different source')
        if path.exists():
            if not path.is_file():
                raise ValueError(f'{destination}: destination is not a regular file')
            if not previous:
                raise ValueError(f'{destination}: existing implementation is unowned; move it aside before importing')
            if digest(path.read_bytes()) != previous.get('sha256') or stat.S_IMODE(path.stat().st_mode) != previous.get('mode'):
                raise ValueError(f'{destination}: imported implementation was edited locally')
        elif previous:
            raise ValueError(f'{destination}: imported implementation was deleted locally')
        core.add_write(plan, destination, contents[destination], mode=claim['mode'])
        records[destination] = claim
    repo = repository(plan.source_root)
    import_key = repository_identity(repo) + '::' + plan.source_root.relative_to(repo).as_posix() + '::' + plan.page
    imports = manifest.setdefault('imports', {})
    previous_files = imports.get(import_key, {}).get('files', [])
    for destination in previous_files:
        if destination not in claims:
            plan.warnings.append(f'{destination}: removed upstream; cleanup candidate retained locally')
    # The graph path is repository-relative so the manifest stays the same across checkouts.
    imports[import_key] = {'source_graph': plan.source_root.relative_to(repo).as_posix(), 'page': plan.page, 'files': sorted(set(previous_files) | set(claims))}
    record_store.save_plan(plan, manifest, migrate=migrate)
