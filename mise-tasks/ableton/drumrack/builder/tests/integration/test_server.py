"""The browser's workflow over HTTP: browse, audition, curate, compare, duplicate and export."""

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from drumrack_builder import adg
from drumrack_builder.server import create_app
from tests.conftest import digest


@pytest.fixture
def client(make_config, base_rack):
    app = create_app(make_config(), background=False)
    with TestClient(app) as c:
        c.app_state = app.state
        assert c.post("/api/scan").json()["started"]
        while app.state.library.analyze_pending(100):
            pass
        yield c


def find(client, name):
    rows = client.get("/api/samples", params={"q": name}).json()["samples"]
    assert rows, name
    return rows[0]


def test_browse_search_sort_group_and_exclude(client):
    data = client.get("/api/samples").json()
    assert data["total"] == 7  # six WAVs and one AIFF; rack samples are the same files
    assert all(r["duration"] is not None for r in data["samples"])
    assert [r["name"] for r in client.get("/api/samples", params={"q": "440Hz"}).json()["samples"]] == ["tone 03 440Hz"]
    by_pitch = client.get("/api/samples", params={"sort": "pitch"}).json()["samples"]
    assert by_pitch[0]["name"] == "tone 00 55Hz"
    groups = client.get("/api/samples", params={"group": "pitch"}).json()["groups"]
    assert {g["label"] for g in groups} >= {"A", "E"}
    target = find(client, "880Hz")
    client.post(f"/api/samples/{target['id']}/exclude", json={"excluded": True})
    assert client.get("/api/samples").json()["total"] == 6
    assert client.get("/api/samples", params={"excluded": "only"}).json()["total"] == 1
    assert client.get("/api/samples", params={"sort": "colour"}).status_code == 400
    assert client.get("/api/samples", params={"rack": "nope"}).status_code == 404


def test_samples_used_by_racks_are_indexed(client):
    racks = client.get("/api/source-racks").json()
    assert [r["name"] for r in racks] == ["Base"]
    used = client.get("/api/samples", params={"rack": racks[0]["id"]}).json()["samples"]
    assert {r["name"] for r in used} == {f"tone 0{i} {hz}Hz" for i, hz in enumerate([55, 110, 220, 440])}


def test_audio_is_served_by_id_and_aiff_is_decoded(client):
    wav = find(client, "55Hz")
    response = client.get(f"/api/samples/{wav['id']}/audio")
    assert response.headers["content-type"] == "audio/wav" and response.content[:4] == b"RIFF"
    aiff = find(client, "stereo")
    response = client.get(f"/api/samples/{aiff['id']}/audio")
    assert response.headers["content-type"] == "audio/wav" and response.content[:4] == b"RIFF"
    assert client.get("/api/samples/9999/audio").status_code == 400
    assert client.get("/api/samples/..%2f..%2fetc%2fpasswd/audio").status_code in (404, 422)


