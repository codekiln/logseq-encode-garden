import gzip
from pathlib import Path

import pytest

from drumrack_builder import adg
from tests.conftest import digest, sample_file


def kit(library: Path) -> list[Path]:
    return sorted((library / "Samples" / "Kit").glob("*.wav"))


def test_live_note_names_and_inverted_receiving_note(base_rack: Path):
    assert adg.note_name(36) == "C1"
    assert adg.note_name(60) == "C3"
    assert adg.note_name(0) == "C-2"
    root = adg.read_xml(base_rack)
    first = adg.branches(root).findall("DrumBranchPreset")[0]
    assert adg.value(first, "ZoneSettings/ReceivingNote") == "92"
    assert adg.branch_note(first) == 36


def test_template_has_one_scrubbed_pad():
    template = adg.template_root()
    pads = adg.branches(template).findall("DrumBranchPreset")
    assert len(pads) == 1
    assert adg.simple_part(pads[0]) is not None
    paths = [e.get("Value") for e in template.iter() if e.tag in ("Path", "RelativePath", "BrowserContentPath")]
    assert paths and all(p == "" for p in paths)
    text = (Path(adg.__file__).parent / "templates" / "drum_rack.xml").read_text()
    assert "/Users/" not in text and "/home/" not in text


def test_parse_reports_pads_samples_and_layering(base_rack: Path):
    rack = adg.read_rack(base_rack)
    assert [p.note for p in rack.pads] == [36, 37, 38, 39, 48]
    assert rack.pad(37).choke == 2
    assert rack.pad(37).name == "pad 1"
    assert rack.pad(36).label.startswith("tone 00")
    assert rack.pad(48).simple is False and len(rack.pad(48).samples) == 2
    assert all(Path(s).is_file() for p in rack.pads for s in p.samples)


def test_new_rack_from_template(tmp_path: Path, library: Path):
    samples = kit(library)
    output = tmp_path / "out" / "New.adg"
    plan = [adg.PadPlan(note=40 + i, name=f"n{i}", sample=sample_file(s)) for i, s in enumerate(samples[:3])]
    adg.write_rack(adg.build_rack(None, plan, output, user_library=library), output)
    assert output.read_bytes()[:2] == b"\x1f\x8b"
    report = adg.verify_rack(output, plan)
    assert report.ok, report.problems
    assert report.added_pads == 3
    root = adg.read_xml(output)
    part = adg.simple_part(adg.branches(root).findall("DrumBranchPreset")[0])
    frames = sample_file(samples[0]).frames
    assert adg.value(part, "SampleEnd") == str(frames)
    assert adg.value(part, "SampleRef/DefaultDuration") == str(frames)
    assert adg.value(part, "SampleRef/FileRef/RelativePathType") == adg.REL_USER_LIBRARY
    assert adg.value(part, "SampleRef/FileRef/RelativePath") == f"Samples/Kit/{samples[0].name}"


def test_sample_outside_user_library_is_relative_to_the_preset(tmp_path: Path, make_tone):
    outside = make_tone(tmp_path / "elsewhere" / "hit.wav")
    output = tmp_path / "presets" / "deep" / "R.adg"
    plan = [adg.PadPlan(note=36, sample=sample_file(outside))]
    root = adg.build_rack(None, plan, output, user_library=tmp_path / "User Library")
    part = adg.simple_part(adg.branches(root)[0])
    assert adg.value(part, "SampleRef/FileRef/RelativePathType") == adg.REL_DOCUMENT
    assert adg.value(part, "SampleRef/FileRef/RelativePath") == "../../elsewhere/hit.wav"
    assert adg.value(part, "SampleRef/FileRef/Path") == str(outside.resolve())


def test_duplicate_keeps_every_pad_and_rack_setting(tmp_path: Path, base_rack: Path, library: Path):
    base = adg.read_xml(base_rack)
    plan = [adg.PadPlan(note=p.note, name=p.name, source_note=p.note) for p in adg.parse_rack(base).pads]
    output = tmp_path / "Copy.adg"
    adg.write_rack(adg.build_rack(base, plan, output, user_library=library), output)
    report = adg.verify_rack(output, plan, base)
    assert report.ok, report.problems
    assert report.preserved_pads == 5 and report.device_settings_preserved
    copy = adg.read_xml(output)
    assert copy.find("GroupDevicePreset/Device/DrumGroupDevice/MacroControls.0/Manual").get("Value") == "42"


def test_replacing_a_sample_keeps_the_pads_settings(tmp_path: Path, base_rack: Path, library: Path):
    base = adg.read_xml(base_rack)
    new = sample_file(kit(library)[5])
    plan = [adg.PadPlan(note=38, name="swapped", source_note=38, sample=new)]
    output = tmp_path / "Swap.adg"
    adg.write_rack(adg.build_rack(base, plan, output, user_library=library), output)
    assert adg.verify_rack(output, plan, base).ok
    branch = adg.branches(adg.read_xml(output))[0]
    part = adg.simple_part(branch)
    assert adg.value(part, "Detune") == "7"  # the old zone's tuning stays
    assert adg.value(branch, "DevicePresets/AbletonDevicePreset/Device/OriginalSimpler/Globals/NumVoices") == "3"
    assert adg.value(part, "SampleEnd") == str(new.frames)
    assert adg.value(part, "Name") == new.path.stem
    assert adg.parse_rack(adg.read_xml(output)).pads[0].samples == [str(new.path.resolve())]


