"""Read, build, write and verify Ableton Live Drum Rack presets (.adg).

An .adg file is gzip-compressed XML. A Drum Rack preset holds a ``GroupDevicePreset`` whose
``Device`` is a ``DrumGroupDevice`` and whose ``BranchPresets`` hold one ``DrumBranchPreset`` per pad.
Live stores a pad's MIDI note inverted: ``ReceivingNote = 128 - note``, so C1 (36) is 92.
"""

from __future__ import annotations

import copy
import gzip
import os
import shutil
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from importlib import resources
from pathlib import Path

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Live's RelativePathType values seen in saved presets: 1 is relative to the preset's own folder,
# 5 to a Pack or the Core Library, 6 to the User Library.
REL_DOCUMENT = "1"
REL_USER_LIBRARY = "6"

# A replaced sample keeps these per-sample settings of the old sample zone; everything tied to the old
# audio (start/end, loops, warp markers, slices) comes from the template's untouched zone instead.
PRESERVED_PART_TAGS = (
    "KeyRange",
    "VelocityRange",
    "SelectorRange",
    "RootKey",
    "Detune",
    "TuneScale",
    "Panorama",
    "Volume",
)


class RackError(ValueError):
    pass


def note_name(note: int) -> str:
    """Live's spelling: middle C (60) is C3, so 36 is C1."""
    return f"{NOTE_NAMES[note % 12]}{note // 12 - 2}"


@dataclass
class SampleFile:
    """What the writer needs to know about an audio file to point a Simpler at it."""

    path: Path
    frames: int
    sample_rate: int
    size: int
    mtime: float

    @classmethod
    def from_path(cls, path: Path, frames: int, sample_rate: int) -> SampleFile:
        stat = path.stat()
        return cls(path=path, frames=frames, sample_rate=sample_rate, size=stat.st_size, mtime=stat.st_mtime)


@dataclass
class Pad:
    note: int
    name: str
    choke: int
    devices: list[str]
    samples: list[str]
    # A pad is "simple" when it is one Simpler zone the builder can re-point at another sample.
    simple: bool

    @property
    def label(self) -> str:
        if self.name:
            return self.name
        return Path(self.samples[0]).stem if self.samples else ""


@dataclass
class Rack:
    path: Path | None
    creator: str
    pads: list[Pad]

    def pad(self, note: int) -> Pad | None:
        return next((p for p in self.pads if p.note == note), None)


@dataclass
class PadPlan:
    """The desired state of one pad.

    ``source_note`` names the base rack's pad this pad starts from: its devices, choke group and mixer
    carry over, even when the pad moves to another note. ``sample=None`` also keeps that pad's sample.
    A pad without a source note starts from the template's default Simpler.
    """

    note: int
    name: str = ""
    sample: SampleFile | None = None
    source_note: int | None = None


@dataclass
class VerifyReport:
    ok: bool
    problems: list[str] = field(default_factory=list)
    pads: list[dict] = field(default_factory=list)
    preserved_pads: int = 0
    replaced_pads: int = 0
    added_pads: int = 0
    removed_pads: int = 0
    device_settings_preserved: bool = True


# ---------------------------------------------------------------------------- reading


def read_xml(path: Path) -> ET.Element:
    data = Path(path).read_bytes()
    if data[:2] == b"\x1f\x8b":
        try:
            data = gzip.decompress(data)
        except (OSError, EOFError) as error:
            raise RackError(f"{path}: damaged gzip data ({error})") from error
    try:
        return ET.fromstring(data)
    except ET.ParseError as error:
        raise RackError(f"{path}: XML does not parse ({error})") from error


def drum_group(root: ET.Element) -> ET.Element:
    device = root.find("GroupDevicePreset/Device/DrumGroupDevice")
    if root.tag != "Ableton" or device is None:
        raise RackError("not an Ableton Drum Rack preset")
    return device


def branches(root: ET.Element) -> ET.Element:
    found = root.find("GroupDevicePreset/BranchPresets")
    if found is None:
        raise RackError("Drum Rack preset has no BranchPresets")
    return found


def value(element: ET.Element | None, path: str, default: str = "") -> str:
    if element is None:
        return default
    found = element.find(path)
    if found is None:
        return default
    return found.get("Value", default)


def set_value(element: ET.Element, path: str, new: object) -> None:
    found = element.find(path)
    if found is None:
        raise RackError(f"missing {path} under {element.tag}")
    found.set("Value", str(new))


def branch_note(branch: ET.Element) -> int:
    return 128 - int(value(branch, "ZoneSettings/ReceivingNote", "0"))


def sample_paths(element: ET.Element) -> list[str]:
    return [value(ref, "FileRef/Path") for ref in element.iter("SampleRef") if value(ref, "FileRef/Path")]


