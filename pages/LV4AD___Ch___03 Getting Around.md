readwise-link:: https://read.readwise.io/read/01m2634dr388xhbqrc9jktg3a0
prev:: [[LV4AD/Ch/02 Modal Editing]]
next:: [[LV4AD/Ch/04 Opening Files]]

- # [Chapter 3: Getting Around - LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/)
	- ## [3.1. Seeking Text](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_seeking_text)
		- > [[LazyVim]] ships with a plugin called [[nvim/Plugin/flash.nvim]], which was created by the [[Person/Folke Lemaitre]] and integrates very nicely with it.
		  >
		  > This plugin provides a code navigation mode that has been available in various [[vim]] plugins for many years, and has historically been quite controversial. A lot of long-time [[vim]] users think it breaks the [[vim]] paradigm. I won't go into the details as to why, but I will acknowledge that this was true in older iterations of the paradigm but is somewhat less true in modern versions such as [[nvim/Plugin/flash.nvim]].
		- > To invoke `flash`, press the `s` key in Normal mode. My mnemonic for `s` for "**s**eek", although I've also heard it referred to as "sneak" or "search" mode. Searching in [[LazyVim]] is a different behaviour (it doesn't care if the text is currently visible or not), and "sneaking" sounds a little too dishonest, so I use "Seek".
		  >
		  > The first thing to notice when you press `s` is that the text fades to a uniform colour and there's a little lightning symbol in the status bar indicating that Flash mode is active:
		  >
		  > ![seek active dark](https://lazyvim-ambitious-devs.phillips.codes/images/book/chapter-3/seek-active-dark.png)
		  >
		  > Figure 11. Flash Mode Active
		- > If you have multiple files open in split windows (which we'll discuss in Chapter 9), Seek mode can be used to move your cursor *anywhere* on the screen, not just in the currently active split.
		- > Now, all instances of `st` in the file are highlighted in blue, and since there aren't as many `st` as `s`, all of those instances have a label beside them. The text I want to move to is labelled with a `p`, so I press `p` and my cursor is moved to the `s` character I wanted to change
			- [[My Note]] *ok, so you enter contiguous characters, then the item highlighted in green and inserted after is the jump key*
		- > For me this happens most often when I want to edit the end of a line. If I type `sn` because I want to edit a line that has `n` as the last character, but there are a bunch of `n` characters closer to my cursor than the one I want to move to, flash may not label the `n` I want to move to, and it won't accept a carriage return as a "next character" input.
		  >
		  > For this reason, I don't seek near ends of lines. Instead, I'll seek to a word somewhere in the middle of the same line and then use `A` which, as you may recall, will put me in Insert mode at the end of the line. Alternatively, if I don't want to enter Insert mode, I will use the `$` symbol (`Shift+4`), which is the Normal mode command for "Move cursor to end of current line".
		- > [[LazyVim]] ships with a plugin called [[nvim/Plugin/flash.nvim]], which was created by the [[Person/Folke Lemaitre]] and integrates very nicely with it.
		- > To invoke `flash`, press the `s` key in Normal mode. My mnemonic for `s` for "**s**eek", although I've also heard it referred to as "sneak" or "search" mode. Searching in [[LazyVim]] is a different behaviour (it doesn't care if the text is currently visible or not), and "sneaking" sounds a little too dishonest, so I use "Seek".
	- ## [3.2. Scrolling the Screen](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_scrolling_the_screen)
		- > The scrolling keys I use the most are definitely `Control-d` and `Control-u`, where the mnemonics are **d**own and **u**p. They scroll the window by half a screen's worth of text. The cursor stays in the same spot relative to the **window**, which means that it is moved up or down by half a screen's worth of text relative to the **document**.
		- > If you need to move even further, you can use the `Control-f` and `Control-b` keybindings (**f**orward and **b**ackward), which scroll by a full page of text. I don't like these ones because I never quite know where the cursor is going to end up and I become disoriented. But it can be handy if you need to scroll something into view quickly to use Seek mode on it. Unlike `Control-d` and `Control-u`, `Control-f` and `Control-b` can be prefixed with a count, so you can type `5<Control-f>` if you need to scroll ahead by `5` pages.
		- > To scroll the window by a single line, use `Control-y` and `Control-e`. I have no idea why these keybindings were chosen. There is no mnemonic. I easily forget them, and so I never use them. These keybindings accept a count, so if you can remember them, they are useful for subtle repositioning of the text. The main advantage of these keybindings is that they don't move the cursor unless it would scroll off the screen, so if you are working on a line and need more visibility but don't want to move the cursor, you could use `Control-y` and `Control-e` to do it.
		- #### [3.2.1. Z Mode](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_z_mode)
			- > The `z` menu mode is an eclectic mix of cursor positioning, code folding, and random commands. You can see a list by pressing the `z` key while in Normal mode:
			  >
			  > ![](https://lazyvim-ambitious-devs.phillips.codes/images/book/chapter-3/z-menu-dark.png)
			  >
			  > z menu dark
				- [[My Note]] *I wish things a way to pin the favorites to the top of the menu*
			- > The relative cursor keybindings I use exclusively are `zt`, `zb`, and `zz`. These move the line that the cursor is currently on to the **t**op, **b**ottom, or middle of the screen, respectively, where middle is represented by the easy-to-type double letter. When moving to the top or bottom it will leave a few lines of context above or below the cursor.
			- > You can find other scrolling keybindings in the [[nvim]] documentation by typing `:help scrolling`, but the ones I just mentioned will probably more than cover your needs as you learn far more nuanced methods of navigating code.
	- ## [3.4. Counting](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_counting)
		- > So, for example, to move the cursor up 15 lines, you would enter Normal mode and hit the keys `15k`. To move it five characters to the right, use `5l`.
		- > Open the file `~/.config/nvim/lua/config/options.lua`, which should have been created for you by [[LazyVim]] but currently won't have anything in it other than a comment describing what it is for.
		  >
		  > You can use the Space mode command `<Space>fc` to quickly find files in the [[LazyVim]] configuration directory. This will pop up one of the file pickers that we'll discuss in detail in the next chapter. Type `options` and press `<Enter>` to open the
		- > Personally, I find line numbers to not be very useful and I don't like wasting valuable screen width on displaying those characters.
	- ## [3.5. Find Mode](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_find_mode)
		- > To enter Find mode, press the `f` key. Like Seek mode, a portion of your screen will dim, indicating that you should type another character. After you do so, all instances of that character *after the cursor* will be highlighted. For example, `fs` will highlight all instances of the letter `s` after the current cursor position.
		- > If you miscounted or misguessed and jump too far, don't worry! You can take advantage of the fact that (Shifted) `F` means "find backwards", and can also be counted. So if you need to move to the 15th highlighted `s`, it's totally fine to guess `18f`, realize you've gone three too far, and use `3F` to jump back to the previous character.
		- > Instead, we need to use counts to jump to later instances of the character. If I want to jump ahead to the third highlighted `s`, I type `3f` and my cursor will move there. However, if you want to jump to a much later `s`, you probably don't want to individually count how many `s` keys there are. Luckily, after you use a count, [[LazyVim]] leaves you in Find mode, so you can just guess how many `s` characters there are, and then once you are closer, repeat with a new count. If you only want to jump ahead by one `s` character, you don't need to enter a count, just press `f` by itself and you'll move ahead.
		- > You might think that To mode is kind of redundant because you could fairly easily use Find mode followed by a single `h` to move the cursor left. But "To" mode is extremely useful when you are combining it with operations to edit the text, which we will discuss later. As a taste, if you use the command `d2ts`, it will delete all text between the cursor and the second `s` it encounters, but leave that `s` alone. This is much easier than the `d2fsis<Escape>` that would be required if you used a find command and then had to enter Insert mode to add the `s` back.
	- ## [3.6. Moving by Words](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_moving_by_words)
		- > Instead, you can just enter Normal mode and press the `w` key to move to the beginning of the next word. If you instead want to move to the *end* of the current word, use the `e` key. If you are *already* at the end of the current word, `e` will go to the end of the *next* word.
		- > Use the `b` key if you want to move backwards instead. This will move you to the beginning of the current word, or if you are already at the beginning of the word, it will move to the beginning of the previous word. As before, use a count to move to the beginning of even more words.
		- > Surprisingly, it takes a bit more work to move to the end of the *previous* word, as you need to press two keys: `g` followed by `e`. The mnemonic for this is "**g**o to **e**nd of previous word". In practice, you'll find that you hardly ever need this functionality for some reason, and the honest truth is I usually use `be` (`b` to move to beginning of previous word, then `e` to go to end of that word) to move to the end of the previous word. If you do use `ge`, however, it can be combined with a count as well. You'll need to type something like `4ge`, depending on the count. The command `g4e` wouldn't do anything useful.
		- > Collectively, you may occasionally hear the `w`, `e`, and `b` commands referred as the "web" words. It just means "moving by words". These are probably the most common movements you will use, more than individual cursor positions, simply because most editing actions tend to involve changing or deleting a word or sequence of words.
	- ## [3.7. Moving by Words, Only BIGGER](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_moving_by_words_only_bigger)
		- > The "shifted" form of the `web` words also move by words, but the definition of "word" is subtly different. Specifically, a capital `W` will move to just after the next whitespace character, where a lowercase `w` will use other forms of punctuation to delimit a word. Consider a method call on an object that looks something like this in many languages:
		- > As a visualization, here are all the stops on that line of code when you use `w` compared to when you use `W`:
		- > Listing 10. Behaviour of `w` and `W`
			- ```
			  myObj.methodName('foo', 'bar', 'baz')
			  -----ww---------w-w--w--ww--w--ww--w---->
			  ------------------------W------W-------->
			  ```
		- > The `B`, `E`, and `gE` motions behave similarly, moving in the appropriate direction by whitespace-delimited words instead of punctuation ones.
		- > One thing that is kind of annoying both in [[vim]] and the way [[LazyVim]] is configured is that there's no way to navigate between the individual words of `CamelCaseWords` or `snake_case_words`. You can use `fC` or `t_` and similar if you want to, but I will later show you how to set up the [[nvim/Plugin/nvim-spider]] plugin that makes navigating these common programming constructs simpler.
	- ## [3.8. Line Targets](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_line_targets)
		- > If you are familiar with regular expressions, you might know that `^` is used to match the start of text or start of the line and that `$` is used to match the end, so the mnemonic of using these two keybindings to match the beginning and end of the current line will hopefully be less unmemorable than they seem at first.
		  >
		  > There is a certain lack of symmetry between the two, however. The `$` (`Shift-4`) command simply means "go to the end of the line", as in the last character before the ending newline, no matter what that character is. The `^` or caret (`Shift-6`) means "go to the beginning of the text on this line". The "of the text" there is important: if your line has whitespace at the beginning (e.g. indentation), the `^` caret will **not** go to the very first column, but will instead go to the first non-whitespace character.
		  >
		  > To move to the very beginning of the line, use the `0` key.
		- > The two character combination `g_` (g underscore) means "go to the last non-blank character". I guess `_` kind of looks like "not a space", so it's kind of mnemonic? I include it to be comprehensive, but you'll likely not use it much. You also have the option of combining other commands you've learned so you don't have to memorize this one-off. For example, you can use the three character `$ge` (combining "end of line" with go backwards to end of word) or `$be` to move to the last non-blank on the line. You have options; pick the one that you find is easiest to remember or type!
	- ## [3.10. Jump History](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-3/#_jump_history)
		- > `[[Key/Control]]-o` is the non-modal control-based keybinding that I use most often. I should honestly bind it to something more accessible, I use it so much. It basically means "Go to the place I jumped from".
		- > If you jump too far, you can use the `Control-i` keybinding to jump *forward* in history. It's just the opposite of `Control-o`. I don't know why `i` and `o` were chosen for these; maybe because they are side-by-side on a Qwerty keyboard? They are used commonly enough that once you learn them, you won't forget.