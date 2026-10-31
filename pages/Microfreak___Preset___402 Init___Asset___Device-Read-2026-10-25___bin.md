logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Init slot 402 capture
	- [Download the slot 402 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___402%20Init___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 402 over USB on October 25, 2026 with `mise run microfreak:download --slot 402`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `4a8c0d8c42b1ad9bda0ea28fd1853371aa0d5ab9445ffd0ef1d6fcac054c99fd`.
