created-by:: [[TrendMicro]]
created-date:: [[2022/08]]

- # [Analyzing the Hidden Danger of Environment Variables for Keeping Secrets | Trend Micro (US)](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html)
	- ## [[AI/Summary]] from #o3
		- ## Rethinking “just use `$ENV_VAR`” for secrets
			- **Baseline**: Environment variables feel convenient—one `-e`, a line in Kubernetes YAML, or a `Dockerfile ENV` and you’re done. No extra infra, works in every language.
			- **Blind spot**: They were designed for *configuration*, not *confidentiality*; nothing in the spec guarantees secrecy ([Trend Micro](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html)).
		- ## Where the risk really lies
			- ### Always-in-clear memory
				- Variables are copied to every process stack and remain in plaintext for the lifetime of the process tree, violating the “short availability” principle of secrets management ([Trend Micro](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html)).
			- ### Easy to scrape
				- `ps -e`, `/proc/$pid/environ`, crash dumps, or a simple memory-dump tool all yield credentials instantly. Most observability/​debug tooling captures env blocks by default .
			- ### Propagates beyond intended scope
				- Child processes, wrapper scripts, and sidecar containers inherit every variable—even if they don’t need it. In container builds the value can end up in intermediate layers; in serverless runtimes it’s injected into *every* invocation context ([Trend Micro](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html)).
			- ### Logs & CI/CD artefacts
				- Panic handlers, verbose flags, or “print env on error” patterns push secrets to log aggregators and build logs; once indexed they’re searchable forever .
			- ### Cloud-wide blast radius
				- Example: a MySQL container’s `MYSQL_ROOT_PASSWORD` obtained from `/proc` grants full DB control; in serverless an AWS CLI token exposed as an env var lets attackers spin up resources or exfiltrate data across the account ([Trend Micro](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html)).
			- ### Actively harvested in the wild
				- Threat groups like **TeamTNT** scan compromised hosts specifically for sensitive env vars; a recent malicious Python package shipped code to steal them at import-time ([Trend Micro](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html)).
		- ## Why your current mitigations aren’t enough
			- **Read-only fs / non-root containers**: env vars are still visible to the running process and anything that can read its memory.
			- **Base-64 encoding**: only obfuscation; attackers dump and decode.
			- **Secrets rotated weekly**: rotation alone doesn’t help if the secret remains in plaintext in the container’s memory for the duration of the pod; attackers can extract (dump) the secret within minutes of the container starting up.
		- ## Secure patterns to adopt instead
			- **Use a secrets manager (Vault, AWS Secrets Manager, GCP Secret Manager)**—fetched at runtime over TLS, held only in process memory, wiped after use.
			- **Short-lived, least-privilege tokens**—prefer IAM roles/OIDC federation to static keys.
			- **Explicit scoping**—inject secrets *only* into the container or function that needs them (init containers > shared env).
			- **Defensive instrumentation**—block `/proc/$pid/environ` in kernels, strip env capture from logs, fail builds on `ENV SECRET=` patterns.
			- **Continuous secret scanning**—treat images, repos, and logs as untrusted; scan for leaked values in CI and at runtime.
		- ## Take-away for DevOps & principal engineers
			- Environment variables trade simplicity for an *unbounded attack surface*.
			- Every time a process spawns a child (e.g., via fork), its environment—including secrets—is inherited, and every debug log or core dump silently widens that exposure.
			- Moving to pull-on-demand secrets, scoped permissions, and memory hygiene closes off entire classes of supply-chain and post-exploitation paths.  
			  
			  > “The best-case scenario is to avoid storing secrets in environment variables completely.” —Trend Micro research team ([Trend Micro](https://www.trendmicro.com/en_us/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html))
	- ## Related Topics
		- [[Secret Management]]
		- [[DevOps/Security]]
		- [[Security]]
		- [[EnvVars]]