def simple_part(branch: ET.Element) -> ET.Element | None:
    """The single sample zone of a pad whose instrument is a Simpler with one sample, else None."""
    if len(list(branch.iter("SampleRef"))) != 1:
        return None
    for preset in branch.findall("DevicePresets/AbletonDevicePreset"):
        simpler = preset.find("Device/OriginalSimpler")
        if simpler is not None:
            parts = simpler.findall("Player/MultiSampleMap/SampleParts/MultiSamplePart")
            return parts[0] if len(parts) == 1 else None
    return None


def device_names(branch: ET.Element) -> list[str]:
    names: list[str] = []
    presets = branch.find("DevicePresets")
    for preset in [] if presets is None else list(presets):
        device = preset.find("Device")
        if device is not None and len(device):
            names.append(device[0].tag)
        else:
            names.append(preset.tag)
    return names


def parse_rack(root: ET.Element, path: Path | None = None) -> Rack:
    drum_group(root)
    pads = []
    for branch in branches(root).findall("DrumBranchPreset"):
        pads.append(
            Pad(
                note=branch_note(branch),
                name=value(branch, "Name"),
                choke=int(value(branch, "ZoneSettings/ChokeGroup", "0")),
                devices=device_names(branch),
                samples=sample_paths(branch),
                simple=simple_part(branch) is not None,
            )
        )
    pads.sort(key=lambda p: p.note)
    return Rack(path=path, creator=root.get("Creator", ""), pads=pads)


def read_rack(path: Path) -> Rack:
    return parse_rack(read_xml(path), path)


# ---------------------------------------------------------------------------- template


def template_root() -> ET.Element:
    text = resources.files("drumrack_builder.templates").joinpath("drum_rack.xml").read_bytes()
    return ET.fromstring(text)


def scrub_file_ref(file_ref: ET.Element) -> None:
    for tag, empty in (
        ("RelativePathType", "0"),
        ("RelativePath", ""),
        ("Path", ""),
        ("LivePackName", ""),
        ("LivePackId", ""),
        ("OriginalFileSize", "0"),
        ("OriginalCrc", "0"),
    ):
        found = file_ref.find(tag)
        if found is not None:
            found.set("Value", empty)


def scrub(root: ET.Element) -> ET.Element:
    """Strip every file path, name and browser location so the XML says nothing about one machine."""
    for file_ref in root.iter("FileRef"):
        scrub_file_ref(file_ref)
    for tag in ("BrowserContentPath", "Name", "UserName", "Annotation"):
        for element in root.iter(tag):
            if element.get("Value") is not None:
                element.set("Value", "")
    for element in root.iter("LastModDate"):
        element.set("Value", "0")
    for last in root.iter("LastPresetRef"):
        for child in list(last):
            last.remove(child)
        ET.SubElement(last, "Value")
    return root


def make_template(source: ET.Element) -> ET.Element:
    """Reduce a Simpler-only Drum Rack to one scrubbed pad, the prototype for every new pad."""
    root = copy.deepcopy(source)
    group = branches(root)
    pads = group.findall("DrumBranchPreset")
    prototype = next((b for b in pads if simple_part(b) is not None and len(device_names(b)) == 1), None)
    if prototype is None:
        raise RackError("template source needs a pad holding only a one-sample Simpler")
    for branch in pads:
        if branch is not prototype:
            group.remove(branch)
    return scrub(root)


def prototype_branch(template: ET.Element) -> ET.Element:
    return branches(template).findall("DrumBranchPreset")[0]


# ---------------------------------------------------------------------------- building


def file_ref_values(sample: SampleFile, output: Path, user_library: Path | None) -> tuple[str, str]:
    """Pick Live's relative-path style: User Library samples stay portable across machines."""
    absolute = sample.path.resolve()
    if user_library is not None:
        library = user_library.expanduser().resolve()
        if absolute.is_relative_to(library):
            return REL_USER_LIBRARY, absolute.relative_to(library).as_posix()
    return REL_DOCUMENT, Path(os.path.relpath(absolute, output.parent.resolve())).as_posix()


def point_file_ref(file_ref: ET.Element, sample: SampleFile, output: Path, user_library: Path | None) -> None:
    kind, relative = file_ref_values(sample, output, user_library)
    set_value(file_ref, "RelativePathType", kind)
    set_value(file_ref, "RelativePath", relative)
    set_value(file_ref, "Path", str(sample.path.resolve()))
    set_value(file_ref, "OriginalFileSize", sample.size)
    # Live writes 0 here for samples it has not hashed yet (see the User Library's own presets); it
    # only uses the CRC to search for a missing file.
    set_value(file_ref, "OriginalCrc", 0)


