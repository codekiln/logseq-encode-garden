logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Amigras slot 125 capture
	- [Download the slot 125 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___125%20Amigras___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 125 over USB on October 25, 2026 with `mise run microfreak:download --slot 125`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `4ceb35d094561a3ed60f799565feffe13d5ddea0ad21927974a51ac675681ebc`.
