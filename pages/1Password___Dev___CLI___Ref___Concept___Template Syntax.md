# [1Password CLI Template Syntax | 1Password Developer](https://developer.1password.com/docs/cli/secrets-template-syntax/)
	- You can create a templated config file that contains [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/), then [use op inject](https://developer.1password.com/docs/cli/secrets-config-files/) to receive a resolved config file that contains the actual secrets.
	- Here's an #Example of a [[1Password/Dev/CLI/Template File]] with enclosed secret references in place of the plaintext secrets: - `config.yml.tpl`
	  id:: 67dfea45-d135-4607-9190-07c6918ce936
		- ```yaml
		  database:
		    host: localhost
		    port: 5432
		    username: {{ op://prod/database/username }}
		    password: {{ op://prod/database/password }}
		  ```