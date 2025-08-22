# [Configuring settings for the AWS CLI - AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
	- ## [Configuration file](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
		- Sample config file at `~/.aws/config`
			- ```toml
			  [default]
			  region = us-east-1
			  output = json
			  
			  [profile mySpecialRole]
			  source_profile = default
			  role_arn = arn:aws:iam::123456789012:role/roleB
			  region = us-east-1
			  
			  ```