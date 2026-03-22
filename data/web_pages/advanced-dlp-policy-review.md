# Policy review and management

Data Loss Prevention > Creating the data flow policy and policy rules > Policy review and management
Policy review and management

Before the automatically created baseline data flow policy is enforced, it has to be reviewed, validated, and approved by the client, because it is the client who inherently knows all the specifics of their business processes and can assess whether they are consistently interpreted in the baseline policy. Also, the client can identify inaccuracies, which are then fixed by the partner administrator.

During the policy review, the partner administrator presents the baseline data flow policy to the client, who reviews each data flow in the policy and validates its consistency with their business processes. The validation does not require any technical skills, because the representation of policy rules in the Cyber Protect console is intuitively clear: each rule describes who are the sender and the recipient of a sensitive data flow.

Based on client’s instructions, the partner administrator manually adjusts the baseline policy by editing, deleting, and creating data flow policy rules. After client’s approval, the reviewed policy is enforced on protected workloads by switching the protection plan applied to these workloads to the Enforcement mode.

Before enforcing a reviewed policy, it is important to change the Allow permission in all automatically created default policy rules for sensitive data categories to Deny or Exception. The Deny permission cannot be overriden by users, while the Exception permission blocks a transfer matching the rule but allows users to override the block in an emergency situation by submitting a business-related exception.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.