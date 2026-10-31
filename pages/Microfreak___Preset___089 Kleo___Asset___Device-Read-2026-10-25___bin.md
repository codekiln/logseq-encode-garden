logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Kleo slot 89 capture
	- [Download the slot 89 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___089%20Kleo___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 89 over USB on October 25, 2026 with `mise run microfreak:download --slot 89`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `f957c138249e42b8d376c20288aaca1e8efe77c1ed8cb957195e120d9d939bcb`.
