logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: preset-synth-microfreak-parameter-payload-sha256
- # Parameter Payload Digest
	- Owning type: [[Logseq/Entity/Preset/Synth/Microfreak]].
	- The 64 lowercase hexadecimal characters of SHA-256 over the exact 4672-byte saved parameter payload. The 35-byte device header is excluded. This digest identifies the bytes from which the raw parameter properties were read; it does not establish that every parameter or external resource has been interpreted.
	- [MicroFreak parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) defines the payload boundary and digest. A fresh read with a different digest requires fresh verification of the raw properties.
