logseq-entity:: [[Logseq/Entity/Software/Project]]
tags:: [[Spotify/Tool/TUI]]

- # [ncspot](https://github.com/hrkfdn/ncspot) [[Spotify/Tool/TUI]]
	- > An [[Curses]] ncurses Spotify client written in Rust using librespot
	- [[GitHub/Star]] count: 6,671 as of [[2026-06-27 Sat]]
	- Requires a [[Spotify/Premium]] account.
	- Simpler than [[spotify-player]]. Resource-friendly Spotify terminal user interface with Vim keybindings and remote control through [[IPC]] to [[Spotify/Desktop]].
	- ## Technical Aspects
		- Built with [[Rust]] 2024.
		- Uses `librespot` for Spotify playback. `librespot` is the open-source Rust implementation of Spotify Connect and Spotify's streaming protocol.
		- Inspired by `ncmpc`, a terminal client for Music Player Daemon. Music Player Daemon is a background music player service that local clients can control.
		- Uses `cursive` for the terminal interface, with `crossterm` as the default terminal backend.
			- Optional backends include `ncurses`, `pancurses`, and `termion`.
		- Uses `rspotify` for Spotify Web API calls. The Spotify Web API is Spotify's [[HTTP]]-based application programming interface for metadata and account actions.
		- Uses `reqwest`, `tokio`, and `tokio-util` for network and asynchronous work.
		- Uses `zbus` for the optional Media Player Remote Interfacing Specification feature. MPRIS lets Linux desktops and other local tools control media players through D-Bus, the desktop message bus many Linux apps use to talk to each other.
		- Uses `notify-rust` for optional desktop notifications.
		- Uses `image` and `viuer` for optional album-cover rendering in terminals.
		- Uses `arboard` for optional clipboard sharing.
	- ## Features
		- Supports tracks, albums, playlists, genres, and search.
		- Small resource footprint compared with the official Spotify desktop client.
		- Supports macOS, Windows, Linux, and Berkeley Software Distribution systems.
		- Vim keybindings by default.
		- Inter-process communication socket for remote control.
		- Optional cover art, desktop notification, clipboard sharing, and media-key integration.
	- ## Supply Chain Notes
	  id:: 6a3f6d42-27fa-4048-81ae-c1222d59d3bf
		- Cargo.lock, Rust's dependency lockfile, shows about 595 locked package entries, 532 unique [[Rust/crate]] names, 37 direct dependencies, and an approximate longest dependency chain of 32 edges.
		- The dependency tree is a little shallower than [[spotify-player]] and much deeper than [[spotify-tui]]. Like [[spotify-player]], ncspot streams audio itself through `librespot`, supports multiple audio paths, and integrates with desktop services.
		- The larger surface area is not automatically bad, but it gives a security review more places to inspect: audio output backends, TLS (Transport Layer Security) networking, D-Bus media control, clipboard access, notifications, image decoding, and terminal rendering.
		- Compared with [[spotify-player]], ncspot has fewer locked package entries and fewer direct dependencies, but a similar dependency-chain depth. The security tradeoff is not simple: ncspot is smaller, while [[spotify-player]] uses newer terminal UI pieces and has a broader feature set.
		- The project uses newer core crates than [[spotify-tui]], including `tokio` 1, `clap` 4, and `rspotify` 0.16. That helps, but it does not remove the need to check advisories before installing from source.