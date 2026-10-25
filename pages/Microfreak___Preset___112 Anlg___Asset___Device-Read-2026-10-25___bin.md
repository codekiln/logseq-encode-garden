logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Anlg slot 112 capture
	- [Download the slot 112 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___112%20Anlg___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 112 over USB on October 25, 2026 with `mise run microfreak:download --slot 112`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `f5474bf7c6f4a596628fe5471f0c315c93d22c514d9ea7513c9b33bfa38d5b73`.
