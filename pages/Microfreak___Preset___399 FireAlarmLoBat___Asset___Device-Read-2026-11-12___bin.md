logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # FireAlarmLoBat slot 399 capture
	- [Download the slot 399 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___399%20FireAlarmLoBat___Asset___Device-Read-2026-11-12.bin)
	- Read from the connected MicroFreak's slot 399 over USB on November 12, 2026 with `mise run microfreak:download --slot 399`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `c1fd8141fd618369eedab241e3df0de7e8699f8d51e9e72b60a9580872d57a51`.
