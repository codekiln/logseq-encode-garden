# [Comparison table](https://developer.1password.com/docs/secrets-automation/#comparison) of when to use [[1Password Service Account]] vs [[1Password/Dev/Connect Server]]
id:: 67dbe69c-b43e-4c52-a130-ffb85330e994
	- | Feature | Service accounts | Connect servers |
	  | ---- | ---- | ---- |
	  | [1Password CLI](https://developer.1password.com/docs/connect/connect-cli/) | ✅ | ✅ |
	  | REST API | ❌ | ✅ |
	  | Self-hosted | ❌ | ✅ |
	  | Infrastructure requirements | ❌ | ✅ |
	  | Low overhead | ✅ | ❌ |
	  | Low latency | ❌ | ✅ |
	  | [Kubernetes integrations](https://developer.1password.com/docs/k8s/k8s-integrations/) | ✅ | ✅ |
	  | [CI/CD integrations](https://developer.1password.com/docs/ci-cd/) | ✅ | ✅ |
	  | Rate limits | ✅ | ❌ |
	  | Request quotas | ✅ | ❌ |
	  | Included with 1Password subscription | ✅ | ✅ |