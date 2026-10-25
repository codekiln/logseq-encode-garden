logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Hihat A slot 144 capture
	- [Download the slot 144 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___144%20Hihat%20A___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 144 over USB on October 25, 2026 with `mise run microfreak:download --slot 144`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `afb0f935766095b723d783e6530ef2669f2cb4393b52c392485f3d2405006d34`.
