# TODO How to use temporary access keys to refresh permissions with AWS
	- It's always better to use [[AWS/IAM/Role]]s attached to instances. But when integrating with third parties who control their own infrastructure, it may be necessary to apply another approach.
	- ## Use Case
		- Be able to have a service user for integrating with an external service that has minimal permissions
		- that user should assume a [[AWS/IAM/Role]] to obtain a temporary token with more permissions
			- this can be revoked based on security and observability tools