def test_moving_and_removing_pads(tmp_path: Path, base_rack: Path, library: Path):
    base = adg.read_xml(base_rack)
    plan = [adg.PadPlan(note=100, name="moved", source_note=37), adg.PadPlan(note=36, source_note=36)]
    output = tmp_path / "Moved.adg"
    adg.write_rack(adg.build_rack(base, plan, output, user_library=library), output)
    report = adg.verify_rack(output, plan, base)
    assert report.ok, report.problems
    assert report.removed_pads == 3
    rack = adg.read_rack(output)
    assert [p.note for p in rack.pads] == [36, 100]
    assert rack.pad(100).choke == 2  # the choke group moves with the pad


def test_layered_pad_gets_a_fresh_simpler_and_keeps_its_choke(tmp_path: Path, base_rack: Path, library: Path):
    base = adg.read_xml(base_rack)
    plan = [adg.PadPlan(note=48, source_note=48, sample=sample_file(kit(library)[0]))]
    output = tmp_path / "Layer.adg"
    adg.write_rack(adg.build_rack(base, plan, output, user_library=library), output)
    pad = adg.read_rack(output).pad(48)
    assert pad.simple and pad.choke == 1 and len(pad.samples) == 1


def test_duplicate_does_not_point_back_at_its_source(tmp_path: Path, base_rack: Path, library: Path):
    base = adg.read_xml(base_rack)
    last = base.find("GroupDevicePreset/Device/DrumGroupDevice/LastPresetRef")
    last.clear()
    value = adg.ET.SubElement(last, "Value")
    ref = adg.ET.SubElement(adg.ET.SubElement(adg.ET.SubElement(value, "FilePresetRef"), "FileRef"), "Path")
    ref.set("Value", str(base_rack))
    out = adg.build_rack(base, [adg.PadPlan(note=36, source_note=36)], tmp_path / "x.adg", library)
    assert str(base_rack) not in adg.ET.tostring(out, encoding="unicode")


@pytest.mark.parametrize(
    "plan, message",
    [
        ([adg.PadPlan(note=36, source_note=36), adg.PadPlan(note=36, source_note=37)], "twice"),
        ([adg.PadPlan(note=128)], "outside"),
        ([adg.PadPlan(note=36)], "needs a sample"),
        ([adg.PadPlan(note=36, source_note=90)], "no pad on note 90"),
    ],
)
def test_invalid_plans_are_refused(base_rack: Path, tmp_path: Path, plan, message):
    with pytest.raises(adg.RackError, match=message):
        adg.build_rack(adg.read_xml(base_rack), plan, tmp_path / "x.adg")


def test_write_refuses_to_replace_without_overwrite_and_backs_up(tmp_path: Path, base_rack: Path):
    root = adg.read_xml(base_rack)
    before = digest(base_rack)
    with pytest.raises(adg.RackError, match="already exists"):
        adg.write_rack(root, base_rack, backup_dir=tmp_path / "b")
    with pytest.raises(adg.RackError, match="source rack"):
        adg.write_rack(root, base_rack, protected=[base_rack])
    assert digest(base_rack) == before
    with pytest.raises(adg.RackError, match=".adg"):
        adg.write_rack(root, tmp_path / "rack.xml")
    backup = adg.write_rack(root, base_rack, overwrite=True, backup_dir=tmp_path / "b")
    assert backup is not None and digest(backup) == before


def test_verify_catches_a_missing_sample_and_changed_settings(
    tmp_path: Path, base_rack: Path, library: Path, make_tone
):
    victim = make_tone(tmp_path / "gone.wav")
    plan = [adg.PadPlan(note=36, sample=sample_file(victim))]
    output = tmp_path / "Gone.adg"
    adg.write_rack(adg.build_rack(None, plan, output, library), output)
    victim.unlink()
    report = adg.verify_rack(output, plan)
    assert not report.ok and any("missing" in p for p in report.problems)

    base = adg.read_xml(base_rack)
    keep = [adg.PadPlan(note=36, source_note=36)]
    root = adg.build_rack(base, keep, output, library)
    adg.set_value(adg.branches(root)[0], "ZoneSettings/ChokeGroup", 5)
    adg.write_rack(root, output, overwrite=True, backup_dir=tmp_path / "b")
    report = adg.verify_rack(output, keep, base)
    assert any("settings changed" in p for p in report.problems)


def test_read_refuses_non_racks(tmp_path: Path):
    junk = tmp_path / "junk.adg"
    junk.write_bytes(
        gzip.compress(
            b"<Ableton><GroupDevicePreset><Device><InstrumentGroupDevice/></Device></GroupDevicePreset></Ableton>"
        )
    )
    with pytest.raises(adg.RackError, match="not an Ableton Drum Rack"):
        adg.read_rack(junk)
    junk.write_bytes(b"\x1f\x8bnot gzip")
    with pytest.raises(adg.RackError):
        adg.read_rack(junk)
