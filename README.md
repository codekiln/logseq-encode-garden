# [logseq-encode-garden](https://codekiln.github.io/logseq-encode-garden/)

My little [Knowledge Garden](https://codekiln.github.io/logseq-encode-garden/#/page/knowledge%2Fgarden)

## Ask My Agent Anything About Me

Want to get to know me? Clone this repo and ask my agent questions about me,
answered from the garden's own pages and journals:

```bash
mise run ask-my-agent-anything-about-me
```

That asks which AI agent you have — Claude Code, Codex, Cursor, or GitHub
Copilot — sets up that tool's skill, and starts it. Skip the prompt with
`--tool claude|codex|cursor|copilot`. GitHub Copilot has a free tier; the others
need a paid plan.

No [mise](https://mise.jdx.dev/)? Open this folder in any of those tools and just
ask — the AI configuration ships with the garden, including an
`ask-my-agent-anything-about-me` skill that teaches the agent how to answer and
cite its sources.

New to all of this? The step-by-step
[Ask My Agent Anything About Me](https://codekiln.github.io/logseq-encode-garden/#/page/My%2FAI%2FAgent%2FAsk%20My%20Agent%20Anything%20About%20Me)
guide walks you through installing everything from scratch.
