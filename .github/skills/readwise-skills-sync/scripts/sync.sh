#!/usr/bin/env bash
# Vendor the Readwise workflow skills into .rulesync/skills/ and regenerate.
# Decision + usage: .rulesync/skills/readwise-skills-sync/SKILL.md
set -euo pipefail

REPO="readwiseio/readwise-skills"
REF="master"
# Skills NOT vendored. readwise-mcp: this graph wires the CLI, not the MCP server.
EXCLUDE=("readwise-mcp")

# Repo root: this script lives at .rulesync/skills/readwise-skills-sync/scripts/.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
DEST="$ROOT/.rulesync/skills"

is_excluded() { local s="$1" e; for e in "${EXCLUDE[@]}"; do [ "$s" = "$e" ] && return 0; done; return 1; }

# Insert `targets: ["*"]` after the description line, if the frontmatter lacks it.
inject_targets() {
  local f="$1"
  [ "$(head -1 "$f")" = "---" ] || return 0
  if awk 'NR>1 && /^---$/{exit} /^targets:/{found=1} END{exit !found}' "$f"; then return 0; fi
  awk '!done && /^description:/{print; print "targets: [\"*\"]"; done=1; next} {print}' "$f" > "$f.tmp"
  mv "$f.tmp" "$f"
}

echo "Fetching skill list from $REPO@$REF ..."
gh api "repos/$REPO/contents/skills?ref=$REF" --jq '.[] | select(.type=="dir") | .name' | while read -r s; do
  if is_excluded "$s"; then echo "skip   $s (excluded)"; continue; fi
  dir="$DEST/$s"
  mkdir -p "$dir"
  # Download every file in the skill dir (SKILL.md + sibling scripts).
  gh api "repos/$REPO/contents/skills/$s?ref=$REF" --jq '.[] | select(.type=="file") | .name' | while read -r file; do
    gh api "repos/$REPO/contents/skills/$s/$file?ref=$REF" --jq '.content' | base64 -d > "$dir/$file"
  done
  inject_targets "$dir/SKILL.md"
  echo "vendor $s"
done

echo "Regenerating rulesync outputs ..."
( cd "$ROOT" && mise exec -- rulesync generate >/dev/null )
echo "Done. Review: git status --short .rulesync/skills .claude/skills .agents/skills"