def test_new_rack_with_shortlists_comparison_and_export(client, make_config):
    rack = client.post("/api/racks", json={"name": "Fresh Kit"}).json()
    ids = [find(client, f"{hz}Hz")["id"] for hz in (55, 110, 220, 440)]
    shortlist = client.post(f"/api/racks/{rack['id']}/pads/36/shortlists", json={"name": "Kick"}).json()
    for sample_id in ids:
        client.post(f"/api/shortlists/{shortlist['id']}/items", json={"sample_id": sample_id})
    second = client.post(f"/api/racks/{rack['id']}/pads/36/shortlists", json={"name": "Kick, softer"}).json()
    assert {s["name"] for s in client.get(f"/api/racks/{rack['id']}").json()["shortlists"]} == {"Kick", "Kick, softer"}
    client.delete(f"/api/shortlists/{second['id']}")

    # Pairwise: the 55 Hz tone wins every comparison it is in.
    for _ in range(6):
        pair = client.get(f"/api/shortlists/{shortlist['id']}/pairwise").json()["pair"]
        winner = ids[0] if ids[0] in pair else min(pair)
        client.post(
            f"/api/shortlists/{shortlist['id']}/votes",
            json={"winner": winner, "loser": pair[1] if pair[0] == winner else pair[0]},
        )
    ranking = client.get(f"/api/shortlists/{shortlist['id']}/pairwise").json()["ranking"]
    assert ranking[0]["sample_id"] == ids[0] and ranking[0]["wins"] == 3
    assert (
        client.post(f"/api/shortlists/{shortlist['id']}/votes", json={"winner": ids[0], "loser": 9999}).status_code
        == 400
    )

    # Bracket, seeded by that ranking.
    view = client.post(f"/api/shortlists/{shortlist['id']}/bracket").json()
    while view["current"]:
        a, b = view["current"]["a"], view["current"]["b"]
        winner = ids[0] if ids[0] in (a, b) else min(a, b)
        view = client.post(f"/api/shortlists/{shortlist['id']}/bracket/pick", json={"winner": winner}).json()
    assert view["champion"] == ids[0]

    client.put(f"/api/racks/{rack['id']}/pads/36", json={"sample_id": view["champion"], "name": "Kick"})
    client.put(f"/api/racks/{rack['id']}/pads/37", json={"sample_id": ids[2]})
    client.post(f"/api/racks/{rack['id']}/pads/37/move", json={"target": 40})
    assert client.put(f"/api/racks/{rack['id']}/pads/38", json={"sample_id": ids[1], "keep": True}).status_code == 400

    result = client.post(f"/api/racks/{rack['id']}/export", json={"filename": "../Fresh Kit"}).json()
    config = make_config()
    assert Path(result["path"]) == config.output_folder / "Fresh Kit.adg"
    assert result["report"]["ok"], result["report"]["problems"]
    assert result["report"]["added_pads"] == 2
    exported = adg.read_rack(Path(result["path"]))
    assert [(p.note, p.name) for p in exported.pads] == [(36, "Kick"), (40, "")]

    # A second export to the same name needs explicit confirmation and keeps a backup.
    again = client.post(f"/api/racks/{rack['id']}/export", json={"filename": "Fresh Kit"})
    assert again.status_code == 400 and "already exists" in again.json()["detail"]
    replaced = client.post(f"/api/racks/{rack['id']}/export", json={"filename": "Fresh Kit", "overwrite": True})
    assert Path(replaced.json()["backup"]).is_file()
    assert Path(replaced.json()["backup"]).is_relative_to(config.state_folder)


def test_duplicate_preserves_the_source_and_its_settings(client, base_rack, library):
    before = digest(base_rack)
    source = client.get("/api/source-racks").json()[0]
    rack = client.post("/api/racks", json={"name": "Base variation", "source": source["id"]}).json()
    assert [p["note"] for p in rack["pads"]] == [36, 37, 38, 39, 48]
    assert all(p["keep"] for p in rack["pads"])
    new = find(client, "1760Hz")["id"]
    client.put(f"/api/racks/{rack['id']}/pads/38", json={"sample_id": new, "name": "bright"})
    client.post(f"/api/racks/{rack['id']}/pads/37/move", json={"target": 44})
    client.delete(f"/api/racks/{rack['id']}/pads/39")
    reverted = client.put(f"/api/racks/{rack['id']}/pads/36", json={"sample_id": new})
    assert not next(p for p in reverted.json()["pads"] if p["note"] == 36)["keep"]
    restored = client.post(f"/api/racks/{rack['id']}/pads/36/revert").json()
    assert next(p for p in restored["pads"] if p["note"] == 36)["keep"]

    result = client.post(f"/api/racks/{rack['id']}/export", json={"filename": "Base variation"}).json()
    report = result["report"]
    assert report["ok"], report["problems"]
    assert (report["preserved_pads"], report["replaced_pads"], report["removed_pads"]) == (3, 1, 1)
    assert report["device_settings_preserved"]
    assert digest(base_rack) == before

    out = adg.read_rack(Path(result["path"]))
    assert out.pad(44).choke == 2
    assert out.pad(38).name == "bright"
    root = adg.read_xml(Path(result["path"]))
    branch = next(b for b in adg.branches(root) if adg.branch_note(b) == 38)
    assert adg.value(adg.simple_part(branch), "Detune") == "7"

    # The exported rack shows up as a source after a rescan, but writing over the original still needs consent.
    client.post("/api/scan")
    names = {r["name"]: r for r in client.get("/api/source-racks").json()}
    assert names["Base variation"]["origin"] == "builder"
    lib = client.app_state.library
    assert base_rack in lib.protected_paths()


def test_launchpad_status_without_a_device(client):
    status = client.get("/api/launchpad").json()
    assert status["connected"] is False
    if status["available"]:
        assert status["ports"] == []  # the test config names a port that does not exist
        assert client.post("/api/launchpad/connect").status_code == 409
