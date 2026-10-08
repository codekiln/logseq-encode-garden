"""Independent proxy page/output records, with a read-only legacy adapter.

The aggregate dictionaries are derived in memory. A page record contains its
identity, declarations, optional task mapping, and requested import references;
an output record contains the implementation path's ownership/hash/mode.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote

import core

LEGACY = '.logseq-proxy/manifest.json'
PAGES = '.logseq-proxy/pages'
FILES = '.logseq-proxy/files'


def empty_store():
    return {'version': 1, 'files': {}, 'imports': {}, 'pages': {}, 'tasks': {}, 'declarations': {},
            '_page_records': {}, '_legacy': False, '_record_paths': {}}


def bounded_name(stem):
    if len((stem + '.json').encode()) > 255:
        stem = stem[:120] + '--' + hashlib.sha256(stem.encode()).hexdigest()
    return stem + '.json'


def page_record_path(page):
    # Logseq reserves ___ for namespace boundaries; reject an ambiguous literal.
    if any('___' in part for part in page.split('/')):
        raise core.SyncError(f'Ambiguous page namespace: {page}')
    return PAGES + '/' + bounded_name(core.page_filename(page).removesuffix('.md'))


def file_record_path(relative):
    core.safe_path(Path('/'), relative)
    return FILES + '/' + bounded_name(quote(relative, safe=' _-.,()[]'))


def encoded(record):
    return (json.dumps(record, indent=2, sort_keys=True) + '\n').encode()


def _read(root, relative, plan=None):
    path = core.safe_path(root, relative)
    data = path.read_bytes()
    if plan is not None:
        plan.source_expected[path] = data
    try:
        value = json.loads(data)
    except (ValueError, UnicodeError) as error:
        raise core.SyncError(f'Invalid proxy record {path}') from error
    return value


def _identity(value):
    return isinstance(value, list) and len(value) == 3 and all(isinstance(x, str) for x in value)


def validate_aggregate(store, label):
    if not isinstance(store, dict) or store.get('version') != 1:
        raise core.SyncError(f'{label}: unsupported proxy manifest')
    for section in ('files', 'imports', 'pages', 'tasks', 'declarations'):
        if not isinstance(store.get(section, {}), dict):
            raise core.SyncError(f'{label}: {section} must be an object')
    for relative, record in store.get('files', {}).items():
        if (not isinstance(record, dict) or not _identity(record.get('source'))
                or not isinstance(record.get('mode'), int) or not isinstance(record.get('sha256'), str)):
            raise core.SyncError(f'{label}: invalid file ownership for {relative}')
        file_record_path(relative)
    for page, identity in store.get('pages', {}).items():
        page_record_path(page)
        if not _identity(identity):
            raise core.SyncError(f'{label}: invalid page ownership for {page}')
    for page, record in store.get('tasks', {}).items():
        if (not isinstance(record, dict) or not isinstance(record.get('identity'), list)
                or len(record['identity']) != 5 or not all(isinstance(x, str) for x in record['identity'])
                or not isinstance(record.get('mapping'), dict)
                or not all(isinstance(k, str) and isinstance(v, str) for k, v in record['mapping'].items())):
            raise core.SyncError(f'{label}: invalid task mapping for {page}')
        if page not in store.get('pages', {}) or record['identity'][:2] != store['pages'][page][:2]:
            raise core.SyncError(f'{label}: task/page ownership disagreement for {page}')
    for page, record in store.get('declarations', {}).items():
        if not isinstance(record, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in record.items()):
            raise core.SyncError(f'{label}: invalid declarations for {page}')
    for key, record in store.get('imports', {}).items():
        if (not isinstance(record, dict) or not isinstance(record.get('page'), str)
                or not isinstance(record.get('files'), list) or not all(isinstance(x, str) for x in record['files'])):
            raise core.SyncError(f'{label}: invalid import reference {key}')
    return store


def load_store(root, source_plan=None, destination_plan=None):
    """Read records or v1; never write. source_plan guards onward-import reads."""
    root = Path(root)
    store = empty_store()
    legacy = core.safe_path(root, LEGACY)
    if destination_plan is not None:
        core.watch_destination(destination_plan, LEGACY)
    if source_plan is not None:
        source_plan.source_expected[legacy] = legacy.read_bytes() if legacy.exists() else None
    paths = []
    for directory in (PAGES, FILES):
        folder = root / directory
        core.safe_path(root, directory + '/.validation')
        inventory = tuple(sorted(p.name for p in folder.glob('*.json'))) if folder.exists() else None
        for plan in (source_plan, destination_plan):
            if plan is not None:
                plan.inventory_expected[folder] = inventory
        if folder.exists():
            paths.extend(str(p.relative_to(root)) for p in sorted(folder.glob('*.json')))
    if legacy.exists() and paths:
        raise core.SyncError('Both legacy manifest and proxy records exist; reconcile the incomplete migration')
    if legacy.exists():
        if destination_plan is not None:
            core.watch_destination(destination_plan, LEGACY)
        value = _read(root, LEGACY, source_plan)
        validate_aggregate(value, legacy)
        store.update(value)
        store['_legacy'] = True
        return store
    for relative in paths:
        if destination_plan is not None:
            core.watch_destination(destination_plan, relative)
        value = _read(root, relative, source_plan)
        if not isinstance(value, dict) or value.get('version') != 2:
            raise core.SyncError(f'Invalid proxy record schema: {relative}')
        if relative.startswith(PAGES + '/'):
            page = value.get('page')
            if not isinstance(page, str) or page_record_path(page) != relative or page in store['pages']:
                raise core.SyncError(f'Ambiguous proxy page record: {relative}')
            store['pages'][page] = value.get('identity')
            store['declarations'][page] = value.get('declarations', {})
            if 'task' in value:
                store['tasks'][page] = value['task']
            if not isinstance(value.get('imports', {}), dict):
                raise core.SyncError(f'Invalid page import references: {relative}')
            for key, record in value.get('imports', {}).items():
                if not isinstance(record, dict) or key in store['imports'] or record.get('page') != page:
                    raise core.SyncError(f'Ambiguous import reference: {relative}')
                store['imports'][key] = record
            store['_page_records'][page] = value
        else:
            destination = value.get('destination')
            if not isinstance(destination, str) or file_record_path(destination) != relative:
                raise core.SyncError(f'Ambiguous proxy output record: {relative}')
            store['files'][destination] = {k: value[k] for k in ('source', 'sha256', 'mode') if k in value}
        store['_record_paths'][relative] = value
    validate_aggregate(store, root / '.logseq-proxy')
    return store


def save_plan(plan, store, *, migrate=False):
    """Add changed independent records to a plan; explicit migration removes v1."""
    if store.get('_legacy') and not migrate:
        raise core.SyncError('Legacy proxy manifest requires --migrate-records before applying new syncs')
    migrating = migrate and store.get('_legacy', False)
    validate_aggregate(store, plan.destination_root)
    named = set(store['pages']) | set(store['declarations']) | set(store['tasks'])
    named.update(record['page'] for record in store['imports'].values())
    for page in sorted(named):
        if page not in store['pages']:
            raise core.SyncError(f'Cannot migrate declarations without source ownership: {page}')
        record = dict(store.get('_page_records', {}).get(page, {}))
        record.update(version=2, page=page, identity=store['pages'][page], declarations=store['declarations'].get(page, {}))
        record['imports'] = {key: value for key, value in store['imports'].items() if value['page'] == page}
        if page in store['tasks']:
            record['task'] = store['tasks'][page]
        else:
            record.pop('task', None)
        target = core.resolve_page(plan.destination_root, page)
        data = plan.writes.get(str(target.relative_to(plan.destination_root)))
        if data is None and target.exists():
            data = target.read_bytes()
        if data is not None and (page in plan.pages or migrating):
            core.watch_destination(plan, str(target.relative_to(plan.destination_root)))
            _, body = core.parse_properties(data.decode())
            record['body_sha256'] = hashlib.sha256(body.encode()).hexdigest()
        relative = page_record_path(page)
        data = encoded(record)
        path = core.safe_path(plan.destination_root, relative)
        if not path.exists() or path.read_bytes() != data:
            core.add_write(plan, relative, data, 0o644)
    for destination, claim in sorted(store['files'].items()):
        relative = file_record_path(destination)
        record = {'version': 2, 'destination': destination, **claim}
        path = core.safe_path(plan.destination_root, relative)
        data = encoded(record)
        if not path.exists() or path.read_bytes() != data:
            core.add_write(plan, relative, data, 0o644)
    if migrate and store.get('_legacy'):
        core.add_delete(plan, LEGACY)
        plan.details.append('Migrate legacy manifest to independent proxy records')


def migration_plan(destination):
    """Plan an atomic v1 split without syncing source pages or implementations."""
    root = core.validate_graph(destination)
    plan = core.Plan(root, root, '')
    store = load_store(root, destination_plan=plan)
    if store['_legacy']:
        save_plan(plan, store, migrate=True)
    else:
        plan.details.append('Already using independent proxy records; no migration needed')
    return plan


def _owned_proxy(plan, store, page):
    path = core.resolve_page(plan.destination_root, page)
    if page not in store['pages'] or not path.exists():
        raise core.SyncError(f'No owned proxy record for {page}')
    core.watch_destination(plan, str(path.relative_to(plan.destination_root)))
    data = path.read_bytes()
    props, body = core.parse_properties(data.decode())
    _, original = core.proxy_identity(props.get('logseq-proxy-url', ''))
    if original != page or store['pages'][page][2] != page:
        raise core.SyncError(f'Proxy source ownership conflict: {page}')
    baseline = store.get('_page_records', {}).get(page, {}).get('body_sha256')
    if baseline is None or hashlib.sha256(body.encode()).hexdigest() != baseline:
        raise core.SyncError(f'{page}: proxy body changed locally; reconcile before removing or renaming')
    return path, data


def _forget_page(plan, store, page):
    for section in ('pages', 'tasks', 'declarations', '_page_records'):
        store[section].pop(page, None)
    for key, reference in list(store['imports'].items()):
        if reference['page'] == page:
            for output in reference['files']:
                plan.warnings.append(f'{output}: companion output retained; review cleanup separately')
            del store['imports'][key]
    core.add_delete(plan, page_record_path(page))


def removal_plan(destination, page):
    """Remove an owned proxy and its record, retaining shared assets/task outputs."""
    root = core.validate_graph(destination)
    plan = core.Plan(root, root, page)
    store = load_store(root, destination_plan=plan)
    if store['_legacy']:
        raise core.SyncError('Run --migrate-records before removing a proxy')
    path, data = _owned_proxy(plan, store, page)
    ids = set(re.findall(r'(?m)^\s*(?:-\s+)?id::\s+([0-9a-fA-F-]{36})\s*$', data.decode()))
    if ids:
        for directory in ('pages', 'journals'):
            folder = root / directory
            core.safe_path(root, directory + '/.validation')
            plan.inventory_expected[folder] = tuple(sorted(p.name for p in folder.glob('*.md'))) if folder.exists() else None
            plan.inventory_patterns[folder] = '*.md'
            for candidate in folder.glob('*.md'):
                if candidate == path:
                    continue
                relative = str(candidate.relative_to(root))
                core.watch_destination(plan, relative)
                text = candidate.read_text()
                if any('((' + block_id + '))' in text for block_id in ids):
                    raise core.SyncError(f'{page}: block ID referenced by {relative}; retain the block before removing')
    core.add_delete(plan, str(path.relative_to(root)))
    _forget_page(plan, store, page)
    plan.details.append(f'Remove proxy {page} and its page record')
    return plan


def rename_plan(source, destination, page, new_page, *, refresh_provenance=False):
    """Rename a proxy to an existing source page, preserving destination-owned properties."""
    import re
    import task_imports
    if page == new_page:
        raise core.SyncError('Rename needs a different logical page name')
    destination = core.validate_graph(destination)
    source = core.validate_graph(source if source is not None else core.resolve_source(destination, page))
    if core.resolve_page(destination, new_page).exists():
        raise core.SyncError(f'Rename destination collision: {new_page}')
    plan = core.build_page_plan(source, destination, new_page, refresh_provenance=refresh_provenance)
    store = load_store(destination, destination_plan=plan)
    if store['_legacy']:
        raise core.SyncError('Run --migrate-records before renaming a proxy')
    old_path, old_data = _owned_proxy(plan, store, page)
    repo = task_imports.repository(source)
    expected = [task_imports.repository_identity(repo), source.relative_to(repo).as_posix(), page]
    if store['pages'][page] != expected:
        raise core.SyncError(f'Proxy source ownership conflict: {page}')
    old_props, old_body = core.parse_properties(old_data.decode())
    if core.proxy_identity(old_props['logseq-proxy-url']) != (core.graph_name(source), page):
        raise core.SyncError(f'Proxy graph ownership conflict: {page}')
    source_path = core.resolve_page(source, new_page)
    source_text = source_path.read_text()
    source_props, new_body = core.parse_properties(source_text)
    ids = lambda body: set(re.findall(r'(?m)^\s*(?:-\s+)?id::\s+([0-9a-fA-F-]{36})\s*$', body))
    if not ids(old_body) <= ids(new_body):
        raise core.SyncError('Renamed source would remove existing block IDs')
    old_lines, _ = core.property_lines(old_data.decode())
    source_lines, _ = core.property_lines(source_text)
    lines, changes = core.merge_properties(old_lines, core.with_proxy_membership(source_lines),
                                           core.destination_owned(plan, source_props))
    target = core.resolve_page(destination, new_page)
    relative = str(target.relative_to(destination))
    props, _ = core.parse_properties(plan.writes[relative].decode())
    metadata = {key: props[key] for key in core.PROXY_KEYS if key in props}
    semantic = ''.join(lines) + new_body
    old_semantic = ''.join(line for line in old_lines if core.property_key(line) not in core.PROXY_KEYS) + old_body
    if semantic == old_semantic and old_props.get('logseq-proxy-last-sync-date'):
        metadata['logseq-proxy-last-sync-date'] = old_props['logseq-proxy-last-sync-date']
    plan.writes[relative] = (''.join(lines) + ''.join(f'{key}:: {value}\n' for key, value in metadata.items()) + new_body).encode()
    core.add_delete(plan, str(old_path.relative_to(destination)))
    _forget_page(plan, store, page)
    plan.record_store = store
    task_imports.extend_plan(plan)
    plan.details.append(f'Rename proxy {page} -> {new_page}')
    plan.details.extend(f'  property {change}' for change in changes)
    return plan
