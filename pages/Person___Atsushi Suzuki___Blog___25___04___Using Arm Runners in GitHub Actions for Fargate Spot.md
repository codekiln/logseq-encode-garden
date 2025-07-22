# [Cost Optimization Gone Wrong: Lessons from Using Arm Runners in GitHub Actions for Fargate Spot - DEV Community](https://dev.to/aws-builders/cost-optimization-gone-wrong-lessons-from-using-arm-runners-in-github-actions-for-fargate-spot-39ap?utm_source=chatgpt.com)
	- [[tldr]]
		- Each github plan has a certain number of "free minutes" included per month, as long as you don't use the "Larger Runners" needed to do ARM linux builds.
		- As a result, you may end up in a situation where you spend more to build arm images on on arm architecture.