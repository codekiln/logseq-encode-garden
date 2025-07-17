tags:: [[Diataxis/How To]], [[mise/Tool]], [[AWS/CLI/Tool]]

- # How To automate [[Okta]] → [[AWS]] login with [[mise]], [[aws_okta_keyman]] & [[1Password/Dev/CLI]], using [[Biometric]] unlock for [[MFA/TOTP]]
	- ## Goal
		- Run `mise aws-okta-login` (alias `mise run aok`) once, approve biometrics, and receive AWS credentials—no typing of password or TOTP.
	- ## Preconditions
		- **mise** ≥ 2024.6 installed and initialised in your shell.
		- **uv** + **pipx** available (mise installs them automatically).
		- **aws_okta_keyman** ≥ 0.9.0 reachable on `$PATH`.
		- 1Password desktop + CLI v2 with biometric unlock enabled.
		- A 1Password login item (e.g. *Okta AWS*) containing
			- `password` — your Okta password
			- `one-time password` (TOTP) — already configured.
		- **expect** installed (`brew install expect` or `apt install expect`).
		- `~/.local/bin` on `$PATH`.
	- ## Procedure
		- ### 1. Install aws_okta_keyman via mise + uvx
			- ~~~toml
			  # mise.toml (project) or ~/.config/mise/config.toml (global)
			  [tools]
			  "pipx:aws-okta-keyman" = "latest"
			  ~~~
			- `mise install` builds an isolated uvx environment.
		- ### 2. Create the [[Linux/expect]] wrapper with [[1Password/Dev/op/read]]
			- ==You will need to edit the values below to point to the vault and item== ... [[1Password Secret References]]
			- ~~~tcl
			  # ~/.local/bin/aws_okta_login.expect
			  #!/usr/bin/env expect -f
			  set timeout -1
			  set pw  [exec op read "op://<VAULT>/<ITEM>/password"]
			  spawn aws_okta_keyman          ;# org & app_id read from config
			  expect {
			      -re "Password:" {
			          send -- "$pw\r"
			          exp_continue
			      }
			      -re "MFA Passcode:" {
			          set otp [exec op read "op://<VAULT>/<ITEM>/one-time password?attribute=otp"]
			          send -- "$otp\r"
			          exp_continue
			      }
			      eof
			  }
			  ~~~
			- `chmod +x ~/.local/bin/aws_okta_login.expect`
		- ### 3. Define global mise tasks
			- ~~~toml
			  # ~/.config/mise/config.toml
			  [tasks.aws-okta-login]
			  description = "Okta→AWS login via 1Password"
			  run = ["op","run","--","aws_okta_login.expect"]
			  
			  [tasks.aok]   # handy alias to call aws_okta_keyman directly
			  description = "Invoke aws_okta_keyman"
			  run = ["uvx","aws_okta_keyman","$@"]
			  ~~~
			- It's unlikely you'll need to do this if you have been using mise for a while, but if this is your first time with mise and the home config,
				- Trust once: `mise trust ~/.config/mise/config.toml`
		- ### 4. Set up aws_okta_keyman.yml in `~/.config/aws_okta_keyman.yml`
			- **Note**: you can instead run `mise run aok config` for [interactive configuration](https://github.com/nathan-v/aws_okta_keyman?tab=readme-ov-file#interactive-configuration).
			- Add (edit values as needed):
				- ~~~yml
				  # corresponds to the `--console` flag for browser log-ins
				  console: null
				  duo_factor: null
				  # duration is in seconds (default 3600 = 1 hour)
				  # duration: 3600
				  org: https://mycompany.okta.com
				  # enable keyring password cache (jaraco/keyring)
				  password_cache: true
				  region: null
				  # re-up mode automatically refreshes credentials
				  reup: true
				  # activate this AWS role by default
				  role: my-account
				  screen: null
				  username: myAWS_username
				  ~~~
			- aws_okta_keyman now runs with the default account specified.
		- ### 5. Use it
			- 1. `mise run aws-okta-login`  
			  2. Approve Touch ID / Windows Hello.  
			  3. Credentials appear in `~/.aws/credentials`; subsequent `aws` commands work.
	- ## Troubleshooting
		- **Script not found** → `command -v aws_okta_login.expect` should show a path.
		- **OTP not injected** → ensure `?attribute=otp` is present in the `op read` call.
		- **“No such file or directory” from mise** → keep `run` in array form or set `shell = "bash -c"`.
		- **1Password session expired** → session idles out after ~10 min; rerun the task.
	- ## References
		- 1Password CLI `read` with `?attribute=otp` — [1Password docs](https://developer.1password.com/docs/cli/reference/commands/read/).
		- mise global config & tasks — [mise documentation](https://mise.jdx.dev/tasks/).
		- aws_okta_keyman — [GitHub repository](https://github.com/nathan-v/aws_okta_keyman).