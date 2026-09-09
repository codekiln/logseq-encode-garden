logseq-entity:: [[Logseq/Entity/Book]]
created-by:: [[Person/Dusty Phillips]]
date-created:: [[2024]]
readwise-link:: https://read.readwise.io/read/01m207ez76jh7f9fb9z5q1wq6a

- # [LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/)
	- Author: [[Person/Dusty Phillips]] ([phillips.codes](https://phillips.codes/))
	- Free online book on [[LazyVim]]; highlights below are from [Chapter 1](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/) (imported [[2026/09/08]])
	- Copyright © 2024 Dusty Phillips
	- ## Summary
		- Positions [[LazyVim]] as a coherent plugin mindset on top of [[nvim]], not a fork of Vim; covers history (ed → ex → Vim), RSI motivations for modal editing, install (including `brew install --HEAD neovim`), recommended CLI deps (`lazygit`, `ripgrep`, `fd`), and the Lazy.nvim dashboard/`S` sync workflow.
	- ## Highlights
		- > You may also be familiar with another iteration of `ed` called `sed`, the "stream editor." To this day it is still used for modifying text in a shell pipeline.
			- Wow, I didn't know the ed -> sed history. Cool.
		- > The `ed` command was also **ex**tended to create another line editor called `ex`, which isn’t really used anymore, except (extensively) as a submode of Vim. In fact, if you install Neovim and type `ex` on your command line, you will get a very crippled instance of Neovim that only supports `ex` commands.
			- I love the historical roots of vim. Reminds me of that experimental Rust rewrite of vim that let you replace the ex substrate with any typescript implementation
		- > This is the big one for me. I used Vim a lot through my early career, though, like many developers, I switched to VS Code when it came out in 2015. I spend a lot of time at my keyboard, and by 2020, I was so crippled by RSI that I spent six months exclusively coding by voice (a blog article on the topic has made me more famous than I expected). A friend suggested I switch back to modal editing, and it made a huge difference. The vast majority of Vim keystrokes do not require holding multiple keys with the same hand, something that really aggravates carpal tunnel syndrome.
			- I never thought about modal editing as a way to prevent RSI before, but I have to say I've kind of felt the "left hand claw" in many programs that require too many keyshorts that rely on that position.
		- > To be clear, LazyVim is Vim. The editing experience is identical. It’s not a new iteration or version of Vim in the way that Neovim is. Instead, LazyVim is a mindset; it starts with an agreement on what constitutes the best plugin configurations for modern development, and a configuration that makes them work well together (keeping different plugins' keybindings from conflicting with each other is one of the major pain-points when managing editor configurations manually).
		  
		  But if you go into using LazyVim with the mindset that this experience will be better than any other editing experience you’ve worked with before, and accept that you will be retraining some keyboard muscle memory, you will find that it is extremely well thought out. In my experience, it is *exactly* what a 2020s-era modal editing experience should be.
			- I'm heartened to hear this pain-point acknowledged, as the main drawback of customization - particularly customization that involves plugins made by others -  is having a hard time knowing everything is going to work together harmoniously.
			- > you will find that it's extremely well thought-out
			- Yes, this is exactly what I want to hear.
		- > Neovim development happens at a super fast pace compared to their release cycle, so it is not uncommon for folks to run the latest nightly build. I have only rarely encountered bugs in builds cut from the master branch on Github, so it’s generally safe. I usually run off the latest stable release when it comes out, and then when some new plugin update says “here’s a cool feature if you use Neovim nightly,” I’ll install the latest Neovim build instead.
		- > If you want to live on the edge, `brew install --HEAD neovim` will install the latest nightly version of Neovim, which is probably, but not guaranteed to be, stable.
		- > If you want to, you can run the command `<Escape>:Tutor<Enter>` to open an interactive text file that you can read through and edit while learning the basics of Neovim. I do recommend doing this at some point, but now may not be the right time. A lot of things that are “normal” in the Vim tutor are different (better!) using LazyVim. The rest of this book does **not** assume you have gone through the tutor.
		- > I strongly recommend installing `lazygit`, `ripgrep` and `fd`, which are used by LazyVim to provide enhanced git, string searching, and file searching behaviours. Most operating system package managers will have these available for trivial installation.
		- > You may see it compile and install a bunch of treesitter grammars; if you see a message to “Show More” use `G` (i.e. `Shift+g`) to skip to the end.
		- > You can access this UI from the dashboard simply by pressing the `l` key, which is labelled in the dashboard as `Lazy`. The label should probably be `Lazy Plugin Manager` to make it a bit clearer, but now you know what `Lazy` means so you won’t forget.
		- > Typically, the only Lazy.nvim keybinding I use is `S`, for `Sync`. This is equivalent to running install, clean, and update in a single action. It guarantees that the versions of plugins that are actually installed are exactly consistent with the ones specified in the LazyVim configuration.
		- id:: 6aa19602-3f9f-42cf-a7f9-1b41a8fd0aaf
		  > you can find my own dot files on GitHub in the [dusty-phillips/dotfiles](https://github.com/dusty-phillips/dotfiles) repository.
	- ## Links
		- [Book home](https://lazyvim-ambitious-devs.phillips.codes/)
		- [Chapter 1](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/)
		- [dusty-phillips/dotfiles](https://github.com/dusty-phillips/dotfiles)