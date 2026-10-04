"""Run a garden command using its existing Fnox assets cache."""
import os
from pathlib import Path
import subprocess
import tomllib


def run_cached(command: list[str], garden: Path) -> int:
    result = subprocess.run(['git', '-C', str(garden), 'rev-parse', '--path-format=absolute', '--git-common-dir'],
                            check=True, capture_output=True, text=True)
    credential_root = Path(result.stdout.strip()).resolve().parent
    cache_path = credential_root / 'fnox.local.toml'
    if not cache_path.is_file():
        raise ValueError('Create the Fnox assets cache in the registered garden checkout first')
    with cache_path.open('rb') as file:
        cache = tomllib.load(file)
    secrets = cache.get('profiles', {}).get('assets', {}).get('secrets', {})
    for name in ('AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY'):
        synced = secrets.get(name, {}).get('sync', {})
        if not synced.get('provider') or not synced.get('value'):
            raise ValueError('Cache both assets credentials before unattended work; vault fallback is disabled')
    env = {key: value for key, value in os.environ.items() if not key.startswith('AWS_')}
    wrapped = ['fnox', '--non-interactive', '--no-daemon', '--no-defaults', '--profile', 'assets',
               '--if-missing', 'error', 'exec', '--', *command]
    return subprocess.run(wrapped, cwd=credential_root, env=env).returncode
