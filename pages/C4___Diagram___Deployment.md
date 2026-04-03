logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Diagram/2 - Containers]], [[C4/Diagram]]

- # **[Deployment diagram](https://c4model.com/diagrams/deployment)** (C4 diagram)
	- ## Overview
		- A **supporting** C4 diagram mapping **software containers** to **infrastructure**: regions, **clusters**, **nodes**, **PaaS** services, **serverless** targets, networking boundaries, and similar **deployment** concerns.
		- Answers *where things **run*** and *what **failure domains** or **environments** exist*.
	- ## Context
		- Complements **logical** [[C4/Diagram/2 - Containers]]—same software boxes, now placed on **real(istic) hardware and cloud** shapes (see [[C4/Diagram]]).
	- ## Key principles
		- **Environment truth** — Distinguish **prod** vs **non-prod** when differences matter for risk discussion.
		- **Infra vocabulary** — Use terms your **SRE / platform** team recognises (VPCs, subnets, k8s namespaces, …) at the right altitude.
	- ## Mechanism
		- Often generated from **IaC** (Terraform, CDK) or **cloud console** exports for accuracy.
	- ## Examples
		- **Multi-region** active-active services; **hybrid** on-prem + cloud **egress** paths; **zero-trust** segmentation between tiers.
	- ## Misconceptions
		- “**Deployment = container diagram**” — **Different** questions—**logical** vs **physical / cloud mapping**.
		- “**Must show every VM**” — **Usually too low**; abstract to **meaningful** deployment units unless troubleshooting.
