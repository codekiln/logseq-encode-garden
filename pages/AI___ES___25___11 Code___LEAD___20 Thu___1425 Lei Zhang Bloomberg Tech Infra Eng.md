chatgpt-link:: https://chatgpt.com/g/g-p-691f249c2fac8191ab8b4b926da5cb3b-ai-es-25-11-code/c/691f76cb-dfec-8330-acea-3400a91a2aee

- # 2:25pm - 2:44pm | AI Leadership | Room: Times Center
	- ![Lei Zhang](https://www.ai.engineer/speakers/lei-zhang.jpg)
	- **[[Person/Lei Zhang]]** - Head of Technology Infrastructure Engineering, [[Bloomberg]]
	- ## Talk: What We Learned Deploying AI within Bloomberg's Engineering Organization
		- When it comes to using AI for software engineering, much of the spotlight falls on how large language models (LLMs) can write code—sometimes entirely from scratch. Countless studies highlight productivity gains from turning requirements directly into runnable code. But the reality of applying AI at scale inside a mature engineering organization is far more complex and nuanced. Over the past year, we've been on that journey at [[Bloomberg]]—integrating AI into the workflows of 9,000+ software engineers—and we've learned a few important lessons worth sharing:
		- Where the real ROI lies once you move beyond toy examples
		- What it takes to actually enable AI across a large, established engineering org
		- The best practices, cultural shifts, and guardrails that are required to make it work in practice
		  
		  If you’re wondering what happens after the first demo magic fades and the real work begins, this talk is for you.
-
- ## Slide —  *Bloomberg by the numbers*
	- **Visual structure (two-column layout)**
		- **Left column = People + roles** with large emoji-style icons; vertically stacked, evenly spaced.
		- **Right column = Data scale + ingestion footprint** with corresponding icons; mirrors left column’s vertical rhythm.
		- Bottom-left: **TechAtBloomberg.com**.
		- Bottom-right: **Bloomberg Engineering** logo.
	- **Left column (organization scale)**
		- **26,000+ employees worldwide** — icon: group of people.
		- **9,000+ engineers** — icon: hard-hat engineer.
		- **2,900+ journalists & analysts** — icon: reporter badge.
		- **2,000+ data specialists** — icon: documents/profile sheets.
		- **400+ employees working on AI & ML applications** — icon: person with shades + device.
	- **Right column (data + workload scale)**
		- **600+ billion ticks per day** across all asset classes/markets — icon: financial bars + currency.
		- **96,000 companies; 2M+ entities; 3.3M executive/government bios** — icon: buildings.
		- **1.5M news articles ingested per day**, from **175,000+ vetted sources** — icon: newspaper.
		- **100+ alternative data sources** across sectors — icon: map pin.
		- Closing line:
		  
		  *“…all to bring the highest quality insights and analysis to decision makers around the world!”*
-
- ## Slide —  *About Bloomberg’s tech stack*
	- **Visual layout**
		- Single-column white text on black background.
		- Four high-level bullets + two indented technology lists.
		- Footer: **TechAtBloomberg.com** (left), **Bloomberg Engineering** (right).
	- **Core points (expanded with functional context)**
		- **One of the largest private networks globally**
		  
		  → Required for the Bloomberg Terminal’s thousands of real-time functions (email, chat, trading, news, analytics).
		- **One of the largest JavaScript codebases** (tens of millions of LoC)
		  
		  → Supports massive UI surface area across Terminal functions.
		- **Wide technology range powering heterogeneous applications**
		  
		  → Data pipelines, analytics engines, risk systems, trading workflows, collaboration tools; each function-family uses tailored stacks.
		- **Growing open-source usage + contributions**
		  
		  → ML/AI stack: *PyTorch, Hugging Face, XGBoost, TensorFlow, KServe, Envoy AI Gateway…*
		  
		  → Distributed systems/data infra: *Apache Solr, Kafka, Hadoop, Cassandra, Ceph…*
	- **Intent**
		- Establish that Terminal-scale = extreme heterogeneity + enormous infra; justifies why integrating AI is non-trivial and must span many stacks.
-
- ## Slide —  *What is AI for coding?*
	- **Visual structure**
		- Full-bleed collage of **~20 AI coding tool logos**, overlapping in chaotic layers.
		- Logos include: Charm CRUSH banner (center-left), abstract geometric agents, chat bubbles, hearts, mascots, terminal-themed icons, kangaroo silhouette, ghost icon, etc.
		- Title anchored top-left: *What is AI for coding?*
	- **Cognitive layout / intended effect**
		- Dense visual clutter → conveys **market fragmentation**, “too many tools,” and the **noise-to-signal problem** engineers face.
		- No grouping, no hierarchy → intentionally mirrors the confusion teams feel when choosing AI tooling.
	- **Speaker intent (your provided context integrated)**
		- Bloomberg engineers saw a **flood of AI coding solutions**, each promising productivity and stability gains.
		- The diversity and rapid turnover of tools made evaluation **overwhelming**, but they recognized that **ignoring AI wasn’t an option**.
		- Sets up the narrative: despite the chaos, they needed a disciplined, internal approach to experimentation.
	- **Implied transition**
		- From external noise → toward Bloomberg’s structured evaluation, pilot programs, and lessons learned.
-
- ## Slide —  *Be careful with what you do with software assets*
	- **Visual layout**
		- Center: embedded X/Twitter post from **@iamdevloper**.
		- Post text:
		  
		  *“vibe coding, where 2 engineers can now create the tech debt of at least 50 engineers.”*
		- Below: full tweet URL.
		- Bottom-left: **TechAtBloomberg.com**.
		- Bottom-right: **Bloomberg Engineering**.
	- **Cognitive framing**
		- Humor used as a **warning**: AI-accelerated coding amplifies both good and bad outcomes.
		- Implied message: productivity gains can balloon into **massive tech-debt risk** if unmanaged.
	- **Intent / narrative role**
		- Signals Bloomberg’s stance: **AI must be adopted deliberately**, with strong review, governance, and safeguards.
		- Serves as a turning point slide → from hype to sober operational responsibility.
-
- ## Slide —  *AI for software engineering*
	- **Visual layout**
		- Centered 5×2 table: left column = engineering activity; right column = engineers’ AI adoption preference.
		- Black background; white text; grid lines visually separating each row.
		- Footer: **TechAtBloomberg.com** (left) and **Bloomberg Engineering** (right).
	- **Table contents (structured)**
		- **Writing new features** → *High preference*
		- **Architectural / Design work** → *High preference*
		- **Code review / Peer review** → *Mixed*
		- **Bug fixing / Maintenance** → *Low preference*
		- **Support / Triaging** → *Low preference*
	- **Interpretive structure**
		- High-preference tasks = **creative, greenfield, forward-building work**, where AI accelerates throughput without clashing with legacy constraints.
		- Mixed = **judgment-heavy gatekeeping tasks** where AI suggestions can help but require careful oversight.
		- Low-preference tasks = **deep context / legacy-entangled work**, where engineers distrust AI due to higher risk of incorrect or incomplete suggestions.
	- **Speaker intent**
		- Establishes **baseline sentiment** inside Bloomberg’s 9,000-engineer org: AI enthusiasm is correlated with *exploratory* work, not *maintenance* work.
		- Sets up later lessons on where AI actually delivers ROI vs. where deployment is fragile.
-
- ## Slide —  *Example 1: Uplift agents*
	- **Visual layout**
		- Left: text block with scenario + challenges.
		- Right: white-line illustration of a small robot pushing a lever (symbolizing “lifting” / “upgrading” code).
		- Footer includes attribution: *Source of generated images: ChatGPT & Google Gemini.*
	- **Core narrative (integrated with your notes)**
		- Vision: **tickets auto-resolved the moment they appear** — engineer opens a bug, and there’s already a **PR with the fix** plus the agent’s **reasoning** for *why* the patch took that shape.
		- Intended purpose: free engineers for **creative work**, not repetitive uplift/patching.
	- **Challenges enumerated on slide**
		- **Deterministic verifiability**
		  
		  → Hard to prove an AI-generated patch is *exactly* correct, especially without a robust refactoring engine (you mentioned they lacked a regex-driven or structured refactoring tool).
		- **Time-to-merge**
		  
		  → AI agents increased the *volume* of PRs; humans became the bottleneck.
		- **“What?” harder than “How?”**
		  
		  → Specifying *what* should change is often harder than implementing the change; agents can produce diffs, but defining the patch’s semantic intent is non-trivial.
	- **Operational reality**
		- When uplift agents scaled, **open PR count rose significantly**.
		- **Verification load increased**, slowing merges and increasing review burden.
		- Reinforces that uplift automation is valuable but must be paired with strong guardrails, structured refactoring tools, and automated verification pipelines.
-
- ## Slide —  *Example 2: Incident Response agents*
	- **Visual layout**
		- Left: bullet list of pain points.
		- Right: illustration of an overwhelmed on-call engineer surrounded by dozens of dashboards, charts, alerts, gauges, timers, logs, and graphs swirling around them.
	- **Slide content**
		- **Overwhelming number of alerts**
		- **Hard to find contextual & relevant information**
		- **Understanding contributing factors**
		- **Hard to determine the impact**
		- **…and more**
	- **Interpretive expansion (your comment integrated)**
		- Human responders bring **bias, tunnel vision, and assumption-driven reasoning**—especially under stress.
		- Agents can triage with **systematic breadth**, surfacing factors a human might ignore or prematurely filter out.
		- Advantage: agents don’t fatigue, don’t anchor on the first hypothesis, and can synthesize signals from huge observability surfaces.
	- **Narrative role**
		- Sets up why Bloomberg wants agents in the incident loop: not to replace humans, but to provide an **unbiased, high-context first pass** that cuts through alert noise and accelerates root-cause discovery.
-
- ## Slide —  *How do you evolve the paved path?*
	- **Visual layout**
		- Large, centered question in white text.
		- Sparse black background with a splash of multicolor particulate texture in the upper-right corner (Bloomberg’s design motif).
	- **Interpretive structure**
		- This is a **transition slide**, signaling a move from examples → organizational strategy.
		- The question frames the problem: once many teams want AI, **how do you scale responsibly?**
	- **Your added context (integrated)**
		- Inside Bloomberg, interest quickly exploded:
			- **10+ teams** wanted to build **PR review bots**.
			- **20+ teams** wanted to build **other agentic tools** (triage bots, uplift bots, workflow optimizers, etc.).
		- This created a challenge:
			- Without coordination, you get **duplicate tooling**, inconsistent standards, drift in security posture, and fractured developer experience.
	- **Implied next step**
		- Bloomberg must evolve the “paved path” (their standardized platform & best practices) to include **AI primitives, guardrails, patterns, and governance**, so teams innovate without chaos.
-
- ## Slide —  *How do you evolve the paved path?*
	- **Visual layout**
		- Large, centered question in white text.
		- Sparse black background with a splash of multicolor particulate texture in the upper-right corner (Bloomberg’s design motif).
	- **Interpretive structure**
		- This is a **transition slide**, signaling a move from examples → organizational strategy.
		- The question frames the problem: once many teams want AI, **how do you scale responsibly?**
	- **Your added context (integrated)**
		- Inside Bloomberg, interest quickly exploded:
			- **10+ teams** wanted to build **PR review bots**.
			- **20+ teams** wanted to build **other agentic tools** (triage bots, uplift bots, workflow optimizers, etc.).
		- This created a challenge:
			- Without coordination, you get **duplicate tooling**, inconsistent standards, drift in security posture, and fractured developer experience.
	- **Implied next step**
		- Bloomberg must evolve the “paved path” (their standardized platform & best practices) to include **AI primitives, guardrails, patterns, and governance**, so teams innovate without chaos.
-
- ## Slide —  *Platform Principle*
	- **Visual layout**
		- Four short bullet points, one highlighted in gold (“Golden Paths…”).
		- Black background; white/gold text.
	- **Bullets (expanded with your interpretation)**
		- **“Freedom and Responsibility” with guardrails**
		  
		  → Engineers can innovate, but the platform enforces boundaries so unsafe patterns are hard to reach.
		- **“Golden Paths” with Platform Enablement teams**
		  
		  → Curated best-practice workflows, tooling, and infrastructure that teams *want* to use because they remove friction.
		- **Democratized infrastructure via InnerSource**
		  
		  → Open contribution model so internal tools evolve through community, not gatekeeping.
		- **Service abstraction and strong contracts**
		  
		  → Clear APIs, standardized behaviors, and predictable integrations.
	- **Intent (your note integrated)**
		- Core philosophy: **make the right thing easy and the wrong thing ridiculously hard.**
		  
		  → Golden paths = paved, safe, fast.
		  
		  → Off-path = friction, reviews, warnings, incompatibility, or simply impossible.
	- **Narrative role**
		- Establishes the principled foundation for AI adoption across thousands of engineers: consistent patterns, trusted infrastructure, and platform-backed safety.
-
- ## Slide —  *The paved path (expanded)*
	- **Visual layout**
		- Four bullets, same structure as previous slide, now with an added principle about demos vs. production.
	- **Bullets (with your added context)**
		- **Models (LLMs) via a Gateway**
		  
		  → Central entry point; ensures visibility, governance, and safe model usage.
		- **Tool discovery (MCP Directory) via a Hub**
		  
		  → Teams find and reuse existing MCP tools instead of rebuilding; encourages collaboration between teams (e.g., Team A + Tool B owners).
		- **Tool creation and deployment via a PaaS**
		  
		  → Standardized scaffolding for MCP-compliant tools; consistent packaging, tracing, contracts.
		- **Demos are easy; production begets quality control**
		  
		  → They intentionally lower the friction for **proof-of-concepts** but raise the bar for **productionization** with reviews, guardrails, validation, and compliance checks.
	- **Intent**
		- Create a **fast lane for experimentation** but a **safety-critical gate** for real workloads—so innovation isn’t slowed, but operational risk stays low.
-
- ## Slide —  *Internal community and leadership*
	- **Visual layout**
		- Four bullets; the third includes two sub-bullets.
		- Standard black-background/white-text Bloomberg slide.
	- **Content (expanded with your context)**
		- **Established cross-organization tech communities (10+ years)**
		  
		  → Longstanding “horizontal” groups where engineers self-organize around shared interests.
		- **Bootstrapped “Engineering AI Productivity” community**
		  
		  → A new domain-specific community formed to accelerate AI adoption and share patterns.
		- **Results**
			- **De-duplicate efforts and shared learning**
			  
			  → Prevent 10 teams from building 10 PR bots.
			- **InnerSource contributions and visiting engineers**
			  
			  → Engineers rotate into other teams to contribute expertise and learn platform patterns.
		- **Leadership workshops (being piloted)**
		  
		  → Targeted at engineering managers who need new frameworks for AI-era leadership.
	- **Your added insight integrated**
		- Bloomberg runs an internal **“champ” program**: passionate engineers band together around emerging technologies and push initiatives forward across org boundaries.
		- A major challenge: **managers in the age of AI often lack experience guiding AI-augmented software teams**.
		  
		  → Their prior knowledge is still valuable, but incomplete.
		  
		  → The community fills this gap by creating a peer-driven space where modern AI practices spread faster than top-down training alone.
-
- ## Slide —  *Brian Eno quote (judgement over skill)*
	- **Visual layout**
		- Two-paragraph quotation in white text; the word **judgement** highlighted in green.
		- Attribution bottom-right: *Brian Eno — Interview in ‘The Wire’ with Paul Schütze (1995)*.
	- **Quotations (structured)**
		- **“The great benefit of computer sequencers is that they remove the issue of skill, and replace it with the issue of judgement.”**
		- …
		- **“So the question becomes not whether you *can* do it—any drudge can do it with a few days at a computer.
		  
		  The question is: *Of all the things you can now do, which do you choose to do?*”**
	- **Integrated interpretation (your note)**
		- AI removes many old constraints of *skill* and replaces them with the harder constraint of *judgement*.
		- This shifts the burden toward **deciding**, not **doing**.
		- For ICs and leaders, this moment forces a return to fundamentals:
			- What is high-quality software?
			- What tradeoffs matter now?
			- What should we stop doing because AI can?
			- What should we start doing because human taste and standards now matter more?
	- **Narrative role**
		- Opens a philosophical close: AI accelerates execution, so engineering excellence increasingly lives in **choice, taste, framing, quality, and discipline** rather than raw implementation effort.
-