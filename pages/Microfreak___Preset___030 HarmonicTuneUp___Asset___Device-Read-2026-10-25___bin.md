logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # HarmonicTuneUp slot 30 capture
	- [Download the slot 30 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___030%20HarmonicTuneUp___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 30 over USB on October 25, 2026 with `mise run microfreak:download --slot 30`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `1161deb38b21ae0cab696b3533c1218cb374a16831be4c01ae843b8e5f1e34dd`.
