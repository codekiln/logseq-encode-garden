logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager)
	- Source repository: [git-ecosystem/git-credential-manager](https://github.com/git-ecosystem/git-credential-manager).
	- A secure, cross-platform [[Git]] credential helper (`git-credential-manager`, "GCM") that stores and retrieves HTTPS credentials in the OS keychain and handles browser-based OAuth sign-in for GitHub, Azure DevOps, Bitbucket and GitLab.
	- Installed on macOS by the Homebrew cask `git-credential-manager`, which unpacks into `/usr/local/share/gcm-core`. Upgrading the cask runs `sudo /usr/local/share/gcm-core/uninstall.sh`, so it is declared in `Brewfile.privileged` and upgraded by `mise run brew:privileged`.
