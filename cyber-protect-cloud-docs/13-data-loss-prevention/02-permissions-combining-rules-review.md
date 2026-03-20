---
title: "Adjusting Permissions, Combining Rules, and Policy Review"
section: "Data Loss Prevention"
subsection: "Policy Rules Management"
page_range: "1457-1459"
tags: [dlp, data-flow-policy, permissions, combining-rules, policy-review, policy-management, enforcement]
acronis_version: "26.02"
---

# Adjusting Permissions, Combining Rules, and Policy Review

## Adjusting the Permissions in Data Flow Policy Rules

Data Loss Prevention supports three types of permissions in data flow policy rules. The permissions are configured individually in each rule of the policy.

- **Allow (permissive)** -- Data transfers that match the combination of sensitivity category, sender, and recipient defined in the rule are allowed.
- **Exception (prohibitive)** -- Data transfers that match the combination of sensitivity category, sender, and recipient defined in the rule are not allowed, but the sender can submit an exception to the rule to allow a specific transfer. All subsequent data transfers between this sender and recipient for this sensitivity category will be allowed for five minutes after the exception is submitted.
- **Deny (prohibitive)** -- Data transfers that match the combination of sensitivity category, sender, and recipient defined in the rule are not allowed, and the sender does not have the option to submit an exception.

In addition, a priority flag can be assigned to the **Allow** and **Exception** permissions to increase policy management flexibility. With this setting, you can override the permissions set for specific groups in other data flow rules in the policy. You can use it to apply a group data flow rule only to some of its members by creating a data flow rule for specific users that you want to exclude from the group rules, and then prioritizing their permissions over the data flow restrictions configured in the rules for the group.

> **Important:** Before switching a company or unit policy from Observation to Enforcement mode, it is crucial to adjust the default rules for each sensitive data category from the permissive to a prohibitive state. Default rules are marked with an asterisk (*) in the **Data flow policy** view.

### To Edit Permissions in Policy Rules

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data flow policy**.
3. Select the policy rule that you wish to edit and click **Edit** above the rules list. The **Edit data flow rule** window opens.
4. In the **Permission** section, select **Allow**, **Exception**, or **Deny**.
5. (Optional) To prioritize the **Allow** or **Exception** permission of this rule over the permissions in other rules, select the **Prioritize** check box. You do not need to use this check box to prioritize a data flow rule over the default Any > Other rule, because it has the lowest priority in the policy by default.
6. (Optional) Select an action to be executed when the rule is triggered.
7. Save the changes to the policy rule.

## Combining Data Flow Policy Rules

When a data transfer matches more than one rule, the permissions and actions configured for all rules are combined and applied as follows.

### Permissions

If a data transfer matches more than one rule and these rules have different permissions for the same data category, the overriding rule is the one with higher priority permission, according to the following permission priority list (in descending order):

1. Exception with the **Prioritized** flag
2. Allow with the **Prioritized** flag
3. Deny
4. Exception
5. Allow

If a data transfer matches more than one rule and these rules have different permissions for different data categories, the following logic is applied for the override:

1. The most restrictive rule permission is defined for each of the sensitivity categories that the data transfer matches.
2. The most restrictive of the rule permissions defined in point 1 is enforced.

**Example:** A file transfer matches three rules in different sensitivity categories:

| Sensitivity category | Permission |
|----------------------|------------|
| PII | Allow - Prioritized |
| PHI | Exception - Prioritized |
| PCI | Deny |

The permission that will be applied is **Deny**.

### Actions

If a data transfer matches more than one rule and these rules have different options configured in the **Action** field, all configured actions in all triggered rules are performed.

## Policy Review and Management

Before the automatically created baseline data flow policy is enforced, it has to be reviewed, validated, and approved by the client, because it is the client who inherently knows all the specifics of their business processes and can assess whether they are consistently interpreted in the baseline policy. Also, the client can identify inaccuracies, which are then fixed by the partner administrator.

During the policy review, the partner administrator presents the baseline data flow policy to the client, who reviews each data flow in the policy and validates its consistency with their business processes. The validation does not require any technical skills, because the representation of policy rules in the Cyber Protect console is intuitively clear: each rule describes who are the sender and the recipient of a sensitive data flow.

Based on the client's instructions, the partner administrator manually adjusts the baseline policy by editing, deleting, and creating data flow policy rules. After the client's approval, the reviewed policy is enforced on protected workloads by switching the protection plan applied to these workloads to the Enforcement mode.

Before enforcing a reviewed policy, it is important to change the **Allow** permission in all automatically created default policy rules for sensitive data categories to **Deny** or **Exception**. The **Deny** permission cannot be overridden by users, while the **Exception** permission blocks a transfer matching the rule but allows users to override the block in an emergency situation by submitting a business-related exception.