def load_sample(
    branch: ET.Element, template_part: ET.Element, sample: SampleFile, output: Path, user_library: Path | None
) -> None:
    """Point a one-Simpler pad at a new sample, keeping its device chain, choke group and mixer."""
    old = simple_part(branch)
    if old is None:
        raise RackError(f"pad {branch_note(branch)} is not a one-sample Simpler")
    part = copy.deepcopy(template_part)
    for tag in PRESERVED_PART_TAGS:
        kept, fresh = old.find(tag), part.find(tag)
        if kept is not None and fresh is not None:
            part[list(part).index(fresh)] = copy.deepcopy(kept)
    part.set("Id", old.get("Id", "0"))
    set_value(part, "Name", sample.path.stem)
    set_value(part, "SampleStart", 0)
    set_value(part, "SampleEnd", sample.frames)
    for loop in ("SustainLoop", "ReleaseLoop"):
        set_value(part, f"{loop}/Start", 0)
        set_value(part, f"{loop}/End", sample.frames)
    ref = part.find("SampleRef")
    assert ref is not None
    for file_ref in ref.iter("FileRef"):
        point_file_ref(file_ref, sample, output, user_library)
    set_value(ref, "LastModDate", int(sample.mtime))
    set_value(ref, "DefaultDuration", sample.frames)
    set_value(ref, "DefaultSampleRate", sample.sample_rate)
    for content in ref.iter("BrowserContentPath"):
        content.set("Value", "")
    holder = branch.find(".//MultiSampleMap/SampleParts")
    assert holder is not None
    holder[list(holder).index(old)] = part
    # The pad's own SourceContext records where the sample was dragged from in Live's browser.
    for file_ref in branch.findall("SourceContext/SourceContext/OriginalFileRef/FileRef"):
        point_file_ref(file_ref, sample, output, user_library)
    for content in branch.findall("SourceContext/SourceContext/BrowserContentPath"):
        content.set("Value", "")


def build_rack(
    base: ET.Element | None,
    plan: list[PadPlan],
    output: Path,
    user_library: Path | None = None,
    template: ET.Element | None = None,
) -> ET.Element:
    """Return a new rack document: the base (or the template when None) with pads set as planned.

    Base pads that no plan entry names as its source are left out.
    """
    template = template if template is not None else template_root()
    proto = prototype_branch(template)
    proto_part = simple_part(proto)
    assert proto_part is not None
    root = copy.deepcopy(base if base is not None else template)
    group = branches(root)
    existing = {} if base is None else {branch_note(b): b for b in group.findall("DrumBranchPreset")}
    notes: set[int] = set()
    for item in plan:
        if not 0 <= item.note <= 127:
            raise RackError(f"pad note {item.note} is outside 0-127")
        if item.note in notes:
            raise RackError(f"pad note {item.note} appears twice in the plan")
        notes.add(item.note)
        if item.source_note is not None and item.source_note not in existing:
            raise RackError(f"the base rack has no pad on note {item.source_note}")
        if item.source_note is None and item.sample is None:
            raise RackError(f"new pad {note_name(item.note)} ({item.note}) needs a sample")
    for branch in list(group):
        group.remove(branch)
    for item in sorted(plan, key=lambda p: p.note):
        if item.source_note is None:
            branch = copy.deepcopy(proto)
            set_value(branch, "ZoneSettings/ChokeGroup", 0)
        else:
            branch = copy.deepcopy(existing[item.source_note])
            if item.sample is not None and simple_part(branch) is None:
                # A layered or nested pad cannot take one sample in place, so it gets a fresh Simpler
                # and keeps only its choke group.
                choke = value(branch, "ZoneSettings/ChokeGroup", "0")
                branch = copy.deepcopy(proto)
                set_value(branch, "ZoneSettings/ChokeGroup", choke)
        set_value(branch, "ZoneSettings/ReceivingNote", 128 - item.note)
        if item.sample is not None:
            load_sample(branch, proto_part, item.sample, output, user_library)
        set_value(branch, "Name", item.name)
        group.append(branch)
    for index, branch in enumerate(group):
        branch.set("Id", str(index))
    # Live offers to save over the preset named here, so a duplicate must not point back at its source.
    device = drum_group(root)
    for last in device.findall("LastPresetRef"):
        for child in list(last):
            last.remove(child)
        ET.SubElement(last, "Value")
    preset_ref = root.find("GroupDevicePreset/PresetRef")
    if preset_ref is not None:
        for file_ref in preset_ref.iter("FileRef"):
            scrub_file_ref(file_ref)
    return root


# ---------------------------------------------------------------------------- writing


def to_bytes(root: ET.Element) -> bytes:
    body = ET.tostring(root, encoding="unicode")
    return gzip.compress(('<?xml version="1.0" encoding="UTF-8"?>\n' + body).encode("utf-8"), mtime=0)


