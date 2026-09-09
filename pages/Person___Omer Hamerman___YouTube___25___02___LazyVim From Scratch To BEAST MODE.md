created-by:: [[Person/Omer Hamerman]]
date-created:: [[2025/02/07]]
readwise-link:: https://read.readwise.io/read/01m02k97g130p60760ahj32qbz

- # [LazyVim From Scratch To BEAST MODE - YouTube](https://www.youtube.com/watch?v=evCmP4hH7ZU)
	- Speaker: [[Person/Omer Hamerman]] (channel credit in Readwise: **DevOps Toolbox**)
	- Channel: [DevOps Toolbox](https://www.youtube.com/@devopstoolbox) · ~20 mins · published [[2025/02/07]]
	- Topic: fresh [[LazyVim]] install, fuzzy file picker defaults, UI toggles, buffers, keymaps docs, mini.files extra
	- ## Video
		- {{video https://www.youtube.com/watch?v=evCmP4hH7ZU}}
	- ## Summary
		- Installs [[LazyVim]] from scratch (backing up prior Neovim state), demos leader/fuzzy picker (fzf-lua default; Telescope available), notification dismiss (`leader u` … `n`), buffer options, and points at the official keymaps table — see [[LazyVim/Doc/Keymaps]].
	- ## Highlights
		- > if you've already used   lazy in the past maybe just as a package manager  like I did this should look very familiar
		- > don't worry telescope is also available here   but it doesn't come as the default option which  I'm not actually sure why
			- LazyVim's default fuzzy finder for files uses `telescope.lua` [configured with a fuzzy file picker](/read/01m02k97g130p60760ahj32qbz?endLexposition=00009_00004_00000-001T&startLexposition=00007&emphasizeText=fuzzy%20file%20picker), though the author notes that [telescope is also available](/read/01m02k97g130p60760ahj32qbz?endLexposition=0000C_00004_00000-001h&startLexposition=0000A&emphasizeText=telescope%20is%20also%20available%20here) as an alternative option.
		- > remember   space starts the main command pallet space  space and your files pop in a fuzzy picker
		- > I don't know if the notifications above  annoy you as much as they annoy me but luckily   these are coming from FKS notifications which is  also the author of lazy so we were blessed with   a notification manager ler and youu opens the UI  options allowing control of animations background   color schemes and many other visual options  including yes dismissing notifications with   n so leader and you does the trick and whatever  no ifications on the screen disappear immediately
			- To dismiss notifications, you press `leader` and then `u` (`leader + u`) to open the notification manager options, where you can then press `n` to [dismiss notifications](/read/01m02k97g130p60760ahj32qbz).
		- > buffers lazy comes with a bunch  of options too many actually
			- good point! too many options. not sure what it means to pick one and roll with it tho
		- > all of lazy V's default mappings can  be of course found in a nice table in the docs and   I suggest going through it at least once to see  what resonates with you and match your workflow
			- see https://www.lazyvim.org/keymaps or https://read.readwise.io/new/read/01m032vkewx64ct28jhms1fe47
		- > I want to stress out again how important it is to   go through the list of mappings where I found gems  like the mapping for creating a comment above or   below line using GCO or GC capital o or get this  leader ft to pop a terminal with a current working   directory just like you do with your typical ID
	- ## Links
		- Duplicate Reader save (same video): https://read.readwise.io/read/01kn8x3tgzg0073yrfny7qg2e0
		- [omerxx/dotfiles](https://github.com/omerxx/dotfiles)
