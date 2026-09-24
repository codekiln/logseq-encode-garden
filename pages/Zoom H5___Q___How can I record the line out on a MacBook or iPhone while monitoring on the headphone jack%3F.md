logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Audio/Connector/Q/What is the difference between a line out port and a headphone port, and how do they differ on the Zoom H5?]], [[Audio/Connector/RCA/Stereo]]

- # How can I record [[Zoom H5/Port/Line Out]] on a [[Macbook]] or an [[iPhone]] while monitoring on [[Zoom H5/Port/Headphone]], with the USB port already given to [[Zoom H5/Mode/Audio Interface/iPad]]?
	- ## [[AI Answer]]
		- **Short answer:** the recorder side already works — both output jacks are live at once and their levels are set independently, so the H5 can feed a second device while the headphones stay under their own control. The obstacle sits entirely on the receiving end. Neither a MacBook's 3.5 mm jack nor a Lightning port will take a stereo line-level signal; both offer a **mono, mic-level** input and nothing else. Stereo therefore costs one small USB device — but it can be a 65 g dongle rather than a second interface in the [[Focusrite/Saffire]] sense.
		- ### What the H5 already does for free
			- [[Zoom H5/Port/Line Out]] and [[Zoom H5/Port/Headphone]] are separate jacks with separate level controls, and the `LINE OUT LEVEL` setting does not touch the headphone jack. The send and the monitoring never fight each other — see [[Audio/Connector/Q/What is the difference between a line out port and a headphone port, and how do they differ on the Zoom H5?]].
			- Turn **direct monitoring** on in the audio interface settings. [[Answer/Official]] from the [H5 Operation Manual](https://www.zoom.co.jp/sites/default/files/products/downloads/pdfs/E_H5_0.pdf): it routes "sound that is input to the H5 before it passes through the connected computer or iPad," so the analog outputs carry the inputs without a round trip through the iPad and its latency.
			- The SD card is not a way out of this. In USB audio interface mode the H5 will not record to its own card, so a second capture has to land on some other device.
		- ### Why each destination behaves the way it does
			- | Destination                | What it will accept                            | Channels | Verdict                                          |
			  | -------------------------- | ---------------------------------------------- | -------- | ------------------------------------------------ |
			  | [[Macbook/Port/Headphone]] | headset mic level on the TRRS sleeve           | mono     | a scratch or reference track, nothing more       |
			  | [[iPhone/Port/Lightning]]  | no analog at all; the Apple adapter's mic pin  | mono     | same ceiling, with an adapter added to the chain |
			  | [[Macbook/Port/USB/C]]     | whatever a class-compliant USB device presents | stereo   | the only stereo path, and it needs a USB device  |
			- No Mac has ever had a stereo analog **input** on the 3.5 mm jack. The jack follows CTIA wiring on an [[Audio/Connector/Phone/TRRS/3.5mm]] plug — tip left, first ring right, second ring ground, **sleeve microphone**. One conductor for input means one channel.
			- macOS also has to see four conductors before it switches the jack into headset mode. A three-conductor [[Audio/Connector/Phone/TRS/3.5mm]] plug reads as headphones, and no input device appears in **Sound**.
			- Lightning is a digital connector; the conversion happens inside Apple's Lightning to 3.5 mm Headphone Jack Adapter, which does pass a headset microphone and is likewise mono.
		- ### The mono path, when a reference track is enough
			- Chain: `LINE OUT` → a 3.5 mm TRS-to-TRRS adapter → the Mac jack, or the Apple Lightning adapter on the phone.
			- Set `LINE OUT LEVEL` near −30 dB. That drops the H5's +1 dBu maximum to roughly −29 dBu, about −31 dBV, which is inside what a headset mic input expects — the recorder does its own padding and no attenuator cable is needed in the line.
			- Watch which channel arrives. A plain mic-style TRS-to-TRRS adapter ties the plug's tip to the mic pin and leaves the ring unconnected, so only the **left** channel is recorded. A cable that sums stereo to the mic pin, sold for feeding phones from a mixer, keeps both.
		- ### The stereo path, and how small it gets
			- | Device                     | Line input | Size and weight         | Host cables                                                                       |
			  | -------------------------- | ---------- | ----------------------- | --------------------------------------------------------------------------------- |
			  | IK Multimedia iRig Stream  | stereo RCA | 105 × 44 × 24 mm, 65 g  | USB-C, Lightning and USB-A, all in the box                                        |
			  | Behringer U-CONTROL UCA202 | stereo RCA | 88 × 60 × 22 mm, ~100 g | captive USB-A tail; needs an adapter for USB-C and a Camera Adapter for Lightning |
			- Either one wants a 3.5 mm TRS to dual-[[Audio/Connector/RCA]] cable off `LINE OUT`, which is the ordinary [[Audio/Connector/RCA/Stereo]] pair.
			- The iRig Stream is the better fit for a one-backpack rig: the Lightning and USB-C cables ship with it, so a single dongle covers the phone and the laptop, and it is bus-powered. Specs are from [IK Multimedia](https://www.ikmultimedia.com/products/irigstream/) and [Behringer](https://www.behringer.com/product.html?modelCode=0805-AAC), read September 2026.
			- The honest trade: this is a second audio interface. There is no passive adapter that turns a stereo analog signal into something a USB-C or Lightning port will record, because both ports are digital and the analog-to-digital conversion has to happen somewhere. The question is only how much the converter weighs, and 65 g is about as light as stereo line input gets.
		- ### Cautions once two hosts share the rig
			- Two mains-or-bus-powered devices joined by an unbalanced analog cable invite a ground loop. If hum appears, an isolating transformer in the RCA run is the usual cure.
			- The iPad recording and the second recording run on independent clocks, so long simultaneous takes drift against each other and need a clap or another sync point to line up afterwards.
			- Set `LINE OUT LEVEL` back to 0 dB when feeding a real line input; the −30 dB pad is only for mic-level destinations.
		- ### Scope of this answer
			- H5 behaviour is from the operation manual. The Mac and iPhone input limits follow from CTIA headset wiring and Apple's adapter design rather than from any single Apple document. Dimensions and weights are manufacturer figures read September 2026; the chains above are worked out from those specifications rather than measured.
