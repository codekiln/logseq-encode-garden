logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]

- # Multiplayer agents
	- ## Overview
		- Team-based agents mark a shift from single-player AI tools—assistants that serve one person, like a personal chief of staff—to agents that act as [shared teammates](https://readwise.io/bookreview/63025623/?highlight=1047806463) inside a team's existing communication channels, per [[AI/Concept/Multiplayer/Log/26/09/21 Mon Readwise Summary of Claude Tag]].
		- Instead of living in a private chat with one user, the agent sits at the [intersection where a team already comes together](https://readwise.io/bookreview/63025623/?highlight=1047806463): a shared channel that every relevant person can see and add to.
	- ## Context
		- [Persistent teammates](https://readwise.io/bookreview/61695516/?highlight=1029402859) in [[Slack]] carry the whole history of a channel, so no individual has to brief them from scratch. One person's agent-assisted work [hands off cleanly](https://readwise.io/bookreview/61695516/?highlight=1029401866) to the next person, because the agent's memory of the thread is continuous rather than scoped to a single conversation.
		- [[Claude/Tag]] is Anthropic's instance of this pattern: @-mentioning it in a Slack thread summons a version of Claude that is not tied to any one person, running instead as an [organization-scoped teammate](https://readwise.io/bookreview/61791140/?highlight=1030620210) with its own permissions, tool access, and persistent memory.
		- [[CursorAI/Cloud Agent]] applies the same pattern to software delivery: mentioning the agent in a Slack channel kicks off work on a [collaborative development surface](https://readwise.io/bookreview/58802703/?highlight=996172072) that the whole channel can watch, rather than one developer's private editor.
	- ## Key Principles
		- **Org-scoped identity, not personal** — permissions, tool access, and memory attach to the team or organization, not to whichever individual happens to type the @-mention.
		- **The conversation is the interface** — work happens inside the channel; agents [call APIs and run commands in the background](https://readwise.io/bookreview/59974345/?highlight=1010372879), surfacing only the approvals and decisions a human needs to see.
		- **Bounded initiative** — a multiplayer agent can [take initiative](https://readwise.io/bookreview/61695516/?highlight=1029401866) by following up on quiet threads, flagging relevant information, and managing long-horizon tasks without being re-prompted each time.
		- **Division of labor** — agents take on the [stable, repeatable layers of work](https://readwise.io/bookreview/60717656/?highlight=1019232660), while humans hold the creative and strategic end of the judgment.
	- ## Mechanism
		- Invocation is an @-mention inside an existing channel (`@Claude`, `@cursor`) rather than a switch to a separate app; the agent reads the thread it is tagged in for context.
		- Specialized [coworker agents](https://readwise.io/bookreview/60717656/?highlight=1019232659) narrow the same pattern to a functional role: an editorial team's agent named Andy collects "nuggets" of story ideas from Slack threads and turns them into newsletter drafts; an always-on product-manager agent keeps a `memory.md` file tracking priorities and tags a human only when their input is needed.
		- At company scale, this becomes part of a broader move toward [headless software](https://readwise.io/bookreview/59974345/?highlight=1010373002)—Salesforce and Slack describe positioning themselves as an [agentic OS](https://readwise.io/bookreview/55644061/?highlight=948289419)—where work happens inside the conversation instead of a separate dashboard login.
	- ## Examples
		- [[Claude/Tag]] handling incident response, bug triage, and shipping code directly from a Slack thread.
		- [[CursorAI/Cloud Agent]] kicking off an investigation from a Slack message, tagging people for input, and producing a [PR-ready artifact](https://readwise.io/bookreview/58802703/?highlight=996162805) visible to everyone in the channel; Anthropic reported that [65% of one product team's code](https://readwise.io/bookreview/61837082/?highlight=1031389023) now originates from Slack-triggered workflows.
		- Andy and the always-on product-manager agent, applying the same pattern to editorial and product-management roles rather than engineering.
	- ## Misconceptions
		- Not a personal assistant shared by copy-pasting a login: a multiplayer agent needs its own org-scoped permissions and continuous channel memory, independent of any one person's session.
		- Not confined to chat: the agent calls APIs and runs commands in the background; the channel is the approval and notification surface, not the whole of its work.
