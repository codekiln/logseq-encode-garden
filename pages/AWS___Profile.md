- An **AWS profile** is a named set of configuration and credential information stored locally (usually in `~/.aws/config` and `~/.aws/credentials`). It lets you manage and switch between multiple AWS accounts or roles without re-entering access keys each time.
- **AWS CLI**: You can specify a profile with `--profile <name>` or set the environment variable `AWS_PROFILE`. The CLI will use the corresponding access keys, region, and output format defined under that profile.
- **boto3**: It loads the same profile definitions. You can select one by creating a session, e.g. `boto3.Session(profile_name="myprofile")`. If not specified, boto3 defaults to the `default` profile.
  
  This allows clean separation of credentials for multiple accounts, roles, or environments (e.g., dev, staging, prod).