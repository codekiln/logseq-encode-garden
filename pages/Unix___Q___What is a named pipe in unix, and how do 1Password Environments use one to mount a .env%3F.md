logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Unix/Pipe]]

- # What is a named pipe in [[Unix]], and how do [[1Password/Environment]]s use one to mount a `.env`?
	- ## [[AI Answer]]
		- **Short answer:** a named pipe (a **FIFO**) is a [[Unix/Pipe]] that has a path in the filesystem. It stores nothing; bytes written into one end are handed straight to whoever is reading the other end. 1Password puts a FIFO at your `.env` path, so when a program opens that "file," the 1Password app writes the secrets into the pipe at that moment and nothing lands on disk.
		- ### Named pipe
			- An ordinary pipe (`a | b`) is an anonymous kernel buffer between two processes the shell started together. A named pipe is the same buffer given a name in a directory, so unrelated processes can find it by path.
			- Create one with `mkfifo path`. `ls -l` shows file type `p`, and the size is always 0, because the data only exists in the kernel buffer while it is in transit.
			- A reader that opens the FIFO blocks until a writer opens it too, and the reverse. Each byte is read once; after one reader consumes it, it is gone.
			- Demo from a Mac shell:
				- ~~~bash
				  mkfifo demo.fifo
				  ls -l demo.fifo          # prw-r--r--  ...  0  demo.fifo
				  printf 'API_KEY=abc\n' > demo.fifo &   # writer waits for a reader
				  cat demo.fifo            # API_KEY=abc
				  rm demo.fifo
				  ~~~
		- ### How 1Password uses it for a mounted `.env`
			- [[Answer/Official]] from [Local .env file — 1Password Developer](https://www.1password.dev/environments/local-env-file)
			- In the desktop app, open an Environment, choose **Connect → Local .env file**, pick a path, and select **Mount .env file**. 1Password creates a FIFO at that path.
			- 1Password is the writer. When a process opens the `.env` for reading, 1Password (if unlocked) writes the Environment's variables into the pipe; the docs say the contents are passed to the reader on demand "through a UNIX-named pipe" and are never stored on disk.
			- Readers need no changes: `dotenv`-style loaders just open and read a file. The docs list Node `dotenv`, `python-dotenv` 1.1.2+, Go, Java, C#, PHP, Ruby, Rust, and Docker Compose.
			- The FIFO properties explain the documented caveats:
				- **Locked means no data** — with 1Password locked, the path still exists but nothing is written, so a reader waits or fails until you unlock.
				- **One reader wins** — each write is consumed once, so if several processes open the file at the same moment, the first reads the secrets and the others may get nothing.
				- **Every process can read it** — while unlocked, 1Password does not tell readers apart. Any process running as you, an AI agent included, can `cat` the values.
				- **Watchers see churn** — opening and reading a FIFO emits filesystem events even when no value changed, so tools that watch `.env` (Vite is the named example) can restart in a loop.
				- **Git ignores it** — Git does not track FIFOs, so the mount stays out of version control. A tracked `.env` already at that path must be deleted and committed first.
			- Limits: Mac and Linux only (FIFOs are a Unix feature; Windows named pipes work differently), and up to ten enabled mounts per device.
			- [[1Password/Environment/MCP]] can create these mounts for an agent client while sending it only variable names.
