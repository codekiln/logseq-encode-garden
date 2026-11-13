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


class PublicLinks(unittest.TestCase):
    MOUNTS = {
        "g": {"path": "assets/.remote/g", "public": "https://example.com/g"},
        "private": {"path": "assets/.remote/private", "bucket": "p", "dvc": "p"},
    }

    def rewrite(self, text):
        return mounts.public_links(text, self.MOUNTS, "pages/A.md")

    def test_link_forms_get_the_public_url(self):
        cases = {
            "![a](../assets/.remote/g/A___B.png)": "![a](https://example.com/g/A___B.png)",
            "[a](../assets/.remote/g/A%20B.mp3)": "[a](https://example.com/g/A%20B.mp3)",
            "![a](<../assets/.remote/g/A B.png>)": "![a](<https://example.com/g/A%20B.png>)",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(self.rewrite(text), expected)

    def test_other_links_and_code_keep_their_text(self):
        text = (
            "- ![a](../assets/A.png) and `![b](../assets/.remote/g/B.png)`\n"
            "- ~~~md\n  [c](../assets/.remote/other/C.png)\n  ~~~\n"
            "- Files sit in ../assets/.remote/<mount>/<file>.\n"
        )
        self.assertEqual(self.rewrite(text), text)

    def test_link_after_code_is_rewritten(self):
        self.assertEqual(self.rewrite("`x` [a](../assets/.remote/g/A.png)"), "`x` [a](https://example.com/g/A.png)")

    def test_errors_name_the_page_and_file(self):
        cases = {
            "pages/A.md links other/C.png, but asset-mounts.toml declares no mounts.other": "[c](../assets/.remote/other/C.png)",
            "pages/A.md links private/D.png, but mounts.private has no public URL": "[d](../assets/.remote/private/D.png)",
        }
        for message, text in cases.items():
            with self.subTest(message=message), self.assertRaisesRegex(mounts.MountError, message):
                self.rewrite(text)


if __name__ == "__main__":
    unittest.main()