def write_rack(
    root: ET.Element,
    output: Path,
    *,
    overwrite: bool = False,
    backup_dir: Path | None = None,
    protected: list[Path] | None = None,
) -> Path | None:
    """Write atomically. An existing file is replaced only with ``overwrite`` and is backed up first.

    Returns the backup path when one was made.
    """
    output = output.expanduser()
    if output.suffix.lower() != ".adg":
        raise RackError(f"{output.name}: a Drum Rack preset must end in .adg")
    resolved = output.resolve()
    for source in protected or []:
        if source.expanduser().resolve() == resolved and not overwrite:
            raise RackError(f"{output} is the source rack; choose another name or confirm overwrite")
    backup = None
    if output.exists():
        if not overwrite:
            raise RackError(f"{output} already exists; confirm overwrite to replace it")
        if backup_dir is None:
            raise RackError("overwriting needs a backup folder")
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup = backup_dir / f"{time.strftime('%Y%m%d-%H%M%S')}-{output.name}"
        shutil.copy2(output, backup)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(f".{output.name}.tmp")
    temporary.write_bytes(to_bytes(root))
    os.replace(temporary, output)
    return backup


# ---------------------------------------------------------------------------- verifying


def canonical(element: ET.Element) -> str:
    return ET.canonicalize(ET.tostring(element, encoding="unicode"), strip_text=True)


def device_settings(root: ET.Element) -> str:
    """The rack-level device (macros, chain selector, view) minus the preset bookkeeping."""
    device = copy.deepcopy(drum_group(root))
    for last in device.findall("LastPresetRef"):
        device.remove(last)
    return canonical(device)


def verify_rack(output: Path, plan: list[PadPlan], base: ET.Element | None = None) -> VerifyReport:
    """Re-read a written rack and check pads, sample references and preserved settings."""
    report = VerifyReport(ok=True)
    try:
        root = read_xml(output)
        rack = parse_rack(root, output)
    except RackError as error:
        return VerifyReport(ok=False, problems=[str(error)])
    planned = {p.note: p for p in plan}
    found = {p.note: p for p in rack.pads}
    if set(found) != set(planned):
        report.problems.append(f"pads {sorted(found)} differ from the plan {sorted(planned)}")
    base_branches = {} if base is None else {branch_note(b): b for b in branches(base).findall("DrumBranchPreset")}
    out_branches = {branch_note(b): b for b in branches(root).findall("DrumBranchPreset")}
    for note, item in sorted(planned.items()):
        pad = found.get(note)
        if pad is None:
            continue
        entry: dict = {"note": note, "note_name": note_name(note), "name": pad.name, "samples": []}
        for path in pad.samples:
            exists = Path(path).is_file()
            entry["samples"].append({"path": path, "exists": exists})
            if not exists:
                report.problems.append(f"{note_name(note)}: sample missing at {path}")
        if not pad.samples:
            report.problems.append(f"{note_name(note)}: pad has no sample")
        if pad.name != item.name:
            report.problems.append(f"{note_name(note)}: name {pad.name!r} is not {item.name!r}")
        original = None if item.source_note is None else base_branches.get(item.source_note)
        if item.sample is not None:
            expected = str(item.sample.path.resolve())
            if pad.samples != [expected]:
                report.problems.append(f"{note_name(note)}: expected sample {expected}, found {pad.samples}")
            if original is None:
                report.added_pads += 1
                entry["status"] = "added"
            else:
                report.replaced_pads += 1
                entry["status"] = "replaced"
                if simple_part(original) is not None and device_names(original) != device_names(out_branches[note]):
                    report.problems.append(f"{note_name(note)}: device chain changed while replacing the sample")
        elif original is None:
            report.problems.append(f"{note_name(note)}: kept pad has no source pad")
        else:
            a, b = copy.deepcopy(original), copy.deepcopy(out_branches[note])
            for branch in (a, b):
                branch.set("Id", "0")
                set_value(branch, "Name", "")
                set_value(branch, "ZoneSettings/ReceivingNote", 0)
            if canonical(a) != canonical(b):
                report.problems.append(f"{note_name(note)}: kept pad's settings changed")
            report.preserved_pads += 1
            source = item.source_note
            assert source is not None
            entry["status"] = "kept" if source == note else f"moved from {note_name(source)}"
        report.pads.append(entry)
    used = {p.source_note for p in plan if p.source_note is not None}
    report.removed_pads = len(set(base_branches) - used)
    if base is not None and device_settings(base) != device_settings(root):
        report.device_settings_preserved = False
        report.problems.append("rack-level settings (macros, chain selector) changed")
    report.ok = not report.problems
    return report
