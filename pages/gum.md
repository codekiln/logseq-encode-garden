logseq-entity:: [[Logseq/Entity/software-project]]
created-by:: [[Charm]]

- # [gum](https://github.com/charmbracelet/gum)
	- CLI for **glamorous shell scripts** [^1]: add interactive, styled UX to bash/zsh by composing subcommands—structured primitives that print to stdout, fit pipes, and capture into variables—instead of writing a full CLI in Go or Python.
	- ## Primitives (examples)
		- `gum input` — text prompt (e.g. placeholder).
		- `gum choose` — menu selection.
		- `gum confirm` — yes/no.
		- `gum filter` — fuzzy finder.
		- `gum spin` — spinner around a command.
		- `gum style` — colors, borders, layout.
	- ## Mental model
		- Not a classic CLI framework; closer to **Unix pipes + TUI-like components**—replace ad hoc `read` / `echo` / raw ANSI with consistent interactive building blocks while staying in the shell.
	- ## Minimal examples
		- ~~~
		  name=$(gum input --placeholder "Enter your name")
		  ~~~
		- ~~~
		  choice=$(gum choose "build" "test" "deploy")
		  ~~~
		- ~~~
		  gum confirm "Deploy to prod?" && ./deploy.sh
		  ~~~
		- ~~~
		  gum spin --title "Deploying..." -- ./deploy.sh
		  ~~~
	- ## Where it sits
		- **Raw shell** — bash, zsh.
		- **Gum** — quick interactive shell UX and prompts.
		- **Full TUI apps** — Bubble Tea, Textual, etc.
		- **Full CLI frameworks** — Cobra, Click, etc.
		- When you want fast script UX upgrades, use gum; when you want a stateful multi-pane app, use a TUI framework instead.
	- ## Why people reach for it
		- Less friction than flags-only scripts (scripts ask instead of you memorizing options). [^2]
		- Better DX: color, layout, spinners, confirmations—still composable shell, no framework lock-in.
	- ## Limitations
		- **Ephemeral** interaction, not a persistent layout; not a Kanban board or long-running dashboard.
		- Not stateful between invocations; no native multi-pane UI.
		- Complements [[tmux]] (layout + persistence), **fzf** (sometimes overlapping with `gum filter`), and agent/orchestration glue—not a replacement for those.
	- ## Footnotes
		- [^1]: https://github.com/charmbracelet/gum
		- [^2]: https://tech.aufomm.com/how-do-i-use-charmbracelet-gum-to-improve-my-scripts/
