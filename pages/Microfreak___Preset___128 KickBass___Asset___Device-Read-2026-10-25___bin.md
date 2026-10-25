logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # KickBass slot 128 capture
	- [Download the slot 128 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___128%20KickBass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 128 over USB on October 25, 2026 with `mise run microfreak:download --slot 128`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `213a55b9cfc9dda7261a4f5668d7359d834ce5b5846e48145387de8c35c81c61`.
