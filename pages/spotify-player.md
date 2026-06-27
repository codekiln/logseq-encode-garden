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
	- ## Features
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
			- {{video https://www.youtube.com/watch/Jbfe9GLNWbA}}
		- see also [asciicast](https://asciinema.org/a/446913)
		- Checkout [examples/README.md](https://github.com/aome510/spotify-player/blob/master/examples/README.md) for more examples.