logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Hold Riser slot 132 capture
	- [Download the slot 132 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___132%20Hold%20Riser___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 132 over USB on October 25, 2026 with `mise run microfreak:download --slot 132`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `beadec309a3f1a3e77a1ff5931e710236689d1bc770838bde475ec35b640565a`.
