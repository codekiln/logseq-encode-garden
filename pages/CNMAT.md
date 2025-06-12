tags:: [[Diataxis/Explanation]]

- # CNMAT Conceptual Overview
	- ## Overview
		- CNMAT (Center for New Music and Audio Technologies) is a multidisciplinary research center at [[Uni/California/Berkeley]] focused on the intersection of music, technology, and performance.
	- ## Context
		- As a pioneering institution, CNMAT addresses the evolving needs of composers, performers, and technologists by developing innovative tools and frameworks that enable new forms of musical expression and real-time interaction.
	- ## Key Principles
		- *Interdisciplinary integration* – combining music, computer science, engineering, and acoustics.
		- *Real-time performance* – emphasizing low-latency, expressive musical control.
		- *Open tools and standards* – building reusable, extensible systems for the global community.
	- ## Mechanism
		- CNMAT develops software and hardware that bridge the gap between artistic intention and technological execution. Key systems include:
			- **CNMAT externals for Max/MSP** – a suite of audio and data processing objects emphasizing time-tagged messaging and OSC (Open Sound Control).
			- **OSC (Open Sound Control)** – co-developed at CNMAT, this protocol enables high-resolution, symbolic control of musical parameters across networks.
			- **o.dot tools** – an approach to structured time-based media manipulation using Max/MSP.
			- **Max JavaScript extensions** – CNMAT enhances Max with scripting capabilities via JS for interactive systems.
	- ## Examples
		- ~~~javascript
		  // CNMAT JavaScript example in Max
		  var osc = require("osc");
		  var udpPort = new osc.UDPPort({
		      localAddress: "127.0.0.1",
		      localPort: 57121
		  });
		  udpPort.open();
		  ~~~
		- ~~~max
		  // Max patch using CNMAT's [o.route] for OSC message routing
		  [udpreceive 57121]
		  |
		  [o.route /synth/frequency /synth/amplitude]
		  ~~~
	- ## Misconceptions
		- CNMAT is only for academic research → CNMAT tools are widely used by practicing musicians and performers globally.
		- OSC is just another MIDI replacement → OSC is much more flexible, supporting symbolic addressing, bundling, and high-resolution parameters.