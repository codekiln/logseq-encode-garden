readwise-link:: https://read.readwise.io/read/01m2f7bejyfk00p4w92re2syz1
prev:: [[LV4AD/Ch/05 Plugin Basics]]
next:: [[LV4AD/Ch/07 Objects and Operator-pending Mode]]

- # [Chapter 6: Basic Editing - LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/)
	- ## [6.1. The Vim Command Mental Model](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_the_vim_command_mental_model) [[Modal/Editing]]
		- > The navigation commands such as `s` and `f` and `hjkl` and `web` that you already know are collectively known as *motion* commands. They move the cursor from its current location to a new location.
		- > Verbs come first, so the structure is always `<verb><count><motion>`. Navigation is the “default” verb, so if you leave the verb blank (i.e. skip it), your cursor moves to the location indicated by the motion. We’ll discuss various important verbs in this chapter.
		  > 
		  > But the model keeps growing! It turns out, verbs can *also* be counted. The syntax becomes `<count><verb><count><motion>`. I have never in my life used all four of those in one command, however. Typically you would either do `<count><verb><motion>` **or** `<verb><count><motion>`.
		- #### [6.1.1. A Note on Insert Mode](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_a_note_on_insert_mode)
			- > Like all models, this one is not perfect. For example, you can use counts with the `i`, `I`, `a`, and `A` commands, but it’s clear that “enter Insert mode” is neither a motion nor a verb.
			  > 
			  > For example, if you type `5ifoo<Escape>`, [[nvim]] will insert `foofoofoofoofoo` for you. That may not seem very useful, but if you ever want an 80 character `*` ruler to underline a heading, `80i*<Escape>` is pretty nifty!
			- > But the `<count>i` “not-motion” commands *cannot* be combined with verbs like the navigation commands you’ve learned. So it’s important to know the limits of the model. In fact, as we’ll see later, [[vim]] uses this effect to its advantage, borrowing the `a`, `i`, and `o` keys to create object motions when combined with a verb.
			- > So now that you understand how the motions you already know can combine with verbs to perform actions other than navigation, you just need to learn some verbs.
				- [[My Note]] *In the Vim mental model, verbs are the actions you perform on the text between your current cursor position and where a motion would take you. You are currently at 20.27% of the document, which is exactly where the text begins to explain these verbs that can be combined with navigation motions.*
					- *Here are the primary examples of verbs mentioned in this chapter:*
					- *Delete (d): This verb deletes text from your cursor to the motion destination. For example, d3w deletes three words. You can also use dd as shorthand to delete an entire line.*
					- *Change (c): This functions exactly like delete, but it automatically enters Insert mode once the text is gone, saving you a keystroke when you need to replace code.*
					- *Delete Single Character (x): A shorthand verb that deletes the character under the cursor without requiring a separate motion command.*
					- *Replace Character (r): This allows you to replace a single character by typing r followed by the new character; it briefly enters Insert mode for you and then snaps back to Normal mode.*
					- *Join Lines (J): A verb used to delete the newline at the end of the current line, effectively merging it with the line below.*
					- *Case Conversion (gU and gu): These are used to convert text to uppercase or lowercase based on the motion that follows.*
					- *The power of this model is that if you leave the verb blank, Neovim assumes you just want to move the cursor, which is why your standard navigation keys work the way they do.*
	- ## [6.2. Deleting Text](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_deleting_text)
		- > I’ve previewed this a couple times already, and even if I hadn’t, you can probably guess that the verb for deleting text is `d`.
		  > 
		  > So where `<motion>` will take you to a specific location in the code, `d<motion>` will delete all the text between the cursor and that location. Here are some examples:
		  > 
		  > •   `dh` to delete the character to the left of the cursor.
		  >     
		  > •   `d3w` to delete three words.
		  >     
		  > •   `3dw` to delete one word, three separate times.
		  >     
		  > •   `d^` to delete from the cursor to the beginning of the line.
		  >     
		  > •   `d2fe` to delete all text between the cursor location and the second `e` after the cursor, including that second `e`.
		  >     
		  > •   `d2Ta` to delete all text between the cursor and the second `a` *behind* the cursor, *not* including that second `a`.
		  >     
		  > •   `dsfoos` to delete text between the current cursor position and the label `s` that pops up when you use [[nvim/Plugin/flash.nvim]] Seek mode to seek to `foo`. Note that Seek mode **always** jumps to the beginning of the word you searched for. This means that if the `foo` you jump to is *after* the current cursor location, the `oo` will not be deleted, but the `f` will. But if the `foo` you jump to is *before* the current cursor location, all three letters of `foo` will be deleted.
	- ## [6.3. Changing Text](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_changing_text)
		- > This *could* easily be handled by combining the delete verb with Insert mode (e.g. `dwi` will delete a word and enter Insert mode.) However, you can save a keystroke by using the `c` verb, which means “**c**hange”. If you replace the `d` in each of the examples I outlined above with a `c`, you will effectively get “delete the text and immediately enter Insert mode.”
	- ## [6.4. Operating to End of the Current Line](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_operating_to_end_of_the_current_line)
		- > Yes you *could* `d$` and `c$` to delete or change to the end of the line, since `$` is the “jump to end of line” motion. That is the “correct” format for the mental model. However, because this is such a common operation, you can “cheat” with one fewer keystrokes and just use the capitalized `D` or `C` instead.
		  > 
		  > There is no inverse shortcut verb for “delete to the beginning of the line”, so you’ll have to use `d^` or `d0` instead, where `^` is the motion to jump to the first non-blank character and `0` is the motion to jump to the first column regardless of whether it is blank.
	- ## [6.5. Operating on Entire Lines](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_operating_on_entire_lines)
		- > In practice, this just means that `dd` deletes an entire line and `cc` deletes it and enters Insert mode. These are nice and easy to type, so it makes for a nice shorthand.
		- > You can combine these bespoke motions with counts. `d3d` will delete three lines, and `3dd` will delete one line three times (which is faster to type because you don’t have to move your finger off of `d` to hit it twice). Yes, that has the same outcome either way, but the model is such that you can use either of them. Note that there are situations where the two formats may have subtly different behaviours, although in practice I have never encountered surprises.
	- ## [6.6. Some Shortcuts for Modifying Individual Characters](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_some_shortcuts_for_modifying_individual_characters)
		- > The `x` command can be used with a count, so if you want to delete five characters starting with the one under the cursor, just use `5x`.
		- > If you need to go the other direction and delete characters *before* the cursor, use a capital `X`. This, too, can have a count, and it will basically delete that many characters to the left. I rarely use this, since the shift brings us up to two keystrokes anyway, and `hx` or `d4h` is no harder.
		- > One shortcut I do use frequently can delete the newline at the end of the current line. Use the `J` (“**J**oin Lines”) command from anywhere in the line. I use this one a lot. If you need to merge multiple consecutive lines together, `J` takes a count. It generally does the right thing around whitespace (replacing indentation with a single space), but if you need to do a join without modifying whitespace, use the two-character verb `gJ`.
	- ## [6.7. Manipulating Case](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_manipulating_case)
		- > If you need to convert a character or sequence of characters to uppercase, use the verb `gU` (that’s a shifted `U` for the second character) followed by any standard navigation motion. I find this particular verb frustrating because `g` is normally assigned to the `Go To` motions. In this case, (as with `gJ` above) it is a verb instead.
		  > 
		  > I guess you can think of it as “Go To and Convert to Uppercase” where `U` is short for `Uppercase`.
		  > 
		  > The inverse function to convert all text between the current cursor position and the motion destination is to use a lowercase `gu` before the motion. Kind of weird to remember, but it does match the common [[vim]] idiom of `gu` means an action and `gU` means the same action BUT BIGGER.
		- > I don’t find these commands very useful. I more frequently use the `~` command, which inverts the case of the character under the cursor.
		- > The duplicate commands `gUU` and `guu` do the same thing as other duplicate verbs, applying the upper/lower case operation to the entire line.
	- ## [6.8. Repeating Commands](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_repeating_commands)
		- > [[LazyVim]] doesn’t have a multiple cursor mode. There *are* plugins to support multiple cursors, but in my experience they don’t work very well. The [[nvim]] developers have multiple cursors on their roadmap, so I am hoping they will come up with a paradigm that integrates nicely with the [[vim]] mental model.
		- > Once you have performed any verb, you can navigate to another place in the document and repeat that verb with a single keypress: `.` (That’s a period, although you will usually hear it referred to as “dot repeat” in this context).
		- > This highlights why `d` and `c` need to be separate verbs, as opposed to using something like `d<motion>i`. When you use `c`, the delete motion **and** the text you inserted is remembered, so you can repeat the entire change with a `.` command. For example, if you want to replace all instances of a variable named `i` with a much better name of `index`, you could jump to the first instance of `i` and type `clindex<Escape>` to “change one character to index”. Then you can use navigation commands to go to the next use of `i`. Now just type `.` to repeat the change. Then continue to the next instance.
		- > Like motions and verbs, the `.` command can be given a count. However, counts with `.` are a little bit nuanced. Rather than blindly repeating the command `<count>` number of times, it will instead *replace* the count of the command being repeated.
		  > 
		  > This means that if you use the verb `3dd` to delete three lines, and the next operation you perform is `2.` (“2 dot”), the second operation will delete *two* lines, rather than six.
	- ## [6.9. Recording Commands](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_recording_commands)
		- > To start a recording, press `qq`. Sorry, but I have no mnemonic to remember `q`. I have a feeling it was just the last available key on the keyboard!
		  > 
		  > After that, type whatever sequence of navigation, editing, and insertion commands you want to record. Delete words, insert text, change text, search for words (don’t use [[nvim/Plugin/flash.nvim]] Seek mode, as the replay mechanism will have no idea what label to jump to). Virtually anything you can do in [[vim]] (even `:` commands) can be recorded and replayed later.
		  > 
		  > When you are finished recording, just press `q` again. The recording will be stored ready for replay whenever you desire.
		- #### [6.9.1. Appending to a Recording](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_appending_to_a_recording)
			- > If you partially complete your recording and then realize you need some more information or need to make an edit before completing the recording, you can pause the recording using `q` as usual and do the thing you need to do.
			  > 
			  > When you are ready to continue recording, use `qQ` to record in *append* mode instead. The main tip here is that you need to make sure your cursor is in a location such that the merged recording will make sense. This usually means the same place it was when you stopped recording, although it may depend on what changes you made in the meantime.
	- ## [6.10. Undo and Redo](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-6/#_undo_and_redo)
		- > Obviously, these are the most important operations in the whole book! Use the `u` key to undo your most recent change. Note that “most recent change” can be a pretty big whack of text, especially if you haven’t exited Insert mode for a while. For example, I wrote this entire paragraph in one Insert session. If I press `u` the entire paragraph will be lost.
		- > That’s ok, though, because I can redo using [[Key/Control]]-r. Like most developers, I use both of these extensively. (Did you know that in the old days of typewriters, secretaries had to get 100% accuracy scores on their typing tests? There was no backspace or delete key, you see).
		- > It’s kind of the same concept as [[git]] branches, except your history is *automatically* tracked for every keystroke you make. Working with branches of undo history using raw [[nvim]] commands can feel pretty clumsy, though (read through `:help undo-branches` if you’re brave). Instead I recommend configuring and installing the [[nvim/Plugin/undotree]] plugin.
