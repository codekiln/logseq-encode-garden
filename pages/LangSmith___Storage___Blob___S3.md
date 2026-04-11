- How to use [[AWS/S3]] [with LangSmith Blob Storage](https://docs.langchain.com/langsmith/self-host-blob-storage#amazon-s3)
	- Create a policy
		- ```json
		  {
		    "Version": "2012-10-17",
		    "Statement": [
		      {
		        "Effect": "Allow",
		        "Action": [
		          "s3:GetObject",
		          "s3:PutObject",
		          "s3:DeleteObject",
		          "s3:ListBucket"
		        ],
		        "Resource": [
		          "arn:aws:s3:::your-bucket-name",
		          "arn:aws:s3:::your-bucket-name/*"
		        ]
		      }
		    ]
		  }
		  ```
	- Once you have the correct policy, there are three ways to authenticate with Amazon S3:
	  id:: 69d7b97b-f795-4b6a-a0a6-e3e76447e192
		- 1 - [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) (Recommended): You can create an IAM role for your LangSmith instance and attach the policy to that role. This is the recommended way to authenticate with Amazon S3 in production.
		- 2 - [Access Key and Secret Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html): You can provide LangSmith with an access key and secret key. This is the simplest way to authenticate with Amazon S3. However, it is not recommended for production use as it is less secure.
		- 3 - [VPC Endpoint Access](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html): You can enable access to your S3 bucket via a VPC endpoint, which allows traffic to flow securely from your VPC to your S3 bucket.
	- You also need to set up [[AWS/S3/Rule/Lifecycle]]; see [here](https://docs.langchain.com/langsmith/self-host-blob-storage#amazon-s3-lifecycle-rules)