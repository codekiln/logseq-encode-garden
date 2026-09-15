tags:: [[ChatGPT/Deep Research]]
date-created:: [[2026-09-15 Tue]]
see-also:: [[Claude/Code]], [[Codex/CLI]], [[GitHub/CoPilot/CLI]], [[CursorAI/CLI]], [[CursorAI/Usage-Based Pricing]]

- # Autonomous Usage-Quota Discovery for Claude Code, Codex CLI, GitHub Copilot CLI, and Cursor Agent
	- ## Executive finding
		- As of September 15, 2026, there is almost already a single command-line tool for this. The strongest match is `aistat`, an open-source Go CLI whose explicit purpose is to report and normalize usage limits for [[Claude/Code]], OpenAI Codex, and [[GitHub/CoPilot/CLI]]. It emits JSON by default, has a human-readable mode, reads the credentials already established by the upstream tools, and normalizes provider-specific quotas into common fields such as `used_percent`, `remaining_percent`, and `resets_at`. It is also explicitly designed for usage-aware agent routing. [^1]
		- The missing provider is Cursor. No maintained CLI covers all four. Cursor is the hardest of the four for an individual subscription: current Cursor CLI documentation still does not expose a command for plan/billing quota, and a Cursor staff response specifically says the interactive `/usage` command reports activity statistics rather than plan spending. Cursor does expose spending and detailed usage APIs for organizational accounts, while individual users are still directed to the Cursor Settings/web usage UI. [^2]
		- Overall recommendation: fork or extend `aistat`, add a Cursor provider, and gradually replace its private-endpoint adapters with supported local protocols/public APIs where practical. That gets to one agent-friendly executable with the least work.
		- Best currently identifiable collection path per provider:
			- [[Claude/Code]]
				- Best autonomous source: Claude status-line JSON; optionally Anthropic's private OAuth usage endpoint for true one-shot polling.
				- What you can get: 5-hour %, 7-day %, reset times; the private endpoint can expose additional model-scoped limits.
				- Requires an LLM request?: status-line cache needs no new request, but must have been refreshed by a session.
				- Stability: supported for status line; private for the direct endpoint.
			- [[Codex/CLI]]
				- Best autonomous source: `codex app-server` account-rate-limit RPC.
				- What you can get: window percentages, durations, resets, plan, credits/reset credits.
				- Requires an LLM request?: no.
				- Stability: best programmatic route.
			- [[GitHub/CoPilot/CLI]]
				- Best autonomous source: GitHub billing REST API; `aistat` currently uses Copilot account/quota data for normalization.
				- What you can get: monthly AI-credit usage; legacy premium-request quota on applicable accounts.
				- Requires an LLM request?: no.
				- Stability: public API for billing data.
			- Cursor Agent ([[CursorAI/CLI]])
				- Best autonomous source: Enterprise Admin API; otherwise authenticated browser automation of Cursor Settings.
				- What you can get: billing-cycle spend/API events for enterprise; rendered usage pools for individual accounts.
				- Requires an LLM request?: no.
				- Stability: public API for eligible orgs; browser fallback for individuals.
		- One important design point: these providers no longer meter in the same unit. Claude and Codex expose rolling usage windows as percentages; current Copilot uses monthly GitHub AI Credits based on model/token cost; Cursor uses model-priced usage pools and billing-cycle spend. A correct abstraction should therefore be "quota windows/resources," not "tokens remaining." [^3]
	- ## The existing tool is very close to what you want
		- `aistat` deserves serious consideration before implementing from scratch. Its README describes exactly the orchestration use case: one terminal command that reads Claude, Codex, and Copilot usage, produces normalized machine-readable JSON, and can be consumed by agents to decide where to route work. Its recent releases added multi-account Codex support, model-scoped Claude limits, current Copilot AI-credit support, native Windows support, watching/notifications, and an agent skill. [^4]
		- Its basic interface is essentially:
			- ~~~bash
			  # JSON by default
			  aistat usage
			  # One provider
			  aistat usage claude
			  aistat usage codex
			  aistat usage copilot
			  # Bypass the usage cache
			  aistat usage --refresh
			  # Human-readable display
			  aistat -h
			  ~~~
		- The normalized contract described by the project gives each limit fields such as:
			- ~~~json
			  {
			    "used_percent": 71,
			    "remaining_percent": 29,
			    "resets_at": "2026-09-17T...",
			    "reset_after_seconds": 190800
			  }
			  ~~~
		- For Claude and Codex it can represent multiple accounts, and the project explicitly positions this JSON as the primitive an orchestrator can inspect before selecting an agent. It ships examples that choose a provider based on quota headroom and a Claude Code skill that lets an agent autonomously issue the read-only usage checks. [^4]
		- As of the currently indexed release history, `aistat` v2.4.0 is the latest release shown. Copilot's migration to AI-credit billing was specifically addressed in v2.2.0, whose release notes say the Copilot provider was changed to report AI-credit usage. [^6]
		- ### How `aistat` gets the numbers
			- `aistat` does not start each coding agent and scrape its TUI. It reads the credential material those tools have already established and performs authenticated read-only requests in parallel. Its current documentation/source history shows adapters for:
				- Claude -> Anthropic OAuth usage/profile services
				- Codex -> ChatGPT/Codex usage backend
				- Copilot -> GitHub/Copilot account or billing usage service
			- It translates the results into its common limit structure and caches provider results briefly so an agent loop does not hammer the services. [^7]
			- Advantage: `aistat usage` is a cheap observation operation rather than a model invocation.
			- Disadvantage: some of these endpoints are implementation details rather than vendor-promised public APIs. The repository itself has already had to adapt to upstream changes—for example, Copilot's 2026 move to AI Credits and changes to Claude's usage response. That is exactly why it's worth keeping `aistat`'s normalization/rendering architecture but introducing a distinction between supported, local-protocol, and private collectors. [^6]
			- There is an `agent-usage` repository derived from `aistat`, but its documented provider architecture remains Claude/Codex/Copilot rather than solving the Cursor gap. No credible current CLI covers all four providers in one executable. [^9]
			- For this use case, `aistat` is therefore not merely prior art; it is probably the right codebase to extend.
	- ## Claude Code has several viable paths
		- Claude is unusual because Anthropic now exposes the information you care about directly in the supported Claude Code status-line protocol.
		- Claude Code's official documentation says the JSON sent to a configured status-line command contains:
			- `rate_limits.five_hour.used_percentage`
			- `rate_limits.five_hour.resets_at`
			- `rate_limits.seven_day.used_percentage`
			- `rate_limits.seven_day.resets_at`
		- The percentage is explicitly defined as 0–100 consumed, and the reset values are Unix timestamps. [^3]
		- So the lowest-risk Claude adapter is not TUI scraping at all. Configure a tiny status-line command that copies the incoming JSON into your unified usage tool's cache:
			- ~~~json
			  {
			    "statusLine": {
			      "type": "command",
			      "command": "~/.local/bin/ai-usage-claude-statusline"
			    }
			  }
			  ~~~
		- Conceptually, the receiving program does nothing more complicated than:
			- ~~~sh
			  #!/bin/sh
			  mkdir -p "$HOME/.cache/ai-usage"
			  tmp="$HOME/.cache/ai-usage/claude.json.tmp"
			  cat > "$tmp"
			  mv "$tmp" "$HOME/.cache/ai-usage/claude.json"
			  ~~~
		- Your `ai-usage` process can then extract fields such as `five_hour.used_percent`/`resets_at` and `seven_day.used_percent`/`resets_at` from `.rate_limits.*`.
		- This has excellent security properties: your collector never needs to extract or duplicate Claude's OAuth credential. It simply receives data Claude Code already intends to expose to user-configured status-line programs. [^3]
		- One important limitation: those rate-limit fields are populated from Claude Code's interaction with the service, so the status-line approach is best regarded as a latest-known snapshot, not necessarily an independently refreshed on-demand query. Anthropic's documentation notes that rate-limit data is available for applicable Claude.ai subscribers/gateway configurations and may be absent until Claude Code has received the relevant API response. [^3]
		- ### The built-in interactive command
			- Claude also has the obvious human-facing source: `/usage`. Anthropic documents `/usage` as showing session cost, plan usage limits, and activity statistics; on Pro, Max, Team, and Enterprise subscriptions it includes a breakdown of what counts against those plan limits. `/cost` and `/stats` are aliases. [^12]
			- That gives a robust fallback: spawn a PTY, launch `claude`, wait for the prompt, send `/usage`, parse the rendered screen, then terminate. PTY automation should be the fallback rather than the primary implementation, because screen layouts, ANSI sequences, and wording are inherently less stable than structured JSON.
		- ### Private and experimental Claude mechanisms
			- There are two additional mechanisms worth knowing about if you need a fresh one-shot query even when Claude Code is not running.
			- First, `aistat` currently queries Anthropic's OAuth usage service using the credentials already established by Claude Code. That is how it can return fresh Claude usage immediately from a normal terminal command. It also surfaces model-scoped weekly windows when the Anthropic response contains them. [^1]
			- This appears to provide richer information than the status-line's basic five-hour/seven-day pair, but it is not an Anthropic-documented public developer API. Classification: functionality excellent, automation excellent, stability medium/low, credential risk higher. It belongs behind an adapter so that endpoint changes do not affect your public CLI contract.
			- Second, investigation in the official Claude Code repository has surfaced a stream/control mechanism using a usage control request of this form:
				- ~~~json
				  {
				    "type": "control_request",
				    "request": {
				      "subtype": "get_usage",
				      "skip_behaviors": true
				    }
				  }
				  ~~~
			- The same discussion references an Agent SDK surface explicitly named along the lines of `usage_EXPERIMENTAL_MAY_CHANGE_DO_NOT_RELY_ON_THIS_API_YET()`. That naming is a very clear signal not to treat it as a stable API contract yet. [^14]
			- Still worth prototyping. If it returns the same data as `/usage` without generating a model response, it could eventually become the ideal Claude collector. Until Anthropic documents/stabilizes it, however, the status-line sink is the best supported implementation and the OAuth endpoint is the most useful pragmatic one-shot implementation.
			- Preferred Claude source ladder:
				- 1. Fresh private OAuth usage query — best one-shot behavior today.
				- 2. Supported status-line cached JSON — best stability/security.
				- 3. Experimental `get_usage` control request — monitor for stabilization.
				- 4. PTY + `/usage` — universal fallback.
				- 5. Browser scraping — unnecessary in normal cases.
	- ## Codex is the cleanest provider programmatically
		- Codex appears to have the best architecture for exactly this kind of integration because the CLI contains an app-server interface that exposes account information programmatically.
		- The OpenAI-maintained Codex implementation has an account-rate-limits operation whose response includes structured snapshots rather than rendered terminal text. Tests in the Codex implementation show the underlying usage response containing a primary rate-limit window with fields including:
			- ~~~json
			  {
			    "used_percent": 88,
			    "limit_window_seconds": 1800,
			    "reset_after_seconds": 600,
			    "reset_at": 1735693200
			  }
			  ~~~
		- and the app-server transforms the backend representation into client-facing data such as:
			- ~~~json
			  {
			    "limitId": "codex",
			    "planType": "team",
			    "primary": {
			      "usedPercent": 42,
			      "windowDurationMins": 60,
			      "resetsAt": 2000000000
			    }
			  }
			  ~~~
		- The same account-rate-limit response can carry a map of limits by ID and rate-limit-reset-credit information. [^15]
		- The relevant app-server request has been exposed as `account/rateLimits/read`, with a response conceptually shaped like:
			- ~~~json
			  {
			    "rateLimits": {
			      "limitId": "codex",
			      "primary": {
			        "usedPercent": 25,
			        "windowDurationMins": 300,
			        "resetsAt": "178..."
			      },
			      "secondary": {
			        "usedPercent": 18,
			        "windowDurationMins": 10080,
			        "resetsAt": "178..."
			      }
			    }
			  }
			  ~~~
		- The important implementation lesson is not to name these fields `five_hour` and `weekly` in your internal schema. Codex reports the actual window duration, and limits can vary by account/plan or evolve over time. Interpret 300 minutes as five hours and 10080 as seven days for display, but preserve the raw duration. The Codex implementation itself treats account rate limits as structured provider data rather than hard-coded plan assumptions. [^15]
		- Conceptually, your adapter can:
			- ~~~text
			  spawn: codex app-server
			  transport: local stdio JSON-RPC
			  initialize connection
			  request:
			      method = account/rateLimits/read
			      params = {}
			  normalize response
			  terminate process
			  ~~~
		- This is preferable to copying Codex authentication tokens into your own HTTP client because the Codex process itself owns authentication and backend compatibility. The underlying current Codex implementation shows why that matters: its own account-rate-limit code makes an authenticated request to an internal Codex usage route and supplies both the ChatGPT bearer token and account identifier; the implementation currently tests a route named `/api/codex/usage`. [^15]
		- In other words, `your tool -> codex app-server -> authenticated Codex backend -> quota information` is much safer architecturally than `your tool -> parse ~/.codex/auth.json -> duplicate internal HTTP request`.
		- `aistat` currently does the latter style of integration and therefore proves that direct querying works, but using the Codex app-server gives a cleaner credential boundary. `aistat`'s release history also demonstrates why window duration must remain dynamic: it had to change its labeling logic so that non-five-hour account windows were not incorrectly classified by their position in the response. [^6]
		- OpenAI's current customer-facing documentation confirms that Codex/Work allowances can involve both five-hour and weekly windows and tells users to inspect Settings → Usage for the current percentage/reset state. It also makes clear that actual allowance consumption depends on task/model/settings rather than corresponding to a fixed number of tokens or messages. [^17]
		- That means the structured percentage is precisely the right thing for your unified tool to expose:
			- ~~~json
			  {
			    "provider": "codex",
			    "limits": [
			      {
			        "id": "codex:300m",
			        "window_seconds": 18000,
			        "used_percent": 25,
			        "remaining_percent": 75,
			        "resets_at": "..."
			      },
			      {
			        "id": "codex:10080m",
			        "window_seconds": 604800,
			        "used_percent": 18,
			        "remaining_percent": 82,
			        "resets_at": "..."
			      }
			    ]
			  }
			  ~~~
		- A TUI `/status` scrape can remain as a compatibility fallback, but should not be used while the structured account-rate-limit interface is available.
	- ## Copilot has a public API, but billing changed substantially this year
		- [[GitHub/CoPilot/CLI]] requires special handling because its billing model changed in June 2026.
		- Current GitHub documentation says Copilot usage is now measured in GitHub AI Credits, with cost determined by model and token usage. Copilot CLI is explicitly among the features that consume AI Credits. Current individual plans receive monthly AI-credit allowances, and the allowance resets at 00:00 UTC on the first day of each calendar month. GitHub's current plan page lists base plus flex allocations rather than the old premium-request model. [^18]
		- There are legacy exceptions: GitHub documents a legacy premium-request regime for some existing annual subscribers who remained on that billing system after the June 1, 2026 migration. The abstraction therefore needs to tolerate both:
			- ~~~text
			  Copilot current account:
			      resource = ai_credits
			      window   = calendar month
			  Copilot legacy account:
			      resource = premium_requests
			      window   = calendar month
			  ~~~
		- rather than assuming "Copilot means premium requests." [^19]
		- ### The strongest supported API
			- GitHub now has a documented REST endpoint specifically for an individual user's AI-credit billing usage. The current Billing Usage documentation exposes `GET /users/{username}/settings/billing/ai_credit/usage`, and says user billing endpoints apply when Copilot is billed directly to that user's personal account. Fine-grained credentials need user `Plan: read` permission. Organization- or enterprise-billed Copilot usage must instead be queried using the corresponding organization/enterprise endpoints. [^20]
			- That means an adapter can be implemented using `gh` without managing the GitHub token itself:
				- ~~~bash
				  USER="$(gh api user --jq .login)"
				  gh api \
				    -H 'X-GitHub-Api-Version: 2026-03-10' \
				    "/users/$USER/settings/billing/ai_credit/usage?year=2026&month=9"
				  ~~~
			- The API response is structured into `usageItems` and includes attributes such as product, SKU, model, unit type, quantity, and billing amounts. GitHub's example for the AI-credit endpoint reports `unitType: "ai-credits"`. [^20]
			- For accounts that remain under premium-request billing, GitHub still documents `GET /users/{username}/settings/billing/premium_request/usage`, with the same `Plan: read` requirement. [^22]
			- This is the most supportable long-term Copilot implementation.
			- There is a wrinkle: these billing-report endpoints are excellent for the amount consumed, but your agent also wants the remaining percentage of the included entitlement. GitHub's entitlement can include a base allocation plus a flex allocation, and the flex amount is conceptually subject to change, so it's worth avoiding permanently hard-coding the current plan table into your binary. [^23]
			- The ideal Copilot collector therefore combines billing usage + current entitlement = used / total / remaining / percentage.
		- ### The Copilot CLI's own server protocol
			- There is another interesting, less documented route. The current Copilot CLI can be launched as a stdio server:
				- ~~~bash
				  copilot --server --no-auto-update --log-level error --stdio
				  ~~~
			- and current behavior reported in the official GitHub Copilot CLI repository shows a JSON-RPC call:
				- ~~~json
				  {
				    "jsonrpc": "2.0",
				    "id": 2,
				    "method": "account.getQuota",
				    "params": {}
				  }
				  ~~~
			- returning quota snapshots with fields such as entitlement, used amount, remaining percentage, and a reset-date field. [^24]
			- This is attractive because it uses the Copilot CLI's own authenticated session and avoids credential extraction. It's not worth making it the primary source today, for two reasons.
			- First, the current Copilot CLI still has an open feature request specifically asking it to expose monthly AI-credit quota and usage; the issue notes that the CLI's `/usage` command currently gives per-session AI-credit usage rather than the monthly allowance shown in IDEs. [^25]
			- Second, a recent Copilot CLI bug report shows `account.getQuota` returning `resetDate` equal to the query timestamp rather than the actual quota reset timestamp. The web UI showed the correct monthly reset while the JSON-RPC result did not. [^24]
			- Copilot source order:
				- 1. Official GitHub AI-credit billing REST API.
				- 2. Current entitlement from account metadata / documented plan data.
				- 3. `aistat`'s existing Copilot adapter.
				- 4. `copilot --server --stdio` + `account.getQuota`.
				- 5. Browser/IDE display as verification.
				- 6. Never use interactive `/usage` as the monthly-quota source.
			- `aistat` is particularly useful here because v2.2.0 explicitly migrated its Copilot provider to AI-credit reporting. Its current documentation also requires a GitHub credential with appropriate user access, which aligns with the GitHub billing APIs. [^6]
			- One extra benefit of the 2026 billing model is that the normalization can become more informative than a bare percentage, for example:
				- ~~~json
				  {
				    "provider": "copilot",
				    "limits": [
				      {
				        "id": "ai_credits",
				        "period": "month",
				        "used": 4312.6,
				        "limit": 7000,
				        "unit": "ai_credit",
				        "used_percent": 61.61,
				        "remaining": 2687.4,
				        "remaining_percent": 38.39,
				        "resets_at": "2026-10-01T00:00:00Z"
				      }
				    ]
				  }
				  ~~~
			- The numbers above are illustrative rather than an assertion about a particular account; the schema is what matters. Current GitHub documentation defines the monthly reset cadence and AI-credit unit. [^23]
	- ## Cursor is the missing adapter
		- Cursor is where the unified CLI requires genuinely new work.
		- Current Cursor Agent documentation documents interactive mode, print mode, JSON output for agent responses, an ACP server, session management, models, and other agent controls, but no documented CLI parameter or subcommand exists for account-plan quota. [^27]
		- Cursor does have `/usage` inside its REPL, but this is misleading for the purpose. A Cursor staff response from March 11, 2026 explicitly states that `/usage` reports activity data such as streaks, lines edited, and daily activity rather than plan/monthly billing usage. The same response directed users seeking plan usage to Settings → Usage or the Cursor web settings page. [^2]
		- That means spawning Cursor in a PTY and entering `/usage` will not solve this particular problem — an important difference from Claude.
		- ### Cursor organizational accounts have a real API
			- For eligible organizational accounts, the picture is much better. Cursor's current API overview includes Admin API surfaces for organization pooled usage, usage events, daily usage, spending data, and related billing controls. The overview currently characterizes the Admin API as an Enterprise-team feature. [^29]
			- The documented spending endpoint is `POST /teams/spend`, and Cursor says it returns information for the current billing cycle. Each user's record includes `spendCents`, `overallSpendCents`, `fastPremiumRequests`, `hardLimitOverrideDollars`, `monthlyLimitDollars`, `effectivePerUserLimitDollars`, plus the response's `subscriptionCycleStart`. `overallSpendCents` includes both included and on-demand usage, while `spendCents` represents on-demand spend. [^30]
			- An implementation can therefore do something like:
				- ~~~bash
				  curl -sS \
				    -u "$CURSOR_ADMIN_API_KEY:" \
				    -H 'Content-Type: application/json' \
				    -d '{
				      "searchTerm": "developer@example.com",
				      "page": 1,
				      "pageSize": 25
				    }' \
				    'https://api.cursor.com/teams/spend'
				  ~~~
			- The same Admin API has a detailed usage-events endpoint, `POST /teams/filtered-usage-events`, which Cursor says provides model usage, token consumption, API calls, and costs, aggregated hourly. Its `cost` field can be reconciled against the spending endpoint. [^30]
			- This lets an enterprise implementation expose useful data such as:
				- ~~~json
				  {
				    "provider": "cursor",
				    "billing_cycle": {
				      "started_at": "...",
				      "overall_spend_cents": 3200.750456,
				      "on_demand_spend_cents": 1875.500123
				    },
				    "spend_limit": {
				      "effective_dollars": 50
				    }
				  }
				  ~~~
			- There is one semantic trap: an enforced dollar spending limit is not automatically the same thing as the user's included Cursor subscription allowance. Do not blindly compute `overallSpend / effectivePerUserLimit = plan quota utilization` and label that "Cursor subscription remaining." The API documents the latter as a spending limit, whereas Cursor's product pricing can involve separate usage pools and included usage. [^30] Preserve these as distinct resources in the normalized model.
		- ### Cursor individual accounts need browser automation today
			- For an individual Cursor subscriber, the best reliable source remains the usage dashboard itself. Cursor staff explicitly points users there when asked how to obtain plan percentage from the CLI, and the current CLI docs still do not list a billing-quota command. [^2]
			- This makes a browser adapter reasonable: `ai-usage` launches/reuses an authenticated Playwright browser profile, opens Cursor settings, waits for the usage section, extracts pool name / amount-percentage used / amount-percentage remaining / billing cycle-reset date, normalizes, and caches the result.
			- It's worth scraping the semantic rendered UI, not CSS class names — anchor to text such as "Usage," "Included," "On-demand," "Resets," or current pool names, and keep the entire Cursor parser behind fixtures/tests.
			- An even better development technique is to run Playwright with network observation while opening the usage page and determine whether the dashboard itself calls a stable JSON resource. If so, you can experimentally implement a second Cursor collector: `cursor-browser` (supported UX, slower but robust to backend auth) as the primary, with `cursor-private-api` (faster, but explicitly unstable) as an optional fast path.
			- It's not worth shipping a reverse-engineered Cursor endpoint as the sole implementation unless Cursor documents it. The 2026 product model is changing enough that the rendered web UI is the safer fallback contract. Cursor's current pricing documentation, for example, describes distinct Cursor Models and Other Models consumption and on-demand usage rather than a single universal token counter. [^34]
			- A browser collector has another important security advantage: you do not need to discover, extract, or persist Cursor's private session credentials. A dedicated persistent browser profile can own authentication while the scraper only receives the values displayed to the account owner.
	- ## A unified design that will survive provider changes
		- Build this as a quota-resource abstraction, not a provider-specific "5h/week" object. A useful output contract would look like this:
			- ~~~json
			  {
			    "schema_version": 1,
			    "checked_at": "2026-09-15T14:21:17-04:00",
			    "providers": {
			      "claude": {
			        "account": "me@example.com",
			        "plan": "max",
			        "source": "oauth_usage",
			        "observed_at": "2026-09-15T18:21:16Z",
			        "limits": [
			          {
			            "id": "five_hour",
			            "kind": "rolling_quota",
			            "unit": "percent",
			            "used_percent": 72,
			            "remaining_percent": 28,
			            "resets_at": "2026-09-15T21:03:00Z"
			          },
			          {
			            "id": "seven_day",
			            "kind": "rolling_quota",
			            "unit": "percent",
			            "used_percent": 41,
			            "remaining_percent": 59,
			            "resets_at": "2026-09-19T04:11:00Z"
			          }
			        ]
			      },
			      "codex": {
			        "source": "app_server",
			        "limits": [
			          {
			            "id": "codex-primary",
			            "kind": "rolling_quota",
			            "window_seconds": 18000,
			            "used_percent": 24,
			            "remaining_percent": 76,
			            "resets_at": "..."
			          },
			          {
			            "id": "codex-secondary",
			            "kind": "rolling_quota",
			            "window_seconds": 604800,
			            "used_percent": 13,
			            "remaining_percent": 87,
			            "resets_at": "..."
			          }
			        ]
			      },
			      "copilot": {
			        "source": "github_billing_api",
			        "limits": [
			          {
			            "id": "ai_credits",
			            "kind": "calendar_quota",
			            "unit": "ai_credit",
			            "used": 4312.6,
			            "limit": 7000,
			            "used_percent": 61.61,
			            "remaining": 2687.4,
			            "remaining_percent": 38.39,
			            "resets_at": "2026-10-01T00:00:00Z"
			          }
			        ]
			      },
			      "cursor": {
			        "source": "browser",
			        "limits": [
			          {
			            "id": "other_models",
			            "kind": "billing_cycle_quota",
			            "unit": "provider_defined",
			            "used_percent": 58,
			            "remaining_percent": 42,
			            "resets_at": "..."
			          }
			        ]
			      }
			    }
			  }
			  ~~~
		- The particular percentages above are examples; the important part is preserving the provider's native semantics rather than pretending that every product has a token balance. Claude officially exposes percentage-based five-hour/seven-day limits, Codex exposes window durations and percentages, GitHub now meters Copilot in AI Credits, and Cursor's current product model uses billing/pool concepts. [^3]
		- Add these metadata fields to every observation: `source`, `observed_at`, `fetched_at`, `stale`, `confidence`, `raw_resource_id`, `unit`, `window_seconds`, `resets_at`. That makes an agent able to reason about freshness — a Claude status-line value from four hours ago should not be treated the same as a Codex app-server result fetched two seconds ago.
		- ### The adapter priority to implement
			- The adapters should follow a source hierarchy that prefers proven collectors, then supported/no-secret protocols, then experimental structured APIs, then PTY/browser scraping as a last resort — matching the per-provider ladders already spelled out above (Claude's five-step ladder, Codex's app-server-first order, Copilot's six-step order, and Cursor's Admin-API-then-browser split).
			- The rationale is not just stability. It also minimizes credential custody. Claude's status line, Codex's local app-server, `gh api`, and an authenticated Cursor browser can all let the official client or authentication agent retain ownership of credentials.
		- ### The CLI surface can stay tiny
			- For autonomous agents, deliberately make the main read path boring:
				- ~~~bash
				  ai-usage
				  ai-usage --json
				  ai-usage --refresh
				  ai-usage claude
				  ai-usage codex
				  ai-usage copilot
				  ai-usage cursor
				  ~~~
			- Then:
				- ~~~bash
				  ai-usage --json | jq '
				    .providers
				    | to_entries
				    | map({
				        provider: .key,
				        min_remaining:
				          ([.value.limits[].remaining_percent // 100] | min)
				      })
				    | sort_by(-.min_remaining)
				  '
				  ~~~
			- gives an orchestrator a deterministic routing primitive.
			- Internally, expose diagnostics separately as `ai-usage doctor`, with output along these lines:
				- ~~~text
				  Claude
				    auth:       found
				    source:     oauth_usage
				    fallback:   statusline
				    last fetch: 8s ago
				  Codex
				    auth:       codex app-server
				    source:     app_server
				    last fetch: 2s ago
				  Copilot
				    auth:       gh
				    source:     github_billing_api
				    billing:    ai_credits
				  Cursor
				    admin API:  unavailable
				    browser:    authenticated
				    source:     browser
				  ~~~
			- That is much more useful to an agent than silently returning null.
		- ### Forking `aistat` is the shortest route
			- The architecture described by `aistat` is already close to what's needed: one provider package per service, credential discovery isolated from normalization, common limit types, caching, JSON-first output, and failures returned independently so one unavailable provider does not prevent the other results. Its maintainers have explicitly described that adapter pattern as the intended way to add more quota providers. [^36]
			- The minimal extension would therefore be conceptually:
				- ~~~text
				  internal/providers/
				      claude/
				      codex/
				      copilot/
				      cursor/       <-- add
				  internal/providers/cursor/
				      cursor.go
				      admin.go
				      browser.go
				      normalize.go
				      testdata/
				  ~~~
			- with something such as:
				- ~~~go
				  type Source string
				  const (
				      SourceAdminAPI Source = "admin_api"
				      SourceBrowser  Source = "browser"
				  )
				  type CursorUsage struct {
				      Source Source
				      Limits []providers.Limit
				  }
				  ~~~
			- Then source selection: if `CURSOR_ADMIN_API_KEY` is present, use the Admin API; otherwise, if an authenticated browser profile is available, use the browser usage collector; otherwise return a clear actionable error.
			- It's worth not making Playwright a required dependency of the core static Go binary. Instead, treat browser collection as a small helper process or optional plugin: `aistat` execs `aistat-cursor-browser`, which owns the Playwright/Chromium dependency. That preserves one top-level command without turning a small quota utility into a browser-distribution package.
			- The result is almost exactly the system described at the outset: one cheap command an AI agent can invoke before choosing a coding backend, returning the latest available headroom without consuming another model turn merely to ask, "How much quota do I have left?"
	- ## Practical recommendation
		- The strongest implementation path today is not to build four independent scrapers. Start from `aistat`, which already gives three providers and already defines the machine-readable normalization and agent-routing behavior wanted. [^4]
		- For Claude, retain its current fresh OAuth collector if accepting reliance on an undocumented endpoint, but add the official status-line JSON collector as a supported/no-secret fallback. Claude Code itself exposes exactly the five-hour and seven-day percentages and reset timestamps needed. [^3]
		- For Codex, replace or supplement direct backend access with the Codex app-server account-rate-limit RPC. The Codex implementation already obtains structured window percentages, durations, reset timestamps, account/plan information, and reset-credit data without needing a model completion. That is the cleanest integration of the four. [^15]
		- For Copilot, move toward GitHub's now-public AI-credit billing API, while retaining the existing `aistat` adapter as a compatibility source for entitlement/percentage information and legacy premium-request accounts. Do not use `/usage` for monthly quota: current Copilot CLI behavior treats it as a per-session usage display, and GitHub's billing system changed materially in June 2026. [^22]
		- For Cursor, add two sources. Organizational/Enterprise users should use Cursor's documented spending and usage APIs. Individual subscribers should use a persistent authenticated-browser collector against the Settings usage display until Cursor exposes a supported account-quota API or CLI command. The evidence found indicates that this remains the one significant gap in September 2026. [^30]
		- Comparative reliability hierarchy (structured response? / fresh on each check? / no model call needed? / public or officially supported?):
			- Claude status-line: structured, cached freshness, no model call needed, publicly supported.
			- Claude OAuth usage (private): structured, fresh, no model call needed, not public.
			- Codex app-server protocol: structured, fresh, no model call needed, supported as a local protocol.
			- Codex direct backend: structured, fresh, no model call needed, not public.
			- Copilot GitHub REST: structured, fresh, no model call needed, publicly supported.
			- Copilot server RPC: structured, fresh, no model call needed, undocumented/buggy.
			- Copilot `/usage`: structured but the wrong metric, fresh, not applicable (no true quota), not usable as source of truth.
			- Cursor Admin API: structured, fresh, no model call needed, publicly supported for eligible orgs.
			- Cursor browser: parsed rather than structured, fresh, no model call needed, only a UI contract.
			- Cursor `/usage`: structured but the wrong metric, fresh, not applicable (no true quota), not usable as source of truth.
		- The key architectural insight is that no AI request is needed to discover usage for any of these providers. Claude's supported status-line mechanism can cache the most recent quota state; Codex exposes an account-rate-limit service; GitHub has billing APIs; Cursor organizational accounts have spending APIs; and individual Cursor can be read from its authenticated dashboard. [^3]
		- So the remaining work is mainly normalization and Cursor, not discovering four entirely new systems. The closest existing project already has the right shape and even the agent-routing use case: `aistat` is effectively the proposed tool at three providers out of four. [^1]
	- ## Footnotes
		- [^1]: https://github.com/drogers0/aistat/blob/main/?utm_source=chatgpt.com
		- [^2]: https://forum.cursor.com/t/usage-via-cli/154101?utm_source=chatgpt.com
		- [^3]: https://code.claude.com/docs/en/statusline
		- [^4]: https://github.com/drogers0/aistat/blob/main/README.md?utm_source=chatgpt.com
		- [^6]: https://github.com/drogers0/aistat/releases?utm_source=chatgpt.com
		- [^7]: https://github.com/drogers0/aistat?utm_source=chatgpt.com
		- [^9]: https://github.com/f4ah6o/agent-usage/blob/main/CLAUDE.md?utm_source=chatgpt.com
		- [^12]: https://code.claude.com/docs/en/commands
		- [^14]: https://github.com/anthropics/claude-code/issues/93107?utm_source=chatgpt.com
		- [^15]: https://github.com/openai/codex/blob/main/codex-rs/app-server/tests/suite/v2/rate_limits.rs
		- [^17]: https://help.openai.com/en/articles/20001516?utm_source=chatgpt.com
		- [^18]: https://docs.github.com/en/copilot/get-started/plans?_hsenc=p2ANqtz--BtXIKnB2sT9GeAqg87zfpM_Hr06nSsPMtl4feOmpBxKq-FLsbyQUhkcppI8RilytrnkmJ&utm_source=chatgpt.com
		- [^19]: https://docs.github.com/api/article/body?pathname=%2Fen%2Fenterprise-cloud%40latest%2Fcopilot%2Freference%2Fcopilot-billing%2Frequest-based-billing-legacy%2Fgithub-copilot-premium-requests&utm_source=chatgpt.com
		- [^20]: https://docs.github.com/en/rest/billing/usage?utm_source=chatgpt.com
		- [^22]: https://docs.github.com/en/rest/billing/usage
		- [^23]: https://docs.github.com/api/article/body?pathname=%2Fen%2Fenterprise-cloud%40latest%2Fcopilot%2Fconcepts%2Fbilling%2Fusage-based-billing-for-individuals&utm_source=chatgpt.com
		- [^24]: https://github.com/github/copilot-cli/issues/4504?utm_source=chatgpt.com
		- [^25]: https://github.com/github/copilot-cli/issues/3932?utm_source=chatgpt.com
		- [^27]: https://cursor.com/docs/cli/using?utm_source=chatgpt.com
		- [^29]: https://cursor.com/docs/api?utm_source=chatgpt.com
		- [^30]: https://cursor.com/docs/account/teams/admin-api
		- [^34]: https://cursor.com/docs/models-and-pricing?utm_source=chatgpt.com
		- [^36]: https://github.com/drogers0/aistat/issues/9?utm_source=chatgpt.com