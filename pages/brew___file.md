- # Brewfile
  - ## What a Brewfile Is
    - A **Brewfile** is a declarative manifest used by Homebrew via its `brew bundle` subcommand to describe the software you want installed on a machine.
    - Instead of imperatively running:
    - ~~~
      brew install tmux
      brew install neovim
      brew install ripgrep
      brew install --cask iterm2
      ~~~
    - You write a Brewfile and run:
    - ~~~
      brew bundle
      ~~~
    - It ensures your system matches the declared state.
  - ## Basic Structure
    - A Brewfile is Ruby-like DSL (but not full Ruby). Example:
    - ~~~
      tap "homebrew/core"
      tap "homebrew/cask"
      brew "tmux"
      brew "neovim"
      brew "ripgrep"
      cask "iterm2"
      cask "visual-studio-code"
      mas "Xcode", id: 497799835
      vscode "ms-python.python"
      ~~~
    - ### Directives
      - | Directive | Meaning |
      - | ---- | ---- | ---- |
      - | `tap` | Add a repository (e.g. custom formula source) |
      - | `brew` | Install CLI formula |
      - | `cask` | Install macOS app bundle |
      - | `mas` | Install Mac App Store app (requires `mas` CLI + login) |
      - | `vscode` | Install VSCode extension |
  - ## Generating a Brewfile From an Existing Machine
    - ~~~
      brew bundle dump
      ~~~
    - Options:
    - ~~~
      brew bundle dump --force        # overwrite existing
      brew bundle dump --describe     # include comments
      brew bundle dump --file=~/dotfiles/Brewfile
      ~~~
    - This is useful if you're version-controlling environment state in something like your chezmoi repo.
  - ## Applying a Brewfile
    - ~~~
      brew bundle
      ~~~
    - Other useful modes:
    - ~~~
      brew bundle check      # see what's missing
      brew bundle cleanup    # remove things not in Brewfile
      brew bundle install    # explicit install
      brew bundle exec cmd   # run command with Brewfile env
      ~~~
    - `cleanup` is especially interesting for drift control.
  - ## Advanced Patterns
    - ### Conditional Installs
      - You can gate installs by OS or architecture:
      - ~~~
        brew "htop" if OS.mac?
        brew "gnu-sed" if OS.linux?
        brew "openssl@3" if Hardware::CPU.arm?
        ~~~
      - This is useful for multi-machine setups (e.g., your 2023 M-series vs Intel).
    - ### Version Pinning
      - Homebrew doesn't support strict version pinning in Brewfiles in a robust way (it tracks latest stable). You can:
      - `brew "postgresql@15"` (versioned formula)
      - Use `brew pin <formula>` manually
      - Vendor your own tap for frozen versions
      - But it's not meant to be a lockfile system like `npm` or `pip`.
    - ### Custom Installation Arguments
      - ~~~
        brew "postgresql", restart_service: true
        brew "imagemagick", args: ["with-webp"]
        ~~~
      - Casks:
      - ~~~
        cask "docker", args: { appdir: "~/Applications" }
        ~~~
  - ## Relationship to Your chezmoi Question
    - Brewfile solves exactly what you were circling around:
    - Dotfiles configure tmux, vim, rg, etc.
    - Brewfile declares that tmux, vim, rg must exist.
    - Typical pattern:
    - ~~~
      dotfiles/
      ├── Brewfile
      ├── .tmux.conf
      ├── .config/nvim/
      ~~~
    - Then bootstrap:
    - ~~~
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      brew bundle --file=~/dotfiles/Brewfile
      chezmoi init
      chezmoi apply
      ~~~
    - That gives you:
    - Provisioning (brew)
    - Configuration (chezmoi)
    - Clean separation of concerns.
  - ## Where Brewfile Fits in the Ecosystem
    - Think of it as:
    - Lighter-weight than Ansible
    - Declarative but not deeply idempotent infrastructure
    - Machine-scoped, not project-scoped
    - Best for macOS dev environments
    - If you want:
    - Cross-platform reproducibility → look at Nix
    - Full provisioning + OS config → Ansible
    - Project isolation → devcontainers / Docker
    - Minimal mac bootstrap → Brewfile is perfect
  - ## Design Philosophy
    - Homebrew intentionally avoids becoming a full configuration manager. `brew bundle` is:
    - Simple
    - Machine-level
    - Developer workstation oriented
    - It's closer to "state reconciliation" than "infrastructure as code."
  - ## Possible Integrations
    - If you want, I can also outline how to integrate:
    - Brewfile + chezmoi
    - Brewfile + devcontainers
    - Brewfile + CI bootstrap
    - Brewfile + M-series vs Intel conditionalization
    - Given your setup experiments, there are some interesting hybrid patterns worth considering.
