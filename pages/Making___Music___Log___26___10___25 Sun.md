prev:: [[Making/Music/Log/26/10/24-Sat]]

- # [[2026-10-25 Sun]]
	- ## [[Ghost Gardener]] requests
		- ((6addc678-7052-4e91-a8af-b4e3f6d99542))
		- ### DONE project - create UI entity types
			- DONE import person entity and also [[UX/Design/Atomic/L1 - Atom]] and other levels from this brief chatgpt transcript
			  collapsed:: true
				- You're remembering Atomic Design, a methodology introduced by UX designer Brad Frost in 2013.
				  
				  It describes a hierarchy of five levels for organizing user interface components, from the simplest building blocks to complete interfaces.
				- ## The  five  official  levels
				  
				  Atoms
				  
				  1
				  
				  Molecules
				  
				  2
				  
				  Organisms
				  
				  3
				  
				  Templates
				  
				  4
				  
				  Pages
				  
				  5
				  
				  | Level | Definition | Example |
				  | 1. Atoms | Indivisible UI building blocks | Button, label, input |
				  | 2. Molecules | Simple combinations of atoms | Search field with button |
				  | 3. Organisms | Complex, self-contained interface sections | Navigation header |
				  | 4. Templates | Page layouts establishing content structure | Dashboard layout |
				  | 5. Pages | Templates populated with real content | Actual user dashboard |
				  
				  ![What Led us to Consider Polaris, Shopify’s Design System - Shopify](https://images.openai.com/static-rsc-4/fsfMdpE5xi9kwVkjjFxOs3e2wzjMNss3LOAOtUH9o6_Tqr1t9Vo1_eTAqVL8LPTUE_HjI_eVaf0hrLAcsCsJ8HjPQipRfATy-Vi-tqROOY4ZjBHsNLEyD3I-ue-yhljDO1Prl1FOiA7RBgCAoagEAgpGYoEgR3V6tjLbkgiMg4o?purpose=inline)
				  
				  [shopify.com](https://www.shopify.com/partners/blog/design-system?utm_source=chatgpt.com)
				- ## Original  sources
				- [Atomic Design — Brad Frost (2013)](https://bradfrost.com/blog/post/atomic-web-design/?utm_source=chatgpt.com) — The original blog post introducing the methodology.
				- [Atomic Design Methodology — Chapter 2](https://atomicdesign.bradfrost.com/chapter-2/?utm_source=chatgpt.com) — The authoritative, detailed explanation from Frost's book Atomic Design.
				  
				  One subtle distinction: "Elements" isn't an official level. Frost uses elements as a generic term for interface building blocks, particularly atoms.
				  
				  Frost also emphasizes that Atomic Design isn't a mandatory bottom-up development process. It's a mental model for thinking about interfaces simultaneously as complete systems and as compositions of reusable parts.
				  
				  The terminology remains useful for component libraries and design systems, including those implemented with React, Storybook, and Figma. 
				  
				  ![](https://www.google.com/s2/favicons?domain=https://atomicdesign.bradfrost.com&sz=32)
				  
				  Atomic Design by Brad Frost
				  
				  +2
			- DONE inspired by that create a [[Logseq/Entity/Definition]] or two that would let us to have a consistent ability to map out hierarchies of UI elements into pages of logseq, structurally inspired by [[Logseq/Entity/Book/Section]]  but defined for a different purpose. I'm thinking that we would let us map out the UI the [[Microfreak]], the [[Launchpad]] and [[Ableton/Live]], so at any point we can have autocompleted in Logseq any part of these and reference them.
				- For example, I already have referenced [[Microfreak/UI/Oscillator/Knob/Timbre]] would model the UI that points to or corresponds to [[Microfreak/UG/06 Dig Osc/01 as Soundgen]]
			- DONE please create a page in the garden for each parameter of each oscillator. For example, in ((6add3dae-8dc8-4156-a5ea-23f7290d9173)) I would like these to be hyperlinks to logseq pages.
			- DONE create a plan for how to model all the types of midi mapping encoders in midi devices - they shouldn't be overfit on Midi though. Maybe  for example,
				- buttons
					- toggle buttons
					- multi-value toggle buttons
						- similar to the [[Microfreak/UG]]
					- buttons that fire an event but aren't toggled
				- continuous rotary encoders
					- rotary encoders that encode nonnegative real numbers beneath a max integer such as 127
					- bidirectional rotary encoders that are centered at zero and can go negative down to some minimum integer such as -1 and go up to some positive integer such as 1
					- rotary button encoders - a rotary encoder combined
				- discrete rotary encoders
				- faders
				- etc
			- DOING drawing from [[Microfreak/UG/03 Overview/01 Front Panel]],  
			  id:: 6addc861-d67d-4a8d-857c-2567919824ed
			   create [[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]], [[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]], [[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]], [[Microfreak/UI/Front/Row/Top/02 Paraphonic Button/Hold]], [[Microfreak/UI/Front/Row/Top/02 Paraphonic Button/Hold/Shift]] [[Microfreak/UI/Front/Row/Top/03 Panel Button]], [[Microfreak/UI/Front/Row/Top/04 OLED]], [[Microfreak/UI/Front/Row/Top/05 Preset Knob]], [[Microfreak/UI/Front/Row/Top/04 OLED]], [[Microfreak/UI/Front/Row/Top/06 Save Button/Hold]], etc and other sections of the UI, so every button and knob is appropriately modeled in the garden
			-
	- ## [[My Notes]]
		- listened through [[GitP/A/Session/26/10/24-Sat]]
		-
-