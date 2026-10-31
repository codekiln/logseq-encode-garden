logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Chord Bass slot 32 capture
	- [Download the slot 32 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___032%20Chord%20Bass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 32 over USB on October 25, 2026 with `mise run microfreak:download --slot 32`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `97e157b8dd61e62d6537fd55923c22e213ce355bec65cc533a85e3940cbd7d01`.
