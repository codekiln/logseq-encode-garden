created-by:: [[Person/Drew Gregory]]

- # [Using Proxies to Hide Secrets from](https://www.joinformal.com/blog/using-proxies-to-hide-secrets-from-claude-code/) [[Claude Code]]
- ## Summary
- ### Key Problems Identified
- **Unrestricted access to secrets**: Claude Code has default access to environment variables (like `ANTHROPIC_API_KEY`) and files (.env, etc.) in the project directory, which can include sensitive credentials
- **Limited sandboxing**: Even with containerization and firewalls, typical allowlists (based on domain or IP) may not be sufficient. Risks of data exfiltration via unexpected channels (SSH, npm package publishing, GitHub gists, etc.)
- **Documented risk surface**: The "lethal trifecta" of untrusted content, external communications, and sensitive data supplied to the sandbox drives complexity
- ### Existing Safeguards & Their Shortcomings
- **Devcontainer firewall**: An init script that allows traffic only to certain hosts (e.g., `api.anthropic.com`, `registry.npmjs.org`, VSCode update servers, etc.). Even this includes broad allowances and only filters at the IP level, not necessarily hostname or application-level filtering
- **Environment variables & directory scope**: `.env` files are often `.gitignored` or `.dockerignored`, but simply being out of version control isn't enough; they still leak into the sandbox if in the project directory
- ### Proxy-Based Solution Strategy
  
  1. **Route HTTP traffic through a proxy**
	- Set `HTTP_PROXY` / `HTTPS_PROXY` environment variables so that all HTTP traffic from Claude Code is intercepted
	- Use the sandbox's `httpProxyPort` to intercept HTTP calls from bash commands inside the sandbox (this is separate from the parent process)
	  
	  2. **Use a man-in-the-middle proxy (e.g., mitmproxy)**
	- Run a proxy like mitmproxy locally that intercepts requests and responses. Provide its TLS certificate so node processes trust it
	- Use proxy add-ons: for example, intercept calls to `api.anthropic.com`, replace dummy/invalid API key from Claude with the real key only at the proxy boundary. Thus, Claude works as if its dummy key is valid, never touching the real key
- ### Integrating with Least Privilege & Access Controls
- **Formal Connector & Native Identity Decoupling**: Organizations can use Formal's infrastructure (Connectors, Resources, Native Users) so that Claude Code is never given direct access to admin-level API keys; rather, credentials are injected only when necessary via policy enforcement
- **Fine-grained policies**: Policies can restrict which endpoints Claude Code can access (e.g. path `"/v1/messages"`), log every request, and enforce least privilege
- ### Practical Recommendations
- **Never provide secrets inside the Claude Code process** when avoidable. Use dummy credentials for development, and let proxies or orchestrators add the real ones outside Claude's context
- **Configure proxy/TLS settings properly**: trust custom CAs if needed, include mitmproxy certs for node processes, etc.
- **Be mindful of firewall limitations**: IP-based allowlists are useful but coarse; domain fronting and headers/sni-based routing can subvert policy unless addressed at higher layers
- ### Benefits & Trade-Offs
- **Benefits**
	- Secrets never enter Claude's context window; reduces risk of leaks or misuse
	- Enables policy enforcement, compliance auditing, and least privilege at scale
	- Provides visibility into Claude's external communications
- **Trade-Offs / Challenges**
	- Setup complexity: configuring proxies, TLS, dummy credentials
	- Potential performance overhead or latency
	- Some actions may not be possible if the API key is invalid from Claude's perspective or if endpoints have dynamic behavior
	- Possible complications with authentication or tooling that assumes direct access