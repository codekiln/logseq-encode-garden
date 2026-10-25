logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Stab One slot 150 capture
	- [Download the slot 150 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___150%20Stab%20One___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 150 over USB on October 25, 2026 with `mise run microfreak:download --slot 150`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `eca06c6a1c7bafc951da55f8a6e4e0a777753f6b4eed188b98748c85c86c2f8d`.
