alias:: [[Attribute-Based Access Control]]
- # Attribute-Based Access Control (ABAC)
	- ABAC is an authorization model that evaluates attributes (rather than roles) to determine access.
	- Unlike [[Security/RBAC]] (Role-Based Access Control), which grants permissions based on predefined roles, ABAC makes decisions based on attributes of:
		- **Subject** - the user or entity requesting access (e.g., department, clearance level, job title)
		- **Resource** - the object being accessed (e.g., classification, owner, creation date)
		- **Action** - the operation being performed (e.g., read, write, delete, approve)
		- **Environment** - contextual factors (e.g., time of day, location, device type)
- ## How ABAC Works
	- Access decisions are made by evaluating policies against attributes at runtime
	- A policy engine evaluates requests against defined rules
	- Example policy: "Allow access if user.department == resource.department AND user.clearance >= resource.sensitivity AND environment.time is within business_hours"
- ## Key Components
	- **Policy Enforcement Point (PEP)** - intercepts access requests and enforces decisions
	- **Policy Decision Point (PDP)** - evaluates policies and returns allow/deny decisions
	- **Policy Information Point (PIP)** - provides attribute values from external sources
	- **Policy Administration Point (PAP)** - manages and stores policies
- ## Advantages
	- **Fine-grained control** - can express complex access rules that RBAC cannot
	- **Dynamic** - decisions made at runtime based on current attribute values
	- **Scalable** - adding new resources doesn't require creating new roles
	- **Context-aware** - can incorporate environmental factors like time, location, risk level
	- **Reduced role explosion** - avoids the proliferation of roles in large organizations
- ## Disadvantages
	- **Complexity** - more difficult to implement and audit than RBAC
	- **Performance** - policy evaluation at runtime can add latency
	- **Debugging** - harder to understand why access was granted or denied
	- **Policy management** - requires careful design to avoid conflicts
- ## Use Cases
	- Healthcare systems requiring access based on patient-provider relationships
	- Financial systems with time-based and amount-based restrictions
	- Multi-tenant [[SaaS]] applications with complex sharing rules
	- Government systems with classification levels and need-to-know requirements
	- [[AWS/IAM]] policies use ABAC principles with resource tags and conditions
- ## ABAC vs RBAC
	- | Aspect | RBAC | ABAC |
	  |--------|------|------|
	  | Basis | Roles assigned to users | Attributes of users, resources, environment |
	  | Flexibility | Limited to predefined roles | Highly flexible, dynamic |
	  | Scalability | Role explosion in complex systems | Scales well with attributes |
	  | Implementation | Simpler to implement | More complex |
	  | Auditability | Easy to audit role assignments | Harder to trace decisions |
- ## Standards and Implementations
	- **XACML** (eXtensible Access Control Markup Language) - OASIS standard for ABAC policies
	- **AWS IAM** - uses ABAC through resource tags and policy conditions
	- **Azure ABAC** - attribute-based conditions for role assignments
	- **Google Cloud IAM Conditions** - supports attribute-based conditions
- ## Related
	- [[Security/RBAC]]
	- [[AWS/IAM]]
	- [[Zero Trust]]
