see-also:: [[My/Pref/Writing/Use Plain language]]

- Write one line per paragraph in a Markdown file and let the viewer wrap it. Hard-wrapping the source at a fixed column makes a page **harder** to read rather than tidier, because the viewer wraps the already-wrapped lines again and the result is ragged: a full-width line followed by a short remainder, repeating down the page.
- The tools that read these files wrap on their own. [[Obsidian]] does, and so does [[nvim/Distro/LazyVim]] — see [[vim/Q/How can I configure (neo-)vim so that by default it wraps in a way that takes word boundaries into account, rather than splitting words in the middle?]] for the option that makes the wrap break on words rather than mid-word.
- A hard wrap also makes a diff lie about what changed. Editing one word in the middle of a paragraph re-flows every line after it, so the change arrives as a rewritten paragraph and review has to find the edit inside it.
- This is a rule about the source, not about sentence length. [[My/Pref/Writing/Use the simpler word]] and the rest of this namespace still govern what the line says.
