tags:: [[YouTube]], [[yt-dlp]], [[Python/Library]], [[CLI]]

- # [[yt-dlp/PyPI]] [yt-dlp · PyPI](https://pypi.org/project/yt-dlp/)
	- A feature-rich command-line audio/video downloader
	- [[yt-dlp/GitHub]] [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
	- ## [Installation](https://github.com/yt-dlp/yt-dlp/wiki/Installation)
		- [[CLI/Tool/Mac/brew]] might be easier - `brew install yt-dlp`
			- see also [Idiot guide to download yt-dlp to Mac : r/youtubedl](https://www.reddit.com/r/youtubedl/comments/1br16c5/idiot_guide_to_download_ytdlp_to_mac/)
				- You'll be using the Terminal app on macOS, which resides in Applications > Utilities.
				- Install [Homebrew](https://brew.sh/) following their instructions.
				- Install ffmpeg by issuing the command: `brew install ffmpeg`
				- Install yt-dlp by issuing the command: `brew install yt-dlp`
				- To update HomeBrew, ffmpeg and yt-dlp, issue the command: `brew upgrade` and when everything is done updating, close the Terminal window and open a new one.
				  
				  After that, you'll be learning to use yt-dlp commands like anyone else does here. Start with the [yt-dlp documentation](https://github.com/yt-dlp/yt-dlp).
		- for python - pip install `yt-dlp[default]`
		- ### DEPENDENCIES
			- While all the other dependencies are optional, [[CLI/Tool/ffmpeg]] and [[ffprobe]] are highly recommended
				- ### [Strongly recommended](https://github.com/yt-dlp/yt-dlp#strongly-recommended)
				- [**ffmpeg** and **ffprobe**](https://www.ffmpeg.org/) - Required for [merging separate video and audio files](https://github.com/yt-dlp/yt-dlp#format-selection), as well as for various [post-processing](https://github.com/yt-dlp/yt-dlp#post-processing-options) tasks. License [depends on the build](https://www.ffmpeg.org/legal.html)
				- There are bugs in ffmpeg that cause various issues when used alongside yt-dlp. Since ffmpeg is such an important dependency, we provide [custom builds](https://github.com/yt-dlp/FFmpeg-Builds#ffmpeg-static-auto-builds) with patches for some of these issues at [yt-dlp/FFmpeg-Builds](https://github.com/yt-dlp/FFmpeg-Builds). See [the readme](https://github.com/yt-dlp/FFmpeg-Builds#patches-applied) for details on the specific issues solved by these builds
				- **Important**: What you need is ffmpeg *binary*, **NOT** [the Python package of the same name](https://pypi.org/project/ffmpeg)
			- ### [Networking](https://github.com/yt-dlp/yt-dlp#networking)
				- [**certifi**](https://github.com/certifi/python-certifi)* - Provides Mozilla's root certificate bundle. Licensed under [MPLv2](https://github.com/certifi/python-certifi/blob/master/LICENSE)
				- [**brotli**](https://github.com/google/brotli)* or [**brotlicffi**](https://github.com/python-hyper/brotlicffi) - [Brotli](https://en.wikipedia.org/wiki/Brotli) content encoding support. Both licensed under MIT [1](https://github.com/google/brotli/blob/master/LICENSE) [2](https://github.com/python-hyper/brotlicffi/blob/master/LICENSE)
				- [**websockets**](https://github.com/aaugustin/websockets)* - For downloading over websocket. Licensed under [BSD-3-Clause](https://github.com/aaugustin/websockets/blob/main/LICENSE)
				- [**requests**](https://github.com/psf/requests)* - HTTP library. For HTTPS proxy and persistent connections support. Licensed under [Apache-2.0](https://github.com/psf/requests/blob/main/LICENSE)
		- ## [Usage and Options](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#usage-and-options)
			- `yt-dlp [OPTIONS] [--] URL [URL...]`
			- ### General Options
				- ```\
				  -h, --help                      Print this help text and exit
				  --version                       Print program version and exit
				  -U, --update                    Update this program to the latest version
				  --no-update                     Do not check for updates (default)
				  --update-to [CHANNEL]@[TAG]     Upgrade/downgrade to a specific version.
				                                  CHANNEL can be a repository as well. CHANNEL
				                                  and TAG default to "stable" and "latest"
				                                  respectively if omitted; See "UPDATE" for
				                                  details. Supported channels: stable,
				                                  nightly, master
				  -i, --ignore-errors             Ignore download and postprocessing errors.
				                                  The download will be considered successful
				                                  even if the postprocessing fails
				  --no-abort-on-error             Continue with next video on download errors;
				                                  e.g. to skip unavailable videos in a
				                                  playlist (default)
				  --abort-on-error                Abort downloading of further videos if an
				                                  error occurs (Alias: --no-ignore-errors)
				  --dump-user-agent               Display the current user-agent and exit
				  --list-extractors               List all supported extractors and exit
				  --extractor-descriptions        Output descriptions of all supported
				                                  extractors and exit
				  --use-extractors NAMES          Extractor names to use separated by commas.
				                                  You can also use regexes, "all", "default"
				                                  and "end" (end URL matching); e.g. --ies
				                                  "holodex.*,end,youtube". Prefix the name
				                                  with a "-" to exclude it, e.g. --ies
				                                  default,-generic. Use --list-extractors for
				                                  a list of extractor names. (Alias: --ies)
				  --default-search PREFIX         Use this prefix for unqualified URLs. E.g.
				                                  "gvsearch2:python" downloads two videos from
				                                  google videos for the search term "python".
				                                  Use the value "auto" to let yt-dlp guess
				                                  ("auto_warning" to emit a warning when
				                                  guessing). "error" just throws an error. The
				                                  default value "fixup_error" repairs broken
				                                  URLs, but emits an error if this is not
				                                  possible instead of searching
				  --ignore-config                 Don't load any more configuration files
				                                  except those given to --config-locations.
				                                  For backward compatibility, if this option
				                                  is found inside the system configuration
				                                  file, the user configuration is not loaded.
				                                  (Alias: --no-config)
				  --no-config-locations           Do not load any custom configuration files
				                                  (default). When given inside a configuration
				                                  file, ignore all previous --config-locations
				                                  defined in the current file
				  --config-locations PATH         Location of the main configuration file;
				                                  either the path to the config or its
				                                  containing directory ("-" for stdin). Can be
				                                  used multiple times and inside other
				                                  configuration files
				  --plugin-dirs PATH              Path to an additional directory to search
				                                  for plugins. This option can be used
				                                  multiple times to add multiple directories.
				                                  Note that this currently only works for
				                                  extractor plugins; postprocessor plugins can
				                                  only be loaded from the default plugin
				                                  directories
				  --flat-playlist                 Do not extract a playlist's URL result
				                                  entries; some entry metadata may be missing
				                                  and downloading may be bypassed
				  --no-flat-playlist              Fully extract the videos of a playlist
				                                  (default)
				  --live-from-start               Download livestreams from the start.
				                                  Currently only supported for YouTube
				                                  (Experimental)
				  --no-live-from-start            Download livestreams from the current time
				                                  (default)
				  --wait-for-video MIN[-MAX]      Wait for scheduled streams to become
				                                  available. Pass the minimum number of
				                                  seconds (or range) to wait between retries
				  --no-wait-for-video             Do not wait for scheduled streams (default)
				  --mark-watched                  Mark videos watched (even with --simulate)
				  --no-mark-watched               Do not mark videos watched (default)
				  --color [STREAM:]POLICY         Whether to emit color codes in output,
				                                  optionally prefixed by the STREAM (stdout or
				                                  stderr) to apply the setting to. Can be one
				                                  of "always", "auto" (default), "never", or
				                                  "no_color" (use non color terminal
				                                  sequences). Use "auto-tty" or "no_color-tty"
				                                  to decide based on terminal support only.
				                                  Can be used multiple times
				  --compat-options OPTS           Options that can help keep compatibility
				                                  with youtube-dl or youtube-dlc
				                                  configurations by reverting some of the
				                                  changes made in yt-dlp. See "Differences in
				                                  default behavior" for details
				  --alias ALIASES OPTIONS         Create aliases for an option string. Unless
				                                  an alias starts with a dash "-", it is
				                                  prefixed with "--". Arguments are parsed
				                                  according to the Python string formatting
				                                  mini-language. E.g. --alias get-audio,-X
				                                  "-S=aext:{0},abr -x --audio-format {0}"
				                                  creates options "--get-audio" and "-X" that
				                                  takes an argument (ARG0) and expands to
				                                  "-S=aext:ARG0,abr -x --audio-format ARG0".
				                                  All defined aliases are listed in the --help
				                                  output. Alias options can trigger more
				                                  aliases; so be careful to avoid defining
				                                  recursive options. As a safety measure, each
				                                  alias may be triggered a maximum of 100
				                                  times. This option can be used multiple times
				  ```