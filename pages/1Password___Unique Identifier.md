# [1Password Unique Identifier](https://developer.1password.com/docs/cli/reference/#unique-identifiers-ids)
	- These are different from [[1Password Secret Reference]]s. Using the [[1Password/Dev/op/item/get]] with [[jq]]:
		- ```
		  $ op item get Netflix
		  ID:          t2Vz6kMDjByzEAcq6peKnHL4k3
		  Title:       Netflix
		  Vault:       Private (sdfsdf7werjgdf8gdfgjdfgkj)
		  Created:     6 months ago
		  Updated:     1 month ago by Wendy Appleseed
		  Favorite:    false
		  Version:     1
		  Category:    API_CREDENTIAL
		  Fields:
		    credential:    [use 'op item get sdfsdf7werjgdf8gdfgjdfgkj --reveal' to reveal]
		    type:          other
		  
		  op item get Netflix --format json | jq .id
		  "t2Vz6kMDjByzEAcq6peKnHL4k3"
		  ```
		- > IDs are the most stable way to reference an item. An item's ID **only changes when you move the item to a different vault**. Commands provided with an ID are also faster and more efficient.
			- this kind of **stinks**, because if you have a reference like `"op://Private/t2Vz6kMDjByzEAcq6peKnHL4k3/credential"` in your [[.env]] and you move that [[1Password/Item]] to another vault, it will break ... and you will have **no way to recover the secret** if you don't remember the vault where it went (I think)
		- In [[1Password/Desktop]], if you open a specific [[1Password/Item/Field/Actions/Copy Secret Reference]], if you have any **spaces or other characters that are unsupported in [[1Password Secret Reference]]s** it will copy something like `"op://Private/t2Vz6kMDjByzEAcq6peKnHL4k3/credential"`.  The `t2Vz6kMDjByzEAcq6peKnHL4k3` here is the unique identifier.
			- **Note**: if you remove the spaces or other characters unsupported in 1password secret references, then in the desktop app if you use Copy Secret Reference it will copy a "traditional" secret reference.
			- Unfortunately, this type of secret reference with a Unique Identifier is a bit less convenient than a "typical" [[1Password Secret Reference]]. So, for the purposes of the below, consider that the name is "Netflix API Key" so "Copy Secret Reference" copies `"op://Private/t2Vz6kMDjByzEAcq6peKnHL4k3/credential"` to the clipboard instead of .  The `t2Vz6kMDjByzEAcq6peKnHL4k3` instead of `op://Private/Netflix API Key/credential` as one might expect
			- DONE is there any way to browse to the credential in [[1Password/Desktop]] app given a 1Password Unique Identifier to verify it is correct? **NO, not directly**
				- This is kind of a stinky UI, IMO, because if I want to construct a reference to a secret that whose location is easy to verify, I have to do it manually
			- DONE is there any way to copy the "typical" [[1Password Secret Reference]] which has the vault name, item name, and field name (and is therefore easier to verify easily) instead of the 1Password Unique Identifier using the [[1Password/Desktop]] app? **ANS: NO, not directly**
			- DONE is there any way to reveal the title and the vault of the item given a 1Password Unique Identifier using the [[1Password/Dev/CLI]]?
				- kind of, but it's clunky and requires grep
				- ```bash
				  # Get full item details including vault
				  $ op item get t2Vz6kMDjByzEAcq6peKnHL4k3 | grep -E "^(Vault|Title):"
				  Title:       Netflix API Key
				  Vault:       Private (abcd123)
				  ```
			- DONE is there any way to reveal the "typical" [[1Password Secret Reference]] using the [[1Password/Dev/CLI]] given a Unique Identifier? **ANS: YES**
				- the unique identifier is a code that identifies a [[1Password/Item]], so you need to specify the field
				- `op item get t2Vz6kMDjByzEAcq6peKnHL4k3 --format json --fields credential | jq .reference`
					- `"op://Private/Netflix API Key/credential"`
		- ## What are the Pros and Cons of using 1Password Unique Identifiers in [[1Password Secret Reference]]s relative to using the name of the item in the secret reference?
		  id:: 680376d0-b6d7-4a8e-bf3f-df9f1421c28c
			- Pros of using Unique Identifiers in secret references, e.g. `"op://Private/t2Vz6kMDjByzEAcq6peKnHL4k3/credential"`
				- In the CLI, resolving the item is faster
				- If you rename the item (but keep the vault the same), the unique id still works
			- Cons of using Unique Identifiers in secret references, e.g.
				- If the item stops working in your code, then it takes multiple steps to figure out which item this refers to and whether it is correct
					- method 1 - `op item get <1PasswordUniqueID> | grep -E "^(Vault|Title):"`
						- result:
							- ```
							  Title:       Netflix API Key
							  Vault:       Private (abcd123)
							  ```
					- method 2 - `op item get <1PasswordUniqueID> --format json --fields credential | jq .reference`
						- here, `"op://Private/Netflix API Key/credential"`
						- **WARNING** - using [[1Password/Dev/op/item/get/--format/json]] **will reveal the secret in plain text, unconcealed**
			-
			-
			-