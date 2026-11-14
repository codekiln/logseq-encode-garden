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


def validate_mount(name, mount):
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
    return {name: validate_mount(name, mount) for name, mount in mounts.items()}


# A markdown link target, plain or in angle brackets, that starts in a mount folder.
LINK = re.compile(r"(\]\(\s*<?)\.\./assets/\.remote/([^/\s<>()]+)/([^)>\n]*)")
# Fenced code from its opening fence to the next line that starts with the same fence, and inline code.
CODE = re.compile(r"^[ \t]*(?:- )?(```|~~~).*?^[ \t]*\1[^\n]*|`[^`\n]+`", re.M | re.S)


def public_links(text, mounts, page):
    """Return text with each link into ../assets/.remote/<mount>/ pointing at the mount's public URL.

    Leaves inline code and fenced code unchanged. Raises MountError, naming the page and the file,
    when a link points into a mount that asset-mounts.toml does not declare or that has no public URL."""

    def swap(match):
        start, name, file = match.groups()
        mount = mounts.get(name)
        if mount is None:
            raise MountError(f"{page} links {name}/{file}, but asset-mounts.toml declares no mounts.{name}")
        if "public" not in mount:
            raise MountError(f"{page} links {name}/{file}, but mounts.{name} has no public URL")
        # A file linked in angle brackets may hold spaces, which a URL cannot.
        return f"{start}{mount['public']}/{file.replace(' ', '%20')}"

    parts, end = [], 0
    for code in CODE.finditer(text):
        parts += [LINK.sub(swap, text[end:code.start()]), code[0]]
        end = code.end()
    parts.append(LINK.sub(swap, text[end:]))
    return "".join(parts)
