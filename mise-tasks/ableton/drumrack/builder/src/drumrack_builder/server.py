"""HTTP API and static web interface. Every file it serves is looked up by id in the index."""

from __future__ import annotations

import io
import logging
from contextlib import asynccontextmanager
from importlib import resources
from pathlib import Path

import soundfile as sf
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import adg, analysis, racks
from .config import Config
from .launchpad import Launchpad
from .library import Library
from .store import Store, StoreError

log = logging.getLogger(__name__)

# Browsers play these directly; anything else (AIFF above all) is decoded and sent as WAV.
DIRECT_TYPES = {"wav": "audio/wav", "mp3": "audio/mpeg", "ogg": "audio/ogg", "flac": "audio/flac"}


class RackIn(BaseModel):
    name: str = ""
    source: str | None = None  # a source rack id to duplicate


class RackPatch(BaseModel):
    name: str


class PadIn(BaseModel):
    sample_id: int | None = None
    name: str | None = None
    keep: bool = False


class PadMove(BaseModel):
    target: int = Field(ge=0, le=127)


class ShortlistIn(BaseModel):
    name: str


class CandidateIn(BaseModel):
    sample_id: int


class VoteIn(BaseModel):
    winner: int
    loser: int


class PickIn(BaseModel):
    winner: int


class ExcludeIn(BaseModel):
    excluded: bool


class ExportIn(BaseModel):
    filename: str
    overwrite: bool = False


class FocusIn(BaseModel):
    note: int = Field(ge=0, le=127)
    sample_id: int | None = None


class LaunchpadRackIn(BaseModel):
    rack_id: int | None = None


