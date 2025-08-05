tags:: [[Security]], [[Secrets]], [[CLI]], [[Article]]

- # [How to Handle Secrets on the Command Line](https://smallstep.com/blog/command-line-secrets/)
	- ### [[tldr]] #Summary
	  id:: 67cdafc5-8105-48cc-a41b-adb7d83f5c10
		- TL;DR: Best practices for #CLI secrets: (1) Use credential files with proper permissions and disk encryption; (2) Use pipes to pass secrets directly between programs; (3) Avoid [[EnvVars]] environment variables when possible; (4) **Never pass secrets directly in command arguments**; (5) Consider using a keyring facility like [[Linux/keyring]] for in-memory storage; (6) For specific tools, use their built-in credential storage (like [[dotfile/.netrc]] for [[curl]]).
	- The command line really wasn't designed for secrets. So, keeping secrets secret on the command line requires some extra care and effort.
	- All of these values, including the precious contents of the private key file, can be seen via `ps` when these commands are running. [[ps]] finds them via `/proc/<pid>/cmdline`, which is globally readable for any process ID.
	- ### Credentials Files
		- What's not to love about a file? It's got an owner. It has permissions and access control.
		- Give each secret a file! Any program that accepts secrets should be able to accept them by passing a filename or by redirecting a file into `STDIN`. You can also use files to pass secrets into Docker containers with mounted volumes.
		- Be sure your disk is encrypted at rest, eg. with LUKS
		- Using environment variables for secrets is very convenient. And we don't recommend it because it's so easy to leak things
		- Some operating systems still make every process's environment variables world readable.
		- In Docker, anyone with access to the [[Docker]] daemon can use `docker inspect` to see all of the environment variables for any running container.
		- Variables can easily end up in shell history. In many shells, adding an extra space before a command will exclude it from shell history.
	- ### What About A Secrets Manager?
		- Speaking of lightweight solutions, there is an keyring facility in the Linux kernel
		- The [[Linux/keyring]] offers several scopes for storing keys safely in memory that will never be swapped to disk. A process or even a single thread can have its own keyring, or you can have a keyring that is inherited across all processes in a user's session. To manage the keyrings and keys, use the [`keyctl`](https://man7.org/linux/man-pages/man1/keyctl.1.html) command or [`keyctl`](https://man7.org/linux/man-pages/man2/keyctl.2.html) system calls.
	- ### Directly in the command
		- In case it isn't already abundantly clear, this is very unsafe. There is no way for the caller of a command to choose to hide the command line from being world readable.
		- any CLI command worth its salt should not accept passwords directly.
		- The alternative for [[curl]] is a credential file: A [`.netrc` file](https://everything.curl.dev/usingcurl/netrc) can be used to store credentials for servers you need to connect to.
	- ### Author
		- [[Person/Carl Tashian]]
			- [Website](https://tashian.com)
			- [LinkedIn](https://www.linkedin.com/in/tashian/)
			- is an engineer, writer, exec coach, and startup all-rounder. He's currently an Offroad Engineer at Smallstep. He co-founded and built the engineering team at Trove, and he wrote the code that opens your Zipcar. He lives in San Francisco with his wife Siobhan and he loves to play the modular synthesizer 🎛️🎚️
- ## [[see-also]]
	- [[EnvVar/Article/22/08/Analyzing the Hidden Danger of Environment Variables for Keeping Secrets]]