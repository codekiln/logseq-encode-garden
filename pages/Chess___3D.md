logseq-entity:: [[Logseq/Entity/Game]]
tags:: [[Diataxis/Concept]]
alias:: [[Three-Dimensional Chess]], [[3D Chess]]
see-also:: [[PKM/Log/26/09/23 Wed - Stacked Discussions in Multi-Tier Gardens]]

- # 3D Chess
	- ## Overview
		- **3D chess** is the family of [[Chess]] variants played on a board with a third spatial axis, so a piece can change level as well as rank and file. The name also travels as a figure of speech for reasoning several layers above the visible one.
		- The family has no single ruleset. Each variant answers the same design question differently: once a piece can leave the plane, which of the new directions is it allowed to travel, and who is allowed to travel them?
	- ## The main variants
		- ### Raumschach
			- Ferdinand Maack's 1907 variant, the oldest 3D chess still played, on a 5×5×5 cube [^1].
			- Each side has a king, a queen, two rooks, two bishops, two knights, two **unicorns**, and five pawns.
			- The unicorn exists because 3D space has a line type that 2D does not. A rook travels the 6 orthogonals, a bishop the 12 face diagonals, and the unicorn the 8 **triagonals** — the corner-to-corner lines through the cube. Without it, a third of the board's straight lines would have no slider.
		- ### Star Trek Tri-Dimensional Chess
			- The set on the *Enterprise* bridge in [[Star Trek]], three main 4×4 boards stacked in a stairstep with four small 2×2 **attack boards** that themselves move between pin positions.
			- The show never gave rules. The rulesets in circulation are fan work, Andrew Bartmess's being the widely used one [^2].
			- The movable attack boards are the interesting part: the geometry of the playing space changes during the game, which no orthodox chess variant does.
		- ### Dragonchess
			- Gary Gygax's 1985 variant, three 12×8 boards read as sky, ground, and underworld, with piece types that can only occupy certain levels [^3].
			- Level here is terrain rather than pure geometry — a griffin belongs to the sky board the way a bishop belongs to one color.
		- ### 5D Chess with Multiverse Time Travel
			- Conor Petersen's 2020 game, which adds time and branching timelines rather than height: a piece can move to an earlier board state, which forks a new timeline that must also be won [^4].
			- It is the clearest demonstration that "another dimension" need not be spatial. What matters is that a move now has coordinates the 2D game had no slot for.
	- ## What adding a dimension does to a game
		- **The board grows as a power.** An `n`-per-side board in `d` dimensions holds `n^d` cells. Chess goes 64 → 512 at 8³; tic-tac-toe goes 9 → 27 at 3³.
		- **Adjacency grows faster.** A cell has `3^d - 1` neighbors: 8 in two dimensions, 26 in three, 80 in four. Every piece that moves by adjacency or by ray gets more expensive to defend against than to play.
		- **Draws get harder to reach.** Winning lines multiply faster than cells do, so the attacker gains relative to the defender. This is the structural reason several multidimensional games that draw easily in the plane are outright first-player wins in the cube.
		- **Visualization becomes the binding constraint.** Nearly every 3D variant is displayed as stacked 2D boards, because humans read a plane and do not read a cube. The design problem is as much interface as rules.
	- ## The same move in tic-tac-toe
		- **Qubic**, 4×4×4 tic-tac-toe, is the canonical multidimensional version. Oren Patashnik solved it by computer in 1980: a first-player win [^5]. The flat 3×3 game is a draw under correct play and 3×3×3 is a trivial first-player win, so the cube takes away the defender's refuge at both sizes.
		- The **Hales–Jewett theorem** makes the draw-killing effect a theorem rather than an observation: for any side length `n` and any number of players, there is a dimension `d` high enough that `n^d` tic-tac-toe cannot end in a draw at all — someone must complete a line [^6]. Combined with the strategy-stealing argument, which shows the first player can always at least draw, that forces a first-player win in high enough dimension.
		- The phrase **hyper tic-tac-toe** is used two ways, and they are different games.
			- `n^d` tic-tac-toe, the literal dimensional generalization above.
			- **Ultimate tic-tac-toe**, a 3×3 grid of 3×3 boards where your move inside a small board dictates which small board your opponent plays in next. This is nesting rather than a new axis, and it is a recursion of the same plane — but it produces the same felt effect, a move that is legal locally and disastrous globally.
	- ## Why the family stays small
		- Raumschach dates to 1907 and Qubic's solution to 1980, and neither displaced its flat parent. The added directions raise the branching factor past what a person can hold, without adding a decision that feels qualitatively new — a unicorn is a bishop that had one more axis to use.
		- The variants that stayed interesting are the ones that changed something other than the count of axes: Star Trek's boards that move, Dragonchess's levels that restrict who may stand on them, 5D Chess's timelines that must each be won. Depth came from making the extra dimension mean something, not from having one.
	- ## Footnotes
		- [^1]: https://en.wikipedia.org/wiki/Raumschach — Maack's 5×5×5 variant, piece set, and the unicorn's triagonal move.
		- [^2]: https://en.wikipedia.org/wiki/Three-dimensional_chess — survey of the family, including the Star Trek set and the Bartmess ruleset's fan origin.
		- [^3]: https://en.wikipedia.org/wiki/Dragonchess — Gygax's three-board variant, published in *Dragon* #100.
		- [^4]: https://en.wikipedia.org/wiki/5D_Chess_with_Multiverse_Time_Travel — time and timeline branching as the added axes.
		- [^5]: https://en.wikipedia.org/wiki/3D_tic-tac-toe — Qubic, and Patashnik's 1980 computer-assisted solution.
		- [^6]: https://en.wikipedia.org/wiki/Hales%E2%80%93Jewett_theorem — the no-draw guarantee for sufficiently high dimension.
