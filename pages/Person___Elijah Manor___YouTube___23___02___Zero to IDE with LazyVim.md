created-by:: [[Person/Elijah Manor]]
date-created:: [[2023/02/01]]
readwise-link:: https://read.readwise.io/read/01m1wbtjz5d24ekb5xxc44d701

- # [Zero to IDE with LazyVim - YouTube](https://www.youtube.com/watch?v=N93cTbtLCIM)
	- Speaker: [[Person/Elijah Manor]]
	- Channel: [Elijah Manor](https://www.youtube.com/@elijahmanor) · ~17 mins · published [[2023/02/01]]
	- Topic: [[LazyVim]] setup, extras (TypeScript/JSON), Mason, leap.nvim, Telescope, Trouble, code actions, customization
	- ## Video
		- {{video https://www.youtube.com/watch?v=N93cTbtLCIM}}
	- ## Summary
		- Walkthrough from starter config to IDE-like workflow: which-key, Neo-tree, Mason + LazyVim language extras, leap/mini.animate navigation, LSP hover and grep, Trouble diagnostics, Spectre replace, Lazygit, and extending plugins (themes, Telescope file browser, alpha dashboard).
	- ## Highlights
		- > You'll notice that several plugins and language servers aren't installed until they're needed, which is great for initial performance.
		  
		  Let's open up Mason, which is a way to manage language servers, linters, formatters, and more with leader cm.
		  
		  So the installed language servers do not include TypeScript, which is something that I regularly use. I could install it using Mason, but there are other settings I would need to manually set up.
		  
		  Thankfully, however, LazyVim has a few modules already coded that include the TypeScript settings already wired up for us.
		  
		  So, let's uncomment lines 14 through 16 to include TypeScript and JSON support, along with the mini animate plugin, which I'll show you what that does later, and we'll save our changes and quit Neovim.
		- > LazyVim comes pre-configured with the leap.nvim plugin to allow you to easily jump to any location, which is what I'm using here to jump directly to the first Styles reference. You might have noticed the cursor animating to the location; well, that was the mini.animate plugin that we enabled earlier.
		- > If you press a capital K, it'll show hover documentation, showing type information.
		  
		  Let's search for a string across our project. We'll hit leader and then s for search, and G for grep, from our root directory, and we'll search for John. Before, I'm a bit zoomed in here, so let's zoom out for a more realistic view. Here on the right, you can see a preview of the search results for the match.
		- > Here, we could use the trouble plugin by pressing leader XX to view Diagnostics, then you could jump directly to the issue, and we'll close that panel. And then we can launch some code actions via the TypeScript LSP by pressing leader CA.
		- > Once you have more than one buffer open, you could toggle between them by pressing leader FB. And Telescope will open with existing buffers, and we'll pick page TSX. You could also use the right bracket B to go to the next buffer and the left bracket.
			- Find buffer
		- > Okay, now let's switch to splits. You could create a vertical split by pressing leader pipe, and create a horizontal split by pressing leader dash. And then you can navigate to the left split with Ctrl H, to the right split with Ctrl L, down a split with Ctrl J, and up a split with Ctrl K. And you can adjust the size of the split with Ctrl Up, Ctrl Down, Control Right, and Control Left.
		- > ou can bring up a huge list of help pages to search by pressing leader sh.
		  
		  Let's search for to do and see its help page. This help page is about the H2 plugin that LazyVim has installed. Let's exit this.
		  
		  Help page and take a look above our home function. Let's add a to-do comment saying do this or that. Already, you can see visually that the to-do comment looks special.
		  
		  Let's switch to the next buffer before pressing leader St to search for to do's, and you'll see the to-do from the other file. If we press enter, it'll switch us back over to that buffer to the correct line.
			- This is the first time I’m hearing about the to-do plug-in ￼
		- > Another piece of functionality that you would probably expect from an IDE is auto-completion. Well, LazyVim wires that all up for you as well. If we start typing 'func', you'll see a list of auto-completions, and one of them is a snippet. So, we'll Ctrl n down to that option and hit enter.
		  
		  Then, we could fill in the stops along the way.
		- > Sometimes, you know, there's a key map that you want, and which key may just not be cutting it.
		  
		  In that case, you could press leader SK to search key maps. Here, we'll type lazy, and you can see that there's a key map for leader L to launch lazy.
			- Wow great tip
			- tags:: [[Tip/Great]]
		- > Here, we're going to leverage the Specter plugin by pressing leader Sr to search and replace. Here, we'll replace description with the term summary, which has 17 matches.
		  
		  And will limit the path to files that end with TSX or CSS, which reduces our matches down to 11. We could view additional help in Specker by typing the question mark.
			- tags:: [[Tip/Great]]
		- > Able to quickly spin up a temporary terminal by pressing leader ft from your root directory. Here, I'll just run npm run which will show a list of available npm scripts that I can run, and I'll just exit when I'm done.
		- > We'll open up neotree and navigate to the Lua config folder and open the options.lua file. This is where you could add your own custom options for Neovim. You can always reference the documentation on what options LazyVim already provides. In our case, let's set the winbar for Neovim, which is content that is displayed at the top of every window, where equals represents a separation point for alignment. M is a modifier flag of the buffer, and F is the path to the file in the buffer. So, let's save our file and source it. And now, you can see the winbar in the upper right of the buffer. This might not be super helpful right now, but if you have multiple splits, it could come in more handy. Speaking of splits, let's make a vertical split and open the keymaps.lua file. Here, we'll add a new keymap for normal mode, and we'll use the leader.sx keymap.
		  
		  That will resume the last telescope picker that happened to be open previously, and we'll make this not recursive and silent.
		  
		  Okay, we'll save this, which will be auto formatted. Now, let's sort this file and test it. If we press leader to kick in, which key we can see s to Surge.
			- I don’t quite understand why the auto formatting happens here. Also I don’t understand what we’re mapping leader SX to …￼
		- > Okay, next let's change this dashboard, lazyvim, with something a little more custom. For this, we'll create a new file in the Plugins folder called alpha.lua, and here I'll paste in a bit of code so in line two we're referencing the existing plugin that lazyvim is already using.
		  
		  The Ops function allows us to take the existing options that were defined elsewhere and to tweak them for our purposes. So, I'm taking the section header value from the options and setting it to a banner that says Neovim with my Twitter handle underneath.
		  
		  So, we'll save this file, quit Neovim, and relaunch. And hey, a customized dashboard.
			- I love the way that this person is giving a tutorial of Neo of them and lace him from the perspective of actually understanding how to customize it rather than just how to use it
			- tags:: [[Tip/Great]]
		- > For this, we'll add yet another file to the plugins folder called disable.lua. In this file, let's return a Lua table.
		  
		  With an entry that disables the Specter plugin, maybe you don't like this plugin, and you'd rather use telescope Quick Fix lists and CDO updates instead.
		  
		  So, let's save this file, quit Neovim, and relaunch.
