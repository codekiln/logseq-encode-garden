"""Load the committed defaults, apply the machine's local overrides and resolve every path."""

from __future__ import annotations

import json
import tomllib
from dataclasses import dataclass
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = PACKAGE_ROOT / "config.toml"
LOCAL_CONFIG = PACKAGE_ROOT / "config.local.toml"


class ConfigError(ValueError):
    pass


@dataclass
class Config:
    user_library: Path
    sample_folders: list[Path]
    rack_folders: list[Path]
    extensions: list[str]
    output_folder: Path
    state_folder: Path
    host: str
    port: int
    open_browser: bool
    launchpad_port: str
    audio_device: str
    base_note: int

    @property
    def curation_db(self) -> Path:
        return self.state_folder / "curation.sqlite3"

    @property
    def analysis_db(self) -> Path:
        return self.state_folder / "analysis.sqlite3"

    @property
    def backup_folder(self) -> Path:
        return self.state_folder / "backups"

    def summary(self) -> dict:
        return {
            "user_library": str(self.user_library),
            "sample_folders": [str(p) for p in self.sample_folders],
            "rack_folders": [str(p) for p in self.rack_folders],
            "extensions": self.extensions,
            "output_folder": str(self.output_folder),
            "state_folder": str(self.state_folder),
            "launchpad_port": self.launchpad_port,
            "base_note": self.base_note,
        }

    def write_resolved(self) -> None:
        """Record what the `~` paths resolved to on this machine, inside the ignored state folder."""
        self.state_folder.mkdir(parents=True, exist_ok=True)
        (self.state_folder / "resolved-config.json").write_text(json.dumps(self.summary(), indent=2) + "\n")


def merge(base: dict, override: dict) -> dict:
    merged = dict(base)
    for key, item in override.items():
        if isinstance(item, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], item)
        else:
            merged[key] = item
    return merged


def resolve(raw: str, root: Path) -> Path:
    if not isinstance(raw, str) or not raw.strip():
        raise ConfigError(f"expected a path, got {raw!r}")
    path = Path(raw).expanduser()
    return (path if path.is_absolute() else root / path).resolve()


def load(paths: list[Path] | None = None, root: Path = PACKAGE_ROOT) -> Config:
    """Read the defaults, then each override that exists. Later files win key by key."""
    files = paths if paths is not None else [DEFAULT_CONFIG, LOCAL_CONFIG]
    data: dict = {}
    for file in files:
        if file.exists():
            try:
                data = merge(data, tomllib.loads(file.read_text()))
            except tomllib.TOMLDecodeError as error:
                raise ConfigError(f"{file}: {error}") from error
    try:
        library, output, state = data["library"], data["output"], data["state"]
        server, launchpad = data.get("server", {}), data.get("launchpad", {})
        base_note = int(launchpad.get("base_note", 36))
        if not 0 <= base_note <= 64:
            raise ConfigError("launchpad.base_note must leave 64 notes on the grid (0-64)")
        extensions = [str(e).lower().lstrip(".") for e in library.get("extensions", [])]
        if not extensions:
            raise ConfigError("library.extensions is empty")
        return Config(
            user_library=resolve(library["user_library"], root),
            sample_folders=[resolve(p, root) for p in library.get("sample_folders", [])],
            rack_folders=[resolve(p, root) for p in library.get("rack_folders", [])],
            extensions=extensions,
            output_folder=resolve(output["folder"], root),
            state_folder=resolve(state["folder"], root),
            host=str(server.get("host", "127.0.0.1")),
            port=int(server.get("port", 8377)),
            open_browser=bool(server.get("open_browser", True)),
            launchpad_port=str(launchpad.get("port", "LPProMK3 MIDI")),
            audio_device=str(launchpad.get("audio_device", "")),
            base_note=base_note,
        )
    except KeyError as error:
        raise ConfigError(f"missing config key {error}") from error
