"""Record migration, mutation guards, and actual sibling Git merge regressions."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'lib'))
import core
import records
import task_imports


class RecordsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.source = self.graph('source')
        self.destination = self.graph('destination')
        for page in ('A', 'B', 'Common'):
            core.resolve_page(self.source, page).write_text('tags:: [[Original]]\n- ' + page + '\n')

    def tearDown(self):
        self.temp.cleanup()

    def graph(self, name):
        root = self.root / name
        (root / 'pages').mkdir(parents=True)
        (root / 'logseq').mkdir()
        return root

    def sync(self, page):
        plan = core.build_page_plan(self.source, self.destination, page)
        task_imports.extend_plan(plan)
        core.apply_plan(plan)
        return plan

    def legacy(self):
        store = records.load_store(self.destination)
        value = {key: store[key] for key in ('version', 'pages', 'files', 'tasks', 'declarations', 'imports')}
        for path in (self.destination / '.logseq-proxy').glob('*/*.json'):
            path.unlink()
        path = self.destination / records.LEGACY
        path.write_bytes(records.encoded(value))
        return path

    def test_atomic_legacy_migration_and_repeat_does_not_acknowledge_local_body(self):
        self.sync('A')
        old_record = (self.destination / records.page_record_path('A')).read_bytes()
        legacy = self.legacy()
        plan = records.migration_plan(self.destination)
        self.assertIn(records.LEGACY, plan.deletes)
        self.assertTrue(legacy.exists())
        core.apply_plan(plan)
        self.assertFalse(legacy.exists())
        self.assertEqual((self.destination / records.page_record_path('A')).read_bytes(), old_record)
        core.resolve_page(self.destination, 'A').write_text(core.resolve_page(self.destination, 'A').read_text() + '- local edit\n')
        again = records.migration_plan(self.destination)
        self.assertEqual(again.writes, {})
        core.apply_plan(again)
        self.assertEqual((self.destination / records.page_record_path('A')).read_bytes(), old_record)
        with self.assertRaisesRegex(core.SyncError, 'changed locally'):
            records.removal_plan(self.destination, 'A')

    def test_preview_guards_added_legacy_and_record_inventory(self):
        self.sync('A')
        for source in (False, True):
            with self.subTest(source=source):
                plan = core.Plan(self.source, self.destination, '')
                root = self.source if source else self.destination
                records.load_store(root, source_plan=plan if source else None, destination_plan=None if source else plan)
                path = root / records.LEGACY
                path.parent.mkdir(exist_ok=True)
                path.write_bytes(records.encoded(records.empty_store()))
                with self.assertRaisesRegex(core.SyncError, 'changed since preview'):
                    core.apply_plan(plan)
                path.unlink()
        plan = records.migration_plan(self.destination)
        added = self.destination / records.page_record_path('B')
        added.write_bytes(b'{}')
        with self.assertRaisesRegex(core.SyncError, 'inventory changed'):
            core.apply_plan(plan)

    def test_malformed_nested_imports_is_a_sync_error(self):
        self.sync('A')
        path = self.destination / records.page_record_path('A')
        value = json.loads(path.read_bytes())
        value['imports'] = []
        path.write_bytes(records.encoded(value))
        with self.assertRaisesRegex(core.SyncError, 'import references'):
            records.load_store(self.destination)

    def test_unchanged_sync_keeps_date_and_unrelated_record_bytes(self):
        self.sync('A')
        self.sync('B')
        before = {str(p.relative_to(self.destination)): (p.read_bytes(), p.stat().st_mtime_ns) for p in self.destination.rglob('*') if p.is_file()}
        with patch.object(core, 'datetime') as now:
            now.now.return_value.date.return_value.isoformat.return_value = '2099-01-01'
            self.sync('A')
        after = {str(p.relative_to(self.destination)): (p.read_bytes(), p.stat().st_mtime_ns) for p in self.destination.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_actual_upstream_rename_preserves_owned_metadata_and_ids_then_remove(self):
        definition = self.source / 'pages/Logseq___Entity___Proxy___Page.md'
        definition.write_text('entity-proxy-destination-properties:: public, podcast-guid, podcast-published-at\n- Proxy\n')
        old_source = core.resolve_page(self.source, 'A')
        old_source.write_text('tags:: [[Original]]\n- body\n\tid:: 12345678-1234-1234-1234-123456789abc\n')
        self.sync('A')
        old = core.resolve_page(self.destination, 'A')
        old.write_text('public:: true\npodcast-guid:: stable-guid\npodcast-published-at:: 2026-10-01\n' + old.read_text())
        old_source.rename(core.resolve_page(self.source, 'New'))
        plan = records.rename_plan(self.source, self.destination, 'A', 'New')
        core.apply_plan(plan)
        self.assertFalse(old.exists())
        self.assertFalse((self.destination / records.page_record_path('A')).exists())
        props, body = core.parse_properties(core.resolve_page(self.destination, 'New').read_text())
        self.assertEqual(props['tags'], '[[Original]]')
        self.assertEqual(props['public'], 'true')
        self.assertEqual(props['podcast-guid'], 'stable-guid')
        self.assertEqual(props['podcast-published-at'], '2026-10-01')
        self.assertIn('id:: 12345678', body)
        self.assertIn('page=New', props['logseq-proxy-url'])
        core.apply_plan(records.removal_plan(self.destination, 'New'))
        self.assertEqual(records.load_store(self.destination)['pages'], {})

    def test_rename_rejects_missing_ids_and_destination_collision(self):
        core.resolve_page(self.source, 'A').write_text('- body\n\tid:: 12345678-1234-1234-1234-123456789abc\n')
        self.sync('A')
        core.resolve_page(self.source, 'New').write_text('- no IDs\n')
        with self.assertRaisesRegex(core.SyncError, 'block IDs'):
            records.rename_plan(self.source, self.destination, 'A', 'New')
        core.resolve_page(self.destination, 'New').write_text('- local\n')
        with self.assertRaisesRegex(core.SyncError, 'collision'):
            records.rename_plan(self.source, self.destination, 'A', 'New')

    def test_delete_guard_and_rollback_restore_bytes_and_modes(self):
        self.sync('A')
        plan = records.removal_plan(self.destination, 'A')
        target = core.resolve_page(self.destination, 'A')
        before = target.read_bytes()
        target.write_bytes(before + b'- changed\n')
        with self.assertRaisesRegex(core.SyncError, 'Destination changed'):
            core.apply_plan(plan)
        target.write_bytes(before)
        plan = records.removal_plan(self.destination, 'A')
        original_unlink = Path.unlink
        calls = []
        def fail_second(path, *args, **kwargs):
            calls.append(path)
            if len(calls) == 2:
                raise OSError('injected delete failure')
            return original_unlink(path, *args, **kwargs)
        with patch.object(Path, 'unlink', fail_second):
            with self.assertRaisesRegex(OSError, 'injected'):
                core.apply_plan(plan)
        self.assertEqual(target.read_bytes(), before)
        self.assertTrue((self.destination / records.page_record_path('A')).exists())

    def test_remove_rejects_live_block_references_and_stale_reference_inventory(self):
        block_id = '12345678-1234-1234-1234-123456789abc'
        core.resolve_page(self.source, 'A').write_text('- body\n\tid:: ' + block_id + '\n')
        self.sync('A')
        ref = core.resolve_page(self.destination, 'Ref')
        ref.write_text('- ((' + block_id + '))\n')
        with self.assertRaisesRegex(core.SyncError, 'block ID referenced'):
            records.removal_plan(self.destination, 'A')
        ref.write_text('- no reference\n')
        plan = records.removal_plan(self.destination, 'A')
        ref.write_text('- ((' + block_id + '))\n')
        with self.assertRaisesRegex(core.SyncError, 'Destination changed'):
            core.apply_plan(plan)
        ref.unlink()
        plan = records.removal_plan(self.destination, 'A')
        ref.write_text('- ((' + block_id + '))\n')
        with self.assertRaisesRegex(core.SyncError, 'inventory changed'):
            core.apply_plan(plan)

    def test_task_forwarding_legacy_and_records_reject_local_output_edits(self):
        source_file = self.source / 'scripts/original'
        source_file.parent.mkdir()
        source_file.write_text('#!/bin/sh\necho stable\n')
        source_file.chmod(0o755)
        core.resolve_page(self.source, 'A').write_text('entity-tasks:: [[Example/Task]]\n- A\n')
        core.resolve_page(self.source, 'Example/Task').write_text(
            'task-owner:: [[Owner]]\ntask-config-root:: .\ntask-name:: example\n'
            'task-entrypoint:: scripts/original\n'
            'task-files:: {"scripts/original":"mise-tasks/example"}\n'
            'source-link:: https://example.test/source\n- Task\n')
        self.sync('A')
        for legacy in (False, True):
            if legacy:
                self.legacy()
            onward = self.graph('onward-' + str(legacy))
            plan = core.build_page_plan(self.destination, onward, 'A')
            task_imports.extend_plan(plan)
            core.apply_plan(plan)
            self.assertEqual((onward / 'mise-tasks/example').read_bytes(), source_file.read_bytes())
            final = self.graph('final-' + str(legacy))
            next_plan = core.build_page_plan(onward, final, 'A')
            task_imports.extend_plan(next_plan)
            core.apply_plan(next_plan)
            self.assertEqual((final / 'mise-tasks/example').read_bytes(), source_file.read_bytes())
        forwarded = self.destination / 'mise-tasks/example'
        forwarded.write_text('#!/bin/sh\necho local edit\n')
        with self.assertRaisesRegex(ValueError, 'forwarded implementation was edited locally'):
            task_imports.extend_plan(core.build_page_plan(self.destination, onward, 'A'))

    def test_cli_usage_environment_migration_and_remove_booleans(self):
        import os
        self.sync('A')
        self.legacy()
        entry = Path(__file__).resolve().parents[1] / 'sync'
        env = {key: value for key, value in os.environ.items() if not key.startswith('usage_')}
        env.update(usage_destination=str(self.destination), usage_migrate_records='true', usage_apply='false')
        result = subprocess.run([sys.executable, str(entry)], env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.destination / records.LEGACY).exists())
        env['usage_apply'] = 'true'
        result = subprocess.run([sys.executable, str(entry)], env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.destination / records.LEGACY).exists())
        env.update(usage_migrate_records='false', usage_remove='true', usage_page='A')
        result = subprocess.run([sys.executable, str(entry)], env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(core.resolve_page(self.destination, 'A').exists())

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.destination), *args], check=True, capture_output=True, text=True).stdout

    def test_real_sibling_branch_merges_in_both_orders_with_common_definition(self):
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.sync('Common')
        self.git('add', '.')
        self.git('commit', '-m', 'baseline common definition')
        baseline = self.git('rev-parse', 'HEAD').strip()
        for branch, page in (('sibling-a', 'A'), ('sibling-b', 'B')):
            self.git('checkout', '-b', branch, baseline)
            self.sync('Common')
            self.sync(page)
            self.git('add', '.')
            self.git('commit', '-m', 'import ' + page)
        for first, second in (('sibling-a', 'sibling-b'), ('sibling-b', 'sibling-a')):
            self.git('checkout', '--detach', first)
            self.git('merge', '--no-edit', second)
            self.assertEqual(set(records.load_store(self.destination)['pages']), {'A', 'B', 'Common'})
            self.assertEqual(self.git('status', '--porcelain'), '')


if __name__ == '__main__':
    unittest.main()
