logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Simon Spati]]
date-created:: [[2026]]

- # [Neomd](https://neomd.ssp.sh)
	- [ssp-data/neomd](https://github.com/ssp-data/neomd) — [[GitHub/Star]]s: 264 as of [[2026-08-07 Fri]]. MIT licensed.
	- Keyboard-first [[TUI]] email client: incoming mail renders as [[Markdown]], outgoing mail is composed in [[Neovim]] and converted to minimal HTML on send.
	- Written in [[Go]] on the [[Charm]] stack — Bubble Tea for the interface, [[Glamour]] for rendering, Lip Gloss for styling, goldmark for the Markdown-to-HTML step. The IMAP client is adapted from msgvault.
	- ## Screener
		- Takes the screener idea from [HEY](https://www.hey.com/how-it-works/): a message from an unknown sender waits in **ToScreen** and the sender gets classified exactly once, after which everything from that address routes on its own.
		- `I` / `O` / `F` / `P` sort a sender into Inbox, ScreenedOut, Feed, or PaperTrail — newsletters and receipts never reach the inbox in the first place.
		- The remaining folders follow [Getting Things Done](https://gettingthingsdone.com/): Waiting, Someday, and Scheduled (`Mw` / `Mm` / `Mc`), then Archive when a thread is finished. Filing stays shallow on purpose — search instead of a folder tree.
	- ## Headless mode
		- `neomd --headless` runs the screener as a daemon with no interface, watching the screener list files for changes via [[Syncthing]]. Meant for a NAS or homeserver, so the TUI on a laptop or phone opens onto mail that has already been sorted.
	- ## Away from the desk
		- Usable from a phone over SSH against that daemon. The project documents an Android setup through Termux; on [[iOS]] a terminal such as [[Blink Shell]] fills the same role.
