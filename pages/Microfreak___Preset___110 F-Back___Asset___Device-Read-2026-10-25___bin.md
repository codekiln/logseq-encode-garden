logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # F-Back slot 110 capture
	- [Download the slot 110 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___110%20F-Back___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 110 over USB on October 25, 2026 with `mise run microfreak:download --slot 110`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `692166f3056b804581afe15374e7b963d6763868fd8fb4e87075c4ac9bf2e243`.
