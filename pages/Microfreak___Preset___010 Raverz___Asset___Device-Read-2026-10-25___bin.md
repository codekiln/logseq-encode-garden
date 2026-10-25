logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Raverz slot 10 capture
	- [Download the slot 10 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___010%20Raverz___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 10 over USB on October 25, 2026 with `mise run microfreak:download --slot 10`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `c05c8c3949031cd78acde893964ea4ead9251fcf3a1e97016dbc211abd204a90`.
