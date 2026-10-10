logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Ableton/Live/Report/26/09/Open-source options for controlling Live 11 from coding agents]]

- # Is there a way to put a time-synced transcript in [[Ableton/Arrangement View]] next to an audio track with words?
	- The words could be song lyrics, the dialogue of a video, or spoken word.
	- ## [[AI Answer]]
		- **Short answer:** Live has no transcript or lyrics lane, but a MIDI track of empty, named clips does the job. Put the MIDI track directly above the audio track and add one clip per line. Each clip's name is the text, and it sits on the timeline exactly where the words are sung or spoken. This works in Live 11 without any add-ons. The work is in getting the timings, and that part can be automated.
		- **Lyrics track by hand**
			- Create a MIDI track next to the audio track. For each line, select its time range on the MIDI track, insert an empty MIDI clip with `Cmd+Shift+M`, and rename it with `Cmd+R` to the line's text.
			- The clips move with edits to the arrangement, and you can read the text while zoomed in.
			- This is the same format [[AbleSet]]'s [lyrics feature](https://ableset.com/docs/lyrics/) reads: "a MIDI track called `Vocals +LYRICS` that contains one clip per lyrics line", with `\` in a clip name for a line break. So a track built this way also works with AbleSet if you ever want a lyrics display on a phone or tablet.
		- **Getting timings automatically**
			- A transcription app such as [[Mac/App/MacWhisper]] ([[OpenAI/Whisper]] under the hood) can export a time-stamped `.srt` subtitle file or `.lrc` lyrics file from the audio.
			- AbleSet has an LRC Lyrics Track Generator that turns an `.lrc` file into a Live project with the lyrics track already built. It also has a generator where you paste plain lyrics and tap along to the backing track ([docs](https://ableset.com/docs/lyrics/)). Drag the track from that project into your set through the browser. Unconfirmed whether the generators need an AbleSet license. AbleSet itself is paid. Its Intro edition shows one lyrics track, and Standard and Pro show any number.
			- To script it yourself, the [Live Object Model](https://docs.cycling74.com/apiref/lom/track/) has `Track.create_midi_clip(start_time, length)`, which inserts an empty MIDI clip in the Arrangement, and clip names are settable. A short Max for Live or Remote Script routine could read an `.srt` and build the track. That function arrived in the Live 12.1.10 beta ([release notes](https://ableton.com/es/release-notes/live-12-beta)), so it is not available in Live 11.
			- In Live 11 a script can create named locators instead: set `Song.current_song_time`, call `Song.set_or_delete_cue`, then set the new `CuePoint.name` ([Song](https://docs.cycling74.com/apiref/lom/song/), [CuePoint](https://docs.cycling74.com/apiref/lom/cuepoint/)). Locators appear in the ruler above all tracks rather than next to one track, so they work for one voice but crowd quickly. The tools in the see-also report, such as AbletonOSC, can send these calls from outside Live.
		- **For video**
			- Burn the subtitles into the picture with `ffmpeg -i in.mp4 -vf subtitles=in.srt out.mp4`, then drop the video on an audio track in the Arrangement. Live shows it in a floating Video Window as it plays ([Working with Video](https://www.ableton.com/en/live-manual/12/working-with-video/)). The captions then stay with the picture even if you never build a lyrics track.
		- **Floating text window** (paid Max for Live devices, untested)
			- [SpaceCue](https://gospaceghost.gumroad.com/l/uzaem) shows the name of the playing clip as a teleprompter, which suits the lyrics track above. [Display Lyrics + Slides](https://abletonkurse.gumroad.com/l/display_slides_images_ableton_live) pages through slides of text or images.
		- **What doesn't work:** [[Ableton/Info Text]] is not tied to a time position. Forum reports say Live does not import the lyric or marker events in a standard MIDI file, so a karaoke `.mid` file won't bring its words along. Ableton doesn't document this either way.
