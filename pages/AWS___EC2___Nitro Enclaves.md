logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[AWS]]

- # [AWS Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html)
	- An Amazon EC2 feature for carving isolated execution environments, called enclaves, out of an EC2 instance. An enclave is a hardened, highly constrained virtual machine with no persistent storage, no interactive access (no SSH), and no external networking. Its only link to the parent instance is a local socket.
	- Processes and users on the parent instance, root included, cannot read the enclave's memory or data. The [[AWS]] Nitro Hypervisor isolates the enclave's vCPUs and memory from the parent.
	- Supports cryptographic attestation, so a service can verify which code is running in an enclave. [[AWS/KMS]] key policies can require that an enclave's measurements match before a key operation succeeds.
	- Meant for sensitive data such as PII and the applications that process it.
	- Limits: up to four enclaves per parent instance, enclaves cannot talk to each other, enclaves stop when the parent stops, no hibernation on the same instance. The enclave must run Linux. The parent runs Linux or Windows on most Intel, AMD, and Graviton instance types built on the Nitro System.
	- No extra charge beyond the EC2 instance and other AWS services used.
