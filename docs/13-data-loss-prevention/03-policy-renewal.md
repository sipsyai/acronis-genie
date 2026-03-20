---
title: "Data Flow Policy Renewal"
section: "Data Loss Prevention"
subsection: "Policy Renewal"
page_range: "1459-1461"
tags: [dlp, data-flow-policy, policy-renewal, observation-mode, adaptive-enforcement, company-policy, user-policy]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#advanced-dlp-policy-renewal.html"
---

# Data Flow Policy Renewal

When the business process of the company or its unit is considerably changed, their DLP policies have to be renewed in order to make them consistent with the changes in sensitive data flows of the updated business process. A policy renewal is also required if an employee's job role is changed -- in this case, the part of the unit policy used to protect employee workload has also to be renewed.

The DLP policy management workflow allows administrators to automate policy renewals for the entire company, a unit, a user, or a part of users in a unit.

## Renewing the Policy for a Company or Unit

All options of the Observation mode can be used to renew the company or unit-wide policy, as well a part of a unit policy for one or more users in the unit.

### To Renew the Policy for a Company or Unit

The renewal process consists of the following steps that must be performed by a Company administrator or a Partner who manages the company workloads:

1. Delete all non-default rules in the enforced policy.
2. To start the renewal, switch the protection plan with DLP applied to the company or unit to one of the observation mode options, depending on which one is the optimal for this particular company or unit, and then apply the plan to all workloads in the company or the unit.
3. When the renewal period ends, review the new company or unit policy with the client, adjust if necessary, and get an approval by the client.
4. Switch the protection plan applied to the company or unit workloads to an appropriate enforcement mode option, which the client considers as optimal for preventing data leakage from the unit's workloads.

## Renewing the Policy for One or More Users in the Company or Unit

User-level policies can be renewed by using any option of the Observation mode, as well as the adaptive enforcement mode.

### Using the Observation Mode for Renewing a User Policy

Using the observation mode for renewing a policy for a user or a part of users in the company (or unit) has the following specifics: the data flow policy enforced for the entire company (or unit) is not enforced over user's data transfers during the renewal period. As a result, new individual rules for the user can be created during the renewal that could contradict with or match existing group rules in the enforced policy for the company (or unit). After the renewal is completed and the policy is re-enforced over the user's data transfers, whether these new individual rules created for the user will be actually applied or not to the user's data transfers depends on their priorities in comparison with other rules in the policy that these data transfers match.

#### To Renew the Policy for a User Through Observation Mode

The renewal process must be performed by a Company administrator or a Partner who manages the company workloads:

1. Delete all non-default rules in the policy enforced for the company (or unit) that have the user as their single sender.
2. Remove the user from the sender lists of all non-default data flow rules in the enforced policy.
3. Create a new protection plan with DLP in observation mode and apply it to the user's workload to start the renewal (observation) period. The duration of the renewal period depends on how long it could take for the user to have performed all or 90-95% of their regular business activities that involve transferring sensitive data from their workloads.
4. When the renewal period ends, review the new rules related to this user that have been added to the enforced policy, adjust them if necessary, and get them approved by the client.
5. Switch the protection plan applied to the user's workload to the **Strict enforcement** mode or the **Adaptive enforcement** mode -- depending on which option the client considers as optimal for preventing data leakage from the user's workload. Alternatively, you can re-apply to the user's workload the protection plan applied to the company (or unit).

### Using the Adaptive Enforcement Mode for Renewing a User Policy

Policy renewal for a single user or a part of all users in the company (or unit) can be performed by using the Adaptive enforcement mode of a protection plan with DLP applied to the user's workload.

> **Note:** This policy renewal method has the following specifics: the enforced company (unit) policy rules for sender groups with the user's membership (i.e. Any internal) are also enforced over data transfers from this user during the renewal. As a result, the renewal will not create new individual rules for the user that would contradict with or match these already existing policy rules for sender groups. Which of these two methods is more effective for user policy renewals for a particular client depends on its specific IT security requirements.

#### To Renew the Policy for a User Through Adaptive Enforcement Mode

The renewal process must be performed by a Company administrator or a Partner who manages the company workloads:

1. Delete all non-default rules in the policy enforced for the company (unit) that have the user as their single sender.
2. Remove the user from the sender lists of all non-default data flow rules in the enforced policy.
3. For all default rules in the policy enforced for the company (or unit), set their permission to **Exception**, and select the **Write in log** action in the **Action** field.
4. If the protection plan currently applied to the user's workload is set to the **Strict enforcement** mode, create a new protection plan with DLP and apply it to the user's workload in the **Adaptive enforcement** mode to start the renewal period. The duration of the renewal period depends on how long it could take for the user to have performed all or 90-95% of their regular business activities that involve transferring sensitive data from their workloads.
5. When the renewal period ends, review the new rules related to this user that have been added to the enforced policy, adjust them if necessary, and get them approved by the client.
6. Switch the protection plan applied to the user's workload to the **Strict enforcement** mode or leave it in the **Adaptive enforcement** mode -- depending on which option the client considers as optimal for preventing data leakage from the user's workload.
