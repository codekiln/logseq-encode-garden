logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Snitch 5 slot 126 capture
	- [Download the slot 126 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___126%20Snitch%205___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 126 over USB on October 25, 2026 with `mise run microfreak:download --slot 126`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `5c06d52c9dc147edb1812f85f64fbb6c890555924acc584c66dfeb066beff4ed`.
