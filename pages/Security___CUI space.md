alias:: [[CUI space]], [[CUI Space]], [[CUI Environment]], [[CUI]]

- # CUI space
	- ## What CUI is
		- **Controlled Unclassified Information (CUI)** is sensitive information that is not classified but still requires protection under federal law, regulation, or policy.
		- It is primarily a U.S. federal compliance concept used by agencies and contractors.
		- Examples include:
			- Export-controlled technical data ([[ITAR]], [[EAR]])
			- Critical infrastructure details
			- Law-enforcement sensitive information
			- Federal contract data
			- Some healthcare or privacy data held by government programs
		- The formal CUI program is governed by [[Org/National Archives and Records Administration (NARA)]].
	- ## What "CUI space" means in practice
		- CUI space is the boundary of the IT environment where CUI is stored, processed, or transmitted.
		- Security teams define this boundary to determine:
			- Which systems must meet compliance requirements
			- Where controls must be enforced
			- Where monitoring and audit coverage must occur
		- Typical in-scope components include:
			- Workstations used to access CUI
			- File servers storing CUI
			- Cloud environments processing CUI
			- Email systems transmitting CUI
			- Identity systems controlling access
		- If a system touches CUI, it is usually in scope for the CUI environment.
	- ## Why organizations isolate CUI space
		- Organizations often segregate CUI-handling systems from the broader enterprise network to reduce compliance scope and operational risk.
		- Common approaches include:
			- Dedicated enclave or subnet
			- Separate cloud tenant
			- Controlled access jump hosts
			- Strict identity and logging controls
		- This supports demonstrating compliance with frameworks such as:
			- [[NIST/800-171]]
			- [[NIST/800-53]]
			- [[CMMC]]
	- ## Example architecture
		- ~~~text
		  Corporate Network
		     |
		     |  (firewall + identity controls)
		     |
		  CUI Enclave
		     |- Engineering workstation
		     |- Secure file server
		     |- Git repository for controlled designs
		     `- Logging/SIEM
		  ~~~
		- Only authorized users and hardened systems are allowed inside the CUI space.
	- ## Key idea
		- CUI space is the compliance boundary for systems handling controlled federal data.
		- Security teams define it to:
			- Apply required protections
			- Limit exposure
			- Demonstrate compliance during audits
	- ## Related
		- [[CMMC]]
		- [[NIST/800-171]]
		- [[NIST/800-53]]