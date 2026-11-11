from pathlib import Path

from drumrack_builder import cli
from drumrack_builder.library import Library
from drumrack_builder.store import Store
from tests.conftest import digest


def write_config(tmp_path: Path, make_config) -> Path:
    make_config()
    return tmp_path / "config.toml"


def test_scan_export_and_verify(tmp_path: Path, make_config, base_rack: Path, capsys):
    config_file = write_config(tmp_path, make_config)
    before = digest(base_rack)
    assert cli.main(["--config", str(config_file), "scan", "--analyze"]) == 0
    config = make_config()
    store = Store(config.curation_db, config.analysis_db)
    library = Library(config, store)
    library.scan_racks()
    source = next(iter(library.source_racks))
    from drumrack_builder import racks

    rack_id = racks.duplicate(store, library, source, "CLI copy")
    store.close()
    output = tmp_path / "cli" / "CLI copy.adg"
    assert cli.main(["--config", str(config_file), "export", str(rack_id), "--output", str(output)]) == 0
    assert '"ok": true' in capsys.readouterr().out
    assert cli.main(["verify", str(output), "--base", str(base_rack)]) == 0
    out = capsys.readouterr().out
    assert "5 pads, 0 problems" in out and "rack-level settings match" in out
    # Refuses to replace the export without --overwrite.
    assert cli.main(["--config", str(config_file), "export", str(rack_id), "--output", str(output)]) == 2
    assert digest(base_rack) == before


def test_verify_reports_missing_samples(tmp_path: Path, base_rack: Path, library: Path, capsys):
    next((library / "Samples" / "Kit").glob("tone 00*")).unlink()
    assert cli.main(["verify", str(base_rack)]) == 1
    assert "MISSING" in capsys.readouterr().out
