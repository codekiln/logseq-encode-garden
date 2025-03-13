alias:: [[1Password/Dev/Doc/SSH Agent Config File]]

- # [SSH agent config file | 1Password Developer](https://developer.1password.com/docs/ssh/agent/config/)
	- ## About
		- uses [[TOML]]
		- The SSH agent config file (`~/.config/1Password/ssh/agent.toml`) is unique to 1Password. It's separate from the SSH *client* config file ([`~/.ssh/config`](https://linux.die.net/man/5/ssh_config)) [[ssh/config]] and the SSH *server* config file ([`/etc/ssh/sshd_config`](https://linux.die.net/man/5/sshd_config)) [[ssh/config/server]] and can be used alongside them.
		- **doesn't alter your SSH agent settings or other SSH config files** on your computer
			- only **which keys the agent can access** and **in which order to make them available** to servers.
	- ## [[1Password/Dev/Doc/SSHnGit/SSH Agent/Agent Config File/Create the SSH agent Config File]] - [Create the SSH Config File](https://developer.1password.com/docs/ssh/agent/config/#create-the-ssh-agent-config-file)
		-