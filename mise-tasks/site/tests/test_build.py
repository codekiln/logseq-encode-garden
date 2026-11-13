from importlib.machinery import SourceFileLoader
import importlib.util
from pathlib import Path
import tempfile
import unittest

loader = SourceFileLoader("site_build", str(Path(__file__).parents[1] / "build"))
spec = importlib.util.spec_from_loader("site_build", loader)
build = importlib.util.module_from_spec(spec)
loader.exec_module(build)

MOUNTS = '[mounts.g]\npath = "assets/.remote/g"\nbucket = "g"\ndvc = "garden"\npublic = "https://example.com/g"\n'


class SiteGraph(unittest.TestCase):
    def garden(self, root, mounts=MOUNTS):
        for name, text in {
            "asset-mounts.toml": mounts,
            "pages/A.md": "- ![f](../assets/.remote/g/F.png)\n",
            "pages/B.md": "- ![l](../assets/L.png)\n",
            "journals/2026_11_13.md": "- [[A]]\n",
            "logseq/config.edn": "{}\n",
            "assets/L.png": "local",
            "assets/.remote/g/F.png": "remote",
            "assets/.remote/g/F.png.dvc": "pointer",
        }.items():
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(text)

    def test_copy_links_public_urls_and_leaves_mounts_out(self):
        with tempfile.TemporaryDirectory() as temp:
            graph, folder = Path(temp) / "garden", Path(temp) / "site-graph"
            self.garden(graph)
            folder.mkdir()
            self.assertEqual(build.copy_graph_with_public_links(graph, folder), 1)
            self.assertEqual((folder / "pages/A.md").read_text(), "- ![f](https://example.com/g/F.png)\n")
            self.assertEqual((folder / "pages/B.md").read_text(), "- ![l](../assets/L.png)\n")
            self.assertEqual((graph / "pages/A.md").read_text(), "- ![f](../assets/.remote/g/F.png)\n")
            self.assertTrue((folder / "journals/2026_11_13.md").is_file())
            self.assertTrue((folder / "logseq/config.edn").is_file())
            self.assertEqual((folder / "assets/L.png").read_text(), "local")
            self.assertFalse((folder / "assets/.remote").exists())
            self.assertFalse((folder / "asset-mounts.toml").exists())

    def test_private_mount_stops_the_copy(self):
        with tempfile.TemporaryDirectory() as temp:
            graph, folder = Path(temp) / "garden", Path(temp) / "site-graph"
            self.garden(graph, MOUNTS.replace('public = "https://example.com/g"\n', ""))
            folder.mkdir()
            with self.assertRaisesRegex(build.mounts.MountError, "pages/A.md links g/F.png"):
                build.copy_graph_with_public_links(graph, folder)


if __name__ == "__main__":
    unittest.main()
