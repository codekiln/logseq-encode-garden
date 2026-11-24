logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Feature Flags/25/04/Market Overview Deep Research]]

- # Is [[Statsig]] open source in such a way I can self host it without licensing it from them?
	- ## [[AI Answer]]
		- **Short answer:** no. The SDKs are open source, but the platform behind them (console, config service, stats engine) is proprietary and runs only as Statsig's cloud service. There is no open-source server to run yourself without a contract.
		- **What is open source:** the client and server SDKs and the forward proxy, all ISC-licensed on GitHub as of [[2026-11-24 Tue]] (`statsig-io/js-client-monorepo`, `statsig-io/statsig-server-core`, `statsig-io/python-sdk`, `statsig-io/statsig-forward-proxy`).
			- The SDKs evaluate flags locally, but they get their rules from Statsig's API.
			- The forward proxy runs inside your network and caches config from Statsig's servers. It does not replace them.
		- **Warehouse Native is not self-hosting:** the experiment analysis runs in your own Snowflake, BigQuery or Databricks, but the control plane is still Statsig's SaaS and needs a paid license.
		- **Ownership:** OpenAI acquired Statsig in 2025. [PostHog reports](https://posthog.com/compare/best-statsig-alternatives) that in May 2026 Amplitude agreed to take over the Statsig brand, platform and customers. That is unconfirmed by Amplitude or Statsig, and no source found says the licensing changed.
		- **Self-hostable alternatives:** [GrowthBook](https://www.growthbook.io/growthbook-vs-statsig) (closest to Statsig for experiments), [[Unleash]], [Flagsmith](https://flagsmith.com/blog/statsig-alternatives) and [PostHog](https://posthog.com/compare/best-statsig-alternatives). Their open-source editions cover the core features, and some enterprise features are paid.
		- **Sources:** Statsig's own [open source](https://www.statsig.com/blog/statsig-open-source) and [cloud-hosted SaaS vs open-source](https://statsig.com/blog/cloud-hosted-saas-vs-open-source-experimentation-platforms) posts. The "cloud-only" claims also come from competitors' comparison pages, so treat their framing with some caution.
