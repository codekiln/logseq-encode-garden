"""Temporary-garden coverage for importing executable companion tasks."""
import json
from pathlib import Path
import stat
import subprocess
import shutil
import os
import sys
import tempfile
import unittest

LIB = Path(__file__).resolve().parents[1] / 'mise-tasks/logseq/entity/proxy/page/lib'
sys.path.insert(0, str(LIB))
import core
import companions


class CompanionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name).resolve() / 'source'
        self.repo.mkdir()
        (self.repo / '.git').mkdir()
        self.a = self.repo / 'garden'
        self.b = Path(self.temp.name).resolve() / 'destination'
        self.a.mkdir()
        self.b.mkdir()
        for graph in (self.a, self.b):
            (graph / 'pages').mkdir()
            (graph / 'logseq').mkdir()
        self.page('Thing', 'logseq-entity:: [[Type]]\n- Thing\n')
        self.page('Type', 'entity-tasks:: [[Task]]\n- Type\n')
        self.page('Task', self.task())
        self.source('mise-tasks/demo', '#!/bin/sh\necho companion-ok\n', 0o755)
        self.source('mise-tasks/lib/helper', 'original\n', 0o644)

    def page(self, name, text):
        path = self.a / 'pages' / (name.replace('/', '___') + '.md')
        path.parent.mkdir(exist_ok=True)
        path.write_text(text)

    def source(self, path, text, mode=0o644):
        file = self.repo / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text)
        file.chmod(mode)

    def task(self, mapping=None, extra=''):
        mapping = mapping or {'mise-tasks/demo': 'mise-tasks/demo', 'mise-tasks/lib/helper': 'mise-tasks/lib/helper'}
        return ('task-owner:: [[Repo]]\ntask-config-root:: .\ntask-name:: demo\n'
                'source-link:: https://example.test/demo\ntask-entrypoint:: mise-tasks/demo\n'
                f'task-files:: {json.dumps(mapping)}\n{extra}- Demo\n')

    def plan(self):
        plan = core.build_page_plan(self.a, self.b, 'Thing')
        companions.extend_plan(plan)
        return plan

    def apply(self):
        plan = self.plan()
        core.apply_plan(plan)
        return plan

    def test_nested_graph_import_and_repeat_update(self):
        self.apply()
        executable = self.b / 'mise-tasks/demo'
        self.assertEqual(stat.S_IMODE(executable.stat().st_mode), 0o755)
        self.assertTrue((self.b / 'pages/Task.md').exists())
        self.source('mise-tasks/lib/helper', 'updated\n')
        self.apply()
        self.assertEqual((self.b / 'mise-tasks/lib/helper').read_text(), 'updated\n')
        self.apply()

    def test_cycles_and_shared_helper(self):
        self.page('Task', self.task(extra='logseq-entity:: [[TaskType]]\ntask-dependencies:: [[Task]]\n'))
        self.page('TaskType', 'entity-tasks:: [[Task]]\n- Task type\n')
        self.apply()
        manifest = json.loads((self.b / companions.MANIFEST).read_text())
        self.assertEqual(len(manifest['files']), 2)

    def test_existing_unowned_same_content_conflicts(self):
        self.source_destination('mise-tasks/demo', (self.repo / 'mise-tasks/demo').read_text(), 0o755)
        with self.assertRaisesRegex(ValueError, 'unowned'):
            self.plan()

    def source_destination(self, path, text, mode=0o644):
        file = self.b / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text)
        file.chmod(mode)

    def test_local_content_mode_and_deletion_conflicts(self):
        self.apply()
        file = self.b / 'mise-tasks/lib/helper'
        original = file.read_text()
        file.write_text('local edit')
        with self.assertRaisesRegex(ValueError, 'edited locally'):
            self.plan()
        file.write_text(original)
        file.chmod(0o755)
        with self.assertRaisesRegex(ValueError, 'edited locally'):
            self.plan()
        file.unlink()
        with self.assertRaisesRegex(ValueError, 'deleted locally'):
            self.plan()

    def test_removed_upstream_reports_retained_helper(self):
        self.apply()
        self.page('Task', self.task({'mise-tasks/demo': 'mise-tasks/demo'}))
        plan = self.apply()
        self.assertTrue(any('cleanup candidate' in warning for warning in plan.warnings))
        self.assertTrue((self.b / 'mise-tasks/lib/helper').exists())

    def test_corrupt_manifest_fails_without_writes(self):
        self.apply()
        manifest = self.b / companions.MANIFEST
        for field in ('files', 'tasks', 'pages', 'imports', 'declarations'):
            manifest.write_text(json.dumps({'version': 1, 'files': {}, field: []}))
            with self.assertRaisesRegex(ValueError, 'invalid import manifest'):
                self.plan()

    def test_runtime_requires_companion_module(self):
        task_dir = Path(self.temp.name).resolve() / 'standalone-task'
        (task_dir / 'lib').mkdir(parents=True)
        shutil.copy(LIB / 'core.py', task_dir / 'lib/core.py')
        shutil.copy(LIB.parent / 'sync', task_dir / 'sync')
        result = subprocess.run([str(task_dir / 'sync'), '--source', str(self.a), '--destination', str(self.b), '--page', 'Thing', '--apply'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('Missing companion importer', result.stderr)
        self.assertFalse((self.b / 'pages/Thing.md').exists())

    def test_missing_task_and_implementation(self):
        self.page('Type', 'entity-tasks:: [[Missing]]\n- Type\n')
        with self.assertRaisesRegex(ValueError, 'missing required task'):
            self.plan()
        self.page('Type', 'entity-tasks:: [[Task]]\n- Type\n')
        (self.repo / 'mise-tasks/lib/helper').unlink()
        with self.assertRaisesRegex(ValueError, 'missing implementation'):
            self.plan()

    def test_reserved_destination_and_escape(self):
        for path in ('pages/Thing.md', '.git/config', '.logseq-proxy/manifest.json', 'mise-tasks/../pages/Thing.md'):
            self.page('Task', self.task({'mise-tasks/demo': 'mise-tasks/demo', 'mise-tasks/lib/helper': path}))
            with self.assertRaises(ValueError):
                self.plan()

    def test_symlink_source_and_destination(self):
        helper = self.repo / 'mise-tasks/lib/helper'
        helper.unlink()
        helper.symlink_to(self.repo / 'mise-tasks/demo')
        with self.assertRaisesRegex(ValueError, 'symlink'):
            self.plan()
        helper.unlink()
        helper.write_text('original\n')
        (self.b / 'mise-tasks').symlink_to(self.repo / 'mise-tasks')
        with self.assertRaises(ValueError):
            self.plan()

    def test_config_discovery_and_task_name(self):
        (self.b / 'mise.toml').write_text('[task_config]\nincludes = ["tasks"]\n')
        with self.assertRaisesRegex(ValueError, 'includes'):
            self.plan()
        (self.b / 'mise.toml').unlink()
        self.page('Task', self.task().replace('task-name:: demo', 'task-name:: other'))
        with self.assertRaisesRegex(ValueError, 'task-entrypoint'):
            self.plan()

    def test_missing_task_contract_and_logical_entity(self):
        self.page('Task', '- Incomplete task\n')
        with self.assertRaisesRegex(ValueError, 'missing task-owner'):
            self.plan()
        self.page('Type', '- No companion declaration\n')
        self.page('Thing', 'logseq-entity:: [[LogicalOnly]]\n- Thing\n')
        self.assertTrue(any('LogicalOnly' in warning for warning in self.plan().warnings))

    def test_imported_source_remaps_nested_config_files(self):
        entry = 'scope/mise-tasks/demo'
        helper = 'scope/mise-tasks/lib/helper'
        self.source(entry, '#!/bin/sh\necho chain-ok\n', 0o755)
        self.source(helper, 'nested helper\n')
        text = self.task({entry: 'mise-tasks/demo', helper: 'mise-tasks/lib/helper'})
        text = text.replace('task-config-root:: .', 'task-config-root:: scope').replace('task-entrypoint:: mise-tasks/demo', 'task-entrypoint:: ' + entry)
        self.page('Task', text)
        self.apply()
        c = self.b.with_name('third-garden')
        (c / 'pages').mkdir(parents=True)
        (c / 'logseq').mkdir()
        plan = core.build_page_plan(self.b, c, 'Thing')
        companions.extend_plan(plan)
        core.apply_plan(plan)
        self.assertEqual((c / 'mise-tasks/lib/helper').read_text(), 'nested helper\n')

    def test_latest_declarations_survive_preserved_proxy_properties(self):
        self.apply()
        mapping = {'mise-tasks/demo': 'mise-tasks/demo', 'mise-tasks/lib/helper': 'mise-tasks/lib/helper', 'mise-tasks/lib/new': 'mise-tasks/lib/new'}
        self.source('mise-tasks/lib/new', 'new helper\n')
        self.source('mise-tasks/other', '#!/bin/sh\ntrue\n', 0o755)
        self.page('Other', self.task({'mise-tasks/other': 'mise-tasks/other'}).replace('task-name:: demo', 'task-name:: other').replace('task-entrypoint:: mise-tasks/demo', 'task-entrypoint:: mise-tasks/other'))
        self.page('Task', self.task(mapping, 'task-dependencies:: [[Other]]\n'))
        self.page('Type', 'entity-tasks:: [[Task]], [[Other]]\n- Type\n')
        self.apply()
        # Existing destination frontmatter stays curated; manifests carry current declarations.
        self.assertNotIn('task-dependencies::', (self.b / 'pages/Task.md').read_text())
        c = self.b.with_name('third-garden')
        (c / 'pages').mkdir(parents=True)
        (c / 'logseq').mkdir()
        plan = core.build_page_plan(self.b, c, 'Thing')
        companions.extend_plan(plan)
        core.apply_plan(plan)
        self.assertTrue((c / 'pages/Other.md').exists())
        self.assertTrue((c / 'mise-tasks/other').exists())
        self.assertEqual((c / 'mise-tasks/lib/new').read_text(), 'new helper\n')

    def test_source_change_after_preview_aborts(self):
        plan = self.plan()
        self.source('mise-tasks/lib/helper', 'changed after preview\n')
        with self.assertRaisesRegex(ValueError, 'Source changed'):
            core.apply_plan(plan)
        self.assertFalse((self.b / 'pages/Thing.md').exists())

    def test_same_graph_basename_different_repository_conflicts(self):
        self.apply()
        other = self.repo.with_name('other-source')
        shutil.copytree(self.repo, other)
        self.repo = other
        self.a = other / 'garden'
        with self.assertRaisesRegex(ValueError, 'different source graph'):
            self.plan()

    def test_source_clone_relocation_keeps_ownership(self):
        shutil.rmtree(self.repo / '.git')
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        subprocess.run(['git', '-C', str(self.repo), 'remote', 'add', 'origin', 'git@example.test:owner/repo.git'], check=True)
        self.apply()
        moved = self.repo.with_name('source-moved')
        self.repo.rename(moved)
        self.repo = moved
        self.a = moved / 'garden'
        self.source('mise-tasks/lib/helper', 'relocated update\n')
        self.apply()
        self.assertEqual((self.b / 'mise-tasks/lib/helper').read_text(), 'relocated update\n')

    def test_imported_sync_runs_and_resyncs_from_destination(self):
        name = 'logseq:entity:proxy:page:sync'
        entry = 'mise-tasks/logseq/entity/proxy/page/sync'
        mapping = {entry: entry}
        for module in ('core.py', 'companions.py'):
            path = 'mise-tasks/logseq/entity/proxy/page/lib/' + module
            mapping[path] = path
            self.source(path, (LIB / module).read_text())
        self.source(entry, (LIB.parent / 'sync').read_text(), 0o755)
        self.page('Task', self.task(mapping).replace('task-name:: demo', 'task-name:: ' + name).replace('task-entrypoint:: mise-tasks/demo', 'task-entrypoint:: ' + entry))
        self.apply()
        imported = self.b / entry
        result = subprocess.run([str(imported), '--help'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--destination', result.stdout)
        self.page('Thing', 'logseq-entity:: [[Type]]\n- Updated from source\n')
        result = subprocess.run([str(imported), '--source', str(self.a), '--destination', str(self.b), '--page', 'Thing', '--apply'], cwd=self.b, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Updated from source', (self.b / 'pages/Thing.md').read_text())

    @unittest.skipUnless(shutil.which('mise'), 'mise executable unavailable')
    def test_mise_discovers_and_runs_imported_fixture(self):
        self.apply()
        global_config = self.b / 'empty-global.toml'
        global_config.write_text('')
        environment = dict(os.environ, MISE_GLOBAL_CONFIG_FILE=str(global_config), MISE_CONFIG_DIR=str(self.b / '.test-config'), MISE_CACHE_DIR=str(self.b / '.test-cache'), MISE_STATE_DIR=str(self.b / '.test-state'), MISE_DATA_DIR=str(self.b / '.test-data'))
        result = subprocess.run(['mise', 'tasks', '--json'], cwd=self.b, env=environment, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('demo', result.stdout)
        result = subprocess.run(['mise', 'run', 'demo'], cwd=self.b, env=environment, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('companion-ok', result.stdout)

    def test_competing_source_claim_same_content(self):
        self.source('mise-tasks/lib/other', 'original\n')
        self.page('Task', self.task(extra='task-dependencies:: [[Other]]\n'))
        self.source('mise-tasks/other', '#!/bin/sh\ntrue\n', 0o755)
        text = self.task({'mise-tasks/other': 'mise-tasks/other', 'mise-tasks/lib/other': 'mise-tasks/lib/helper'})
        self.page('Other', text.replace('task-name:: demo', 'task-name:: other').replace('task-entrypoint:: mise-tasks/demo', 'task-entrypoint:: mise-tasks/other'))
        with self.assertRaisesRegex(ValueError, 'Competing source'):
            self.plan()


if __name__ == '__main__':
    unittest.main()
