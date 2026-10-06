from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from cached_credentials import run_cached


class CachedCredentialTests(unittest.TestCase):
    def test_missing_or_incomplete_cache_never_runs_fnox(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            git_result = Mock(stdout=str(root / '.git') + '\n')
            for content in (None, '[profiles.assets.secrets]\n'):
                if content is not None:
                    (root / 'fnox.local.toml').write_text(content)
                with patch('cached_credentials.subprocess.run', return_value=git_result) as run:
                    with self.assertRaises(ValueError):
                        run_cached(['python3', 'asset-command.py'], root / '.worktree' / 'feature')
                    self.assertEqual(run.call_count, 1)

    def test_worktree_uses_registered_cache_without_inherited_aws_credentials(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'fnox.local.toml').write_text(
                '[profiles.assets.secrets.AWS_ACCESS_KEY_ID.sync]\nprovider="sync-age"\nvalue="synthetic-cache"\n'
                '[profiles.assets.secrets.AWS_SECRET_ACCESS_KEY.sync]\nprovider="sync-age"\nvalue="synthetic-cache"\n')
            git_result = Mock(stdout=str(root / '.git') + '\n')
            with patch.dict('os.environ', {'AWS_SECRET_ACCESS_KEY': 'inherited-test-value'}), patch(
                    'cached_credentials.subprocess.run', side_effect=[git_result, Mock(returncode=0)]) as run:
                self.assertEqual(run_cached(['python3', 'asset-command.py'], root / '.worktree' / 'feature'), 0)
                invocation = run.call_args
                self.assertEqual(invocation.kwargs['cwd'], root.resolve())
                self.assertNotIn('AWS_SECRET_ACCESS_KEY', invocation.kwargs['env'])
                self.assertIn('--non-interactive', invocation.args[0])
                self.assertIn('--no-daemon', invocation.args[0])


if __name__ == '__main__':
    unittest.main()
