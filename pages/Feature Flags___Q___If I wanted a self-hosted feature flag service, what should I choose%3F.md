logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Feature Flags/25/04/Market Overview Deep Research]]
via:: [[Statsig/Q/Is Statsig open source in such a way I can self host it without licensing it from them?]]

- # If I wanted a self-hosted [[Feature Flags]] service, what should I choose?
	- ## [[AI Answer]]
		- **Short answer:** Flagsmith, unless one of the cases below fits better. It has a permissive license (BSD-3), a polished UI, a Terraform provider, and Docker Compose and Helm installs. Whichever you pick, call it from your code through [[OpenFeature]] so you can change backends later without touching call sites.
		- **Pick by what you need:**
			- **Just flags, with a UI, and no license worries:** [Flagsmith](https://github.com/Flagsmith/flagsmith). It was also the top self-hosted pick in [[Feature Flags/25/04/Market Overview Deep Research]].
			- **The biggest community and most rollout strategies:** [[Unleash]]. Its open-source edition moved from Apache 2.0 to **AGPL-3.0** on 2026-05-26. Running it unmodified for internal use is fine. If you modify it and expose it over a network, AGPL requires you to publish your changes.
			- **Experiments as well as flags, the closest replacement for Statsig:** [GrowthBook](https://github.com/growthbook/growthbook). The core is MIT, the `enterprise` directories are under a commercial license, and it needs a database for analysis.
			- **Flags kept in Git and reviewed like code:** [Flipt](https://github.com/flipt-io/flipt). Version 2 is under the Fair Core License (`FCL-1.0-MIT`), which is source-available rather than open source. Some features need a license key, and each release becomes MIT two years after it ships.
			- **No UI, flags in a file or in Git, as light as possible:** [flagd](https://github.com/open-feature/flagd), OpenFeature's own Apache-2.0 flag daemon.
			- **Product analytics in the same tool:** [PostHog](https://github.com/PostHog/posthog), which includes feature flags. Self-hosting it is a much bigger job than any of the options above.
		- **Licenses and activity on GitHub, checked [[2026-11-24 Tue]]:**
			- Unleash: AGPL-3.0, 14.3k stars.
			- Flagsmith: BSD-3-Clause, 9.4k stars.
			- GrowthBook: MIT core with an enterprise license, 8.7k stars.
			- Flipt: FCL-1.0-MIT, 5.0k stars, v2.14.2 released 2026-11-18.
			- FeatBit: MIT, 2.0k stars.
			- Flagr: Apache-2.0, 2.6k stars.
			- flagd: Apache-2.0, 1.0k stars.
			- All of these had commits in November 2026.
		- **Common caveat:** Unleash, Flagsmith and GrowthBook all keep some features for their paid editions, typically SSO, fine-grained roles and audit logs. Check each one's edition comparison before you commit to it.
