"""Synthetic tests for read-only MicroFreak field interpretation."""

import copy
import unittest

import semantics


def field(name, descriptor, raw):
    return {"name": name, "descriptor": descriptor,
            "value_le_unsigned": raw,
            "value_le_signed": raw if raw < 0x8000 else raw - 0x10000,
            "raw_hex": bytes((descriptor, raw & 255, raw >> 8)).hex()}


class SemanticsTest(unittest.TestCase):
    def test_saved_index_two_is_superwave_and_three_controls_are_ordered(self):
        source = [field("VCO.Type", 22, 2979), field("VCO.Param1", 3, 10922),
                  field("VCO.Param2", 238, 2500), field("VCO.Param3", 238, 5119)]
        original = copy.deepcopy(source)
        result = semantics.interpret_fields(source)
        self.assertEqual(source, original)
        self.assertEqual(result["oscillator"]["index"], 2)
        self.assertEqual(result["oscillator"]["model"], "SuperWave")
        self.assertEqual([item["label"] for item in result["fields"][1:]],
                         ["Wave", "Detune", "Volume"])
        self.assertEqual(result["fields"][1]["kind"], "metadata_scaled_integer")
        self.assertEqual(result["fields"][1]["value"], 1)
        self.assertEqual(result["fields"][2]["kind"], "normalized_0_1")
        self.assertNotIn("raw_hex", result["fields"][2])

    def test_wavetable_is_saved_index_three(self):
        result = semantics.interpret_fields([field("VCO.Type", 22, round(3 * 32767 / 22)),
                                            field("VCO.Param1", 15, 32767),
                                            field("VCO.Param2", 238, 0),
                                            field("VCO.Param3", 238, 0)])
        self.assertEqual(result["oscillator"]["model"], "Wavetable")
        self.assertEqual([item["label"] for item in result["fields"][1:]],
                         ["Table", "Position", "Chorus"])

    def test_firmware_five_order_places_vocoder_after_noise(self):
        result = semantics.interpret_fields([field("VCO.Type", 22, round(14 * 32767 / 22)),
                                            field("VCO.Param1", 238, 0)])
        self.assertEqual(result["oscillator"]["model"], "Vocoder")
        self.assertEqual(result["fields"][1]["label"], "Wave")
        result = semantics.interpret_fields([field("VCO.Type", 22, 32767)])
        self.assertEqual(result["oscillator"]["model"], "Hit Grains")

    def test_missing_chords_third_control_name_stays_unassigned(self):
        result = semantics.interpret_fields([field("VCO.Type", 22, round(10 * 32767 / 22)),
                                            field("VCO.Param1", 238, 0),
                                            field("VCO.Param2", 238, 0),
                                            field("VCO.Param3", 238, 0)])
        self.assertEqual([item["label"] for item in result["fields"][1:]],
                         ["Type", "Inv/Transp", "VCO.Param3"])
        self.assertNotIn("arturia_guide_control_order", result["fields"][3]["evidence"])

    def test_conservative_domains_and_raw_fallback(self):
        result = semantics.interpret_fields([
            field("Co1.LFO", 0xee, 0xc000),
            field("Seq.Length", 12, 32767),
            field("Kbd.Foo", 0xf7, 0x3f80),
            field("VCF.Cutoff", 0xee, 16384),
            field("Unknown.Value", 0xee, 45000),
        ])
        values = {item["name"]: item for item in result["fields"]}
        self.assertEqual(values["Co1.LFO"]["kind"], "normalized_minus_1_1")
        self.assertLess(values["Co1.LFO"]["value"], 0)
        self.assertEqual(values["Seq.Length"]["value"], 16)
        self.assertEqual(values["Seq.Length"]["range"], [4, 16])
        self.assertEqual(values["Kbd.Foo"]["value"], -1)
        self.assertEqual(values["VCF.Cutoff"]["kind"], "normalized_0_1")
        self.assertEqual(values["Unknown.Value"]["kind"], "raw_only")
        self.assertIsNone(result["oscillator"])

    def test_unsupported_type_does_not_assign_model_specific_names(self):
        result = semantics.interpret_fields([field("VCO.Type", 22, 50000),
                                            field("VCO.Param1", 238, 0)])
        self.assertIsNone(result["oscillator"])
        self.assertEqual(result["fields"][1]["label"], "VCO.Param1")
        self.assertEqual(result["fields"][0]["kind"], "raw_only")


if __name__ == "__main__":
    unittest.main()
