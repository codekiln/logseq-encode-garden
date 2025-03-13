alias:: [[1Password/How To/Import an SSH Key]]

- ## [Import an SSH key](https://developer.1password.com/docs/ssh/manage-keys/#import-an-ssh-key)
	- ### [[My Notes]]
		- #### [[My Question]] Where is the expected location for [[ssh/Key/Public]] in [[1Password]]? By default the New Item of type SSH Key only has a single private key field.
			- I can click `add more` and then select a number of different types of items, including one item for items of type `Text`, but I'm a bit surprised that the SSH Key type doesn't have native support for a public key as well as a private key.
			- [[My Answer]] - the [[SSH Public Key]] is computed from the private key *by 1Password*; there's no need to add your public key separately. It will show up in the main screen. See [[1Password/Dev/Doc/SSHnGit/Manage SSH Keys/Share a public Key]]
		- #### When done, add a new 1Password item of type `Password` and add the [[ssh/Key/Passphrase]]
			- This isn't part of the instructions, but it's a good idea to store the passphrase *on* the SSH key item to keep them together in 1Password.
	- ### Add [[SSH Private Key]]
		- #### New Item > SSH Key
			- navigate to location of private key & select (it opens up to `~/.ssh/id_rsa`, which is convenient)
		- #### Decrypt [[SSH Private Key]]
			- enter the passphrase
				- if the passphrase is stored in [[1Password]], use [[1Password/Quick Access]]   to find and copy it without needing to switch context.
					- ![quick access](https://developer.1password.com/img/ssh/copy-ssh-passphrase-quick-access.png)
			- > After you import the SSH key into 1Password, it'll be encrypted according to the [1Password security model](https://support.1password.com/1password-security/#encryption).
			-
	-