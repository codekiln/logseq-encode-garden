icmc25-id:: 374
cgpt-link:: https://chatgpt.com/g/g-p-6845c013a1dc8191953259251f424f3c-icmc25/c/684d8503-6784-800a-a793-fd4c47fc54cd

- # G.L.I.D.E.: Correlating Real-Time Multi-Sensor Data to Figure Skating Movement Patterns as an Interface for Musical Expression
	- ## [[AI Notes]]
		- ### 10:10 — G.L.I.D.E. real-time figure skating data as musical interface
			- Alyssa Aska, Martin Ritter, and Jeffrey Boyd presented a full paper on the G.L.I.D.E. project, which uses figure skating as a new interface for musical expression.
			- The system uses an M5StickC Plus2 device embedded in a skater’s boot to collect real-time movement data. This data is synchronized with video and transformed into musical parameters and audio processing routines.
			- The result is a series of audiovisual works that explore artistic documentation, gesture-music mapping, and movement-derived sonic expression.
			- The project builds on prior tools for speed skater tracking but extends them toward aesthetic applications. Emphasis is placed on gesture-musicality, not just movement capture.
			- The skating gestures—variations in speed, direction, and axes—are used to structure musical materials dynamically, with the authors arguing that figure skating is inherently musical and suitable as a gestural performance interface.
			- This fusion of data capture, movement, and music offers a novel lens into embodied musicality, positioning skating not just as a metaphor but a literal tool for musical creation.
		- ### 🎿 G.L.I.D.E. Max Patch Breakdown
			- **1. Real-Time Movement Data Plot (Top):**
			- 6 colored waveform plots represent sensor data, likely from the M5StickC Plus2.
			- Data dimensions could include acceleration, gyroscope, and magnetometer values along x, y, z axes.
			- Time series plot syncs movement data to musical or video frames.
			  
			  **2. Video + Data Alignment (Bottom Left):**
			- Embedded video shows Alyssa Aska executing a skating maneuver.
			- This is synchronized with the sensor data to allow precise gesture-to-sound mapping and analysis.
			  
			  **3. Alignment + Playback Controls (Center):**
			- File: `Alyssa_07_01_25_data02`
			- Adjustable frame offset (`frame diff`, `cur data frame`, `cur vid frame`) indicates the calibration step for temporal alignment between motion and sound/video.
			- Controls to reset, loop, scrub through frames.
			  
			  **4. Speed and Positional Data (Bottom):**
			- Scalar values likely represent sensor-derived parameters (e.g. acceleration magnitude, angular velocity, orientation quaternions or Euler angles).
			- These can be directly mapped to musical parameters: pitch, timbre, density, spatialization, etc.
			  
			  **5. Context of Use:**
			- This system was developed to explore the *gesture-to-sound* mapping in the context of artistic performance, where skating becomes a dynamic gestural interface for sound synthesis and composition.
			- Rather than simply tracking motion, this interface enables the *translation* of those motions into expressive sonic outcomes — a core premise of the G.L.I.D.E. research and performance project.
		- ### 🩰 Blade-Amplitude Visual Sonification (Speculative Breakdown)
			- #### 🖼️ Visual Structure:
				- **Left panel**: thresholded black-and-white / edge-detected feed — possibly from `jit.rota` + `jit.rgb2luma` + `jit.op @op >` → then passed through `jit.convolve` or a `sobel` kernel.
				- **Center panel**: magenta color wash — probably driven by **blade amplitude tracking** (see below) applied as a video layer, maybe using `jit.gl.slab` or `jit.gl.pix`.
				- **Right panel**: filtered / quantized grayscale video — may be a delayed or alternate camera angle; preserves movement for spatial context.
			- #### 🎧 Blade Sound Amplitude Tracking:
				- Likely involves:
					- **Contact mic or shotgun mic** mounted near the rink surface or skater’s boot.
					- A **bandpass filter** centered around frequencies produced by skate-ice contact (e.g., friction sibilance, scraping, or blade taps).
					- Real-time RMS tracking via `average~`, `snapshot~`, or `loudness~` (or `sigmund~` for better onset extraction).
					- Output mapped to:
						- Video alpha modulation (fade-in on blade hits).
						- Color saturation / brightness shifts in the central panel.
						- Audio control (e.g. triggering grain envelopes, convolution reverb responses, etc.).
			- #### 🔁 Artistic Logic:
				- As the **skater carves, scrapes, or pivots**, the **amplitude of the blade interaction** feeds into:
					- Smoother or harsher visuals.
					- Dynamic reverb tails or spectral filtering.
					- Compositional structures reflecting *gesture density* or *contact force*.
	- ## #Author
		- [[Person/Alyssa Aska]]
			- ![Alyssa Aska](https://icmc2025.sites.northeastern.edu/files/2025/05/IMG_0346-221x300.jpg)
			- **Alyssa Aska** is fascinated with the architecture of music, both spatially and temporally. She composes works which explore extremes in time and space, using rigid proportions to generate forms in acoustic works and exploring the unpredictable duration and lack of control in gamified works. This is closely tied to her compositional style, which is concerned with a delicate balance between elements of functional form and elements of pure aesthetic purpose. As much structure as possible, as many ornaments as necessary (and vice versa). She believes in a careful balance between craft and emotion in her music. Her passions include the ==study of ancient cultures and Stargate SG-1, both of which have influenced her life path and compositional aesthetic==.
			- https://www.youtube.com/@AlyssaAska
		- [[Person/Martin Ritter]]
			- #Pic
				- ![Martin Ritter](https://icmc2025.sites.northeastern.edu/files/2025/05/Martin-Ritter_BW_accented-221x300.jpg)
			- #Bio
				- **Martin Ritter** studied composition in Canada and currently lives in Graz, Austria. He writes both electronic as well as instrumental works and is performed across Europe, North America, and Asia. As a composer he is interested in the spaces sounds emerge in/from and the intersection of music, technology, and performance/performance practice. In recent years he has started to explore microtonality as a conceptual space for his work. As a researcher he works with digital tools in order to analyze and understand electronic music. His music and research are featured regularly at conferences and festivals such as Wien Modern, MikroFest Helsinki, ICMC, NIME, EMS, Audio Mostly, eContact!, Impuls, Darmstadt, ComposIt, MusCan, TENOR, Ars Electronica. He has received scholarships like the Joseph-Armand Bombardier Canada Graduate Scholarship, the University of Calgary Technologies International Inc. Fellowship Scholarship, Alberta Innovates – Technologies Futures Scholarship, the Joseph and Melitta KANDLER Scholarship for Advanced Music Study. He founded, co-founded, or is on the board of several arts organizations such as Zeitschleife, Die Andere Saite, OEGZM, Graz Orchestra of Noise and Distortion.
				  He currently works at the University of music and performing arts Vienna as a senior scientist.
		- [[Person/Jeffrey E. Boyd]]
			- #Pic
				- ![Jeffrey E. Boyd](https://icmc2025.sites.northeastern.edu/files/2025/06/Jeffrey-Edwin-Boyd-221x300.jpg)
			- #Bio
				- **Jeffrey E. Boyd** received the Ph.D. degree in computer science from the University of British Columbia, BC, Canada, in 1994.,He is currently an Associate Professor and the Associate Head with the Department of Computer Science, University of Calgary, Calgary, Canada. He was with the Visual Computing Laboratory, University of California, San Diego, USA, and the Department of Computer Science, University of British Columbia, BC, Canada
	- ## #Description
		- Motion tracking and movement capture are effective tools for creating new interfaces for musical expression. Tracking systems can encompass everything from computer vision to physical gestural control. The authors have developed a system for tracking the movement of a figure skater in real time using an M5StickC Plus2 laced into a skater’s boot. The authors conducted experiments with this setup by recording skater movement data along with corresponding video. This data was then played back and applied to musical parameters and audio processes to create several works the authors describe as artistic documentation, or documentation modified for aesthetic purposes to become a standalone artistic work. A previously developed tool for tracking speed skaters was enhanced and combined with artistic research into gestural controllers for musical expression. Figure skating is already closely linked with music and with a framework that favours musicality and intimately connects gesture with music. Additionally, many of the movements within figure skating contain variations in direction, speed, and movements on various axes. For this reason, we decided to explore the potential of figure skating as not just a tool of embodying music through movement, but also as using movement as an extension of musical expression. Figure skating offers a compelling and novel way to explore the connection of physical movement with music and sound.