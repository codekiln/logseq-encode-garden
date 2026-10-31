logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Dirty slot 209 capture
	- [Download the slot 209 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___209%20Dirty___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 209 over USB on October 25, 2026 with `mise run microfreak:download --slot 209`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `48d5561bf615faabad46a7ccde6903bdd98c488274cbc87135a60ad1518c6f0c`.
