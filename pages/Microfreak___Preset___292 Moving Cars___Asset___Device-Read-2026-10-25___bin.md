logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Moving Cars slot 292 capture
	- [Download the slot 292 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___292%20Moving%20Cars___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 292 over USB on October 25, 2026 with `mise run microfreak:download --slot 292`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `b4d2ec3ec68120526514c0c1f4b072e4f47f778d56f024c477eb28aeed25a8d0`.
