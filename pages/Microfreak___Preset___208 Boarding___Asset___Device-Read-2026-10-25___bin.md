logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Boarding slot 208 capture
	- [Download the slot 208 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___208%20Boarding___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 208 over USB on October 25, 2026 with `mise run microfreak:download --slot 208`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `b0cbdcfd69e7e34baa3d03dca93537feebf84e87fcbca9d0d302090ee4cd3d21`.
