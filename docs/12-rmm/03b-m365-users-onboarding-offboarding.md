---
title: "Microsoft 365 User Management - Onboarding and Offboarding"
section: "RMM"
subsection: "Microsoft 365 User Management"
page_range: "1256-1267"
tags: [rmm, microsoft-365, user-management, onboarding, offboarding, user-risks, templates, baselines]
acronis_version: "26.02"
---

# Microsoft 365 User Management

Microsoft 365 management enables you to manage user accounts, including onboarding new users and offboarding existing users from Microsoft 365 tenants.

## Working with Baseline Templates

Microsoft 365 management enables you to create and manage baseline templates. Templates are collections of baseline configurations that can be applied to one or more Microsoft 365 tenants. Templates help you standardize security configurations across multiple tenants.

When you map a tenant to a customer in Cyber Protect Cloud, the system applies the predefined tenant baselines to the customer tenant. You can create custom templates to override or extend these baselines.

### Creating a Baseline Template

1. In the Cyber Protect console, go to **Microsoft 365 management > Templates**.
2. Click **Create template**.
3. Enter a name for the template.
4. Select the baselines you want to include in the template.
5. Configure the baseline settings as needed.
6. Click **Create**.

### Applying a Template to a Tenant

1. In the Cyber Protect console, go to **Microsoft 365 management > Templates**.
2. Select the template you want to apply.
3. Click **Apply to tenants**.
4. Select the tenants to apply the template to.
5. Click **Apply**.

## Managing User Risks

The Risk dashboard highlights user account risks within a Microsoft 365 tenant. You can review and manage the following user risk categories:

| Risk Category | Description |
|---------------|-------------|
| MFA | User accounts where MFA is disabled or not enrolled |
| Admin mailboxes | Global administrator accounts that have a mailbox |
| Anonymous admins | Possible shared administrator accounts |
| Shared mailboxes | User accounts with shared mailboxes |
| Dormant accounts | Users who have not logged in for three months |
| Dormant admins | Administrator accounts that have not logged in for six months |
| Guests | Guest user accounts |

### Reviewing User Risks

1. In the Cyber Protect console, go to **Microsoft 365 management > Security posture**.
2. Click on the relevant tenant row. The Risk dashboard is displayed.
3. In the **User account risks** section, click on a risk category to view the affected users.
4. Review the list of affected users and take appropriate action.

## Onboarding Users

You can onboard users to a Microsoft 365 tenant through the Microsoft 365 management service.

### Steps to Onboard Users

1. In the Cyber Protect console, go to **Microsoft 365 management > Users**.
2. Click **Onboard user**.
3. Configure the user's Microsoft 365 settings in the following sections:
   - **User configurations**: Set up basic user properties including display name, username, password, and license assignments.
   - **Group memberships**: Add the user to relevant Microsoft 365 groups.
   - **User policies**: Apply relevant security policies to the new user.
4. Click **Save**.
5. In the confirmation dialog, click **Close**.

The user is onboarded to the relevant Microsoft 365 tenant.

## Offboarding Users

You can offboard users from a Microsoft 365 tenant through the Microsoft 365 management service.

In service-based licensing, this functionality requires the **RMM > Microsoft 365 seats** service quota to be applied to all the customer's Microsoft 365 seats. In solution-based licensing, the functionality is enabled with either **Security and RMM** or **Ultimate Protection** license.

### Steps to Offboard Users

1. In the Cyber Protect console, go to **Microsoft 365 management > Users**.
2. Select the checkbox in the far left column of the user you want to offboard, and then click **Offboard user**.
3. Modify the user's Microsoft 365 settings in the following sections, as required:
   - **User configurations**: Disable or modify user properties.
   - **Assign mailbox delegates**: Assign the user's mailbox to another user.
   - **Automatic response action**: Configure automatic responses for the offboarded user's mailbox.
   - **Litigation hold**: Place the user's mailbox on litigation hold to preserve all mailbox content.
4. Click **Save**.
5. In the confirmation dialog, click **Close**.

The user is offboarded from the relevant Microsoft 365 tenant.
