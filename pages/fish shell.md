- # fish shell
	- People choose **fish shell** mainly because it prioritizes **interactive usability out of the box**. Unlike traditional shells such as **Bash** or **Zsh**, it ships with many conveniences enabled by default instead of requiring configuration frameworks.
	- ## 1. Rich autosuggestions
		- Fish shows **inline suggestions based on history and completions** while you type.
		- You can accept them with `→` or a keybinding.
		- Example:
			- ~~~
			  git chec
			  ~~~
		- Fish might automatically suggest:
			- ~~~
			  git checkout main
			  ~~~
		- This feels similar to IDE-style completion inside the terminal.
	- ## 2. Strong tab completion system
		- Fish includes **context-aware completions for thousands of commands**.
		- It often shows arguments, options, and descriptions.
		- Example:
			- ~~~
			  git checkout <TAB>
			  ~~~
		- You may see a list of branches with descriptions instead of just raw filenames.
		- Docs:
			- [fish shell docs: completions](https://fishshell.com/docs/current/completions.html)
	- ## 3. Human-readable scripting syntax
		- Fish intentionally avoids POSIX shell syntax in favor of something closer to structured programming.
		- Example comparison:
			- Bash:
				- ~~~bash
				  for f in *.txt; do
				    echo $f
				  done
				  ~~~
			- Fish:
				- ~~~fish
				  for f in *.txt
				      echo $f
				  end
				  ~~~
		- The syntax is easier for many people to read and avoids some quoting pitfalls.
		- Docs:
			- [fish shell docs: language reference](https://fishshell.com/docs/current/language.html)
	- ## 4. No configuration needed to feel modern
		- A new install already includes:
			- autosuggestions
			- syntax highlighting
			- good completions
			- a helpful prompt
		- With **Zsh**, many users install frameworks like **Oh My Zsh** to get similar features.
	- ## 5. Built-in web configuration UI
		- Running:
			- ~~~
			  fish_config
			  ~~~
		- opens a local web UI where you can change:
			- prompt themes
			- colors
			- variables
			- keybindings
	- ## 6. Better error handling
		- Fish surfaces errors clearly and avoids silent failures common in POSIX shells.
		- Example:
			- using an undefined variable shows a warning rather than expanding to empty.
	- ## 7. Friendly scripting primitives
		- Features like:
			- universal variables
			- structured loops and conditions
			- easier array handling
		- make interactive scripting less fragile.
		- Docs:
			- [fish shell](https://fishshell.com)
	- ## The main tradeoff
		- Fish **is not POSIX-compatible**, so many scripts written for Bash will not run in Fish without modification.
		- For that reason, many people use:
			- **fish** for interactive use
			- **bash** or **sh** for scripts
	- ## Typical users who prefer fish
		- Fish tends to appeal to:
			- developers who want **IDE-like terminal ergonomics**
			- people who do not want to maintain large shell config frameworks
			- users who spend lots of time in an interactive terminal
