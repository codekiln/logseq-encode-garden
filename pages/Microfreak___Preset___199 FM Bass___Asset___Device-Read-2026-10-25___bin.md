logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # FM Bass slot 199 capture
	- [Download the slot 199 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___199%20FM%20Bass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 199 over USB on October 25, 2026 with `mise run microfreak:download --slot 199`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `5e81465e9bf7436c651f072fcbbdd65364da40237509a67a7208b19c77dc0a92`.
