logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Kendrok slot 63 capture
	- [Download the slot 63 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___063%20Kendrok___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 63 over USB on October 25, 2026 with `mise run microfreak:download --slot 63`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `01099414a2e79ab3f6c25402698144da3e4eeffa1e1259d57dfa002cdf716ed2`.
