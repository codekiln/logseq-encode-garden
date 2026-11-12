"""Asset mounts declared in a garden's asset-mounts.toml."""
from pathlib import Path
import re
import tomllib

FILE = "asset-mounts.toml"
PAGE = "https://github.com/codekiln/logseq-encode-garden/blob/main/pages/Asset___Mount.md"
OWNING = {"path", "bucket", "dvc"}
BORROWING = {"path", "public", "source"}
KEYS = OWNING | BORROWING


class MountError(ValueError):
    def __init__(self, message):
        super().__init__(f"{FILE}: {message}; see {PAGE}")


def check(name, mount):
    if not isinstance(mount, dict):
        raise MountError(f"mounts.{name} must be a table")
    keys = set(mount)
    if unknown := keys - KEYS:
        raise MountError(f"mounts.{name} has unknown keys: {', '.join(sorted(unknown))}")
    if not all(isinstance(value, str) and value for value in mount.values()):
        raise MountError(f"mounts.{name} values must be non-empty strings")
    owning = keys & {"bucket", "dvc"}
    if owning and "source" in keys:
        raise MountError(f"mounts.{name} mixes owning keys ({', '.join(sorted(owning))}) with source")
    required = OWNING if owning else BORROWING
    if missing := required - keys:
        raise MountError(f"mounts.{name} is missing keys: {', '.join(sorted(missing))}")
    if mount["path"] != f"assets/.remote/{name}":
        raise MountError(f"mounts.{name} path must be assets/.remote/{name}")
    if "public" in mount and not re.fullmatch(r"https://[^\s]+[^/\s]", mount["public"]):
        raise MountError(f"mounts.{name} public must be an https URL without a trailing slash")
    return mount


def load(root):
    """Return {name: mount} from root/asset-mounts.toml, or {} when the garden has none."""
    path = Path(root) / FILE
    if not path.is_file():
        return {}
    try:
        data = tomllib.loads(path.read_text())
    except tomllib.TOMLDecodeError as error:
        raise MountError(str(error)) from None
    if unknown := set(data) - {"mounts"}:
        raise MountError(f"unknown tables: {', '.join(sorted(unknown))}")
    mounts = data.get("mounts", {})
    if not isinstance(mounts, dict):
        raise MountError("mounts must be a table")
    return {name: check(name, mount) for name, mount in mounts.items()}
