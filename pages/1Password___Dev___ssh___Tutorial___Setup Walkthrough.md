# Setting up 1Password Dev SSH Support
	- ## Prerequisites
		- install [[OP]] - see [[1Password/Dev/Doc/CLI/Get Started]]
		- enable [[1Password/Desktop/Settings/Developer/Show 1Password Developer experience]]
		- get some SSH keys into 1Password
			- see [[1Password/How To/Import an SSH Key]] to import an SSH key
			- There are also options to [generate](https://developer.1password.com/docs/ssh/manage-keys/#generate-an-ssh-key) a key in 1Password
	- ## Steps
		- ### click [[1Password/Desktop/Settings/Developer/SSH Agent/Set up the SSH Agent]]
			- Below this is a link to [[1Password/Dev/Doc/SSHnGit/SSH Agent/Overview]], which is worth a read
			- #### Modal 1 - Allow 1Password to save SSH key names to disk?
				- To display the name of your SSH key when authorizing an SSH connection, we have to store an unencrypted copy of the **item title** on your hard drive.
				- This **will help you recognize the SSH key** if you have more than one.
				- **Button Options:**
					- [Use Key Fingerprints Only]
					  id:: 67d29d5f-451e-41d7-868c-381cae45301e
					- [Use Key Names]
				- ##### [[My Notes]]
					- this is a #Hypothesis but *presumably* **all** the SSH keys available in your current 1Password vaults will be persisted to disk either as a key title or a fingerprint, which is more likely than not, **more than you need**
					- so I think it's likely
						- **more convenient** to use key names
							- *if* you have nice, clean separation between SSH keys in vaults
							- this *would* help with debugging SSH issues
						- **more secure** to use key fingerprints
							- using key fingerprints can help leaking information accidentally
							- if you have multiple SSH keys of mixed origin available in your vaults, which is a common scenario
			- #### Modal 2 - Set Up SSH Agent
				- Add this snippet to `~/.ssh/config` to use the SSH Agent:
					- ~~~plaintext
					  
					  Host *
					    IdentityAgent "~/Library/Group Containers/2BUA8C4S2C.com.1password/t/agent.sock"
					  ~~~
				- Or, select **"Edit Automatically"** to allow 1Password to update `~/.ssh/config` for you.
				- **Options:**
					- [Copy Snippet]
					- [Edit Automatically]
		- ### Migrating to using the SSH agent
			- At this point, you may want to move your [[ssh/Key/Private]] and update your [[ssh/config]] to no longer reference it
				- for example `cd ~/.ssh && mkdir -p tbd && mv <PRIVATE_KEY_NAME> tbd/<PRIVATE_KEY_NAME>.to_be_deleted.txt`
			- After doing that, try `ssh -T git@github.com` to try testing out whether your keys are loaded
				- you might get permission denied, which might mean that your keys are not stored in a vault that makes them an [eligible key](https://developer.1password.com/docs/ssh/agent/#eligible-keys) [[1Password/Dev/Doc/SSHnGit/SSH Agent/Overview/Eligible Keys]]
		- ### Ensure your SSH key is in Eligible Keys
			- See [[1Password/Dev/Doc/SSHnGit/SSH Agent/Overview/Eligible Keys]] for an overview, but in particular, note that if your key is in a custom vault, **it is not eligible by default** and the solution is to create a 1Password SSH Agent Config File;  [SSH agent config file | 1Password Developer](https://developer.1password.com/docs/ssh/agent/config/) [[1Password/Dev/Doc/SSHnGit/SSH Agent/Agent Config File]]
			- In particular, if you have selected to use key fingerprints only as in ((67d29d5f-451e-41d7-868c-381cae45301e)), you may want to [use IDs as values](https://developer.1password.com/docs/ssh/agent/config/#use-ids-as-values), which requires special configuration
				- > To find and copy an item ID, go to the [**Advanced** settings](onepassword://settings/advanced) in the 1Password app and turn on **Show debugging tools**. Find the item you want and select it, then select  > **Copy UUID**. Then paste the UUID value in the config file entry.
				- > You can also [use 1Password CLI to find the IDs for your items, vaults, and accounts](https://developer.1password.com/docs/cli/reference/#unique-identifiers-ids).
	- ## Follow-up Configuration
		- ### Review [[1Password/Desktop/Settings/Developer/SSH Agent/Advanced]] options
		  collapsed:: true
			- **Ask approval for each new:**
				- `application and terminal session` (dropdown)
			- **Remember key approval:**
				- `until 1Password locks` (dropdown)
			- [ ] **Display key names when authorizing connections**
				- An unencrypted copy of the item title will be stored locally.
					- See [[1Password/Dev/Doc/SSHnGit/SSH Agent/Suppressing Background Requests]] - [[My Note]] - it's important to be aware of this behavior when setting it up
			- [ ] **Generate SSH config file with bookmarked hosts**
				- An unencrypted copy of bookmarked SSH host URLs will be stored locally.
					- See [[1Password/Dev/ssh/Bookmarks]]
			- **Open SSH URLs with:**
				- `Terminal` (dropdown to pick terminal)
					- [[My Note]] - you likely want to customize this to your preferred [[Terminal]] program rather than using the default
		- ### Command-Line Interface (CLI)
		  collapsed:: true
			- [x] **Integrate with [[1Password/Dev/CLI]]**
				- Use the desktop app to sign in to 1Password in the terminal.
		- ### Watchtower ([[1Password/Dev/Watchtower]])
		  collapsed:: true
			- [x] **Check for developer credentials on disk**
				- See [[1Password/Dev/Doc/Watchtower]]
			- **Options:**
				- [Show in Watchtower]
			- [[My Note]] *so far, watchtower seems like a great way to improve one's security posture*