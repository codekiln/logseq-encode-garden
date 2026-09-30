logseq-entity:: [[Logseq/Entity/YouTube]]
created-by:: [[1Password]]
date-created:: 2025-11-17
logseq-created-time-year:: [[20/2/5]]

- # [How 1Password Environments makes secrets management simple for developers](https://www.youtube.com/watch?v=mrhtzh05jG4)
	- ## Overview
		- A recorded live demo from [[1Password]]. Sid, a developer on the 1Password developer tools team, walks a hypothetical Raptors stats app from a Slack-shared plaintext [[EnvVar/.env]] file to [[1Password/Environment]]s: a mounted local `.env` for development and an AWS Secrets Manager sync for production.
	- ## Sources
		- [YouTube](https://www.youtube.com/watch?v=mrhtzh05jG4)
		- [Readwise Reader](https://read.readwise.io/read/01m36tvy1k0v56zcrkxjqnr9my)
	- ## Video
		- {{video https://www.youtube.com/watch?v=mrhtzh05jG4}}
			- ### {{youtube-timestamp 0}} Introduction to 1Password
			  collapsed:: true
				- Transcript
				  collapsed:: true
					- {{youtube-timestamp 0}} right. Hey folks, uh my name is Saradir. I go by Sid. And today I'll be uh showcasing some of the latest tools we've been building over at One Password. So by now I'm guessing or hoping at least a couple of you have heard of One Pastor before. So we're traditionally known as
					- {{youtube-timestamp 15}} the password manager application. Uh but we've grown a lot in the last few years and we've expanded from just a basic BTOC application to a full-fledged security platform for both businesses and individuals. So what I work on at one password is the developer side and the
					- {{youtube-timestamp 30}} developer story. Uh as developers I think a lot of you know that uh we deal with secrets daily whether that's API keys, API tokens, party tokens or SSH keys. And historically those have been painful to manage to say the least. So at
					- {{youtube-timestamp 45}} one password our mission is pretty uh simple. U make the safe thing the easy thing to do. So, and one password actually already has a lot of great developer tools like our SSH agent, our SDKs, and our CLI. But today, I want to show you guys something a little newer,
					- {{youtube-timestamp 60}} and that's one password environments. So, instead of talking about it, I'll get straight into a demo.
			- ### {{youtube-timestamp 66}} The pain of managing secrets
			  collapsed:: true
				- Transcript
				  collapsed:: true
					- {{youtube-timestamp 66}} So, I'll make this. So, what I have here is a little hypothetical situation. So, hopefully you all will entertain this, but let's imagine a couple friends and me were talking and they recently recruited me to work on a Raptors app for all big Raptors fans. And
					- {{youtube-timestamp 81}} the app basically pulls the latest stats from the team, uh the box scores, and uh provides an AI summary of what's been going on with the team in the last couple of weeks. And like most apps, this will need a M file with things like API keys and tokens to access these services. And
					- {{youtube-timestamp 96}} if you've ever joined a project like this, you know the routine. You clone the repo, you pull it up in ID, and you see a N.example file. From there, uh you go Slack the most recent person to join this team and ask them to send over their file. From there, uh, you copy
					- {{youtube-timestamp 111}} and paste and you realize I'm missing a few credentials. You slack another person. They tell you to go look in notion. You dig around notion and after this whole song and dance, what you end up with at the end is essentially a plain text file with some of the most important credentials and powerful credentials on your computer. So,
					- {{youtube-timestamp 126}} let's simulate me doing that. So, I have a Oops, got this. So, I've simulated us doing that. So now we have ain file with some credentials uh
					- {{youtube-timestamp 141}} filled up and uh like I said one these are just in plain text so that just sucks. Two if any of these keys get rotated in the future I'm out of sync again and we got to go through this whole song and dance once more. And three is that uh by default files are
					- {{youtube-timestamp 156}} just plain text files. So they can get uh committed up to git. Uh, of course you could put them in your git ignore and ignore them, but if you name them incorrectly or forget to put that in your git ignore, it's a little too easy to accidentally commit those. Uh, so before I show you how one password is
					- {{youtube-timestamp 171}} now trying to solve this, let me show you. And full transparency, this app doesn't actually do any of the things I said, all it does is just console log the variables it theoretically would have needed uh for demo purposes, just keeping it simple.
			- ### {{youtube-timestamp 183}} Introducing 1Password Environments
			  collapsed:: true
				- Transcript
				  collapsed:: true
					- {{youtube-timestamp 183}} So let's switch over to one password. And uh, this is where one password environments come in. So if we right now I'm logged into an account that my team has set up. So if we head over to environments, environments comes in and basically allows you to define secrets and other environment variables
					- {{youtube-timestamp 198}} right within one password. So let's go ahead and create a new environment for local So I'll call it Raptor's app local. And if we head in there, we can go ahead and directly import that file that we just created. So
					- {{youtube-timestamp 214}} let's do that. And now all our environment variables are here. So, some of these aren't really like credentials, so I'm just going to mark them as plain text so they're a little easier to read. Like the AI model, uh, let's do like support summary and log level and say.
					- {{youtube-timestamp 230}} So, sweet. Now, your credentials are in one password. Uh, and if you've used one password before, baults, you know, another cool thing about one password is it sharability. So, we can go ahead and manage access and I can go ahead and add my whole team to this uh, environment. So, we'll go
					- {{youtube-timestamp 245}} ahead and do that. And Steve is our CEO Koda code. So I'm going to give him managing access. And Emily's the intern. And it's not that I don't trust interns, but I'm just going to remove her editing access so she doesn't mess with it. We can go ahead and do that. And now when my teammates log
					- {{youtube-timestamp 260}} into one password, the environment will be there. And any updates they make, if they have edit permission, will show up live to all of our devices. So this is cool, but it brings the question like they're stored in one password. They're fully encrypted, but how do you actually use them in your application now?
			- ### {{youtube-timestamp 274}} Local development integration
				- {{youtube-timestamp 360}}
					- > ... you'll notice that before we had that one git ... file staged, but because this is not a normal plain text file, it's a FIFO file. Git doesn't track these files. So you can't accidentally commit this up to git no matter what you name it. Like it doesn't have to be in your gitignore anymore. ... And just to prove that this is live updating, let's for example change the debug level to warn ... ([Readwise](https://read.readwise.io/read/01m398ac89b9s5rfxzz3exahrb))
						- The mounted `.env` is a named pipe: [[Unix/Q/What is a named pipe in unix, and how do 1Password Environments use one to mount a .env?]]
				- {{youtube-timestamp 396}}
					- > ... gives you a bunch of other ... advantages too. One of these is versioning. ... So you can go ahead and see at 6:37 this was the state of the environment, at 6:40 this was the state of the environment where I changed it to warn, so I'm going to restore it back to its original and we go back to that state, and this works if other teammates make changes too ... ([Readwise](https://read.readwise.io/read/01m3h3m1svfxxeyxkmhxxbped9))
				- Transcript
				  collapsed:: true
					- {{youtube-timestamp 274}} So that's where the new destination uh tab comes into play. These the destinations tab is how you're going to get your secrets into the various places you need. So because this is local development, I'm going to use the new local end file destination. And what this destination does is essentially
					- {{youtube-timestamp 289}} mount at inmemory. MV file in your project that my app can just read like any other normal file. So no need to change your application code. So let's go ahead and do that. So I'm going to choose uh in that repo. Let me make sure. Yeah. EMB.
					- {{youtube-timestamp 307}} And it's asking me, do I want to replace the existing one? So I'm going to say yes. And I'm going to mount it. So now I'm going to come back to my app and everything looks more or less the same. But you'll notice if I run the application now, we get an op prompt. And it's basically
					- {{youtube-timestamp 322}} asking that one password's access has been requested. Would you like to populate this with the environment? And only if I give my fingerprint approval do the environment variables actually get streamed into the file. And this means your environment variables are no longer sitting on disk. And
					- {{youtube-timestamp 337}} if I run the command again, you can see because I already approved it once within the session, one password access is not uh requested. So if I lock it and run it, then of course we'll get the op prompt. And this time, let's just deny it. And you can see no secrets uh were passed in. And
					- {{youtube-timestamp 352}} that works even if I try to open the file to zukine vs code, get the off prompt. It's only if I approve it that the file actually uh gets the contents. And you'll notice that before we had that one git uh file staged, but because this
					- {{youtube-timestamp 367}} is not a normal plain text file, it's a fifu file. Git doesn't track these files. So you can't accidentally commit this up to get no matter what you name it. Like it doesn't have to be in your git ignore anymore. Uh and just to prove that this is live updating,
					- {{youtube-timestamp 382}} let's for example change the debug level to warn or whatever. And now if I run this command again, they'll see that before it was debug and now it's become a warn level. So it's constantly live fetching from one password. The environments gives
					- {{youtube-timestamp 397}} you a bunch of other uh advantages too. One of these is versioning. So you can imagine if for example me or teammate is comes in gear and decides to keep working with decides to delete everything uh one crash rig actually
					- {{youtube-timestamp 412}} has uh a versioning of deer environment. So you can go ahead and see at 637 this was the state of the environment at 640 this was the state of the environment where I changed it to warn so I'm going to restore it back to its original and
					- {{youtube-timestamp 427}} we go back to that state and this works if other teammates make changes too if they make changes it'll show up as X teammate made this change at this So this
			- ### {{youtube-timestamp 437}} Production secrets management
				- {{youtube-timestamp 454}}
					- > You probably want something like a production environment, ... where I'd only invite a few select people because obviously I don't want everyone to have access to production. And within this environment, you can actually select one of our ... currently supported destinations which is AWS Secrets Manager. And what this will do is create a one-way secure sync between 1Password and AWS. ... So then when a secret is updated in 1Password, production gets it instantly. ([Readwise](https://read.readwise.io/read/01m3h3q01dnv3jwjvsfwrdv5zd))
				- {{youtube-timestamp 495}}
					- > ... once you configure this once no other teammate has to configure it. It's a one-time thing. So now if I share with other teammates you'll be able to edit right within 1Password without having to deal with all the IAM and AWS rules. So no more secret sprawl, no more confusion over who has access to what, and no need to touch IAM or redeploying. ([Readwise](https://read.readwise.io/read/01m3h3s3hewfqva0c49cj2tabx))
						- [[My Notes]]: Um … this is actually really confusing. Is there bidirectional sync? Is there a bypass of iam?
				- Transcript
				  collapsed:: true
					- {{youtube-timestamp 437}} is all pretty powerful, but one password environments don't just stop there. In real Teams, you're not just dealing with local development. Uh you've got staging, you've got production, and uh you need different credentials for each of those. So for our example, uh if I head back here, you can imagine we
					- {{youtube-timestamp 452}} have Raptor's app local. You probably want something like a production environment, uh where I'd only invite a few select people because obviously I don't want everyone to have access to production. And within this environment, you can actually select one of our uh currently supported destinations which is AWS secret
					- {{youtube-timestamp 467}} s. And what this will do is create a one-way secure sync between one password and AWS. Uh so then when a secret is updated in one password, production gets it instantly. So in this hypothetical uh I'm on now the one password web app and you can see
					- {{youtube-timestamp 482}} up here I'm logged in as Steve who I said was the core conc. So Steve can come in here and for example just share this production environment with me and I'm going to give it managing. I'm Seduct by the way. So I'm like sharing it with myself. That makes sense as Steve. So
					- {{youtube-timestamp 497}} if I come back here you can see immediately the production environment shows up and I can see all the production environment variables. I can edit them if I need and I can go ahead and configure an AWS uh secret sync destination. Uh so uh
					- {{youtube-timestamp 512}} and once you configure this once no other teammate has to configure it. It's a onetime thing. So now if I share with other teammates you'll be able to edit right within one password without having to deal with all the AM and AWS rules. So no more secret scroll no more confusion over who has access
					- {{youtube-timestamp 527}} to what and no need to touch AM or redeploying. Everything just stays up to date with one passer.
			- ### {{youtube-timestamp 534}} Recap and benefits
			  collapsed:: true
				- Transcript
				  collapsed:: true
					- {{youtube-timestamp 534}} And uh to show that like for time sake I'm not going to set up the AWS integration but in another account if I go to the environment I have an environment here that I was shared with my teammate. You can see here this environment is currently syncing with AWS. So any
					- {{youtube-timestamp 549}} changes made to this environment will uh get reflected in prod right away. So to recap uh we went from plain text files and slackdms to a world where secrets never have to touch disk. access is fully auditable uh
					- {{youtube-timestamp 564}} versioned and sharable and onboarding a teammate is as simple as just adding them to the environment and then they can go and mount it uh in their project and just get up and running and uh keeping production credentials uh updated. It just takes a few clicks. Yeah, that's
					- {{youtube-timestamp 579}} one password environments uh making the safe thing the easier thing to do. Thank you.
			- ### {{youtube-timestamp 589}} Q&A session
				- {{youtube-timestamp 609}}
					- Audience member
						- > ... is there a concept of ... an overlay, like let's say I have a different database configured for my development but we need all the same ... dev ... provider keys or whatever, but we need to override certain things locally? ... is there a provision for doing this within, or do I have to use like a ... dev.local? ([Readwise](https://read.readwise.io/read/01m3h3ypgw69v53hh0gxgrrs8q))
					- Sid
						- > Yeah. So, at the moment, 1Password, we don't support ... an overlay ... right now Environments is in ... beta, but that is definitely a lot of feedback we received.
				- Transcript
				  collapsed:: true
					- {{youtube-timestamp 589}} Yeah, if anyone has questions. >> So, this is pretty amazing. >> Uh, hi. This looks pretty amazing. I'm pretty sure I'm going to implement this tomorrow in
					- {{youtube-timestamp 605}} my team whether the I mean they're what? Um my question is is there a concept of kind of like a I don't really know what to call it but like as an overlay like let's say I have a different database configured for
					- {{youtube-timestamp 620}} my development but we need all the same you know dev uh all provider keys or whatever but we need to override certain things locally um is there a provision for doing this within or is do I have to use like a you know
					- {{youtube-timestamp 636}} deb.local local. >> Yeah. So, at the moment, one password we don't support like a overlay, but that was definitely in our uh beta launch like right now environments is in uh beta, but that is definitely a lot of feedback we received. Uh at the moment, like I think we have a sponsor uh demo
					- {{youtube-timestamp 651}} from like go lock and like tools like that. You'll actually be able to like you said have kind of like a local file where you overlay some of the credentials. Yeah, at the moment it's kind of just the one sync, but that's definitely feedback we've gotten and uh planning on in to attend.
