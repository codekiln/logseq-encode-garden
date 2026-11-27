tags:: [[Idea]]
date-created:: [[2026-11-26 Thu]]
see-also:: [[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]], [[Launchpad/Q/Do Custom Modes have pagination for selecting more MicroFreak presets?]], [[Ableton/Live/Idea/Keep-Commentary-in-Live-Sets]], [[Ableton/Max for Live]], [[GitP/A/Log/26/11/26-Thu]]

- # Pick MicroFreak Presets through Live
	- [[My Note]]
		- ### Translate in Live
			- It occurred to me that we don't actually need to have the Launchpad send messages directly to the MicroFreak. We could also use Max for Live or other things in Ableton to do an intermediate translation so that it's really intuitive.
			- It's a little bit difficult for me to figure out what's possible here and what would be intuitive.
		- ### Digit columns
			- For example, one idea I had was that, since there are 8 rows and columns, in groups of 2 we can get up to 10 digits. So maybe the first 2 rows or the first 2 columns would signify the first digit, the second 2 columns the second digit, the third 2 columns the third digit.
		- ### A number pad
			- Actually, I thought of a different way. You could have almost like a calculator pad: a number pad that would let me key in the number of the preset, and then maybe even hit enter, and then it would send the program change.
		- ### Arrows and colors
			- And maybe there would even be a way to select it with up and down arrows, that kind of thing, and then be able to see whether it's a pad based on the color.
	- [[AI/Response]]
		- ## Recommendation
			- Build the number pad with Enter. You key in the slot number that the MicroFreak's screen and the garden's preset pages already use, such as 259 for [[Microfreak/Preset/259 Infini Pad]]. The sound changes when you press Enter, so a wrong digit costs nothing while a recording runs.
			- The number pad takes twelve pads. The rest of the grid holds step pads, the presets GitP sessions have used, and the last eight presets sent, so a preset you return to takes one press.
			- Each change is written into the Set as a short clip named after the preset, on a MIDI track named `presets`. That is the record [#501 Record which MicroFreak preset is playing in GitP Sets, from Launchpad Custom Modes](https://github.com/codekiln/logseq-encode-garden/issues/501) asks for.
			- Nothing here has been built or tried. I sent nothing to the Launchpad, the MicroFreak or Live.
		- ## The translation layer
			- Every design below uses the same three parts, so the designs differ only in what the Max for Live device does with a pad press.
			- ### The Launchpad sends plain notes
				- One Custom Mode has all 64 pads set as Midi Note pads on channel 16, numbered 11 to 88 as in the Programmer layout: the bottom-left pad is 11 and the top-right pad is 88 ([[Launchpad/PRG/05 Software Integration/11 Programmer Layout]]). Factory Custom Mode 8 uses the same numbers ([[Launchpad/PRG/05 Software Integration/12 Factory Custom Modes]]).
				- The pads carry no meaning of their own. The device decides what each pad does, so trying another design means changing the device and leaving the Custom Mode alone.
				- Notes also make the pads lightable. Live can light a Custom Mode pad by sending the Launchpad a note with the pad's number, and the velocity picks the colour ([[Launchpad/UG/08 Custom Modes/05 Lighting Pads with External MIDI]]). Novation's guides describe lighting by note number and CC number only, so a Program Change pad probably stays in the colour Components gave it.
			- ### A device turns a press into bank and program
				- The device is a Max for Live MIDI effect on the `LPP CM2 to MF` track from [[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]]: MIDI From the Launchpad on channel 16, Monitor In, MIDI To the MicroFreak on channel 1.
				- For slot N it sends CC 0 with value `(N − 1) // 128`, then Program Change `(N − 1) % 128`, the pair that selected slot 323 in [[Microfreak/CLI/Upload a preset]]. It sends the bank every time, so one press reaches a slot in any bank.
				- The device keeps the pad notes to itself. Passed on, they would play the MicroFreak.
				- Ableton says Max for Live devices can send Program Change ([Sending Program Change messages from Ableton Live](https://help.ableton.com/hc/en-us/articles/209070489-Sending-Program-Change-messages-from-Ableton-Live)). Cycling '74 says a device's MIDI is "limited to those messages that Live will recognize and pass between devices" ([Max for Live Limitations](https://docs.cycling74.com/userguide/m4l/live_limitations/)). Whether CC 0 and Program Change from a device reach the MicroFreak is the first thing to try.
				- The device needs a table of slot, name, category and number of GitP sessions. A mise task can write it as JSON from the `Microfreak/Preset/*` pages, which hold 372 presets in slots 1 to 402, each with a category ([[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category]]). The designs below use that table for colours and for skipping empty slots.
				- The device knows only the presets it sent. A preset chosen on the MicroFreak's panel leaves the pads and the Set showing the old one, because no known message reports the selected preset ([[Microfreak/CLI/Audition a sequence]]).
			- ### A second track lights the pads
				- A device's MIDI output goes to its own track's output, and that track feeds the MicroFreak. A second MIDI track, `MF picker lights`, has MIDI To set to `Launchpad Pro MK3 (LPProMK3 MIDI)` and holds a small device that turns colour messages from the picker into notes.
				- The note number picks the pad and the velocity picks one of 128 palette colours. The channel picks the behaviour: 1 static, 2 flashing, 3 pulsing ([[Launchpad/PRG/04 Controlling the Surface/01 Lighting LEDs]], [[Launchpad/PRG/04 Controlling the Surface/02 Colour Palette]]). A track sends on one channel, so the designs below use static colours.
				- Each of the 12 categories gets a palette colour. The current preset's pad is white.
			- ### The Set keeps a record
				- When the device sends a preset, it reads the Arrangement position from `current_song_time` and calls `create_midi_clip` on the `presets` track, then sets the clip's `name` to the slot and preset name, such as `259 Infini Pad`, and its `color` to the category colour. The Live Object Model documents all four: [Song](https://docs.cycling74.com/apiref/lom/song/), [Track](https://docs.cycling74.com/apiref/lom/track/), [Clip](https://docs.cycling74.com/apiref/lom/clip/).
				- `create_midi_clip` throws an error "when the track is currently being recorded into", so `presets` stays unarmed.
				- A locator is the other option. `set_or_delete_cue` toggles a locator at the playback position and a CuePoint's `name` can be set ([CuePoint](https://docs.cycling74.com/apiref/lom/cuepoint/)). The toggle deletes a locator that already sits at that position, and the locator sync overwrites locators at chapter times, as [[Ableton/Live/Idea/Keep-Commentary-in-Live-Sets]] records. Clips on `presets` stay clear of both.
				- A clip has no property for its Bank and Program fields in the Live Object Model, so the clip is a label. Replaying the Arrangement would not re-send the preset.
		- ## Designs
			- In each sketch, `·` is an unlit spare pad and the top row of the sketch is the top row of the grid.
			- ### Digit columns
				- Your column idea, with two columns and five rows for each digit. The hundreds digit stops at 5 because the last slot is 512.
				  ~~~
				  hundreds  tens  ones
				    0 1     0 1   0 1   − +
				    2 3     2 3   2 3   · ·
				    4 5     4 5   4 5   · ·
				    · ·     6 7   6 7   · ·
				    · ·     8 9   8 9   · ·
				    · ·     · ·   · ·   · ·
				    · ·     · ·   · ·   · ·
				    · ·     · ·   · ·   · ·
				  ~~~
				- **Lights:** the three digits of the current slot are lit in its category colour, so the grid always reads as the slot number. A hundreds or tens digit you have pressed and not yet sent is white. The other digit pads are dim.
				- **Presses:** a hundreds or tens press only stages the digit. A ones press sends the slot. Any slot takes at most three presses, and a slot in the same ten takes one: from 259, pressing 7 in the ones columns sends 257. `−` and `+` step to the neighbouring slot.
				- **Translation:** the device holds three digits, and on a ones press it works out the slot and sends bank and program. It refuses 000 and anything above 512.
				- **Live use:** the grid shows where you are at a glance, and stepping to a neighbour is fast. Finding a digit among 30 pads is slower than on a number pad, and the layout needs the lights: with the pads dark, three identical groups of digits are hard to tell apart. Turned sideways, with two rows per digit, each digit reads as a number line from 0 to 9.
			- ### Number pad with Enter
				- A phone-style number pad in the top-left corner, with Backspace, Clear, step pads and a wide Enter.
				  ~~~
				  7 8 9 ⌫   S S S S
				  4 5 6 C   S S S S
				  1 2 3 ▲   S S S S
				  · 0 · ▼   S S S S
				  E E E E   S S S S
				  · · · ·   S S S S
				  R R R R   S S S S
				  R R R R   S S S S
				  ~~~
				- `S` pads hold the presets GitP session pages link, 30 today, ordered by slot. `R` pads hold the last eight presets sent, newest first.
				- **Lights:** digit pads are white and each flashes brighter when pressed. Enter shows the category colour of the number typed so far, so 2 5 9 turns Enter the Pad colour before you commit. Enter is red when the number is 0, above 512, or an empty slot. `S` and `R` pads are in their category colours, and the current preset's pad is white.
				- **Presses:** digits and Enter, so two to four for any slot: 1 6 Enter for [[Microfreak/Preset/016 Voidom]]. `▲` and `▼` send the next and previous filled slot in one press. An `S` or `R` pad sends its preset in one press.
				- **Translation:** the device collects up to three digits. Backspace drops the last digit and Clear drops them all. Enter sends the slot and empties the entry. Digits left untouched for a few seconds are dropped, so a stray press never combines with the next number.
				- **Live use:** the number is the one on the MicroFreak's screen, on the preset pages and in the session notes, so there is nothing new to memorize. The sound changes only on Enter. The digits sit where a phone puts them, so the pad works with every light off, and the MicroFreak's screen shows the result. The cost is three or four presses for a preset outside the `S` and `R` pads.
			- ### Browse with arrows
				- The arrow buttons do nothing in a Custom Mode ([[Launchpad/Q/Do Custom Modes have pagination for selecting more MicroFreak presets?]]), so four grid pads act as arrows. The top six rows are a window onto the list of presets, 48 at a time.
				  ~~~
				  p p p p p p p p
				  p p p p p p p p
				  p p p p p p p p
				  p p p p p p p p
				  p p p p p p p p
				  p p p p p p p p
				  # c · ▲ · · « »
				  · · ◀ ▼ ▶ · · ·
				  ~~~
				- **Lights:** each `p` pad is a preset in its category colour, brighter when a GitP session has used it. The current preset is white. `#` and `c` show which order is on: by slot number, or by category and then slot.
				- **Presses:** `◀` and `▶` move one preset, `▲` and `▼` move one row of eight, and the window scrolls to keep the white pad in view. `«` and `»` turn the page by 48. Pressing a `p` pad selects it. The 372 filled slots make eight pages, so any preset takes at most seven page presses and one pad press.
				- **Translation:** the device keeps an ordered list and a position. Every arrow press sends bank and program, so you hear each preset as you pass it. It writes a clip only after a preset has stayed selected for two seconds, which keeps a run of arrow presses from leaving a clip for each step.
				- **Live use:** this suits looking for a sound by ear. In a recording, every step is audible, and the pads carry no names, so going straight to a preset you know means counting pads or remembering a place in a list that moves.
			- ### Category first
				- The top two rows choose what the other six rows show.
				  ~~~
				  Ba Br Ke Le Or Pa Pe SF
				  Sq St Te Vo GP Re ◀  ▶
				  p  p  p  p  p  p  p  p
				  p  p  p  p  p  p  p  p
				  p  p  p  p  p  p  p  p
				  p  p  p  p  p  p  p  p
				  p  p  p  p  p  p  p  p
				  p  p  p  p  p  p  p  p
				  ~~~
				- The top rows hold the 12 categories, Bass to Vocoder, then `GP` for presets used in GitP sessions and `Re` for recent ones. `◀` and `▶` turn the page inside a category.
				- **Lights:** each category pad has its own colour and the chosen one is white. The `p` pads show that category's presets in slot order, brighter when a GitP session has used them. Pads past the end of the category are dark.
				- **Presses:** a category press, then a preset press. Ten categories fit on one page of 48. Bass has 54 presets and Sequence has 83, so their later presets take a page press as well.
				- **Translation:** a category press changes what the `p` pads mean and sends nothing. A `p` press sends that preset's bank and program.
				- **Live use:** colour answers "give me a pad" in one press, and choosing a category makes no sound. Within a category the pads are unlabelled, so finding one known preset among 43 SFX pads means remembering its place. It also depends on the lights more than any other design: with the pads dark it cannot be used.
			- ### Session presets on one press
				- The `S` and `R` pads from the number pad sketch also work alone: a grid of the presets GitP has used, in category colours that grow brighter with the number of sessions. Custom Mode 2 holds eight of these today as Program Change pads behind four bank pads ([[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]]). Through the device, each pad sends bank and program together, and the table from the garden fills the pads, so a preset used in a new session appears without a trip to Components.
				- **Presses:** one, for the 30 presets session pages link today. Every other slot needs one of the designs above beside it.
		- ## Why the number pad
			- It depends least on what is still untested. Digit columns, browsing and the category grid all need Live to light the pads. The number pad needs only notes in and bank and program out.
			- A known preset needs no searching. You read 259 off a session page and type it.
			- Enter separates choosing from changing the sound. With Arrangement Record on, that keeps half-finished choices out of the recording and out of the `presets` track.
			- Your arrows and colours fit inside it: `▲` and `▼` step through filled slots, and Enter shows the category colour before you commit.
		- ## What would change the recommendation
			- You pick presets by sound more often than by number. Category first then earns a place as a second layout in the same device, switched by one pad.
			- You mostly move between neighbouring slots, as when comparing a run of factory presets. Digit columns do that in one press and show the slot all the time.
			- Three or four presses feels slow in a session. The `S` and `R` pads then matter more than the number pad, and the grid should give them more room.
			- Live keeps CC 0 or Program Change from a device away from the MicroFreak. The pads would go back to Program Change pads in the Custom Mode, or to Session clips that carry bank and program, as [[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]] describes.
			- Lighting a Custom Mode from Live proves unreliable. Programmer Mode lights every pad and button by note, including the arrow buttons ([[Launchpad/PRG/05 Software Integration/10 Programmer Mode]]), at the cost of leaving the Custom Modes while picking.
		- ## Check before building
			- ### In Live
				- CC 0 and Program Change sent by a Max for Live MIDI effect reach the MicroFreak through the track's MIDI To.
				- The device can keep the pad notes from passing through to the MicroFreak.
				- Max's `pgmout` counts programs from 1 unless its `zerobased` attribute is on ([pgmout](https://docs.cycling74.com/reference/pgmout/)). The device must send program `(N − 1) % 128` counted from 0.
				- [[Launchpad/Custom/1/Ableton-Ctrl]] also sends on channel 16. Its CCs arrive at this track too, and the device should drop them.
				- Two devices on different tracks can pass colour messages with Max's `send` and `receive`. The limitations page rules that out for audio and says nothing about messages.
				- `create_midi_clip` works on an unarmed track while Arrangement Record is on and the Arrangement plays, and how late the clip lands after the press. The Track page gives no Live version for the function; Producer Pal already creates Arrangement clips in your Live 12.
				- Whether a Max for Live device can send SysEx. With it, the device could send Select Layout after Enter and put the Launchpad back on the sequencer ([[Launchpad/PRG/03 MIDI/03 Selecting Layouts]]).
			- ### On the Launchpad
				- Which channel lights a Custom Mode pad that sends on channel 16. The programmer's reference names channels 1 to 3 for lighting ([Launchpad Pro MK3 Programmer's Reference](https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/downloads/LPP3_prog_ref_guide_200415.pdf)) and does not say whether the pad's own channel matters.
				- Whether colours sent from Live stay after you leave the Custom Mode and come back. If the Launchpad redraws the colours from Components, the device re-sends all 64 on the next press.
				- Whether Components accepts 64 Midi Note pads numbered 11 to 88 on channel 16, and whether factory Custom Mode 8 can be copied as a start.
			- ### On the MicroFreak
				- How soon after a Program Change a note plays the new sound. An Ableton forum thread reports the first note after a Program Change coming out silent or wrong on a MicroFreak ([Program Change Problem // First Note Weird/Off](https://forum.ableton.com/viewtopic.php?p=1804422)).
				- What a preset change does while the Launchpad's sequencer is playing the MicroFreak: whether held notes cut off and whether the next step sounds.
				- Whether the MicroFreak keeps the last bank select. The device sends the bank every time, so this matters only if Program Change pads stay in a Custom Mode beside it.
		- ## What I couldn't verify
			- Everything under Check before building. I read documentation and garden pages and tried nothing.
			- Whether 12 category colours read apart on the pads. The palette has 128 entries and I have not seen them on the hardware.
			- Whether Live's [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects/03 MIDI Monitor]] shows Program Change. The manual lists notes, pitch bend and aftertouch.
			- Whether the `presets` clips survive Live's own recording on other tracks without side effects, such as a new take lane.
		- ## Next steps
			- TODO Try the number pad with the lights and the record left out. In Components, make a Custom Mode for slot 3 with twelve Midi Note pads on channel 16, laid out as in the sketch: digits 0 to 9 as notes 60 to 69, Clear as 70, Enter as 71. In Live, add a Max MIDI Effect to `LPP CM2 to MF` that reads those notes, collects digits, and on Enter sends CC 0 and Program Change. Press 2 5 9 Enter and look for 259 Infini Pad on the MicroFreak, then 1 5 1 Enter for 151 The Unstable, which is in another bank.
			- TODO Add `MF picker lights` with MIDI To the Launchpad. Send one note from a clip on it and see which channel lights a pad of the new Custom Mode, and whether the colour stays after switching to the sequencer and back.
			- TODO With Arrangement Record on, have the device create and name a clip on an unarmed `presets` track, and check where the clip lands against the moment of the press.
			- TODO Time the MicroFreak: send a preset, then a note after 10, 50, 100 and 250 ms, and listen for the first delay at which the new sound plays whole.
			- TODO Write a mise task that builds the device's preset table from the `Microfreak/Preset/*` pages and the GitP session pages.
			- TODO Extend `ableton:set:import` to read the `presets` clips onto the session's Set pages, beside the `notes` clips from [[Ableton/Live/Idea/Keep-Commentary-in-Live-Sets]].
	- [[AI/Response]] [[2026-11-26 Thu]]
		- ### Prototype
			- #### Custom Mode 3
				- Custom Mode 3 on the Launchpad now holds [[Launchpad/Custom/3/MF-Number-Pad]], also saved under My Custom Modes in [[Novation/Components]]. Reading slot 3 back from the Launchpad in Components showed the same twelve pads, notes, channel and colours.
				- It replaced `71-78VertFadeCh2`, a mode of eight vertical faders that is still saved under My Custom Modes. Custom Modes 1 and 2 are unchanged.
				- The pads sit in rows 3 to 6 and columns 3 to 5, counted from the top left. Each one is a Momentary Midi Note on channel 16:
				  ~~~
				  pad          note
				  7  8  9      67 68 69
				  4  5  6      64 65 66
				  1  2  3      61 62 63
				  C  0  E      70 60 71
				  ~~~
				- Digits are white, Clear (C) is red and Enter (E) is green. A pad turns yellow while held.
				- Custom Modes 1 and 2 send only CCs and Program Changes on channel 16, so notes 60 to 71 on that channel come from Custom Mode 3 alone.
			- #### The device
				- [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live/Asset/Device/MF-Number-Pad/amxd]] is a Max MIDI Effect named MF Number Pad. A copy sits in Live's User Library at `Presets/MIDI Effects/Max MIDI Effect/MF Number Pad.amxd`. [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live/Asset/Device/MF-Number-Pad/maxpat]] holds its patcher as JSON.
				- Each digit pressed is added to the end of the slot number, up to three digits. A fourth digit is ignored. 0 1 6 and 1 6 both mean slot 16, so [[Microfreak/Preset/016 Voidom]] can be typed as its page name writes it.
				- Clear empties the number.
				- Enter with a number from 1 to 512 sends CC 0 = `(N − 1) // 128`, then Program Change `(N − 1) % 128`, on MIDI channel 1, and empties the number. For 259 that is CC 0 = 2 and program 2. Enter with nothing typed, with 0, or with a number above 512 only empties it.
				- The device keeps every note-on, note-off and poly aftertouch message out of its output, so pad presses never play the MicroFreak. All other MIDI passes through unchanged, including the bank and Program Change pads of Custom Mode 2.
				- The device shows `Slot:` with the number typed so far and `Sent:` with the last slot it sent.
				- The device reads notes 60 to 71 on any channel. The Max for Live guide says MIDI Effects receive on channel 1 by convention ([Creating MIDI Effects](https://docs.cycling74.com/userguide/m4l/live_midieffects/)), so the track's MIDI From does the channel filtering.
				- The logic is JavaScript in a `v8.codebox` between `midiin` and `midiout`. Open the device in Max to edit it. `v8.codebox` needs Max 9, and Live 12.4 bundles Max 9.1.
				- Checked without Max or Live: the patcher JSON parses, and the length in the `.amxd` header matches the JSON after it. The JavaScript, run in Node with Max's `outlet` stubbed, sent the right bank and program for slots 1, 128, 129, 151, 259 and 512, sent nothing for 0 and 513, kept notes back, and passed CCs, Program Changes, pitch bend, SysEx and clock.
			- #### Set up Live
				- 1. On a MIDI track, `LPP CM2 to MF` if the Set has it or a new one, set MIDI From to `Launchpad Pro MK3 (LPProMK3 MIDI)` and `Ch. 16`, Monitor to `In`, and MIDI To to `Arturia MicroFreak (unknown mididevice)` and `Ch. 1`.
				- 2. Drag MF Number Pad from the browser's User Library, under Presets › MIDI Effects › Max MIDI Effect, onto that track.
			- #### Test
				- 1. On the Launchpad, press Custom, then the third button of the bottom row, to open Custom Mode 3.
				- 2. Press 2 5 9 Enter. The device should show `Sent: 259`, and the MicroFreak should show [[Microfreak/Preset/259 Infini Pad]].
				- 3. Press 1 5 1 Enter. The MicroFreak should show [[Microfreak/Preset/151 The Unstable]], which is in bank 1.
				- 4. Hold a digit pad down and press it hard. The MicroFreak should stay silent and keep its sound.
			- #### Result
				- [[2026-11-27 Fri]] It worked. In Custom Mode 3, codekiln pressed 2 5 9 and green Enter; the device showed `Sent: 259`, and the MicroFreak switched to [[Microfreak/Preset/259 Infini Pad]].
				- So Live loads the `.amxd`, and CC 0 and Program Change from the device reach the MicroFreak through the track's MIDI To. Still untried: 1 5 1 Enter for a preset in another bank, and the hard-press check for leaking notes and aftertouch.
			- #### Not yet tried
				- Whether Live loads the `.amxd`. Its header follows Live's own `Max MIDI Effect.amxd` template, but nothing here ran in Max or Live. If Live refuses it, opening the `.maxpat` in Max shows the error in the Max Console.
				- Whether CC 0 and Program Change sent by a Max for Live device reach the MicroFreak through the track's MIDI To. If the device shows `Sent: 259` and the MicroFreak keeps its preset, the messages stopped between the device and the MicroFreak.
				- Whether the swallowed notes leak. With the device switched off, Live could pass the pad notes straight to the MicroFreak. Hard presses may also send aftertouch: the device keeps poly aftertouch back and passes channel aftertouch, which the MicroFreak may treat as pressure. The held pad in the test checks both.
