icmc25-id:: 326
cgpt-link:: https://chatgpt.com/g/g-p-6845c013a1dc8191953259251f424f3c-icmc25/c/684d7cdc-0e20-800a-8562-1a925f6ea620

- # bellplay A Symbolic Framework for Offline Algorithmic Audio - used for [[ICMC/25/Installation/Screening/06 ludus vocalis]]
	- ## Notes
		- ### [[My Notes]]
			- 09:47 oh! this was the person who did [[ICMC/25/Installation/Screening/06 ludus vocalis]] and this technology was actually done with this
			- 09:50 I love that we can use an external editor, [[VSCode]].
		- ## [[AI Notes]]
			- ### 09:40 — bellplay~ motivations and outcomes
				- **Motivations**
					- Emphasis on affordances of non-linear/offline workflows such as multi-passing, lookaheads, and backtracking.
					- Builds on experience with computer-assisted algorithmic composition tools like OpenMusic and bach.
						- Investigates symbolic vs. audio domain discontinuities (e.g., acoustic vs. electronic music).
					- Draws from related work integrating symbolic music and algorithmic audio:
						- **Real-time audio**: _CataRT_ and its variants (Einbond, Trapani, Agostini, Ghisi, Schwarz).
						- **Offline tools**: _AudioGuide_ (Hackbarth, Schnell, Esling, Schwarz) and _Orchidea_ (Cella).
				- **Outcomes**
					- Creation of **bellplay~**: an offline algorithmic audio framework in the Bell programming language.
					- Case study in **«ludus vocalis»**: a multimedia work using bellplay~ for algorithmic audio control and data automation in TouchDesigner.
			- ### 09:40 — Felipe Tovar-Henao context and bellplay~ paper
				- Felipe Tovar-Henao is a Colombian multimedia artist, developer, and researcher with a focus on human-AI creative partnerships, generative algorithms, and immersive art.
				- His ICMC short paper presentation titled **“bellplay~: A Symbolic Framework for Offline Algorithmic Audio”** introduces:
					- bellplay~ as a new audio framework enabling offline algorithmic audio rendering.
					- Application to a 25-minute multimedia work titled **ludus vocalis** (8.1-channel audio + 4K video).
					- Integration of bellplay~ with TouchDesigner for automated visual parameter control.
					- Description of bellplay~'s software architecture, scripting language, and its pedagogical potential.
			- ### 09:45 — bellplay~ syntax, workflow, and developer tools
				- **Workflow Summary (Three Steps)**:
				  1. **Generation**: Create audio buffers (e.g. `cycle`, `importaudio`).
				  2. **Transcription**: Queue buffers using `transcribe(...)` with `@onset` control.
				  3. **Rendering**: Execute with `render()` — can be repeated as needed.
				- **Examples**:
					- Generate a sine tone and transcribe:
					  ```bell
					  $buffer = cycle(@frequency 440 @duration 1000);
					  transcribe(@buffer $buffer @onset 0);
					  render();
					  ```
					- Process audio with sequential effects:
					  ```bell
					  $buffer = importaudio('poem.wav');
					  $cmds = onepole() overdrive() freeverb();
					  $buffer = process($buffer, $cmds);
					  ```
					- Analyze audio features in parallel:
					  ```bell
					  $buffer = importaudio('poem.wav');
					  $descr = onsets() spectralcentroid();
					  $buffer = analyze($buffer, $descr);
					  $onsets = getkey($buffer, 'onsets');
					  $centroid = getkey($buffer, 'spectralcentroid');
					  ```
				- **Audio Feature Modes**:
					- Sequential: filtering, distortion, reverb.
					- Parallel: onset detection, spectral centroid analysis.
				- ** [[VSCode]] Ecosystem**:
					- `bell syntax`: adds syntax highlighting, autocompletion, and inline doc hints.
					- `bellplay~ plugin`: extends for bellplay-specific dev flow:
						- Run scripts directly from VS Code.
						- Mirror bellplay~ console output.
						- Show contextual help for bellplay-specific functions.
				- **Screenshot shows**:
					- `demo.bell` script running via `bellplay~ listener` inside VSCode.
					- Console output of evaluated code (e.g., `bach.eval • hello world`).
			- ### 09:50 — bellplay~ pedagogical context and teaching resources
				- **University-level adoption**: bellplay~ is integrated into a course on *Computer-Assisted Algorithmic Composition (CAAC)*.
				- **Supports dual paradigms**:
					- Symbolic composition
					- Audio-based algorithmic sound generation
				- **Supplementary resources**:
					- 📘 Online tutorials: [https://felipe-tovar-henao.com/bell-tutorials/](https://felipe-tovar-henao.com/bell-tutorials/)
					- 🧩 Algorithmic music puzzles for practice: [https://felipe-tovar-henao.com/replay/](https://felipe-tovar-henao.com/replay/)
	- ## #Author [[Person/Felipe Tovar-Henao]]
		- **Felipe Tovar-Henao** is a Colombian multimedia artist, developer, and researcher whose work explores computer algorithms as expressive tools for human and post-human creativity, cognition, and pedagogy. His work spans digital instrument design, software development, immersive art installations, generative algorithms, machine learning, music information retrieval, and human-computer interaction. His music is often rooted in transformative experiences with technology, philosophy, and cinema, focusing on perception, memory, and recognition.
		  He has been featured at international festivals and conferences including TIME:SPANS, ICMC, the Mizzou International Composers Festival, Ravinia Festival, NYCEMF, WOCMAT, CAMPGround, SEAMUS, SICMF, and IRCAM’s ManiFeste Academy. He has received awards such as the SCI/ASCAP Student Commission Award and ASCAP Foundation Morton Gould Young Composer Award.
		  His music has been performed by ensembles and artists including Alarm Will Sound, the Grossman Ensemble, Quatuor Diotima, Sound Icon, and the Orquesta Sinfónica EAFIT. He has held academic positions at University of Cincinnati, Universidad EAFIT, University of Chicago, and Indiana University, and is currently Assistant Professor of AI and Composition at the University of Florida.
	- ## #Description
		- In this article, I introduce bellplay~, an offline algorithmic audio framework and software initially developed for the realization of a 25-minute multimedia work for 8.1-channel audio and 4K video, titled ludus vocalis. bellplay~ played an exclusive role in producing the audio elements of ludus vocalis and in generating control data for automating various visual parameters in TouchDesigner. The paper begins with a brief overview of the context and motivation behind bellplay~, followed by a description of its software architecture, scripting language, and key features. I then discuss its application in ludus vocalis and conclude by reflecting on its potential as a pedagogical tool in a university course on computer-assisted algorithmic composition.