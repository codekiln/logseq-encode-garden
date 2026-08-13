tags:: [[herdr]], [[Diataxis/Explanation]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[herdr/Explanation/Copy Mode on the Alternate Screen]], [[tmux/Mode/Copy]]

- # Doubled history after a pane resize
	- Observed in `herdr 0.8.0` with [[Claude/Code]] 2.1.228.
	- ## Overview
		- Scrolling up in copy mode in an ordinary interactive pane shows the same content twice — once soft-wrapped to roughly 60 columns, once at the pane's full width — with a hard visual seam between the two regions. It reads like corrupted history. The seam marks where the pane was resized.
		- Where copy mode refuses to scroll above the visible screen at all, the cause is different — see [[herdr/Explanation/Copy Mode on the Alternate Screen]].
	- ## Mechanism
		- A [[TUI]] that wraps its own output emits real line breaks at the width in force when it printed. Those breaks belong to the program, so the terminal keeps them as written when the pane changes size; only soft wraps can be reflowed.
		- Widening a pane makes [[Claude/Code]] repaint its recent transcript at the new width, while the old narrow rendering stays above it in scrollback. The same text then exists at two widths, and the boundary between them is the resize.
	- ## Example
		- On a 165-column pane (`herdr pane layout` reported width 165) holding a 699-row retained buffer, one sentence appeared 4 times and several others twice:
			- ~~~sh
			  herdr pane read <pane> --source recent-unwrapped --lines 700 \
			    | sed 's/^ *//' | awk 'length($0)>40' | sort | uniq -c | sort -rn | head
			  ~~~
	- ## How to read it
		- The width change marks the resize point. Everything is present, and the narrow block carries its full text.
		- Widening a pane mid-session produces this artifact every time. For clean history, size a pane before starting an agent in it and leave it at that width.
