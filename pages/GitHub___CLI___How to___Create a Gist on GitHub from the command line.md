- [[GitHub/CLI/gh/gist/create]] docs
	- ```
	  # Create a gist from a file
	  gh gist create [<filename>...] [flags]
	  
	  # Common flags:
	  -d, --desc <string>    # Add a description
	  -p, --public          # Make the gist public (default is secret)
	  -f, --filename        # Specify filename when reading from stdin
	  -w, --web            # Open in browser after creation
	  ```
	- # Create a public gist from a file
		- `gh gist create --public hello.py`
		- By default, **gists are created as secret (private)**. Use the `--public` flag to make them publicly visible.
	- # Create a gist with a description
		- `gh gist create hello.py -d "my Hello-World program in Python"`
	- # Create a gist with multiple files
		- `gh gist create hello.py world.py cool.txt`
	- # Create a gist from standard input
		- `gh gist create -`
	- # Create a gist from piped input
		- `cat cool.txt | gh gist create`