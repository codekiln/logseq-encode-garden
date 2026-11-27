logseq-entity:: [[Logseq/Entity/Definition]]

- # Launchpad Custom Slot
	- In this garden, **Launchpad Custom Slot** pages document one of the eight Custom Mode slots on the [[Novation/Launchpad/Pro/Mk3]]: which named mode it holds now, and which modes it held before.
	- ## When a page is a Launchpad Custom Slot
		- The page's subject is one slot on the device, opened with a Track Select button in Custom mode ([[Launchpad/UG/08 Custom Modes/02 Default Custom Modes]]).
		- Not this entity: the mode itself, which is a [[Logseq/Entity/Launchpad/Custom/Mode]] page under `Launchpad/Custom/Available/`.
	- ## Naming
		- `Launchpad/Custom/Slot/<N>`, with `<N>` from 1 to 8, so there are exactly eight pages. [[Launchpad/Custom/Slot]] embeds all eight.
	- ## Frontmatter
		- Set `logseq-entity` to [[Logseq/Entity/Launchpad/Custom/Slot]].
		- Set `current-custom-mode` to the `Launchpad/Custom/Available/<Name>` page of the mode the slot holds now. Leave it out while the slot holds its factory layout or a mode with no page.
	- ## Page shape
		- First block: the mode the slot holds now and since when, and the slot's Track Select button page under [[Launchpad/UI]]. For a slot with no recorded mode, its factory layout from [[Launchpad/UG/11 Appendix/01 Default MIDI Mappings]].
		- `## History`, collapsed: one child per change, oldest first, starting with the date page and the mode's page, then the log, session or idea page where the change is recorded.
	- ## Sending a mode to a slot
		- Add a History entry, then point `current-custom-mode` and the first block at the new mode. No page is renamed: the mode's page stays under `Launchpad/Custom/Available/`.
