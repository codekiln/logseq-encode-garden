- `list-keys [-1aN] [-P prefix-string] [-T key-table] [key]`
                   (alias: lsk)
             List key bindings.  There are two forms: the default lists keys as bind-key
             commands; -N lists only keys with attached notes and shows only the key and
             note for each key.
	- With the default form, all key tables are listed by default.  -T lists only
	             keys in key-table.
	- With the -N form, only keys in the root and prefix key tables are listed by
	             default; -T also lists only keys in key-table.  -P specifies a prefix to print
	             before each key and -1 lists only the first matching key.  -a lists the
	             command for keys that do not have a note rather than skipping them.