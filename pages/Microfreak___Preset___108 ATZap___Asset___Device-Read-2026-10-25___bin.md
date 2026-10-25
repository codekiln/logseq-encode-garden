logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # ATZap slot 108 capture
	- [Download the slot 108 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___108%20ATZap___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 108 over USB on October 25, 2026 with `mise run microfreak:download --slot 108`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `5c59e8fdcdf449874c086ac003feccd032ffa50cb1b3dfba1da54bb0d1c50422`.
