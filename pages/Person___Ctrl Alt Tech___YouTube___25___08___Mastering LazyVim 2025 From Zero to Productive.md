created-by:: [[Person/Ctrl Alt Tech]]
date-created:: [[2025/08/18]]
readwise-link:: https://read.readwise.io/read/01m1wbvmfekmhsf78faa576t29

- # [Mastering LazyVim 2025: From Zero to Productive - YouTube](https://www.youtube.com/watch?v=B2Og3oDEp4s)
	- Speaker: [[Person/Ctrl Alt Tech]] (creator goes by **Kiran**; channel [@CtrlAltTechWithKiran](https://www.youtube.com/@CtrlAltTechWithKiran))
	- Channel: [Ctrl Alt Tech](https://www.youtube.com/@CtrlAltTechWithKiran) · ~18 mins · published [[2025/08/18]]
	- Topic: [[LazyVim]] 2025 tour — init/lazy.lua, statusline breadcrumbs, windows vs buffers, which-key vs Neovim defaults (Backspace), [[nvim/Plugin/hardtime.nvim]]
	- ## Video
		- {{video https://www.youtube.com/watch?v=B2Og3oDEp4s}}
	- ## Summary
		- Orientation for a productive LazyVim setup: leave `lazy.lua` alone, read the statusline breadcrumbs, use which-key (`Space`) and Backspace for stock Neovim maps, and install [[nvim/Plugin/hardtime.nvim]] to break bad motion habits.
	- ## Highlights
		- > Init Lua is your
		  
		  initialization script which initializes your lazy vim configuration onto the neoim installation. If you go to Lua config lazylua, all your lazy whims configurations are actually set up inside of this file. Try not to edit this file as much. It leads to it leads to different complications. You can always restore it, yes, but generally not recommended.
		- > Moving forward, we have our breadcrumbs after the mode. You can see the folder name is NVIM and the path of my current file. On the right hand side, I can see a normal clock, the cursor where the cursor is located, the line number and the column number, where am I in the in the document. For example, if I do 10J, it'll tell me that I am 64% through the file. Then I have three objects in my current file. And 10J is the command that I have given
			- I hadn’t referred to this as breadcrumbs before. I found this overview of the significance of the items in the bottom bar to be useful.
		- > actions. I can do check out symbols that are present on the screen. I fixed everything. I can also see all the lsb references, definitions and so on. Space W shows you all the different things you can do with the window. Now windows are different from buffers in that a window can contain multiple buffers. That's how Neov does it for you. So if I press spacew WQ, it'll close that entire window. There are multiple different default commands that you can do. So one handy technique that
		- > I use to find out which keys should I use for what is I press space which shows me the key maps for lazy vim. However, if I press backspace, it gives me all the commands for default neoim installations as well. Right? So if you see you do Ctrl D to scroll down, scroll down and it'll show you all the different kind of things that you can do everywhere. If
			- tags:: [[Tip/Great]]
		- > All right, you remember I told you there was this one
		  
		  plugin which would change how you code. That plug-in is called Hard Time. Hardtime.la or hardtime.nv is an insanely helpful plug-in. So the notifications that you were seeing when I do this or when I do this or when I do this or this that's hard time telling me hey you need to get better at neoam stop using either your keys
		  
		  your arrow keys or using too much of hj hjkl use shorter key sets instead that'll make your life easier. I can do this, this or this or this and neoim or hard time will keep telling me hey stop doing it. This is bad habit learn. So it forces you to learn and get better at neoim. Definitely install hard time. It will give you a hard time but at the same time it will ensure that your
			- tags:: [[Plugin]], [[Tip/Great]]
