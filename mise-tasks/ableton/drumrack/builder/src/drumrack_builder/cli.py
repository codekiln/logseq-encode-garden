"""Command line: serve the web interface, or scan, analyze, export and verify without it."""

from __future__ import annotations

import argparse
import json
import logging
import sys
import threading
import webbrowser
from pathlib import Path

from . import adg, racks
from . import config as config_module
from .library import Library
from .store import Store, StoreError


def load_config(args: argparse.Namespace) -> config_module.Config:
    files = None
    if args.config:
        files = [config_module.DEFAULT_CONFIG, *[Path(c).expanduser() for c in args.config]]
    return config_module.load(files)


def cmd_up(args: argparse.Namespace) -> int:
    import uvicorn

    from .server import create_app

    config = load_config(args)
    host = args.host or config.host
    port = args.port or config.port
    app = create_app(config)
    url = f"http://{host}:{port}/"
    print(f"Drum Rack builder on {url}  (state: {config.state_folder})", flush=True)
    if config.open_browser and not args.no_browser:
        threading.Timer(1.0, webbrowser.open, args=(url,)).start()
    uvicorn.run(app, host=host, port=port, log_level="warning")
    return 0


def open_library(args: argparse.Namespace) -> tuple[config_module.Config, Store, Library]:
    config = load_config(args)
    store = Store(config.curation_db, config.analysis_db)
    return config, store, Library(config, store)


def cmd_scan(args: argparse.Namespace) -> int:
    config, store, library = open_library(args)
    print(json.dumps(library.scan()))
    if args.analyze:
        while (done := library.analyze_pending(100)) > 0:
            print(f"analyzed {done} more; {store.counts()}", flush=True)
    return 0


def cmd_racks(args: argparse.Namespace) -> int:
    _, store, library = open_library(args)
    library.scan_racks()
    for rack in sorted(library.source_racks.values(), key=lambda r: r.name.lower()):
        print(f"{rack.id}  {len(rack.pads):3d} pads  {rack.name}  [{rack.creator}]")
    print("\nbuilder racks:")
    for row in store.racks():
        print(f"{row['id']:>4}  {row['pad_count']:3d} pads  {row['name']}  base={row['base_path'] or 'template'}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    config, store, library = open_library(args)
    library.scan_racks()
    try:
        result = racks.export(
            store,
            library,
            config,
            args.rack,
            args.filename or store.rack(args.rack)["name"],
            overwrite=args.overwrite,
            target=Path(args.output) if args.output else None,
        )
    except StoreError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result["report"]["ok"] else 1


def cmd_verify(args: argparse.Namespace) -> int:
    """Check an .adg on its own: it parses, it is a Drum Rack, and every sample it names exists."""
    path = Path(args.rack).expanduser()
    try:
        rack = adg.read_rack(path)
    except (adg.RackError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    missing = 0
    for pad in rack.pads:
        flags = []
        for sample in pad.samples:
            if not Path(sample).is_file():
                flags.append(f"MISSING {sample}")
                missing += 1
        print(
            f"{adg.note_name(pad.note):>4} ({pad.note:3d})  {pad.label or '-':40.40}  "
            f"{'+'.join(pad.devices)}  choke={pad.choke}  {' '.join(flags)}"
        )
    if args.base:
        base = adg.read_xml(Path(args.base).expanduser())
        same = adg.device_settings(base) == adg.device_settings(adg.read_xml(path))
        print(f"rack-level settings match {args.base}: {same}")
        missing += 0 if same else 1
    print(f"{len(rack.pads)} pads, {missing} problems ({rack.creator})")
    return 0 if missing == 0 else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="drumrack-builder", description=__doc__)
    parser.add_argument("--config", action="append", help="extra config file layered over config.toml")
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)

    up = sub.add_parser("up", help="serve the web interface")
    up.add_argument("--host")
    up.add_argument("--port", type=int)
    up.add_argument("--no-browser", action="store_true")
    up.set_defaults(func=cmd_up)

    scan = sub.add_parser("scan", help="index sample folders and racks")
    scan.add_argument("--analyze", action="store_true", help="also analyze every new or changed sample")
    scan.set_defaults(func=cmd_scan)

    sub.add_parser("racks", help="list source racks and builder racks").set_defaults(func=cmd_racks)

    export = sub.add_parser("export", help="write a builder rack as an .adg and verify it")
    export.add_argument("rack", type=int, help="builder rack id (see `racks`)")
    export.add_argument("--filename", help="preset name inside the output folder")
    export.add_argument("--output", help="write to this path instead of the output folder")
    export.add_argument("--overwrite", action="store_true", help="replace an existing file (it is backed up)")
    export.set_defaults(func=cmd_export)

    verify = sub.add_parser("verify", help="check an .adg's pads and sample references")
    verify.add_argument("rack")
    verify.add_argument("--base", help="also compare rack-level settings with this .adg")
    verify.set_defaults(func=cmd_verify)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")
    try:
        return args.func(args)
    except config_module.ConfigError as error:
        print(f"config error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
