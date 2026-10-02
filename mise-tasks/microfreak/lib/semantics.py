"""Read-only interpretations of named MicroFreak saved-preset fields.

The engine-index formula and conservative value classes come from Freakout's
firmware research and structured-payload parser:
https://github.com/kmorrill/freakout/blob/main/docs/microfreak-firmware-notes.md
https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py

Control names come from the garden's Arturia user-guide transcription at
pages/Microfreak___UG___06 Dig Osc___03 Types___*.md. A value's ``kind``
states what its number means; a normalized number is not an OLED reading.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence


# Firmware 5 runtime indices are one-based: Vocoder is 14 and Hit Grains 22.
# Vocoder was added before the firmware-5 engines, so the manual's page order
# differs after Noise. Index zero has no documented engine name.
ENGINE_MODELS = (
    None,
    "BasicWaves", "SuperWave", "Wavetable", "Harmo", "KarplusStr",
    "V.Analog", "Waveshaper", "Two Op. FM", "Formant", "Chords",
    "Speech", "Modal", "Noise", "Vocoder", "Bass", "SawX", "Harm",
    "WaveUser", "Sample", "Scan Grains", "Cloud Grains", "Hit Grains",
)

# These are the three physical oscillator controls, in Wave/Timbre/Shape
# position order. Chords' third control has no name in the garden guide.
MODEL_CONTROLS = {
    "BasicWaves": ("Morph", "Sym", "Sub"),
    "SuperWave": ("Wave", "Detune", "Volume"),
    "Wavetable": ("Table", "Position", "Chorus"),
    "Harmo": ("Content", "Sculpting", "Chorus"),
    "KarplusStr": ("Bow", "Position", "Decay"),
    "V.Analog": ("Detune", "Shape", "Wave"),
    "Waveshaper": ("Wave", "Amount", "Asym"),
    "Two Op. FM": ("Ratio", "Amount", "Shape"),
    "Formant": ("Interval", "Formant", "Shape"),
    "Chords": ("Type", "Inv/Transp", None),
    "Speech": ("Type", "Timbre", "Word"),
    "Modal": ("Inharm", "Timbre", "Decay"),
    "Noise": ("Wave", "Timbre", "Shape"),
    "Vocoder": ("Wave", "Timbre", "Shape"),
    "Bass": ("Saturate", "Fold", "Noise"),
    "SawX": ("Saw Mod", "Shape", "Noise"),
    "Harm": ("Spread", "Rectification", "Noise"),
    "WaveUser": ("Table", "Position", "Bitdepth"),
    "Sample": ("Start", "Length", "Loop"),
    "Scan Grains": ("Scan", "Density", "Chaos"),
    "Cloud Grains": ("Starts", "Density", "Chaos"),
    "Hit Grains": ("Start", "Density", "Shape"),
}

_BIPOLAR_GROUPS = {f"Co{number}" for number in range(1, 8)}
_BIPOLAR_NAMES = {"EG1", "EG2", "LFO", "Xpr", "Key"}
_NORMALIZED_TAGS = {
    "VCO.Param1", "VCO.Param2", "VCO.Param3", "VCF.Cutoff", "VCF.Reso",
    "EG1.RiseLvl", "EG1.RiseSlp", "EG1.FallLvl", "EG1.Hold",
    "EG1.FallSlp", "EG1.Amount", "Kbd.Glide", "Arp.Rate", "Arp.Spice",
    "Arp.Dice", "LFO.Rate", "EG2.Attack", "EG2.DecRel", "EG2.Sustain",
    "Gen.Volume", "Gen.UniSprd",
}
_METADATA_INTEGER_OFFSETS = {"Seq.Length": 4, "Seq.GateLen": 10}
_FIELD_LABELS = {"VCO.Type": "Oscillator Type", "VCF.Cutoff": "Filter Cutoff",
                 "VCF.Reso": "Filter Resonance"}


def _field_value(field: Mapping[str, object]) -> dict[str, object]:
    """Return an interpretation that never changes the parser's raw field."""
    name = str(field["name"])
    descriptor = int(field["descriptor"])
    raw = int(field["value_le_unsigned"])
    signed = int(field["value_le_signed"])
    if not 0 <= descriptor <= 255 or not 0 <= raw <= 65535:
        raise ValueError(f"Invalid parsed field {name}")

    if name == "VCO.Type" and 1 <= descriptor <= 127 and raw <= 32767:
        index = round(raw * descriptor / 32767)
        model = ENGINE_MODELS[index] if index < len(ENGINE_MODELS) else None
        return {"kind": "engine_index", "value": index, "range": [0, descriptor],
                "model": model, "evidence": ["freakout_fw5_saved_type_formula",
                                               "freakout_fw5_engine_order"]}
    group, _, short_name = name.partition(".")
    if group in _BIPOLAR_GROUPS and short_name in _BIPOLAR_NAMES:
        return {"kind": "normalized_minus_1_1",
                "value": max(-1.0, min(1.0, signed / 32767)),
                "range": [-1.0, 1.0], "evidence": ["freakout_structured_scaling"]}
    if descriptor == 0xF7 and raw <= 0x7FFF:
        return {"kind": "signed_offset_shift7", "value": (raw - 0x4000) >> 7,
                "range": [-128, 127], "evidence": ["freakout_structured_scaling"]}
    if 1 <= descriptor <= 127 and raw <= 32767:
        offset = _METADATA_INTEGER_OFFSETS.get(name, 0)
        return {"kind": "metadata_scaled_integer", "value": round(raw * descriptor / 32767) + offset,
                "range": [offset, descriptor + offset],
                "evidence": ["freakout_structured_scaling"]}
    if name in _NORMALIZED_TAGS and raw <= 32767:
        return {"kind": "normalized_0_1", "value": raw / 32767,
                "range": [0.0, 1.0], "evidence": ["freakout_structured_scaling"]}
    return {"kind": "raw_only", "value": raw, "range": [0, 65535],
            "evidence": ["saved_field_raw_value"]}


def interpret_fields(fields: Sequence[Mapping[str, object]]) -> dict[str, object]:
    """Interpret ``parse_parameters(payload)['fields']`` without mutating it.

    The return value keeps interpretations separate from raw parser records.
    Model-specific labels name controls by their physical position. Numeric
    readings are normalized or metadata-scaled according to their ``kind``.
    """
    type_field = next((field for field in fields if field["name"] == "VCO.Type"), None)
    type_value = _field_value(type_field) if type_field is not None else None
    model = type_value.get("model") if type_value is not None else None
    oscillator = ({"index": type_value["value"], "model": model,
                   "evidence": type_value["evidence"]}
                  if type_value is not None and type_value["kind"] == "engine_index" else None)
    interpretations = []
    for field in fields:
        name = str(field["name"])
        item = {"name": name, "label": _FIELD_LABELS.get(name, name), **_field_value(field)}
        if name.startswith("VCO.Param") and name[-1:] in ("1", "2", "3"):
            position = int(name[-1]) - 1
            control = MODEL_CONTROLS[model][position] if model in MODEL_CONTROLS else None
            if control is not None:
                item["label"] = control
                item["evidence"] = [*item["evidence"], "arturia_guide_control_order"]
            item["oscillator_control_position"] = position + 1
        interpretations.append(item)
    return {"oscillator": oscillator, "fields": interpretations}