def create_app(config: Config, *, background: bool = True) -> FastAPI:
    config.write_resolved()
    store = Store(config.curation_db, config.analysis_db)
    library = Library(config, store)
    launchpad = Launchpad(config.launchpad_port, config.base_note, config.audio_device)
    state: dict = {"launchpad_rack": None}

    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        if background:
            library.start()
        yield
        library.stop()
        if launchpad.connected:
            launchpad.disconnect()
        store.close()

    app = FastAPI(title="Drum Rack builder", lifespan=lifespan)
    app.state.store, app.state.library, app.state.launchpad = store, library, launchpad

    @app.exception_handler(StoreError)
    async def store_error(_request: Request, error: StoreError):
        return JSONResponse({"detail": str(error)}, status_code=400)

    @app.exception_handler(KeyError)
    async def not_found(_request: Request, error: KeyError):
        return JSONResponse({"detail": str(error.args[0] if error.args else error)}, status_code=404)

    @app.exception_handler(adg.RackError)
    async def rack_error(_request: Request, error: adg.RackError):
        return JSONResponse({"detail": str(error)}, status_code=400)

    # ------------------------------------------------------------------ library

    @app.get("/api/status")
    def status():
        return {"library": library.status, "counts": store.counts(), "config": config.summary()}

    @app.post("/api/scan")
    def scan():
        return library.scan()

    @app.get("/api/folders")
    def folders():
        return store.folders()

    @app.get("/api/samples")
    def samples(
        q: str = "",
        folder: str = "",
        excluded: str = "hide",
        rack: str = "",
        sort: str = "name",
        group: str = "",
        limit: int = 500,
        offset: int = 0,
    ):
        rack_path = str(library.source_rack(rack).path) if rack else ""
        total, rows = store.samples(
            query=q,
            folder=folder,
            include_excluded=excluded == "show",
            only_excluded=excluded == "only",
            rack_path=rack_path,
            sort=sort,
            limit=min(max(limit, 1), 2000),
            offset=max(offset, 0),
        )
        result: dict = {"total": total, "samples": rows}
        if group:
            try:
                result["groups"] = [
                    {"label": g["label"], "ids": [s["id"] for s in g["samples"]]} for g in analysis.group(rows, group)
                ]
            except ValueError as error:
                raise StoreError(str(error)) from error
        return result

    @app.get("/api/samples/{sample_id}")
    def sample(sample_id: int):
        return store.sample(sample_id)

    @app.post("/api/samples/{sample_id}/exclude")
    def exclude(sample_id: int, body: ExcludeIn):
        store.set_excluded(sample_id, body.excluded)
        return {"ok": True}

    @app.get("/api/samples/{sample_id}/audio")
    def audio(sample_id: int):
        row = store.sample(sample_id)
        path = Path(row["path"])
        if not path.is_file():
            raise HTTPException(404, "sample file is missing")
        kind = DIRECT_TYPES.get(row["ext"])
        if kind is not None:
            return FileResponse(path, media_type=kind)
        if analysis.live_only(path):
            raise HTTPException(415, "this sample is encoded for Ableton Live only; audition it in Live")
        try:
            data, rate = sf.read(str(path), always_2d=True)
        except sf.LibsndfileError as error:
            raise HTTPException(415, f"cannot decode this file: {error}") from error
        buffer = io.BytesIO()
        sf.write(buffer, data, rate, format="WAV", subtype="PCM_24")
        return Response(buffer.getvalue(), media_type="audio/wav")

    @app.get("/api/source-racks")
    def source_racks():
        return [
            {
                "id": r.id,
                "name": r.name,
                "path": str(r.path),
                "creator": r.creator,
                "origin": r.origin,
                "pads": len(r.pads),
            }
            for r in sorted(library.source_racks.values(), key=lambda r: r.name.lower())
        ]

    @app.get("/api/source-racks/{key}")
    def source_rack(key: str):
        try:
            rack = library.source_rack(key)
        except KeyError as error:
            raise HTTPException(404, str(error)) from error
        return {
            "id": rack.id,
            "name": rack.name,
            "path": str(rack.path),
            "creator": rack.creator,
            "pads": [
                {
                    "note": p.note,
                    "note_name": adg.note_name(p.note),
                    "label": p.label,
                    "choke": p.choke,
                    "devices": p.devices,
                    "samples": p.samples,
                    "simple": p.simple,
                }
                for p in rack.pads
            ],
        }

    # ------------------------------------------------------------------ racks

    @app.get("/api/racks")
    def list_racks():
        return store.racks()

    @app.post("/api/racks")
    def create_rack(body: RackIn):
        if body.source:
            try:
                rack_id = racks.duplicate(store, library, body.source, body.name.strip() or None)
            except KeyError as error:
                raise HTTPException(404, str(error)) from error
        else:
            rack_id = store.create_rack(body.name or "New rack")
        return rack_detail(rack_id)

    def rack_detail(rack_id: int) -> dict:
        rack = store.rack(rack_id)
        pads = store.pads(rack_id)
        for pad in pads:
            pad["note_name"] = adg.note_name(pad["note"])
        rack["pads"] = pads
        rack["shortlists"] = store.shortlists(rack_id)
        rack["default_filename"] = rack["name"]
        return rack

    @app.get("/api/racks/{rack_id}")
    def get_rack(rack_id: int):
        return rack_detail(rack_id)

    @app.patch("/api/racks/{rack_id}")
    def rename_rack(rack_id: int, body: RackPatch):
        store.update_rack(rack_id, name=body.name.strip())
        return rack_detail(rack_id)

    @app.delete("/api/racks/{rack_id}")
    def delete_rack(rack_id: int):
        store.delete_rack(rack_id)
        return {"ok": True}

    @app.put("/api/racks/{rack_id}/pads/{note}")
    def set_pad(rack_id: int, note: int, body: PadIn):
        store.set_pad(rack_id, note, sample_id=body.sample_id, name=body.name, keep=body.keep)
        refresh_launchpad(rack_id)
        return rack_detail(rack_id)

    @app.post("/api/racks/{rack_id}/pads/{note}/move")
    def move_pad(rack_id: int, note: int, body: PadMove):
        store.move_pad(rack_id, note, body.target)
        refresh_launchpad(rack_id)
        return rack_detail(rack_id)

    @app.post("/api/racks/{rack_id}/pads/{note}/revert")
    def revert_pad(rack_id: int, note: int):
        racks.revert(store, rack_id, note)
        refresh_launchpad(rack_id)
        return rack_detail(rack_id)

    @app.delete("/api/racks/{rack_id}/pads/{note}")
    def remove_pad(rack_id: int, note: int):
        store.remove_pad(rack_id, note)
        refresh_launchpad(rack_id)
        return rack_detail(rack_id)

    @app.post("/api/racks/{rack_id}/export")
    def export(rack_id: int, body: ExportIn):
        return racks.export(store, library, config, rack_id, body.filename, overwrite=body.overwrite)

    # ------------------------------------------------------------------ shortlists and comparison

    @app.post("/api/racks/{rack_id}/pads/{note}/shortlists")
    def create_shortlist(rack_id: int, note: int, body: ShortlistIn):
        shortlist_id = store.create_shortlist(rack_id, note, body.name)
        refresh_launchpad(rack_id)
        return store.shortlist(shortlist_id)

    @app.patch("/api/shortlists/{shortlist_id}")
    def rename_shortlist(shortlist_id: int, body: ShortlistIn):
        store.rename_shortlist(shortlist_id, body.name)
        return store.shortlist(shortlist_id)

    @app.delete("/api/shortlists/{shortlist_id}")
    def delete_shortlist(shortlist_id: int):
        store.delete_shortlist(shortlist_id)
        return {"ok": True}

    @app.post("/api/shortlists/{shortlist_id}/items")
    def add_candidate(shortlist_id: int, body: CandidateIn):
        store.add_candidate(shortlist_id, body.sample_id)
        return store.shortlist(shortlist_id)

    @app.delete("/api/shortlists/{shortlist_id}/items/{sample_id}")
    def remove_candidate(shortlist_id: int, sample_id: int):
        store.remove_candidate(shortlist_id, sample_id)
        return store.shortlist(shortlist_id)

    @app.get("/api/shortlists/{shortlist_id}/pairwise")
    def pairwise(shortlist_id: int):
        return store.pairwise(shortlist_id)

    @app.post("/api/shortlists/{shortlist_id}/votes")
    def vote(shortlist_id: int, body: VoteIn):
        store.vote(shortlist_id, body.winner, body.loser)
        return store.pairwise(shortlist_id)

    @app.delete("/api/shortlists/{shortlist_id}/votes/last")
    def undo_vote(shortlist_id: int):
        store.undo_vote(shortlist_id)
        return store.pairwise(shortlist_id)

    def bracket_view(shortlist_id: int) -> dict:
        found = store.bracket(shortlist_id)
        if found is None:
            return {"bracket": None}
        _, bracket = found
        current = bracket.current()
        return {
            "bracket": bracket.to_dict(),
            "champion": bracket.champion,
            "current": None
            if current is None
            else {"round": current[0], "match": current[1], "a": current[2].a, "b": current[2].b},
        }

    @app.get("/api/shortlists/{shortlist_id}/bracket")
    def get_bracket(shortlist_id: int):
        return bracket_view(shortlist_id)

    @app.post("/api/shortlists/{shortlist_id}/bracket")
    def start_bracket(shortlist_id: int):
        try:
            store.start_bracket(shortlist_id)
        except ValueError as error:
            raise StoreError(str(error)) from error
        return bracket_view(shortlist_id)

    @app.post("/api/shortlists/{shortlist_id}/bracket/pick")
    def pick(shortlist_id: int, body: PickIn):
        store.pick(shortlist_id, body.winner)
        return bracket_view(shortlist_id)

    # ------------------------------------------------------------------ Launchpad

    def launchpad_pads(rack_id: int) -> dict[int, dict]:
        pads: dict[int, dict] = {}
        for shortlist in store.shortlists(rack_id):
            pads[shortlist["note"]] = {"path": None, "state": "shortlist", "label": shortlist["name"]}
        for pad in store.pads(rack_id):
            if pad["sample_id"] is None:
                continue
            missing = not pad["sample_path"] or not Path(pad["sample_path"]).is_file()
            pads[pad["note"]] = {
                "path": None if missing else pad["sample_path"],
                "state": "missing" if missing else ("kept" if pad["keep"] else "assigned"),
                "label": pad["name"] or pad["sample_name"],
            }
        return pads

    def refresh_launchpad(rack_id: int) -> None:
        if state["launchpad_rack"] == rack_id:
            launchpad.set_pads(launchpad_pads(rack_id))

    @app.get("/api/launchpad")
    def launchpad_status():
        return {**launchpad.status(), "rack_id": state["launchpad_rack"]}

    @app.post("/api/launchpad/connect")
    def launchpad_connect():
        try:
            launchpad.connect()
        except Exception as error:
            raise HTTPException(409, str(error)) from error
        return launchpad_status()

    @app.post("/api/launchpad/disconnect")
    def launchpad_disconnect():
        launchpad.disconnect()
        return launchpad_status()

    @app.post("/api/launchpad/rack")
    def launchpad_rack(body: LaunchpadRackIn):
        state["launchpad_rack"] = body.rack_id
        launchpad.focus.clear()
        launchpad.set_pads({} if body.rack_id is None else launchpad_pads(body.rack_id))
        return launchpad_status()

    @app.post("/api/launchpad/focus")
    def launchpad_focus(body: FocusIn):
        path = None if body.sample_id is None else store.sample(body.sample_id)["path"]
        launchpad.set_focus(body.note, path)
        return launchpad_status()

    # ------------------------------------------------------------------ web interface

    static = resources.files("drumrack_builder").joinpath("static")
    app.mount("/static", StaticFiles(directory=str(static)), name="static")

    @app.get("/")
    def index():
        return FileResponse(str(static.joinpath("index.html")))

    return app
