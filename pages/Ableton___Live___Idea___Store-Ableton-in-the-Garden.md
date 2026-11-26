tags:: [[Idea]]
date-created:: [[2026-11-26 Thu]]
see-also:: [[Ableton/Live/Idea/Keep Live Projects as DVC Assets]], [[Ableton/Live/Idea/Declare a Live Set in Logseq]]

- # Store Ableton in the Garden
	- [[My Note]]
		- ## Why move Ableton files
			- I would like to experiment with how best to start storing Ableton in Logseq. I think this is actually probably an idea entity.
			- Lately, Claude has been having some issues because I normally store my Ghost in the Patch Ableton sessions inside of a folder inside of my Mac Documents folder. I don't really want to grant Claude access to all my documents, but I do want to have Claude work on my Ableton files.
			- So I've been thinking about how I think I want to start storing my Ableton assets in logseq-encode-garden. I think this is going to require some kind of preparation in order to figure out how best to do this.
		- ## A dedicated repository or the garden
			- I had a Claude session yesterday or the day before where I was trying to figure out what to do about this, and we were on the fence about whether to make a dedicated repository for Ableton things or whether to try to make a way to put them inside of Logseq.
			- I can see advantages to both approaches. If I do it in Logseq, then that just makes my Logseq setup more powerful.
		- ## Sets as XML
			- ### Smudge filters
				- I'm thinking that if I make my own repository of music making things, then I'll probably try doing Git smudge filters again so that I'm actually storing the XML and then zipping it. I prototyped this in some repositories a while back. Never quite got it working, but maybe now's the time.
				- It would be nice if I could get that working in logseq-encode-garden.
				- Ideally it's XML under the hood, so ideally I would store it as the text of the XML, but then be able to use it as binary.
			- ### The published website
				- If I did that, I'm not totally certain how it would relate to the published version of the website.
				- I do have control over the rendering of the Logseq engine using Logseq Gardener, and it would be great if I could continue my custom Ableton set rendering so that it could render sets that are stored.
		- ## Traits for Sets
			- I also want a way to define something kind of like a Python protocol or a Scala trait, or maybe a Rust trait, for Ableton sets.
			- For example, by default, I want my custom Arrangement View Novation Launchpad Mini CC numbers to control the transport in Ableton. I also want certain keyboard shortcuts set up for being able to control locators, that kind of thing.
			- These traits should be able to be stored as expectations somewhere in Logseq and then applied to set templates. That way I could have more than one set template that adheres to the same set of expectations.
		- ## Large files
			- ### WAV files behind a login
				- There's another wrinkle: I don't really want to make large files public by default. Part of me thinks I should, and then just deal with it when it's a problem.
				- Earlier, with the agent I was working with the other day about where to store Ableton assets like WAV files, I was exploring the idea of maybe storing them in logseq-garden. But then I realized I actually want the Ableton sets inside of the public garden. It's just that I want the WAV files to be available behind a login, and I haven't built the login functionality yet.
				- I might eventually even make a little shop where you can download the uncompressed assets.
			- ### Principles
				- So I'm figuring out what my precedents, or principles, are here. One of my principles might be that bigger things should go behind a login.
		- ## Offloading
			- I also want to be able to offload things from my computer. I don't need every single Ableton set on my computer at all times.
			- Ideally I would have a dedicated media backup service, but I could use B2 for backing that up and then also back it up to a drive.
