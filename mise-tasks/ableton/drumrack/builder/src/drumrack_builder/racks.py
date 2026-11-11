"""Turn a rack in the curation database into an .adg file, starting from a source rack or the template."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict
from pathlib import Path

import soundfile as sf

from . import adg
from .analysis import live_only
from .config import Config
from .library import Library
from .store import Store, StoreError

MAX_NAME = 120


def safe_filename(name: str) -> str:
    """A preset filename that cannot leave the output folder: no separators, dots-only or hidden names."""
    text = unicodedata.normalize("NFC", name).strip()
    text = re.sub(r"\.adg$", "", text, flags=re.IGNORECASE)
    text = re.sub(r'[\x00-\x1f\x7f/\\:*?"<>|]', "-", text)
    text = re.sub(r"(?:^|(?<=-))\.+(?=-|$)", "", text).strip(" .-")
    if not text or set(text) <= {"-", " "}:
        raise StoreError("the preset needs a name with letters or digits")
    return text[:MAX_NAME] + ".adg"


def duplicate(store: Store, library: Library, source_key: str, name: str | None = None) -> int:
    """Create a rack whose pads start as the source rack's pads. The source file is only read."""
    source = library.source_rack(source_key)
    rack_id = store.create_rack(name or f"{source.name} copy", str(source.path))
    for pad in source.pads:
        sample_id = store.upsert_sample(Path(pad.samples[0]), in_rack=True) if pad.samples else None
        store.set_pad(
            rack_id,
            pad.note,
            sample_id=sample_id,
            name=pad.name,
            keep=True,
            source_note=pad.note,
            base_label=pad.label + ("" if pad.simple else f" ({', '.join(pad.devices)})"),
        )
    return rack_id


def revert(store: Store, rack_id: int, note: int) -> None:
    """Put a pad back to its source pad's sample and settings, keeping its current note and name."""
    pad = next((p for p in store.pads(rack_id) if p["note"] == note), None)
    base_path = store.rack(rack_id)["base_path"]
    if pad is None or pad["source_note"] is None or base_path is None:
        raise StoreError("only a pad that came from the source rack can be reverted")
    source = adg.read_rack(Path(base_path)).pad(pad["source_note"])
    if source is None:
        raise StoreError(f"the source rack no longer has a pad on note {pad['source_note']}")
    sample_id = store.upsert_sample(Path(source.samples[0]), in_rack=True) if source.samples else None
    store.set_pad(rack_id, note, sample_id=sample_id, name=pad["name"], keep=True)


def sample_file(path: Path) -> adg.SampleFile:
    if not path.is_file():
        raise StoreError(f"sample missing: {path}")
    if live_only(path):
        raise StoreError(
            f"{path.name} is encoded for Live only, so it can stay on its original pad but not go on a new one"
        )
    info = sf.info(str(path))
    return adg.SampleFile.from_path(path, frames=info.frames, sample_rate=info.samplerate)


def plan(store: Store, rack_id: int) -> list[adg.PadPlan]:
    pads = store.pads(rack_id)
    result = []
    for pad in pads:
        if pad["keep"]:
            result.append(adg.PadPlan(note=pad["note"], name=pad["name"], source_note=pad["source_note"]))
        elif pad["sample_id"] is None:
            continue  # an empty pad is only a placeholder for its shortlists
        else:
            result.append(
                adg.PadPlan(
                    note=pad["note"],
                    name=pad["name"],
                    source_note=pad["source_note"],
                    sample=sample_file(Path(pad["sample_path"])),
                )
            )
    if not result:
        raise StoreError("assign at least one sample before exporting")
    return result


def base_root(store: Store, rack_id: int):
    base_path = store.rack(rack_id)["base_path"]
    if base_path is None:
        return None
    path = Path(base_path)
    if not path.is_file():
        raise StoreError(f"the source rack is gone: {path}")
    return adg.read_xml(path)


def output_path(config: Config, filename: str) -> Path:
    path = (config.output_folder / safe_filename(filename)).resolve()
    if not path.is_relative_to(config.output_folder):
        raise StoreError("the preset must be written inside the output folder")
    return path


def export(
    store: Store,
    library: Library,
    config: Config,
    rack_id: int,
    filename: str,
    overwrite: bool = False,
    target: Path | None = None,
) -> dict:
    """Write and verify the rack. ``target`` (CLI only) replaces the configured output folder."""
    base = base_root(store, rack_id)
    pads = plan(store, rack_id)
    output = target.expanduser().resolve() if target is not None else output_path(config, filename)
    root = adg.build_rack(base, pads, output, user_library=config.user_library)
    try:
        backup = adg.write_rack(
            root, output, overwrite=overwrite, backup_dir=config.backup_folder, protected=library.protected_paths()
        )
    except adg.RackError as error:
        raise StoreError(str(error)) from error
    report = adg.verify_rack(output, pads, base)
    store.update_rack(rack_id, last_export=str(output))
    return {"path": str(output), "backup": None if backup is None else str(backup), "report": asdict(report)}
