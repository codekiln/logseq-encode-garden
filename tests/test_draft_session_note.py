import json
import hashlib
from datetime import date
import gzip
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.draft_session_note import (
    description_from_note,
    explicit_description,
    find_note,
    note_facts,
    transcript_quality,
    draft,
    project_date,
    ableton_tracks,
    verify_public_audio,
)


class DraftSessionNoteTests(unittest.TestCase):
    def test_logseq_manual_link_is_evidence_without_episode_specific_rules(self):
        with tempfile.TemporaryDirectory() as temporary:
            note = Path(temporary) / "session.md"
            note.write_text(
                "- # [[GitP/Session/26/09/24 Thu]] with Microfreak and Launchpad\n"
                "\t- On the [[Microfreak]], started with [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]] on initialized patch.\n",
                encoding="utf-8",
            )
            devices, observations, references = note_facts(note)
            self.assertEqual(description_from_note(devices), "A MicroFreak and Launchpad session.")
            self.assertEqual(observations, ["On the Microfreak, started with Two Op.FM on initialized patch."])
            self.assertEqual(references, ["Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM"])

    def test_repeated_asr_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            transcript = Path(temporary) / "transcript.json"
            transcript.write_text(
                json.dumps({"segments": [{"text": "Thank you."}] * 25 + [{"text": "This is weird."}]}),
                encoding="utf-8",
            )
            self.assertFalse(transcript_quality(transcript)[0])

    def test_note_discovery_uses_contents_when_filename_lacks_gitpa(self):
        with tempfile.TemporaryDirectory() as temporary:
            pages = Path(temporary) / "pages"
            pages.mkdir()
            note = pages / "Music___Composition___Log___26___09___25 Fri.md"
            note.write_text("- Podcast title: GitP.26.09.25\n\t- Description: A synth session.\n", encoding="utf-8")
            self.assertEqual(find_note(Path(temporary), date(2026, 9, 25), None), note)
            self.assertEqual(explicit_description(note), "A synth session.")

    def fixture(self, root):
        project = root / "GitP26.09.24 Project"
        project.mkdir()
        (project / "GitP.26.09.24.mp3").write_bytes(b"prepared audio")
        with gzip.open(project / "Session.als", "wb") as target:
            target.write(b'<Ableton><LiveSet><Tracks><AudioTrack><Name><EffectiveName Value="Commentary"/></Name></AudioTrack><MidiTrack><Name><EffectiveName Value="MicroFreak"/></Name><ProgramChange Value="-1"/></MidiTrack></Tracks></LiveSet></Ableton>')
        garden = root / "garden"
        (garden / "pages").mkdir(parents=True)
        note = garden / "pages" / "Music___Composition___Log___26___09___24 Thu.md"
        note.write_text("- Podcast title: GitP.26.09.24\n\t- Description: A synth session.\n")
        return project, garden, note

    def test_ableton_track_names_and_program_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            project, _, _ = self.fixture(Path(temporary))
            self.assertEqual(project_date(project), date(2026, 9, 24))
            self.assertEqual(ableton_tracks(project), (["Commentary (audio)", "MicroFreak (MIDI)"], False))

    def test_handoff_is_production_metadata_without_publication_identity(self):
        with tempfile.TemporaryDirectory() as temporary:
            project, garden, note = self.fixture(Path(temporary))
            original = (project / "GitP.26.09.24.mp3").read_bytes()
            with patch("scripts.draft_session_note.duration_seconds", return_value=180):
                output = draft(project, garden, note)
            record = json.loads(output.with_name("handoff.json").read_text())
            self.assertEqual(record, {"recorded_on": "2026-09-24", "episode_title": "GitP.26.09.24", "description": "A synth session."})
            self.assertIn("MP3 SHA-256", output.read_text())
            self.assertEqual((project / "GitP.26.09.24.mp3").read_bytes(), original)
            self.assertFalse((garden / "pages" / "Ceremony___2026___09___24.md").exists())

    def test_verified_media_attaches_only_public_enclosure_fields(self):
        with tempfile.TemporaryDirectory() as temporary:
            project, garden, note = self.fixture(Path(temporary))
            with patch("scripts.draft_session_note.duration_seconds", return_value=180), patch("scripts.draft_session_note.verify_public_audio") as verify:
                output = draft(project, garden, note, audio_url="https://example.com/audio.mp3")
            record = json.loads(output.with_name("handoff.json").read_text())
            self.assertEqual(record["audio_url"], "https://example.com/audio.mp3")
            self.assertEqual(record["audio_length"], 14)
            self.assertEqual(record["audio_type"], "audio/mpeg")
            verify.assert_called_once()

    def test_existing_evidence_and_handoff_are_preserved_before_inspection(self):
        for existing in ("session-note.md", "handoff.json"):
            with self.subTest(existing=existing), tempfile.TemporaryDirectory() as temporary:
                project, garden, note = self.fixture(Path(temporary))
                output = garden / "assets" / "GitP" / "Session" / "2026" / "09" / "24"
                output.mkdir(parents=True)
                (output / existing).write_text("Human edits")
                with patch("scripts.draft_session_note.duration_seconds") as inspect:
                    with self.assertRaisesRegex(ValueError, "Output already exists"):
                        draft(project, garden, note)
                    inspect.assert_not_called()
                self.assertEqual((output / existing).read_text(), "Human edits")
                self.assertEqual(len(list(output.iterdir())), 1)

    def test_invalid_upload_leaves_no_partial_outputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            project, garden, note = self.fixture(Path(temporary))
            with patch("scripts.draft_session_note.duration_seconds", return_value=180), patch("scripts.draft_session_note.verify_public_audio", side_effect=ValueError("length differs")):
                with self.assertRaisesRegex(ValueError, "length differs"):
                    draft(project, garden, note, audio_url="https://example.com/audio.mp3")
            self.assertFalse((garden / "assets").exists())

    def test_transcript_findings_stay_in_evidence_and_not_public_copy(self):
        with tempfile.TemporaryDirectory() as temporary:
            project, garden, note = self.fixture(Path(temporary))
            transcript = Path(temporary) / "speech.json"
            transcript.write_text(json.dumps({"segments": [{"text": "Thank you."}] * 25}))
            with patch("scripts.draft_session_note.duration_seconds", return_value=180):
                output = draft(project, garden, note, transcript)
            self.assertIn("Speech recognition: rejected", output.read_text())
            self.assertEqual(json.loads(output.with_name("handoff.json").read_text())["description"], "A synth session.")

    def test_permanent_url_validation_happens_before_network(self):
        with tempfile.TemporaryDirectory() as temporary:
            mp3 = Path(temporary) / "audio.mp3"
            mp3.write_bytes(b"abc")
            for url in ("http://example.com/audio.mp3", "https://example.com/audio.mp3?token=x", ("https://" + "fixture-user" + ":" + "fixture-pass" + "@example.com/audio.mp3"), "https://example.com/audio.mp3#fragment"):
                with self.subTest(url=url), patch("scripts.draft_session_note.urlopen") as network:
                    with self.assertRaisesRegex(ValueError, "permanent public HTTPS"):
                        verify_public_audio(url, mp3)
                    network.assert_not_called()

    def test_public_length_range_and_audio_content_checks(self):
        from unittest.mock import MagicMock
        with tempfile.TemporaryDirectory() as temporary:
            mp3 = Path(temporary) / "audio.mp3"
            mp3.write_bytes(b"abc")
            def response(status, headers, body=b""):
                result = MagicMock()
                result.__enter__.return_value = result
                result.status = status
                result.headers = headers
                result.read.return_value = body
                return result
            head = response(200, {"Content-Type": "audio/mpeg", "Content-Length": "3"})
            ranged = response(206, {"Content-Range": "bytes 0-2/3"}, b"abc")
            with patch("scripts.draft_session_note.urlopen", side_effect=[head, ranged]):
                verify_public_audio("https://example.com/audio.mp3", mp3)
            for bad_range in (response(200, {}, b"abc"), response(206, {"Content-Range": "bytes 0-2/3"}, b"xyz")):
                with patch("scripts.draft_session_note.urlopen", side_effect=[head, bad_range]):
                    with self.assertRaises(ValueError):
                        verify_public_audio("https://example.com/audio.mp3", mp3)
            head.headers["x-bz-content-sha1"] = hashlib.sha1(b"wrong content").hexdigest()
            with patch("scripts.draft_session_note.urlopen", return_value=head):
                with self.assertRaisesRegex(ValueError, "checksum differs"):
                    verify_public_audio("https://example.com/audio.mp3", mp3)
            del head.headers["x-bz-content-sha1"]
            head.headers["Content-Length"] = "4"
            with patch("scripts.draft_session_note.urlopen", return_value=head):
                with self.assertRaisesRegex(ValueError, "length differs"):
                    verify_public_audio("https://example.com/audio.mp3", mp3)


if __name__ == "__main__":
    unittest.main()
