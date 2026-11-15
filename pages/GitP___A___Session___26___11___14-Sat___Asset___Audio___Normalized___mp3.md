logseq-entity:: [[Logseq/Entity/Asset/B2]]
public:: true
duration-seconds:: 280
- # Episode recording, loudness-normalized
	- ![Episode recording, loudness-normalized](../assets/.remote/logseq-encode-garden/GitP___A___Session___26___11___14-Sat___Asset___Audio___Normalized.mp3)
	- 192 kbps stereo MP3 at 44.1 kHz, 4:40, made from the 24-bit, 48 kHz WAV exported from Ableton Live 11.3.43 on November 14, 2026 (`26.11.14-Fallveter-04-perf-post.wav`). Integrated loudness −16.0 LUFS; true peak −2.2 dBFS; loudness range 14.9 LU.
	- The WAV was raised 16.8 dB and passed through a true-peak limiter at −2 dBFS, run at 192 kHz. The limiter takes 4 to 6 dB off the hand-struck cue balls between 04:09 and 04:18 and up to 2 dB off a few drum strikes between 01:04 and 02:11; the rest passes unchanged.
	- ffmpeg filter: `aresample=192000,volume=16.8dB,alimiter=limit=0.7943:attack=1:release=60:level=disabled:asc=1,aresample=48000`, then `libmp3lame -b:a 192k -ar 44100 -ac 2`.
