logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Incoming Ship slot 160 capture
	- [Download the slot 160 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___160%20Incoming%20Ship___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 160 over USB on October 25, 2026 with `mise run microfreak:download --slot 160`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `c095f96461f2f3fa3e1053a6f1dc64a92f5d6427a8983f90c2473f56c2a58604`.
