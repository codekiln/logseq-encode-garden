# Logseq #Math Rendering
	- [[My Note]] I have a [[rulesync/command]] in this repo for doing cleanup of logseq math in a #Markdown page: `.rulesync/commands/logseq-cleanup-math.md`
	- Logseq supports **[[LaTeX]] math rendering** using **[[KaTeX]]** — both inline and block math. Here's how to use it:
		- ## 🧮 Inline Math
			- Wrap your LaTeX expression in single dollar signs:
				- This is inline math: $E = mc^2$
			- Example:
				- ~~~
				  This is inline math: $E = mc^2$
				  ~~~
		- ## 📐 Block Math
			- Wrap your expression in double dollar signs on **separate lines** (not inline):
				- $$
				  \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
				  $$
			- Example format:
				- ~~~
				  - $$
				    \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
				    $$
				  ~~~
			- **Important:** The `$$` must be on separate lines, not inline like `$$formula$$`. This ensures proper rendering in Logseq.
		- ## ⚙️ Optional Settings
			- If math doesn't render:
				- Open **Settings → Editor**.
				- Ensure **"Enable math rendering (KaTeX)"** is toggled on.
				- Reload Logseq (Cmd/Ctrl+R).
		- ## ✅ Tip
			- You can mix math and Markdown freely — KaTeX supports most LaTeX commands except for those that rely on packages not supported by KaTeX (e.g. `\usepackage`).