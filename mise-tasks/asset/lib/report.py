"""List the files that garden pages link in each asset mount."""
import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mounts  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
FOLDERS = ("pages", "journals")
FILE_NAME = re.compile(r"[^/<>`]+\.[A-Za-z0-9]+")
HEADER = ["mount", "file", "pages", "form", "pointer", "local", "space"]


def link_pattern(prefix):
    """Match a file under prefix, written plainly or inside angle brackets."""
    quoted = re.escape(prefix)
    return re.compile(rf"<{quoted}([^>\n]+)>|{quoted}([^\s)\]<>\"'`|]+)")


def file_name_from_link(text):
    """Drop a link's query, fragment and trailing punctuation, and decode its percent escapes."""
    name = re.split(r"[?#]", text, maxsplit=1)[0].rstrip(".,;:")
    return urllib.parse.unquote(name)


def scan(root, garden_mounts):
    """Return {(mount, file): {"pages": set, "forms": set}} for every link into a mount."""
    patterns = []
    for name, mount in garden_mounts.items():
        patterns.append((name, "relative", link_pattern(f"../{mount['path']}/")))
        if "public" in mount:
            patterns.append((name, "public", link_pattern(f"{mount['public']}/")))
    found = defaultdict(lambda: {"pages": set(), "forms": set()})
    for folder in FOLDERS:
        for page in sorted((Path(root) / folder).glob("*.md")):
            text = page.read_text(errors="replace")
            for name, form, pattern in patterns:
                for match in pattern.finditer(text):
                    file = file_name_from_link(match.group(1) or match.group(2))
                    if not FILE_NAME.fullmatch(file):
                        continue
                    entry = found[(name, file)]
                    entry["pages"].add(page.relative_to(root).as_posix())
                    entry["forms"].add(form)
    return found


def public_status(url):
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return str(response.status)
    except urllib.error.HTTPError as error:
        return str(error.code)
    except urllib.error.URLError:
        return "error"


def rows(root, garden_mounts, check_public=False):
    found = scan(root, garden_mounts)
    result = []
    for (name, file), entry in sorted(found.items()):
        folder = Path(root) / garden_mounts[name]["path"]
        forms = entry["forms"]
        result.append({
            "mount": name,
            "file": file,
            "pages": str(len(entry["pages"])),
            "form": "both" if len(forms) > 1 else next(iter(forms)),
            "pointer": "yes" if (folder / f"{file}.dvc").is_file() else "no",
            "local": "yes" if (folder / file).is_file() else "no",
            "space": "yes" if " " in file else "no",
        })
    if check_public:
        def check(row):
            base = garden_mounts[row["mount"]].get("public")
            return public_status(f"{base}/{urllib.parse.quote(row['file'])}") if base else "private"
        with ThreadPoolExecutor(max_workers=16) as pool:
            for row, status in zip(result, pool.map(check, result)):
                row["public"] = status
    return result


def summary(result):
    total = len(result)
    counts = {key: sum(row[key] == "yes" for row in result) for key in ("pointer", "local", "space")}
    line = f"{total} linked files: {counts['pointer']} with a DVC pointer, {counts['local']} with a local copy, {counts['space']} with a space in the name"
    if result and "public" in result[0]:
        line += f", {sum(row['public'] == '200' for row in result)} answering at their public URL"
    return line


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--public", action="store_true", help="send a HEAD request to each file's public URL")
    args = parser.parse_args()
    garden_mounts = mounts.load(ROOT)
    if not garden_mounts:
        raise ValueError(f"{mounts.FILE} declares no mounts; see {mounts.PAGE}")
    result = rows(ROOT, garden_mounts, check_public=args.public)
    columns = HEADER + (["public"] if args.public else [])
    print("\t".join(columns))
    for row in result:
        print("\t".join(row[column] for column in columns))
    print(summary(result), file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
