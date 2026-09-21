alias:: [[AWS/Secrets Manager/Secret/Single-Value]]
logseq-entity:: [[Logseq/Entity/Software/Option]]

- # [[AWS/Secrets Manager/Secret]] stored as plaintext
	- The [[AWS/Secrets Manager/Secret]] field holding one raw string, no internal structure — an API key, OAuth token, certificate, private key. AWS's console calls this the **Plaintext** tab. [[Answer/Official]] from [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html): *"choose Other type of secret. In Key/value pairs, either enter your secret in JSON Key/value pairs, or choose the Plaintext tab and enter the secret in any format."*
	- **codekiln's term for this: single-valued.**
	- **Setting it:** console → Store a new secret → Other type of secret → Plaintext tab. CLI → `aws secretsmanager create-secret --name <name> --secret-string '<raw value>'` with any non-JSON string. ([Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html))
	- **Accepted values:** any string, up to 64 KB. [CreateSecret API reference](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html): *"Type: String Length Constraints: Minimum length of 1. Maximum length of 65536."* Compare [[AWS/Secrets Manager/Secret/KeyValue]] — the same field, holding a JSON object instead of a bare string.
