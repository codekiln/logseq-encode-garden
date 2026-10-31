logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Karpad slot 188 capture
	- [Download the slot 188 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___188%20Karpad___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 188 over USB on October 25, 2026 with `mise run microfreak:download --slot 188`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `de181805063472a4540f60d0be94892d96e354edf1b6b37ab17f115452fe773c`.
