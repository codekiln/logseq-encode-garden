logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: preset-synth-microfreak-vcf-cutoff-raw-hex
- # Filter Cutoff Raw Bytes
	- Owning type: [[Logseq/Entity/Preset/Synth/Microfreak]].
	- A saved `VCF.Cutoff` field as `0x` followed by six lowercase hexadecimal digits. The first byte is a raw descriptor; the next two bytes are the raw value in little-endian order. Preserve all three bytes together. The descriptor's meaning, display conversion, units and range are unverified.
	- [MicroFreak parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) documents the serialized field and byte layout. The saved payload is identified by [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-parameter-payload-sha256]].
	- [[Microfreak/UG/07 Filter/01 Modifying Sound/04 Cutoff Frequency]] names the related human control Cutoff; the guide does not define this saved byte encoding.
