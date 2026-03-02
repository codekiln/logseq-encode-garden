- [Declarative secrets, every environment, any provider | SecretSpec](https://secretspec.dev/)
	- `secretspec.toml` declares which secrets your application needs and their requirements
	- ```toml
	  [project]
	  name = "my-app"
	  revision = "1.0"
	  
	  [profiles.default]
	  DATABASE_URL = { description = "PostgreSQL connection string", required = true }
	  REDIS_URL = { description = "Redis connection string", required = false }
	  TLS_CERT = { description = "TLS certificate", as_path = true }
	  ```
	- you can define providers
		- [[Linux/keyring]]
		- [[dotenv]]
		- [[1Password]]
		- etc
	- [[SDK]] in [[Rust]] [Rust SDK | SecretSpec](https://secretspec.dev/sdk/rust/)
		- right now other languages are just a sparkle in their eye, perhaps never to come?
	- [[Via]]
		- [[devenv/Blog/25/07/Announcing SecretSpec]]