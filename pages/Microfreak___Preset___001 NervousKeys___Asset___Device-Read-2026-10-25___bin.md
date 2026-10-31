logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # NervousKeys slot 1 capture
	- [Download the slot 1 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___001%20NervousKeys___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 1 over USB on October 25, 2026 with `mise run microfreak:download --slot 1`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `7ddbc3e577cac6cf965d35c5c403bb292c67495c033fc10443ef8aae2b787a8d`.
