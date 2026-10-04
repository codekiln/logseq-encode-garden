import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import wave

spec = importlib.util.spec_from_file_location("assets", Path(__file__).parents[1] / "lib/assets.py")
assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assets)


class Names(unittest.TestCase):
    def test_roundtrip_spelling(self):
        self.assertEqual(assets.filename("Course Name/Asset/Audio/Lesson/mp3"), "Course Name___Asset___Audio___Lesson.mp3")

    def test_ambiguous_names_rejected(self):
        for page in ["Course/Asset/../wav", "Course/Asset/a___b/mp3", "Course//Asset/mp3", "Course/Asset/A:Z/mp3", "Course/Asset/MP3"]:
            with self.subTest(page=page), self.assertRaises(ValueError):
                assets.filename(page)


class Conversion(unittest.TestCase):
    def test_changed_wav_requires_rebuild(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            helper = root / "mise-tasks/asset/lib/assets.py"
            helper.parent.mkdir(parents=True)
            shutil.copy2(assets.__file__, helper)
            prepare = root / "mise-tasks/gitpa/media/prepare"
            prepare.parent.mkdir(parents=True)
            shutil.copy2(assets.ROOT / "mise-tasks/gitpa/media/prepare", prepare)
            subprocess.run(["git", "init", "-q", temp], check=True)
            subprocess.run([sys.executable, "-m", "dvc", "init", "-q"], cwd=root, check=True)
            (root / ".gitignore").write_text("assets/.remote/*\n!assets/.remote/*.dvc\n")
            folder = root / "assets/.remote"
            folder.mkdir(parents=True)
            source = folder / "Lesson___Asset___Full.wav"
            def recording(frames):
                with wave.open(str(source), "wb") as wav:
                    wav.setnchannels(1)
                    wav.setsampwidth(2)
                    wav.setframerate(44100)
                    wav.writeframes(b"\x01\x00" * frames)
            recording(44100)
            command = [sys.executable, str(helper), "convert", "Lesson/Asset/Full/wav", "Lesson/Asset/Full/mp3"]
            subprocess.run(command, cwd=root, check=True, capture_output=True)
            output = folder / "Lesson___Asset___Full.mp3"
            original = output.read_bytes()
            recording(88200)
            status = subprocess.check_output([sys.executable, "-m", "dvc", "status"], cwd=root, text=True)
            self.assertIn("changed deps", status)
            subprocess.run(command, cwd=root, check=True, capture_output=True)
            self.assertNotEqual(original, output.read_bytes())
            self.assertIn("up to date", subprocess.check_output([sys.executable, "-m", "dvc", "status"], cwd=root, text=True))
            self.assertIn("stages:", (root / "dvc.lock").read_text())


if __name__ == "__main__":
    unittest.main()
