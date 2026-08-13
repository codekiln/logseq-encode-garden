tags:: [[herdr]], [[Diataxis/Explanation]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Claude/Code/Q/Why can't I scroll up in tmux copy mode when Claude Code is in TUI mode?]], [[herdr/Explanation/Doubled History After a Pane Resize]], [[tmux/Mode/Copy]]

- # Copy mode on the alternate screen
	- Line references read the [herdrdev/herdr](https://github.com/herdrdev/herdr) source at commit `952729ee` — `herdr 0.8.0`, `preview-2026-08-04-d78e3d3b5126-90-g952729ee`. Pane figures measured with [[Claude/Code]] 2.1.228.
	- ## Overview
		- `prefix+[` enters copy mode. In some panes running [[Claude/Code]], Ctrl-U (half page up) and `k` (line up) leave the viewport pinned at the top of the visible screen, with no bell and no message. In other Claude Code panes the same keys page through history normally. The mouse wheel scrolls in both, which makes copy mode look broken.
		- The panes that stay pinned are on the terminal's **alternate screen**, and the alternate screen is built with zero scrollback. Copy mode is a viewport over the pane's scrollback, so in those panes it has nothing above the visible rows to reach.
		- Where copy mode *does* page through history but the same text appears twice at two different widths, the cause is a pane resize — see [[herdr/Explanation/Doubled History After a Pane Resize]].
	- ## Context
		- [[tmux]] shows the same symptom for the same underlying reason, framed there around Claude Code's `/tui fullscreen` mode: [[Claude/Code/Q/Why can't I scroll up in tmux copy mode when Claude Code is in TUI mode?]]. The alternate-screen state seen in herdr arrives by a different route — the attached view of a session running as a background agent.
		- herdr's keyboard reference (`docs/next/website/src/content/docs/keyboard.mdx:67`) lists every copy-mode motion and even warns about the Ctrl-B prefix collision, while leaving out that alternate-screen panes have no scrollback for those motions to traverse. The copy-mode CHANGELOG entries (`docs/next/CHANGELOG.md:251`, `:419`, `:458`) leave the same connection out. That gap is what makes the symptom read as a broken keybinding.
	- ## Mechanism
		- ### The alternate screen is created with zero scrollback
			- herdr's vendored terminal sets `max_scrollback` to zero for the alternate screen by construction (`vendor/libghostty-vt/src/terminal/Terminal.zig:3723-3726`):
			- ~~~zig
			  .max_scrollback = switch (key) {
			      .primary   => primary.pages.explicit_max_size,
			      .alternate => 0,
			  },
			  ~~~
			- With no scrollable range, `PageList.scrollbar()` special-cases its answer to `total == rows` (`vendor/libghostty-vt/src/terminal/PageList.zig:3375-3385`). The C getter reads the **active** screen (`vendor/libghostty-vt/src/terminal/c/terminal.zig:852`), and the header spells out the alternate-screen consequence (`vendor/libghostty-vt/include/ghostty/vt/terminal.h:241-248`).
			- herdr turns that scrollbar into `ScrollMetrics`, where `max_offset_from_bottom = scrollbar.total - scrollbar.len` (`src/pane/terminal.rs:1648-1651`). On the alternate screen that subtraction yields 0.
		- ### Copy mode holds a viewport offset and a cursor
			- `CopyModeState` carries a pane id, cursor row and column, an entry offset, a selection, and a search state (`src/app/input/copy_mode.rs:64-74`). It owns no buffer — everything it shows comes from the pane's terminal.
			- So with `max_offset_from_bottom = 0`, every paging key takes the clamp branch (`src/app/input/copy_mode.rs:517-533`), which pins the offset at its maximum and spends the remaining motion walking the cursor upward inside the visible screen.
			- `k` at cursor row 0 calls `scroll_pane_up`, which clamps to a no-op (`:474-481`).
			- The silence is deliberate. Two tests assert this shape: `copy_mode_ctrl_u_moves_cursor_when_history_top_clamps` (`:1988`) and the symmetric `copy_mode_ctrl_d_moves_cursor_when_live_bottom_clamps` (`:2020`).
		- ### The keys themselves are bound as expected
			- Bindings live at `src/app/input/copy_mode.rs:151-165`, with PageUp/PageDown at `:132` and `:136`, and `g`/`G` at `:179-180`.
			- | Key               | Motion                |
			  | ----------------- | --------------------- |
			  | Ctrl-U / Ctrl-D   | half page up / down   |
			  | Ctrl-B / Ctrl-F   | full page up / down   |
			  | PageUp / PageDown | full page up / down   |
			  | g / G             | history top / bottom  |
			- One wrinkle: the herdr prefix is checked before copy-mode dispatch (`:19-22`), and the default prefix is `ctrl+b`, so inside copy mode Ctrl-B enters prefix mode instead of paging up. Test: `copy_mode_prefix_takes_priority_over_ctrl_b_page_up` (`:1195`). Documented at `docs/next/website/src/content/docs/keyboard.mdx:67`.
	- ## Which Claude Code panes land on the alternate screen
		- The ordinary REPL runs on the **primary** screen and accumulates real scrollback, which is why copy mode works there.
		- Claude Code's full-screen views are alternate-screen interfaces. The one behind this symptom is the attached view of a session running as a background agent — started with `claude --bg` or `--background`, or a running session moved to the background. The marker is `"template": "bg"` alongside `"backend": "daemon"` in `~/.claude/jobs/<short-id>/state.json`, and `ls ~/.claude/jobs/` lists them.
		- Measured on one machine at one moment, across panes all running an identical `claude --permission-mode auto`:
			- | Pane                          | `scroll.max_offset_from_bottom` |
			  | ----------------------------- | ------------------------------- |
			  | running as a background agent | 0                               |
			  | running as a background agent | 0                               |
			  | ordinary interactive          | 254                             |
			  | ordinary interactive          | 483                             |
			  | ordinary interactive          | 696                             |
			  | ordinary interactive          | 892                             |
			  | ordinary interactive          | 2705                            |
		- One command reads it for any pane:
			- ~~~sh
			  herdr pane get <pane-id> | python3 -c "import json,sys; print(json.load(sys.stdin)['result']['pane']['scroll'])"
			  ~~~
			- `max_offset_from_bottom = 0` on a pane that has been running for a while places it in this state.
	- ## What remains reachable
		- The primary screen's scrollback is kept in its own screen and returns when the program leaves the alternate screen.
		- A pane respawn reuses the same `PaneTerminal`, so scrollback survives an agent process exiting and relaunching in place (`src/app/api.rs:526-605`, test `:2139-2178`).
		- The mouse wheel reaches the program. herdr's wheel arms run whatever mode the pane is in (`src/app/input/mouse.rs:950-956`, routing at `:1761-1806`), so the wheel is forwarded and the program scrolls its own transcript. Copy mode has its own path: its search and word motions read the active screen's rows (`src/pane/terminal.rs:377-386`).
		- herdr has a programmatic alt-screen history path for **reads**. `src/server/alt_screen_read.rs` drives an idle, recognized agent's own wheel scrollback and returns the viewport to the bottom afterwards; it requires `WheelRouting::MouseReport` (`:364-376`). Documented at `docs/next/website/src/content/docs/agent-automation.mdx:84-88` and `skills/herdr/SKILL.md:183`.
			- It did not engage on the panes measured here: `herdr pane read <pane> --source recent --lines 500` returned 45 rows — the visible row count — on a background-agent pane, against 483 rows on an ordinary pane.
	- ## Workarounds
		- 1. Treat a long-lived agent's pane as a view and have the agent write its reports to files.
		- 2. The session transcript on disk is the real scrollback: `~/.claude/projects/<path-slug>/<session-id>.jsonl`.
		- 3. The mouse wheel, which reaches the program.
		- 4. `export CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` puts Claude Code on its inline renderer, so conversation output flows into the pane's scrollback.
		- 5. Keep long-lived agents as ordinary interactive sessions, which stay on the primary screen.
	- ## Misconceptions
		- **"The scrollback limit is too low."** That limit is `advanced.scrollback_limit_bytes`, default 10,000,000 bytes (`src/config/model.rs:941-947`, `src/config.rs:53`), and `0` disables scrollback outright. It is the first thing people suspect, and it is unrelated to the alternate screen.
		- **"Something cleared the scrollback."** `CSI 3J` and `CSI ?3J` do drop herdr's scrollback (`src/pane/osc.rs:713-758`), so that is worth ruling out on its own.
		- **"herdr's copy mode is broken."** Alternate screen means zero scrollback in every terminal; [[tmux]] behaves the same way in the same situation.
		- **"The wheel and copy mode are interchangeable."** The wheel reaches the program; copy mode reaches the terminal. In a full-screen program those are two different sources, and that asymmetry is the whole puzzle.
