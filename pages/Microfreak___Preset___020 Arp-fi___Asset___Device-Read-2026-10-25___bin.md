logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Arp-fi slot 20 capture
	- [Download the slot 20 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___020%20Arp-fi___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 20 over USB on October 25, 2026 with `mise run microfreak:download --slot 20`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `5b2fe603d487f78e0d11dd02860bb73ec425dd0739722e4e0794f5c292cb2290`.
