"""Page-named working files with adjacent DVC metadata."""
import argparse
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[3]


def filename(page):
    segments = page.split("/")
    if len(segments) < 4 or "Asset" not in segments[1:-2]:
        raise ValueError("use an asset page name ending in its format")
    if any(not p or p in (".", "..") or "___" in p or re.search(r'[<>:"\\|?*\x00-\x1f\x7f]', p) for p in segments):
        raise ValueError("invalid asset page segment")
    if not re.fullmatch(r"[a-z0-9]+", segments[-1]):
        raise ValueError("format must contain lowercase letters or digits")
    return "___".join(segments[:-1]) + "." + segments[-1]


def asset(page):
    return ROOT / "assets" / ".remote" / filename(page)


def dvc(*args, remote=False):
    command = [sys.executable, "-m", "dvc", *map(str, args)]
    cwd = ROOT
    environment = os.environ.copy()
    if remote:
        common = subprocess.check_output(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=ROOT, text=True).strip()
        cache_root = Path(common).parent
        cache_file = cache_root / "fnox.local.toml"
        if not cache_file.is_file():
            raise ValueError("asset credentials need an encrypted fnox cache in the main checkout")
        cached = tomllib.loads(cache_file.read_text()).get("profiles", {}).get("assets", {}).get("secrets", {})
        if not all(cached.get(key, {}).get("sync", {}).get("provider") and cached.get(key, {}).get("sync", {}).get("value") for key in ("AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY")):
            raise ValueError("encrypted fnox cache is missing asset credentials; refresh it while signed in")
        environment = {key: value for key, value in environment.items() if not key.startswith("AWS_")}
        command = ["fnox", "--profile", "assets", "--no-defaults", "--no-daemon", "--non-interactive", "exec", "--", sys.executable, str(Path(__file__).resolve()), "_dvc", str(ROOT), *map(str, args)]
        cwd = cache_root
    subprocess.run(command, cwd=cwd, env=environment, check=True)


def prepare(source, output):
    """DVC owns replacing a generated output; prepare still refuses overwrite."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent) as tmp:
        target = Path(tmp) / "prepared.mp3"
        subprocess.run([str(ROOT / "mise-tasks/gitpa/media/prepare"), str(source), str(target)], check=True, cwd=ROOT)
        os.replace(target, output)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "_dvc":
        subprocess.run([sys.executable, "-m", "dvc", *sys.argv[3:]], cwd=sys.argv[2], check=True)
        return
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    add = sub.add_parser("add", help="copy a local file to its page-derived path and track it")
    add.add_argument("source", type=Path)
    add.add_argument("page")
    for action in ("fetch", "push", "status"):
        p = sub.add_parser(action)
        p.add_argument("page")
    convert = sub.add_parser("convert", help="register and reproduce a WAV-to-MP3 DVC stage")
    convert.add_argument("wav_page")
    convert.add_argument("mp3_page")
    build = sub.add_parser("_prepare")
    build.add_argument("source", type=Path)
    build.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.action == "_prepare":
        prepare(args.source, args.output)
    elif args.action == "add":
        destination = asset(args.page)
        if args.source.suffix != destination.suffix:
            raise ValueError("source extension must match the page format")
        if not args.source.is_file():
            raise ValueError("source file does not exist")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and args.source.resolve() != destination.resolve():
            raise ValueError("working file exists; use its path as source to update tracking")
        if args.source.resolve() != destination.resolve():
            shutil.copy2(args.source, destination)
        dvc("add", destination.relative_to(ROOT))
    elif args.action == "convert":
        source, output = asset(args.wav_page), asset(args.mp3_page)
        if source.suffix != ".wav" or output.suffix != ".mp3":
            raise ValueError("conversion requires WAV and MP3 asset pages")
        if not source.is_file():
            raise ValueError("fetch or add the WAV first")
        stage = "mp3-" + output.stem
        helper = Path(__file__).resolve().relative_to(ROOT)
        command = shlex.join(["python", str(helper), "_prepare", str(source.relative_to(ROOT)), str(output.relative_to(ROOT))])
        # Existing definitions reproduce; changes to parameters belong in dvc.yaml.
        stages = ROOT / "dvc.yaml"
        import yaml
        existing = yaml.safe_load(stages.read_text()) if stages.exists() else {}
        if stage not in (existing or {}).get("stages", {}):
            if output.exists() or output.with_suffix(output.suffix + ".dvc").exists():
                raise ValueError("choose a fresh MP3 asset page for the conversion stage")
            dvc("stage", "add", "-n", stage, "-d", source.relative_to(ROOT), "-d", helper, "-d", "mise-tasks/gitpa/media/prepare", "-o", output.relative_to(ROOT), command)
        dvc("repro", stage)
    else:
        metadata = Path(str(asset(args.page)) + ".dvc")
        target = metadata if metadata.is_file() else asset(args.page)
        dvc({"fetch": "pull", "push": "push", "status": "status"}[args.action], target.relative_to(ROOT), remote=args.action != "status")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
