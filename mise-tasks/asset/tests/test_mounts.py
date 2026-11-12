import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("mounts", Path(__file__).parents[1] / "lib/mounts.py")
mounts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mounts)

GARDEN = Path(__file__).resolve().parents[3]
OWNING = '[mounts.g]\npath = "assets/.remote/g"\nbucket = "g"\ndvc = "garden"\n'


def load(text):
    with tempfile.TemporaryDirectory() as temp:
        (Path(temp) / mounts.FILE).write_text(text)
        return mounts.load(temp)


class GardenFile(unittest.TestCase):
    def test_garden_declares_its_public_mount(self):
        mount = mounts.load(GARDEN)["logseq-encode-garden"]
        self.assertEqual(mount["path"], "assets/.remote/logseq-encode-garden")
        self.assertEqual(mount["public"], "https://s3.us-east-005.backblazeb2.com/logseq-encode-garden")

    def test_first_line_links_the_schema_page(self):
        first = (GARDEN / mounts.FILE).read_text().splitlines()[0]
        self.assertEqual(first, f"# Schema: {mounts.PAGE}")
        self.assertTrue((GARDEN / "pages/Asset___Mount.md").is_file())


class Roles(unittest.TestCase):
    def test_private_owning_mount(self):
        self.assertNotIn("public", load(OWNING)["g"])

    def test_borrowing_mount(self):
        mount = load('[mounts.g]\npath = "assets/.remote/g"\npublic = "https://example.com/g"\nsource = "github.com/o/g"\n')["g"]
        self.assertEqual(mount["source"], "github.com/o/g")

    def test_missing_file_means_no_mounts(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(mounts.load(temp), {})


class Rejections(unittest.TestCase):
    def test_each_error_links_the_page(self):
        cases = {
            "unknown keys: region": OWNING + 'region = "us"\n',
            "unknown tables: extra": OWNING + "[extra]\n",
            "missing keys: dvc": '[mounts.g]\npath = "assets/.remote/g"\nbucket = "g"\n',
            "missing keys: public, source": '[mounts.g]\npath = "assets/.remote/g"\n',
            "mixes owning keys": OWNING + 'source = "github.com/o/g"\n',
            "path must be assets/.remote/g": OWNING.replace("assets/.remote/g", "assets/g"),
            "trailing slash": OWNING + 'public = "https://example.com/g/"\n',
            "non-empty strings": OWNING + 'public = ""\n',
        }
        for message, text in cases.items():
            with self.subTest(message=message), self.assertRaisesRegex(mounts.MountError, message) as caught:
                load(text)
            self.assertIn(mounts.PAGE, str(caught.exception))

    def test_invalid_toml(self):
        with self.assertRaisesRegex(mounts.MountError, "asset-mounts.toml"):
            load("[mounts.g\n")


if __name__ == "__main__":
    unittest.main()
