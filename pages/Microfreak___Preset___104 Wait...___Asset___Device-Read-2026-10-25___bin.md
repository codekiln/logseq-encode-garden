logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Wait... slot 104 capture
	- [Download the slot 104 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___104%20Wait...___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 104 over USB on October 25, 2026 with `mise run microfreak:download --slot 104`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `e266aabdf69d57c45d2571b0cb1e19991b6e8b7b583a739a88c77b0673e74a77`.
