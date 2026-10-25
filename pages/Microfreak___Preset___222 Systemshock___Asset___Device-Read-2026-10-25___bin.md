logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Systemshock slot 222 capture
	- [Download the slot 222 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___222%20Systemshock___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 222 over USB on October 25, 2026 with `mise run microfreak:download --slot 222`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `c562f72f82bea35434413c0d11e50ba1a04f9d51f7031a95bfd0af5c95c3c708`.
