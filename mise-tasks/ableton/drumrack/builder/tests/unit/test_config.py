import tomllib
from pathlib import Path

import pytest

from drumrack_builder import config, racks
from drumrack_builder.store import StoreError


def committed_paths() -> list[str]:
    data = tomllib.loads(config.DEFAULT_CONFIG.read_text())
    lib = data["library"]
    return [
        lib["user_library"],
        *lib["sample_folders"],
        *lib["rack_folders"],
        data["output"]["folder"],
        data["state"]["folder"],
    ]


def test_committed_config_names_no_personal_folder():
    for raw in committed_paths():
        assert raw.startswith("~/") or not Path(raw).is_absolute(), raw
    assert "/Users/" not in config.DEFAULT_CONFIG.read_text()


def test_defaults_resolve_under_home():
    loaded = config.load([config.DEFAULT_CONFIG])
    home = Path.home().resolve()
    assert loaded.user_library.is_relative_to(home)
    assert loaded.output_folder.is_relative_to(loaded.user_library)
    assert loaded.state_folder == (config.PACKAGE_ROOT / ".local").resolve()
    assert loaded.host == "127.0.0.1"


def test_local_override_wins_key_by_key(tmp_path: Path):
    local = tmp_path / "local.toml"
    local.write_text('[server]\nport = 9000\n[library]\nsample_folders = ["~/Samples"]\n')
    loaded = config.load([config.DEFAULT_CONFIG, local])
    assert loaded.port == 9000
    assert loaded.sample_folders == [(Path.home() / "Samples").resolve()]
    assert loaded.rack_folders  # untouched keys keep their defaults


def test_bad_config_is_reported(tmp_path: Path):
    bad = tmp_path / "bad.toml"
    bad.write_text("[launchpad]\nbase_note = 90\n")
    with pytest.raises(config.ConfigError, match="base_note"):
        config.load([config.DEFAULT_CONFIG, bad])
    bad.write_text("not toml [")
    with pytest.raises(config.ConfigError):
        config.load([bad])


def test_resolved_paths_go_to_ignored_state(make_config):
    loaded = make_config()
    loaded.write_resolved()
    assert (loaded.state_folder / "resolved-config.json").is_file()
    ignored = (config.PACKAGE_ROOT / ".gitignore").read_text()
    assert ".local/" in ignored and "config.local.toml" in ignored


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Kit A", "Kit A.adg"),
        ("Kit A.adg", "Kit A.adg"),
        ("../../etc/passwd", "etc-passwd.adg"),
        ("a/b\\c", "a-b-c.adg"),
        (".hidden", "hidden.adg"),
        ("Bä:ss?", "Bä-ss.adg"),
    ],
)
def test_safe_filename(name, expected):
    assert racks.safe_filename(name) == expected


@pytest.mark.parametrize("name", ["", "  ", "..", "/", "..adg"])
def test_safe_filename_refuses_empty_names(name):
    with pytest.raises(StoreError):
        racks.safe_filename(name)


def test_output_path_stays_in_the_output_folder(make_config):
    loaded = make_config()
    for name in ["../../escape", "/abs/olute", "ok"]:
        assert racks.output_path(loaded, name).parent == loaded.output_folder
