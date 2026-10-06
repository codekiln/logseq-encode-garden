import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

LIB = Path(__file__).resolve().parents[1] / 'lib'
sys.path.insert(0, str(LIB))
from core import (SyncError, add_write, apply_plan, build_page_plan, graph_url,
                  parse_properties, recover_transaction, resolve_page, resolve_source)


class PageSyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.source = self.graph('source')
        self.destination = self.graph('destination')
        self.page = 'Book/A? B'
        self.source_page = self.source / 'pages/Book___A%3F B.md'
        self.source_page.write_text('tags:: [[Original]]\nlogseq-entity:: [[Logseq/Entity/Book]]\n- body\n')

    def tearDown(self):
        self.temp.cleanup()

    def graph(self, name):
        root = self.root / name
        (root / 'pages').mkdir(parents=True)
        (root / 'logseq').mkdir()
        return root

    def plan(self):
        return build_page_plan(self.source, self.destination, self.page)

    def test_preview_first_copy_and_resync_take_source_properties(self):
        plan = self.plan()
        target = resolve_page(self.destination, self.page)
        self.assertFalse(target.exists())
        apply_plan(plan)
        props, body = parse_properties(target.read_text())
        self.assertEqual(props['tags'], '[[Original]]')
        self.assertIn('[[Logseq/Entity/Proxy/Page]]', props['logseq-entity'])
        original = ('tags:: [[Local]]\r\nowner:: punctuation ?  \r\n'
                    'logseq-entity:: [[Local/Type]]\r\n'
                    f'logseq-proxy-url:: {graph_url(self.source, self.page)}\r\n- old\n')
        target.write_bytes(original.encode())
        self.source_page.write_text('tags:: [[Changed]]\nnew-key:: source only\n- fresh\n')
        apply_plan(self.plan())
        text = target.read_bytes().decode()
        self.assertTrue(text.startswith('tags:: [[Local]]\r\nlogseq-entity:: [[Logseq/Entity/Proxy/Page]]\nnew-key:: source only\n'))
        self.assertNotIn('owner::', text)
        self.assertIn('- fresh\n', text)
        second = self.plan()
        before = target.stat().st_mtime_ns
        apply_plan(second)
        self.assertEqual(target.stat().st_mtime_ns, before)

    def test_resync_keeps_properties_definitions_give_the_destination(self):
        (self.source / 'pages/Logseq___Entity___Book.md').write_text(
            'entity-proxy-destination-properties:: podcast-guid, podcast-published-at\n- # Book\n')
        (self.source / 'pages/Logseq___Entity___Proxy___Page.md').write_text(
            'entity-proxy-destination-properties:: public\n- # Proxy Page\n')
        self.source_page.write_text('tags:: [[Original]]\nlogseq-entity:: [[Logseq/Entity/Book]]\n'
                                    'kept:: same\nchanged:: old\ndropped:: soon\n- body\n')
        apply_plan(self.plan())
        target = resolve_page(self.destination, self.page)
        target.write_text('public:: true\npodcast-guid:: stable\nlocal:: note\n' + target.read_text())
        self.source_page.write_text('tags:: [[Changed]]\nlogseq-entity:: [[Logseq/Entity/Book]]\n'
                                    'kept:: same\nchanged:: new\nadded:: later\npodcast-guid:: source\n'
                                    'podcast-published-at:: source\n- body\n')
        plan = self.plan()
        props, body = parse_properties(plan.writes['pages/Book___A%3F B.md'].decode())
        self.assertEqual(props['public'], 'true')
        self.assertEqual(props['podcast-guid'], 'stable')
        self.assertNotIn('podcast-published-at', props)
        self.assertEqual(props['tags'], '[[Original]]')
        self.assertEqual(props['logseq-entity'], '[[Logseq/Entity/Book]], [[Logseq/Entity/Proxy/Page]]')
        self.assertEqual((props['kept'], props['changed'], props['added']), ('same', 'new', 'later'))
        self.assertNotIn('dropped', props)
        self.assertNotIn('local', props)
        self.assertEqual(body, '- body\n')
        for change in ('updated changed', 'added added', 'removed dropped', 'removed local'):
            self.assertIn(f'  property {change}', plan.details)
        self.assertNotIn('  property updated kept', plan.details)
        apply_plan(plan)
        before = target.read_bytes()
        apply_plan(self.plan())
        self.assertEqual(target.read_bytes(), before)

    def test_follow_embeds_syncs_embedded_pages_recursively(self):
        (self.source / 'assets').mkdir()
        (self.source / 'assets/take.mp3').write_bytes(b'audio')
        self.source_page.write_text('- # Session\n\t- {{embed [[Session/Asset]]}}\n\t- {{embed [[Absent]]}}\n')
        (self.source / 'pages/Session___Asset.md').write_text(
            '- [Take](../assets/take.mp3)\n- {{embed [[Book/A? B]]}}\n')
        self.assertNotIn('pages/Session___Asset.md', self.plan().writes)
        plan = build_page_plan(self.source, self.destination, self.page, follow_embeds=True)
        self.assertIn('pages/Session___Asset.md', plan.writes)
        self.assertEqual(plan.writes['assets/take.mp3'], b'audio')
        self.assertIn('Missing embedded page: Absent', plan.warnings)
        apply_plan(plan)
        props, _ = parse_properties((self.destination / 'pages/Session___Asset.md').read_text())
        self.assertEqual(props['logseq-proxy-url'], graph_url(self.source, 'Session/Asset'))

    def test_page_collision_and_wrong_proxy_source_have_no_writes(self):
        target = resolve_page(self.destination, self.page)
        target.write_text('tags:: [[Local]]\n- original\n')
        with self.assertRaisesRegex(SyncError, 'collision'):
            self.plan()
        self.assertEqual(target.read_text(), 'tags:: [[Local]]\n- original\n')
        target.write_text('logseq-proxy-url:: logseq://graph/other?page=Book%2FA%3F%20B\n- old\n')
        with self.assertRaisesRegex(SyncError, 'source conflict'):
            self.plan()

    def test_assets_nested_encoded_spaces_missing_and_traversal(self):
        (self.source / 'assets/nested').mkdir(parents=True)
        (self.source / 'assets/nested/a b.pdf').write_bytes(b'PDF')
        self.source_page.write_text('- [pdf](../assets/nested/a%20b.pdf)\n- [missing](../assets/no.png)\n')
        plan = self.plan()
        self.assertEqual(len(plan.warnings), 1)
        apply_plan(plan)
        self.assertEqual((self.destination / 'assets/nested/a b.pdf').read_bytes(), b'PDF')
        self.source_page.write_text('- [unsafe](../assets/%2E%2E/outside)\n')
        with self.assertRaisesRegex(SyncError, 'Unsafe'):
            self.plan()

    def test_symlink_source_and_destination_reject_before_write(self):
        (self.source / 'assets').symlink_to(self.root)
        self.source_page.write_text('- [x](../assets/data.pdf)\n')
        with self.assertRaisesRegex(SyncError, 'Symlink'):
            self.plan()
        (self.source / 'assets').unlink()
        self.source_page.write_text('- new\n')
        (self.destination / 'pages').rmdir()
        (self.destination / 'pages').symlink_to(self.source / 'pages')
        with self.assertRaisesRegex(SyncError, 'Symlink'):
            self.plan()

    def test_filename_ambiguity_and_question_slash_url_identity(self):
        plan = self.plan()
        self.assertIn('page=Book%2FA%3F%20B', plan.writes['pages/Book___A%3F B.md'].decode())
        (self.source / 'pages/Book___A? B.md').write_text('- duplicate\n')
        with self.assertRaisesRegex(SyncError, 'Ambiguous'):
            self.plan()

    def test_apply_checks_preview_preconditions(self):
        plan = self.plan()
        target = resolve_page(self.destination, self.page)
        target.write_text('- concurrent edit\n')
        with self.assertRaisesRegex(SyncError, 'changed since preview'):
            apply_plan(plan)
        self.assertEqual(target.read_text(), '- concurrent edit\n')
        target.unlink()
        plan = self.plan()
        self.source_page.write_text('- changed source\n')
        with self.assertRaisesRegex(SyncError, 'Source changed'):
            apply_plan(plan)

    def test_transaction_rolls_back_existing_and_new_files(self):
        target = resolve_page(self.destination, self.page)
        apply_plan(self.plan())
        before = target.read_bytes()
        self.source_page.write_text('- changed\n')
        plan = self.plan()
        add_write(plan, 'mise-tasks/new/task', b'hello', 0o755)
        add_write(plan, '.logseq-proxy/manifest.json', b'{}')
        real_replace = os.replace
        calls = 0
        def fail_after_first(source, destination):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('fixture failure')
            real_replace(source, destination)
        with patch('core.os.replace', side_effect=fail_after_first):
            with self.assertRaisesRegex(OSError, 'fixture failure'):
                apply_plan(plan)
        self.assertEqual(target.read_bytes(), before)
        self.assertFalse((self.destination / 'mise-tasks').exists())
        self.assertFalse((self.destination / '.logseq-proxy').exists())
        self.assertFalse((self.destination / '.logseq-proxy-transaction').exists())

    def test_explicit_recovery_of_interrupted_transaction(self):
        txn = self.destination / '.logseq-proxy-transaction'
        txn.mkdir()
        target = resolve_page(self.destination, self.page)
        target.write_text(f'logseq-proxy-url:: {graph_url(self.source, self.page)}\n- partial\n')
        (txn / 'journal.json').write_text(json.dumps({'directories': [], 'files': [
            {'path': str(target.relative_to(self.destination)), 'original': None, 'mode': None}]}))
        with self.assertRaisesRegex(SyncError, 'Interrupted'):
            apply_plan(self.plan())
        recover_transaction(self.destination)
        self.assertFalse(target.exists())
        apply_plan(self.plan())
        self.assertTrue(target.exists())

    def test_plain_page_gains_proxy_membership(self):
        self.source_page.write_text('- plain\n')
        plan = self.plan()
        text = plan.writes['pages/Book___A%3F B.md'].decode()
        self.assertIn('logseq-entity:: [[Logseq/Entity/Proxy/Page]]', text)
        self.assertRegex(text, r'logseq-proxy-last-sync-date:: \[\[\d{4}-\d{2}-\d{2}\]\]')

    def test_invalid_codeforge_override_rejected(self):
        with self.assertRaisesRegex(SyncError, 'different source file'):
            build_page_plan(self.source, self.destination, self.page, 'https://github.com/a/b/blob/main/pages/Other.md')

    def test_same_graph_name_other_repo_ownership_rejected(self):
        source_repo = self.root / 'first'
        source_repo.mkdir()
        other_repo = self.root / 'other'
        other_repo.mkdir()
        for repo, owner in ((source_repo, 'first'), (other_repo, 'other')):
            subprocess.run(['git', 'init', '-q', str(repo)], check=True)
            subprocess.run(['git', '-C', str(repo), 'remote', 'add', 'origin', f'git@github.com:{owner}/repo.git'], check=True)
        first = self.graph('first/source')
        other = self.graph('other/source')
        for root in (first, other):
            (root / 'pages/Book___A%3F B.md').write_text('- body\n')
        apply_plan(build_page_plan(first, self.destination, self.page))
        before = resolve_page(self.destination, self.page).read_bytes()
        with self.assertRaisesRegex(SyncError, 'ownership conflict'):
            build_page_plan(other, self.destination, self.page)
        self.assertEqual(resolve_page(self.destination, self.page).read_bytes(), before)

    def test_invalid_recovery_journal_keeps_evidence(self):
        txn = self.destination / '.logseq-proxy-transaction'
        txn.mkdir()
        journal = txn / 'journal.json'
        journal.write_text('{}')
        with self.assertRaisesRegex(SyncError, 'Invalid recovery'):
            recover_transaction(self.destination)
        self.assertEqual(journal.read_text(), '{}')

    def test_registry_inference(self):
        apply_plan(self.plan())
        registry = self.root / 'registry'
        registry.mkdir()
        encoded = str(self.source).replace('/', '++')
        (registry / f'logseq_local_{encoded}.transit').touch()
        self.assertEqual(resolve_source(self.destination, self.page, registry), self.source)

    def test_inferred_source_url_omits_remote_credentials(self):
        repo = self.root / 'authenticated-repo'
        repo.mkdir()
        source = self.graph('authenticated-repo/source')
        page = source / 'pages/Example.md'
        page.write_text('- Example\n')
        subprocess.run(['git', 'init', '-q', str(repo)], check=True)
        subprocess.run(['git', '-C', str(repo), 'remote', 'add', 'origin',
                        'https://fixture-user:fixture-password@example.test/owner/repo.git'], check=True)
        plan = build_page_plan(source, self.destination, 'Example')
        output = plan.writes['pages/Example.md'].decode()
        self.assertIn('https://example.test/owner/repo/blob/main/source/pages/Example.md', output)
        self.assertNotIn('fixture-user', output)
        self.assertNotIn('fixture-password', output)
        with self.assertRaisesRegex(SyncError, 'omit embedded credentials'):
            build_page_plan(source, self.destination, 'Example',
                            'https://fixture-user:fixture-password@example.test/owner/repo/blob/main/source/pages/Example.md')

    def test_codeforge_inference_nested_graph_encoded_filename(self):
        repo = self.root / 'repo'
        repo.mkdir()
        nested = self.graph('repo/sub/source')
        nested_page = nested / self.source_page.relative_to(self.source)
        nested_page.write_bytes(self.source_page.read_bytes())
        subprocess.run(['git', 'init', '-q', str(repo)], check=True)
        subprocess.run(['git', '-C', str(repo), 'remote', 'add', 'origin', 'git@github.com:owner/repo.git'], check=True)
        apply_plan(build_page_plan(nested, self.destination, self.page))
        with patch('core.run_local', return_value=str(repo)):
            self.assertEqual(resolve_source(self.destination, self.page), nested)
        text = resolve_page(self.destination, self.page).read_text()
        self.assertIn('/blob/main/sub/source/pages/Book___A%253F%20B.md', text)

    def test_manifest_records_repository_relative_graph(self):
        import companions
        repo = self.root / 'checkout'
        repo.mkdir()
        nested = self.graph('checkout/sub/source')
        (nested / 'pages/Example.md').write_text('- Example\n')
        subprocess.run(['git', 'init', '-q', str(repo)], check=True)
        subprocess.run(['git', '-C', str(repo), 'remote', 'add', 'origin', 'git@github.com:owner/repo.git'], check=True)
        plan = build_page_plan(nested, self.destination, 'Example')
        companions.extend_plan(plan)
        manifest = plan.writes['.logseq-proxy/manifest.json'].decode()
        self.assertNotIn(str(self.root), manifest)
        record = json.loads(manifest)['imports']['github.com/owner/repo::sub/source::Example']
        self.assertEqual(record['source_graph'], 'sub/source')

if __name__ == '__main__':
    unittest.main()
