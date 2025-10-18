date-created:: [[2025-03-19 Wed]]
created-by:: [[Person/Simon Willison]]

- # [Not all AI-assisted programming is vibe coding (but vibe coding rocks)](https://simonwillison.net/2025/Mar/19/vibe-coding/)
	- **Vibe coding** is having a moment. The term [was coined by Andrej Karpathy](https://twitter.com/karpathy/status/1886192184808149383) just a few weeks ago (on February 6th) and has since been featured [in the New York Times](https://www.nytimes.com/2025/02/27/technology/personaltech/vibecoding-ai-software-programming.html), [Ars Technica](https://arstechnica.com/ai/2025/03/is-vibe-coding-with-ai-gnarly-or-reckless-maybe-some-of-both/), [the Guardian](https://www.theguardian.com/technology/2025/mar/16/ai-software-coding-programmer-expertise-jobs-threat) and countless online discussions.
	- I’m concerned that the definition is already escaping its original intent. I’m seeing people apply the term “vibe coding” to all forms of code written with the assistance of AI. I think that both dilutes the term and gives a false impression of what’s possible with responsible [AI-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/).
	- Vibe coding is *not* the same thing as writing code with the help of LLMs!
	- To quote Andrej’s [original tweet](https://twitter.com/karpathy/status/1886192184808149383) in full (with my emphasis added):
		- > There’s a new kind of coding I call “vibe coding”, where you fully give in to the vibes, embrace exponentials, and **forget that the code even exists**. It’s possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper so I barely even touch the keyboard.
		- > I ask for the dumbest things like “decrease the padding on the sidebar by half” because I’m too lazy to find it. I “Accept All” always, I don’t read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I’d have to really read through it for a while. Sometimes the LLMs can’t fix a bug so I just work around it or ask for random changes until it goes away.
		- > **It’s not too bad for throwaway weekend projects, but still quite amusing**. I’m building a project or webapp, but it’s not really coding—I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works.
	- I *love* this definition. Andrej is an extremely talented and experienced programmer—he has no need for AI assistance at all. He’s using LLMs like this because it’s fun to try out wild new ideas, and the speed at which an LLM can produce code is an order of magnitude faster than even the most skilled human programmers. For low stakes projects and prototypes why not just *let it rip*?
	- When I talk about vibe coding I mean **building software with an LLM without reviewing the code it writes**.
	- #### Using LLMs for code responsibly is not vibe coding  [#](https://simonwillison.net/2025/Mar/19/vibe-coding/#using-llms-for-code-responsibly-is-not-vibe-coding)
	  
	  Let’s contrast this “forget that the code even exists” approach to how professional software developers use LLMs.
	  
	  The job of a software developer is not (just) to churn out code and features. We need to create code that demonstrably works, and can be understood by other humans (and machines), and that will support continued development in the future.
	  
	  We need to consider performance, accessibility, security, maintainability, cost efficiency. Software engineering is all about trade-offs—our job is to pick from dozens of potential solutions by balancing all manner of requirements, both explicit and implied.
	  
	  We also *need* to read the code. My golden rule for production-quality AI-assisted programming is that I won’t commit any code to my repository if I couldn’t explain exactly what it does to somebody else.
	  
	  If an LLM wrote the code for you, and you then reviewed it, tested it thoroughly and made sure you could explain how it works to someone else that’s not vibe coding, it’s software development. The usage of an LLM to support that activity is immaterial.
	  
	  I wrote extensively about my own process in [Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/). Vibe coding only describes a small subset of my approach.
	- #### Let’s not lose track of what makes vibe coding special  [#](https://simonwillison.net/2025/Mar/19/vibe-coding/#let-s-not-lose-track-of-what-makes-vibe-coding-special)
	  
	  I don’t want “vibe coding” to become a negative term that’s synonymous with irresponsible AI-assisted programming either. This weird new shape of programming has so much to offer the world!
	  
	  I believe **everyone deserves the ability** to automate tedious tasks in their lives with computers. You shouldn’t need a computer science degree or programming bootcamp in order to get computers to do extremely specific tasks for you.
	  
	  If vibe coding grants millions of new people the ability to build their own custom tools, I could not be happier about it.
	  
	  Some of those people will get bitten by the programming bug and go on to become proficient software developers. One of the biggest barriers to that profession is the incredibly steep initial learning curve—vibe coding shaves that initial barrier down to almost flat.
	  
	  Vibe coding also has a ton to offer experienced developers. I’ve talked before about how [using LLMs for code is difficult](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)—figuring out what does and doesn’t work is a case of building intuition over time, and there are plenty of hidden sharp edges and traps along the way.
	  
	  I think vibe coding is the best tool we have to help experienced developers build that intuition as to what LLMs can and cannot do for them. I’ve published more than [80 experiments](https://tools.simonwillison.net/colophon) I built with vibe coding and I’ve learned so much along the way. I would encourage any other developer, no matter their skill level, to try the same.
	- #### When is it OK to vibe code?  [#](https://simonwillison.net/2025/Mar/19/vibe-coding/#when-is-it-ok-to-vibe-code-)
	  
	  If you’re an experienced engineer this is likely obvious to you already, so I’m writing this section for people who are just getting started building software.
	- Projects should be **low stakes**. Think about how much harm the code you are writing could cause if it has bugs or security vulnerabilities. Could somebody be harmed—damaged reputation, lost money or something worse? This is particularly important if you plan to build software that will be used by other people!
	- Consider **security**. This is a really difficult one—security is a huge topic. Some high level notes:
		- Watch out for **secrets**—anything that looks similar in shape to a password, such as the API key used to access an online tool. If your code involves secrets you need to take care not to accidentally expose them, which means you need to understand how the code works!
		- Think about **data privacy**. If you are building a tool that has access to private data—anything you wouldn’t want to display to the world in a screen-sharing session—approach with caution. It’s possible to vibe code personal tools that you paste private information into but you need to be very sure you understand if there are ways that data might leave your machine.
	- Be a **good network citizen**. Anything that makes requests out to other platforms could increase the load (and hence the cost) on those services. This is a reason I like [Claude Artifacts](https://simonwillison.net/tags/claude-artifacts/)—their sandbox prevents accidents from causing harm elsewhere.
	- Is **your money on the line**? I’ve seen horror stories about people who vibe coded a feature against some API without a billing limit and racked up thousands of dollars in charges. Be very careful about using vibe coding against anything that’s charged based on usage.
	  
	  If you’re going to vibe code anything that might be used by other people, I recommend checking in with someone more experienced for a vibe check (hah) before you share it with the world.
	- #### How do we make vibe coding better?  [#](https://simonwillison.net/2025/Mar/19/vibe-coding/#how-do-we-make-vibe-coding-better-)
	  
	  I think there are some fascinating software design challenges to be solved here.
	  
	  Safe vibe coding for complete beginners starts with a [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)). Claude Artifacts was one of the first widely available vibe coding platforms and their approach to sandboxing is fantastic: code is restricted to running in a locked down `<iframe>`, can load only approved libraries and can’t make any network requests to other sites.
	  
	  This makes it very difficult for people to mess up and cause any harm with their projects. It also greatly limits what those projects can do—you can’t use a Claude Artifact project to access data from external APIs for example, or even to build software that runs your own prompts against an LLM.
	  
	  Other popular vibe coding tools like Cursor (which was initially intended for professional developers) have far less safety rails.
	  
	  There’s plenty of room for innovation in this space. I’m hoping to see a cambrian explosion in tooling to help people build their own custom tools as productively and safely as possible.
	- #### Go forth and vibe code  [#](https://simonwillison.net/2025/Mar/19/vibe-coding/#go-forth-and-vibe-code)
	  
	  I really don’t want to discourage people who are new to software from trying out vibe coding. The best way to learn anything is to build a project!
	  
	  For experienced programmers this is an amazing way to start developing an intuition for what LLMs can and can’t do. For beginners there’s no better way to open your eyes to what’s possible to achieve with code itself.
	  
	  But please, don’t confuse vibe coding with all other uses of LLMs for code.