date-created:: [[2022/07]]

- # [1Password Developer Tools Walkthrough - YouTube](https://www.youtube.com/watch?v=z67zoIN8sCA)
	- ## [[Video]]
		- {{video https://www.youtube.com/watch?v=z67zoIN8sCA}}
			- ### [[My Notes]]
			  id:: 67cff1ee-baac-4066-a027-6cac39f06983
				- [[Person/Floris van der Grinten]] provides a competent overview of how to use [[op]] CLI tool to be an [[ssh/agent]] as well as how to use it to inject secret references using a [[Biometric]] unlock that persists in a shell session.
				- After watching this video I had more confidence that Biometrics could be used to get secrets off of disk in all the "normal" cases, but I still have questions about how this interacts with local VMs and Docker.
				- Runtime: 16.5 min
					- ((67cff279-ee66-4500-8b2a-e07261d61e00))
					- ((67cff333-cf9a-4e73-a020-5d46c506f576))
					- ((67cff3b2-2083-4121-8e06-7fdd5227a76d))
					- ((67cff615-7e1f-439b-862a-f3e3707020ec))
					- ((67cffa6f-4a80-4557-ad48-b63be1aa3410))
					- ((67cffac0-8c8b-402c-8246-26e86c6fc0ec))
					- ((67cffb6e-46e0-4298-bfa5-030b95635165))
					-
			- ### {{youtube-timestamp 3}} Securely Creating an [[ssh]] key in [[GitHub]] with [[1Password]] and then using the [[1Password/Dev/ssh/agent]] to establish a session with [[Mac/TouchID]]
			  id:: 67cff279-ee66-4500-8b2a-e07261d61e00
			  collapsed:: true
				- {{youtube-timestamp 3}} demo time so um what i'm going to be showing you today is how easy it is now to set up ssh authentication for git and then i'll show how to use the agent to ssh into vms and i'll be using digital ocean droplets as an example and then i'll show how to how you can
				- {{youtube-timestamp 20}} integrate the one password developer tools in a local development workflow so i just set up a new machine and yeah i'd like to continue working on my project that's on github but yeah it's a private project and i want to clone this now to start developing on it so i'm
				- {{youtube-timestamp 36}} going to click the ssh url and i'm going to clone it now the only problem is i don't have any ssh keys on my on my new laptop so i also don't have them on github so if i now try to clone this it's not going to work unfortunately so what i'm gonna do now is i'm gonna head
				- {{youtube-timestamp 59}} over to the github ssh key settings and it's telling me about a guide that i can follow and actually it's a whole guide portal that explains me everything about ssh about openssh ssh keygen the openssh ssh agent and ssh ad but luckily today we don't have to do
				- {{youtube-timestamp 80}} that anymore we can now go straight to new ssh key and because i have the one password browser extension installed there's now a one password logo on the text box and it's giving me the option to create an ssh key right from the browser so i'm going to click that
				- {{youtube-timestamp 97}} i'm going to give it a name have an r key and i can select the key type here so it's i can create an ed2 for 519 key or an rsa key and i can also change the bit length and because not everyone knows the difference between those the differences
				- {{youtube-timestamp 112}} between those keys we have a little explanation here to help you make the the right decision um so i'm going to go with `ed25519` here because yeah it's the the fastest the most modern standard and if i now click create and fill what will happen is it will generate an
				- {{youtube-timestamp 129}} ed2509 key on the fly and it will then save it in my private vault hero1 password and it's going to also derive the public key and auto fill that into the text box so let's see that in action so here we are so the public key is now in the
				- {{youtube-timestamp 148}} text box also it also filled in the title i'm going to click add ssh key and now it's here on github but it's also on one password so if i use quick access now to uh and type in webinar key so here you can see the key that just got created as well
				- {{youtube-timestamp 165}} as some shortcuts to easily copy the public key or the fingerprint or even show the item here in a new window the fingerprint public key private key and the key type and it's also here in one password so now if i go back to my terminal um and i run the clone command again
				- {{youtube-timestamp 191}} it uh it will try to talk to the 1password agent because the key didn't just get added to my vault and to my github it also got added in the third place and that's the one password ssh agent and that happened automatically um so now if i run this command it will
				- {{youtube-timestamp 204}} talk to the ssh agent and it will try to use that key but notice i said try because unlike the standard openssh agent which basically gives every process on your system um blanket approval to use any key in any way it likes the password ssh agent will
				- {{youtube-timestamp 222}} always ask for your consent first and it does that through biometrics so because i'm on mac os that's uh that's touch id um i can also use it with with apple watch or on windows with windows hello on linux with with bulkhead and what will ask for my consent first so let's
				- {{youtube-timestamp 238}} see what that what that looks like so if i run this command it says here one password is trying to allow item two because that's my my terminal to use the webinar key so i'm gonna put my finger on the fingerprint reader and now the uh that way i i approved
				- {{youtube-timestamp 254}} this this ssh request and now i can successfully clone um but i didn't just approve a one-off ssh command there's actually now a session established between this terminal window and my ssh key that's that's stored on one password so that means that now the next command
				- {{youtube-timestamp 274}} does not need my consent again because i already gave it so if i now cd into that directory and i try to run git fetch for example i don't need to approve that again because i already did that but that's only for this terminal window so if i now open vs code for example
				- {{youtube-timestamp 293}} that's a different environment so if i open terminal here and here i run git fetch that's a different environment so it's going to ask me but now the same question but now for vs code so i could also allow this and i can now run git fetch again um so
				- {{youtube-timestamp 318}} **now you've seen how it works with git**
			- ### {{youtube-timestamp 322}} Creating a [[DigitalOcean/Droplet]] [[Virtual Machine]] and registering a new [[ssh]] key with it using the [[1Password/Browser Extension]]
			  id:: 67cff333-cf9a-4e73-a020-5d46c506f576
			  collapsed:: true
				- i'm also going to show you **how you can use the agent for ssh-ing into a vm** i'm going to create a [[DigitalOcean/Droplet]] here i'm gonna go with ubuntu basic settings um new york and here i'm gonna for authentication
				- {{youtube-timestamp 340}} i'm gonna select ssh keys and i'm gonna register a new ssh key and this time i'm gonna pick the one that i already created the webinar key click ok to auto fill also again filled in the name i'm going to click add and now i'm going to let's give it a name demo droplet
				- {{youtube-timestamp 364}} and i'm going to create the droplet and now for this demo i'm not going to use the vanilla ssh cli instead i'm going to show you how you can use it in a local terraform workflow so i have a simple terraform project here which manages a digital ocean droplet
				- {{youtube-timestamp 384}} and it prints the the ip of the droplet that gets created and it then uses an ssh provisioner and it's very simple all it does it creates a file on the on the host at this path um and it's a json file change the message here and then it runs through ssh a few commands
			- ### {{youtube-timestamp 410}} Using [[1Password/Dev/CLI]] with [[tf]] to transfer a file to the [[DigitalOcean/Droplet]]
			  id:: 67cff3b2-2083-4121-8e06-7fdd5227a76d
			  collapsed:: true
				- {{youtube-timestamp 405}} to prove that ssh works so let's go back to my droplet and it successfully created it so yeah
				- now enough with the [[UI/Graphical]] i'm going to start i'm going to **continue in terraform now** so i'm going to **copy the droplet id** and now i'm gonna transfer ownership to
				- {{youtube-timestamp 423}} my uh to my terraform projects i'm gonna use [[tf/import]] here digital ocean **paste in the droplet id** now i will use [[tf/apply]] which will **run my provisioners using ssh**
					- i'm gonna confirm yes and **now it's gonna try to ssh into the machine**
					- *here is the [[Mac/TouchID]]*
				- {{youtube-timestamp 458}} and i'm gonna confirm that and **now it's connecting to the host using the ssh agent** and it's printing out my commands um and now again yeah session got created here so i can now just run turf refresh and i don't have to authorize again and
				- {{youtube-timestamp 482}} um to confirm that the file actually successfully got there i'm also going to use yet another yet another ssh client and this and this time i'm going to use a gui application transmit to sftp into the server i'm going to click connect paste in ip
				- {{youtube-timestamp 498}} i'm going to accept the host key first and now it's going to talk to the agent but now it's saying transmit i'm gonna prove that again and now transmit can sftp into my server and here's the file that i just created with the message
			- ### {{youtube-timestamp 515}} Summary of [[ssh]] demo so far with [[1Password]]
			  id:: 67cff5b4-ad7f-4fcf-867f-8ad2d2f07732
			  collapsed:: true
				- **now you've seen how to use  ssh with the one password ssh agent**
					- using a bunch of different ssh clients
					- **what they all have in common is that none of these clients will ever be able to to see the private key**
					- because **the private key never leaves the one password** process
				- {{youtube-timestamp 537}} so **that means no more ssh keys on disk** also **here still no ssh keys**
					- *he's looking at `~/.ssh/config`*
				- it's **very clean just the config** and the **known hosts**
			- ### {{youtube-timestamp 540}} [[1Password/Dev/CLI]] for [[API/Key]] management and how to keep [[Secrets]] from holding your [[dotfiles]] hostage
			  id:: 67cff615-7e1f-439b-862a-f3e3707020ec
			  collapsed:: true
				- that was ssh keys but **if you're a developer like i am** then you know that **ssh keys are not the only keys and secrets on your on your local disk**
				- {{youtube-timestamp 563}} for example for this exact terraform project to work it needs to talk to digital ocean and for that **i need a digital ocean access token**
				- and this is not just a digital ocean or a terraform thing it's basically any developer platform or or [[SAAS]] that i'm {{youtube-timestamp 578}} trying to incorporate in my local workflows
				- there is some secret that i need to to authenticate there and that's usually more often than not on my on my local disk
				- and in this case i have my digital ocean access token in a in a [[dotfile]]
				- {{youtube-timestamp 597}} it can be in any config file and ... that's **now sitting on disk** and **that sucks**
				- because first of all **it's a plain text secret** that's secret is **now on disk** but also **i now cannot sync or my my dot files or my config files**
				- i'd like to sync them with my {{youtube-timestamp 615}} other machines
				- or maybe **even share some of them with my colleagues**
				- sometimes **people even open source their [[dotfiles]]** and **now that's not possible** because **there's a hard-coded secret** in there
				- so basically **those secrets are holding my super awesome configuration hostage** {{youtube-timestamp 630}} because the whole file is now sensitive - so let's get rid of that
				- i'm gonna first unset the plain text secret digitalocean access token
				- i have the secret store here and one password in my dev vault
				- so it's an item called digital ocean and
				- {{youtube-timestamp 650}} here it is the access token
				- now what i'm going to do is i'm going to **use the 1password cli version 2** which **introduced the new secret provision provisioning features** that tyler just mentioned
				- i'm going to show you how that works
				- i'm going to go back to where i {{youtube-timestamp 667}} configured the digital ocean access token
				- but now **instead of pasting in the plain text value i'm gonna use a reference** [[1Password/Dev/CLI/Secret Reference]]
					- so i'm replacing those **the plain text value with a reference to the secret**
					- and you can use those references using a special syntax {{youtube-timestamp 688}}
					- and that starts with `op://`
					- after that you can enter the **vault name** which was `dev` in my case
					- and then the **item** name `DigitalOcean`
					- and then the **field name** which was `axis-token`
				- so now i'm gonna rerun my terraform {{youtube-timestamp 713}} command
				- but now i'm gonna wrap it **in a new command called** [[op/run]]
					- which is new in the one password cli version two
					- i'm gonna do [[tf/refresh]] here
					- **what this will do is**
						- it will scan the environment for those those secret references
						- it will then {{youtube-timestamp 734}} if it finds it, it will **inject the plain text values**
							- *but only at runtime* - only *when this command runs*
						- and **when it ends the secrets are wiped**
				- so let's see that in action
					- **side note**: first it's also good to note the the [[1Password/Dev/CLI]] {{youtube-timestamp 755}} **by itself does not have any bootstrap secret or any authentication secret that's that's that's stored on my disk****
						- instead, simply **because i have the one password desktop app installed,**
						- the CLI **can connect to that** and **authenticate**
						- **without** having to {{youtube-timestamp 777}} have **yet another secret sitting there** in between
				- *another [[Mac/TouchID]] here*
				- using, you guessed it, the [[Biometric]] unlock
			- ### {{youtube-timestamp 786}} Example of using `op://` protocol with [[Mac/TouchID]]
			  collapsed:: true
				- let's let's see that in action
					- again it's going to ask for permission
					- this looks very similar to the ssh prompt
					- but now it's for CLI access to my account
				- so i'm {{youtube-timestamp 794}} going to approve that
					- and now it's loading the digital ocean access token from my one password vault
					- and it's replacing the reference with the actual secret and passing it to terraform
					- which now succeeds ... and now **the secret is wiped**
				- so **if i if i now** {{youtube-timestamp 822}} **echo the digital ocean access token**
					- again **i can just do that because it's not sensitive** it's **just a reference**
					- it's **only during the time that this command is running that the the real sensitive value is in there**
			- ### {{youtube-timestamp 835}} After authenticating one shell to the 1Password app, that shell can be used to authorize subsequent commands
			  id:: 67cffa6f-4a80-4557-ad48-b63be1aa3410
			  collapsed:: true
				- i can rerun this without the {{youtube-timestamp 840}} prompt
				- because this shell is now connected to my one password app
			- ### {{youtube-timestamp 846}} another feature - items are masked by default in the [[CLI]] during the run of [[OP]]
			  id:: 67cffac0-8c8b-402c-8246-26e86c6fc0ec
			  collapsed:: true
				- #### Demo of 1Password conceal by default UI
					- there's another feature next to biometrics that we've taken from the desktop app to the terminal
					- now i can just show you the desktop app even just screen share it
					- {{youtube-timestamp 860}} without being worried that i'm leaking any sensitive information
					- and that's because **these the sensitive part is concealed here**
						- ... **until i explicitly tell it to reveal**
						- which i'm not gonna do obviously right now
					- and now now we've taken that same {{youtube-timestamp 875}} concept **to the terminal as well**
				- #### {{youtube-timestamp 877}} demo of equivalent feature in CLI
					- because in op1 what operon will do is it will automatically conceal all the sensitive values
					- if i now **print the digital ocean access token**
					- **it says digital ocean access token concealed by 1password**
					- and then i **can** {{youtube-timestamp 904}} **use** the **no masking flag** to **opt out of that**
					- so that was [[op/run]]
			- ### {{youtube-timestamp 916}} Technique for utilizing [[op/run]] using [[Shell/alias]]
			  id:: 67cffb6e-46e0-4298-bfa5-030b95635165
			  collapsed:: true
				- **and i can already hear you thinking** now that **okay so wait i now need to always remember to always wrap my terraform commands with op run** true but luckily there's a good old uh
				- {{youtube-timestamp 927}} shell trick for this
				- and that's called **aliases**
				- so if i use this is a pretty pretty nice pattern
				- `alias terraform='op run -- terraform'`
				- now i don't need to remember anymore that i need to wrap it with terraform with op run
				- i can just say terraform {{youtube-timestamp 947}} refresh
				- and it works without me having to wrap it manually in op run and this is and you can also set this set this up globally because op run will never get in your way operon will only show the biometric metrics prompt if it detects one or more
			- {{youtube-timestamp 968}} secret secret references if there aren't any then it will just just run the command right away without doing anything else now you've seen how to use both the ssh agent and version 2 of the cli in a local development workflow and all of that without having to keep a single
			- {{youtube-timestamp 985}} secret on disk