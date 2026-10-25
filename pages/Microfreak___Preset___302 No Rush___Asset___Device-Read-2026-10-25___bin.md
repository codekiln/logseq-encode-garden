logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # No Rush slot 302 capture
	- [Download the slot 302 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___302%20No%20Rush___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 302 over USB on October 25, 2026 with `mise run microfreak:download --slot 302`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `b45a2982d1128052cd05087b2df72e37133d609cb8ce5ed70081dea97f81fd2f`.
