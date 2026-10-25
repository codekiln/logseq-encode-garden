logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Analog Chaser slot 116 capture
	- [Download the slot 116 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___116%20Analog%20Chaser___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 116 over USB on October 25, 2026 with `mise run microfreak:download --slot 116`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `a4ec1d179de154900e2c88540a51a0154976433023ee9645a7c42a4bae3118a2`.
