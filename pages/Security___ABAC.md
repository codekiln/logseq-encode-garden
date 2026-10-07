alias:: [[Attribute-Based Access Control]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Security/RBAC]]
- # Attribute-Based Access Control (ABAC)
	- ## Overview
		- Authorization decides whether a subject may perform an action on a resource. Role-Based Access Control (RBAC) assigns permissions to named roles, then assigns users or services to those roles. Attribute-Based Access Control (ABAC) evaluates policy conditions over attributes of the subject, resource, action, and sometimes the surrounding environment.
		- RBAC answers, “Which permissions come with this role?” ABAC answers, “Do the facts about this request satisfy the policy?”
	- ## Example
		- A role might let a clinician read patient records. That rule applies to every record covered by the role.
		- An attribute policy can narrow access to records for patients assigned to that clinician, or allow access only when the record's sensitivity is within the clinician's clearance.
		- The same distinction applies outside healthcare: a project-reader role gives broad project access, while an attribute rule can restrict it to projects tagged for the reader's team or environment.
	- ## How they fit together
		- RBAC groups permissions around stable job functions, which makes common access patterns easier to assign and review.
		- ABAC expresses conditions that vary across resources or requests without creating a separate role for every combination. Policies can inspect attributes such as department, resource owner, classification, or request location.
		- Systems often combine them: roles provide a broad permission set, and attribute policies refine the decision. The exact combination rules depend on the system. For example, [LangSmith ABAC](https://docs.langchain.com/langsmith/abac) considers both role permissions and attribute policies; a matching deny takes precedence, and an allow policy can grant access even without the corresponding RBAC permission.
	- ## Choosing a model
		- RBAC is a good fit when access follows a manageable set of job functions and permissions are mostly stable. Its main pressure is role growth when every team, resource class, or exception gets a distinct role.
		- ABAC is useful when access depends on changing relationships or resource-specific facts. It reduces the need for narrowly specialized roles, but shifts the work to defining trustworthy attributes, writing policies, and explaining each decision.
		- ABAC is not automatically safer or simpler. Missing, stale, or inconsistent attributes can produce incorrect decisions, and policies can be difficult to reason about without clear evaluation and audit tools.
