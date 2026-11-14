import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("report", Path(__file__).parents[1] / "lib/report.py")
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)

PUBLIC = "https://example.com/g"
MOUNTS = {
    "g": {"path": "assets/.remote/g", "bucket": "g", "dvc": "garden", "public": PUBLIC},
    "p": {"path": "assets/.remote/p", "bucket": "p", "dvc": "private"},
}


class Fixture(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "pages").mkdir()
        (self.root / "journals").mkdir()
        folder = self.root / "assets/.remote/g"
        folder.mkdir(parents=True)
        (folder / "A___Asset___Pic.png").write_text("image")
        (folder / "A___Asset___Pic.png.dvc").write_text("outs: []\n")
        (folder / "A___Asset___Song.mp3.dvc").write_text("outs: []\n")
        (self.root / "pages/A.md").write_text(
            f"- ![pic]({PUBLIC}/A___Asset___Pic.png)\n"
            "- ![pic](../assets/.remote/g/A___Asset___Pic.png)\n"
            f"- see {PUBLIC}/A___Asset___Song.mp3.\n"
            f"- ![old]({PUBLIC}/Screen%20Shot.png?raw=1)\n"
        )
        (self.root / "journals/2026_11_12.md").write_text(
            "- ![spaced](<../assets/.remote/g/Screen Shot.png>)\n"
            "- [secret](../assets/.remote/p/B___Asset___Note.pdf)\n"
            f"- {PUBLIC}/nested/folder.png\n"
            f"- `{PUBLIC}/<page-derived filename>` and `../assets/.remote/g/`\n"
        )

    def table(self, **kwargs):
        return {(row["mount"], row["file"]): row for row in report.rows(self.root, MOUNTS, **kwargs)}

    def test_every_link_form_is_found(self):
        self.assertEqual(set(self.table()), {
            ("g", "A___Asset___Pic.png"), ("g", "A___Asset___Song.mp3"),
            ("g", "Screen Shot.png"), ("p", "B___Asset___Note.pdf"),
        })

    def test_columns(self):
        table = self.table()
        pic, song, shot, note = (table[key] for key in [("g", "A___Asset___Pic.png"), ("g", "A___Asset___Song.mp3"), ("g", "Screen Shot.png"), ("p", "B___Asset___Note.pdf")])
        self.assertEqual((pic["pages"], pic["form"], pic["pointer"], pic["local"], pic["space"]), ("1", "both", "yes", "yes", "no"))
        self.assertEqual((song["form"], song["pointer"], song["local"]), ("public", "yes", "no"))
        self.assertEqual((shot["pages"], shot["form"], shot["pointer"], shot["space"]), ("2", "both", "no", "yes"))
        self.assertEqual((note["form"], note["pointer"], note["local"]), ("relative", "no", "no"))

    def test_public_check_quotes_names_and_skips_private_mounts(self):
        with patch.object(report, "public_status", side_effect=lambda url: url) as status:
            table = self.table(check_public=True)
        self.assertEqual(table[("g", "Screen Shot.png")]["public"], f"{PUBLIC}/Screen%20Shot.png")
        self.assertEqual(table[("p", "B___Asset___Note.pdf")]["public"], "private")
        self.assertEqual(status.call_count, 3)

    def test_summary(self):
        self.assertEqual(report.summary(report.rows(self.root, MOUNTS)), "4 linked files: 2 with a DVC pointer, 1 with a local copy, 1 with a space in the name")


if __name__ == "__main__":
    unittest.main()
