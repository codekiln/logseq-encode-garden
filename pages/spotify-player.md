created-by:: [[Person/Thang Pham]]
tags:: [[Rust]], [[Spotify]], [[TUI]], [[Spotify/Tool/TUI]] 
logseq-entity:: [[Logseq/Entity/Software/Project]]
- # [spotify-player](https://github.com/aome510/spotify-player) by [[GitHub/User/aome510]] aka [[Person/Thang Pham]]
	- > A Spotify player in the terminal with **full feature parity**
	- [[GitHub/Star]] count: 6,888 as of [[2026-06-27 Sat]]
	- ## Technical Aspects
		- Built with [[Rust]]
			- uses [[RustAudio/rodio]] [as its backend](https://github.com/aome510/spotify-player#audio-backend). Other backends include
				- `alsa-backend`
				- `pulseaudio-backend`
				- `rodio-backend`
				- `portaudio-backend`
				- `jackaudio-backend`
				- `rodiojack-backend`
				- `sdl-backend`
				- `gstreamer-backend`
		- Uses `librespot` crates for Spotify playback, metadata, OAuth login, and Spotify Connect.
		- Uses `rspotify` for Spotify Web API calls. The Spotify Web API is Spotify's [[HTTP]]-based application programming interface for metadata and account actions.
		- Uses [[Ratatui]] for terminal layout and rendering, with `crossterm` for terminal input, screen control, and styling.
		- Uses `reqwest`, `tokio`, and `rustls` for network and asynchronous work.
		- Uses `souvlaki` and `winit` for optional media-key integration.
		- Uses `image` and `viuer` for optional album-cover rendering in terminals.
		- Uses `notify-rust` for optional desktop notifications.
		- Uses `rustfft` for optional audio visualization when direct streaming is enabled.
	- ## Features
	  id:: 6a3f6744-5403-429d-ad4a-4391e01224ea
		- [configurable](https://github.com/aome510/spotify-player/blob/master/docs/config.md)
		- To enable [fuzzy search](https://en.wikipedia.org/wiki/Approximate_string_matching), build with the `fzf` feature (disabled by default).
			- > To enable [fuzzy search](https://en.wikipedia.org/wiki/Approximate_string_matching), build with the  [[fzf]] feature (disabled by default).
		- remote control with [Spotify Connect](https://github.com/aome510/spotify-player#spotify-connect).
		- [streaming](https://github.com/aome510/spotify-player#streaming) songs directly from the terminal.
		- [audio visualization](https://github.com/aome510/spotify-player#audio-visualization).
		- synced lyrics.
		- [cross-platform media control](https://github.com/aome510/spotify-player#media-control).
		- [image rendering](https://github.com/aome510/spotify-player#image).
		- [desktop notification](https://github.com/aome510/spotify-player#notify).
		- running the application as [a daemon](https://github.com/aome510/spotify-player#daemon)
		- [CLI commands](https://github.com/aome510/spotify-player#cli-commands)
			- [scripting](https://github.com/aome510/spotify-player#scripting)
				- ```
				  read -p "Search spotify: " query
				  spotify_player playback start track --id $(spotify_player search "$query" | jq '.tracks.[0].id' | xargs)
				  ```
	- ## [Examples](https://github.com/aome510/spotify-player#examples)
		- A demo of `spotify_player` `v0.5.0-pre-release`
		  collapsed:: true
			- {{video https://www.youtube.com/watch/Jbfe9GLNWbA}}
		- see also [asciicast](https://asciinema.org/a/446913)
		- Checkout [examples/README.md](https://github.com/aome510/spotify-player/blob/master/examples/README.md) for more examples.
	- ## Supply Chain Notes
		- Cargo.lock shows about 778 locked package entries, 700 unique [[Rust/crate]] names, 47 direct dependencies, and an approximate longest dependency chain of 33 edges.
		- This is the largest dependency tree of the three Spotify terminal clients in this comparison. It is slightly deeper than [[ncspot]] and much larger than [[spotify-tui]].
		- The larger tree comes from feature breadth: direct Spotify streaming through `librespot`, multiple audio backends, terminal rendering, image display, desktop notifications, media-key integration, OAuth login, and audio visualization.
		- The project uses a modern core stack: `tokio` 1.50, `clap` 4.6, `ratatui` 0.30, `crossterm` 0.29, `rspotify` 0.15, `reqwest` 0.13, and `rustls` 0.23.
		- The main review areas are audio output backends, TLS networking, OAuth token handling, terminal rendering, image decoding, notifications, media-key integration, and daemon mode.
		- Optional Cargo features matter here. A smaller build can avoid features such as `image`, `notify`, `daemon`, `fzf`, and non-default audio backends when those are not needed.
