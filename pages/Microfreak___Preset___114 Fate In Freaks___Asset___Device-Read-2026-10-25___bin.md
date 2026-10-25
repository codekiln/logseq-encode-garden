logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Fate In Freaks slot 114 capture
	- [Download the slot 114 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___114%20Fate%20In%20Freaks___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 114 over USB on October 25, 2026 with `mise run microfreak:download --slot 114`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `4e872de3514746a49f56dc95ac18e0c9c041b5abfdb9deda4afe46c97e550e27`.
