logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Sweep SQ slot 71 capture
	- [Download the slot 71 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___071%20Sweep%20SQ___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 71 over USB on October 25, 2026 with `mise run microfreak:download --slot 71`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `677dcc4d1f4743769c59ddccf783a5138afdada7a286648aaf7b5e639755eb77`.
