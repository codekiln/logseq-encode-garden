logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: preset-synth-microfreak-vco-type-raw-hex
- # Oscillator Type Raw Bytes
	- Owning type: [[Logseq/Entity/Preset/Synth/Microfreak]].
	- A saved `VCO.Type` field as `0x` followed by six lowercase hexadecimal digits. The first byte is a raw descriptor; the next two bytes are the raw value in little-endian order. Preserve all three bytes together. The descriptor's meaning, display conversion, units and range are unverified.
	- [MicroFreak parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) documents the serialized field and byte layout. The saved payload is identified by [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-parameter-payload-sha256]].
	- [[Microfreak/UG/06 Dig Osc/02 Param Controls]] names the related human control Type; the guide does not define this saved byte encoding.
