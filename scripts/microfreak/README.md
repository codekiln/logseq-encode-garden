# MicroFreak preset metadata

From a garden worktree, preview the saved presets on the connected MicroFreak:

```sh
mise run microfreak:sync
mise run microfreak:sync --apply
```

The task needs `uv` on PATH and installs `python-rtmidi==1.5.8` in uv's environment. Connect the MicroFreak over USB. Close MIDI Control Center if reads time out. Use `--port 'Arturia MicroFreak'` when endpoint selection is ambiguous.

Capture an inventory for review or offline use:

```sh
mise run microfreak:sync --save-inventory /tmp/microfreak-inventory.json
mise run microfreak:sync --inventory /tmp/microfreak-inventory.json --apply
```

`--garden /absolute/path/to/worktree` chooses a different checkout. Offline inventories describe the device at capture time; read the live device again to refresh the garden. The command defaults to preview. `--apply` updates the pages and records the preset hub in today's journal; review the Git diff and commit through the usual PR workflow. Run the command again whenever saved presets change. A repeated unchanged capture produces no page changes.

The command reads every saved preset header before planning changes. It aborts an incomplete or malformed inventory. Pages use `Microfreak/Preset/<slot> <name>` titles. It updates the number, name, category, initialized flag, and on-device flag, retaining prose, tags, and manually assigned origin. A name change creates a new page and marks the old page absent. Existing unmanaged pages and duplicate identities cause an error so notes can be reconciled before import.

`preset-origin` starts as `unknown`: slot numbers do not establish factory or custom provenance. `preset-initialized` identifies an initialization flag in the saved header; initialized slots are included in the inventory and omitted from page creation. A formerly populated slot that becomes initialized has its existing page marked absent. Saved headers omit the sound parameters, so an edit that retains a name is not versioned. Historical composition references need exported preset files for sound-level identity. Binary export, restore, and B2 publication remain future work.

The only instrument command sent is a saved-header read (`0x19`, mode `0`). The [Elektroid MicroFreak connector](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c) documents the request and header layout used here. Live validation on the connected device returned slot 397 as `Imit`, category `Keys`. The task does not require Elektroid to be built.

Run the regression checks with:

```sh
python3 -m unittest discover -s scripts/microfreak -p 'test_*.py'
```
