readwise-link:: https://read.readwise.io/read/01m21kgh70j94h35vnjppfg9x9

- # [Chapter 2: What is Modal Editing, Anyway? - LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-2/)
	- ## [2.1. Introduction to Modal Editing](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-2/#_introduction_to_modal_editing) [[Modal/Editing]]
		- > This discoverability of keybindings in a given mode is a common theme in [[LazyVim]], and a huge improvement over the opaque default behaviour of [[nvim]] itself.
		- > You can access *some* keyboard shortcuts in Insert mode using [[Key/Control]] and [[Key/Alt]]. For example, you can hit `Control-r` to enter the “Registers” mini-mode, which pops up a list of “registers” you can paste from. We’ll cover registers in detail in Chapter 8. For now, it is enough to know that `Control-r` followed by the plus key (i.e. `Shift-=`) will paste text from the [[Clipboard]] when in Insert mode.
		- > [[vim]] and [[nvim]] aren’t very discoverable, but they ARE generally memorable. As often as possible, the keyboard shortcuts to perform an action start with a letter that makes sense for the action being performed. You might think `p` stands for “**p**aste”, but in fact the concept has been around for longer than the [[Clipboard]] abstraction. You are welcome to think of it as “paste” if that’s easier for you, but in [[vim]] parlance, it actually stands for “put”, and I’ll use that word throughout the book.
		- > For some contrast, the `Control-r` key that pops up the list of registers in Insert mode does **not** pop up a list of registers in Normal mode. Instead, `Control-r` means “redo” (i.e. undo an undo). In order to enter the Registers mini-mode from Normal mode, you would press the `"` (quote, as in `<Shift>-apostrophe`) key instead.
		- > Your operating system is probably also capable of remapping keys. A lot of modal users replace the useless `Capslock` with the `Escape` key. (For non-modal paradigms it can be more comfortable to remap `Capslock` to the commonly-held `Control` key, especially on laptop keyboards).
		- > Commonly, you want to enter Insert mode *after* the current cursor position. To do that, use the `a` key instead (mnemonic: i for **I**nsert Before, a for **A**ppend, although I usually think of it as **A**fter).
		- > Two other very common operations are to insert at the very beginning or the very end of the current line. You *could* use navigation commands to move to the start or end and then use `i` and `a`, but it’s easier to use the commands `I` and `A` instead (The difference is that they are capitalized, so you need the `Shift` key with them).
		- #### [2.1.1. A Note on Keybinding Mnemonics](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-2/#_a_note_on_keybinding_mnemonics)
			- > The `o` key is used to enter Insert mode on a new line *below* the current one. For the “do the opposite thing” scenario, the shifted `O` means “create a new line *above* the current one and enter Insert mode on it”.
			- > One final useful command that takes two keystrokes is `gi`. That is a single press and release of `g` followed by `i`. It means “Go to the last place you entered Insert mode, and enter Insert mode again”. In this case, the `g` key is actually switching to a new mini-mode I call “Go To” mode, though not all the commands accessible from it are strictly related to going places. You can see the entire list of commands available in “Go To” mode by pressing the `g` key in Normal mode and waiting for the menu to pop up at the bottom of the window:
			  >
			  > ![](https://lazyvim-ambitious-devs.phillips.codes/images/book/chapter-2/goto-mode-dark.png)
	- ## [2.3. Command Mode](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-2/#_command_mode)
		- > Command mode is kind of weird. It’s like an Insert mode in the sense that you can type text into it, and some of the keybindings that work in Insert mode also work in Command mode (including `Control-r` to paste from a register). But other keybindings work differently in Command mode. The most important one is the `Tab` key, which will do a sort of “tab completion” on the command. For example, `:q<Tab>` pops up a menu like this:
		  >
		  > This completion menu is disturbingly unintuitive to navigate. You’re probably going to want to bookmark this section or take some notes to refer to until you get used to it!
		- > You can type `:e f<tab>b<tab><tab><tab>` to select `foo/baz`, but at this point the menu is still open:
		  >
		  > ![edit baz dark](https://lazyvim-ambitious-devs.phillips.codes/images/book/chapter-2/edit-baz-dark.png)
		  >
		  > Figure 10. Edit Command with Completion Menu
		  >
		  > If you press `Enter` now, it’s going to open the `baz` *folder* instead of just confirming the selection, which is not what you want. And if you press `Tab` again it will cycle through the menu some more.
		  >
		  > Instead, you have a couple of options. The `Down` arrow key will (unintuitively) move “into” the selected directory, allowing you to tab through the files inside it. Alternatively, use the `Control-y` (`y` for “**y**es”) key combination. This will confirm the `baz` selection and close the menu but leave you in Command mode. Now you can press tab again to complete the `fizz.txt` portion of the command.
		- > For now, remember `<Tab>` and `Control-y` and you’ll be able to navigate the Command menu when you need to.