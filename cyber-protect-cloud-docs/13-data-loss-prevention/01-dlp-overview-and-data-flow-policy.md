---
title: "Data Loss Prevention Overview and Data Flow Policy Creation"
section: "Data Loss Prevention"
subsection: "Creating Data Flow Policy and Policy Rules"
page_range: "1453-1456"
tags: [dlp, data-loss-prevention, data-flow-policy, policy-rules, observation-mode, enforcement-mode, sensitive-data]
acronis_version: "26.02"
---

# Data Loss Prevention Overview and Data Flow Policy Creation

The Data Loss Prevention (DLP) module analyzes the content and context of data transfers on protected workloads and prevents leakage of sensitive data through peripheral devices or network transfers within and outside the company network based on data flow policy.

DLP features can be included in any protection plan for a customer tenant if the Protection service and the Data Loss Prevention pack are enabled for that customer.

## Creating the Data Flow Policy and Policy Rules

The key principle of data loss prevention demands that users of a corporate IT system should be allowed to handle sensitive data only to the extent necessary to perform their job duties. Any other sensitive data transfers -- irrelevant to the business processes -- should be blocked. It is crucial to distinguish between business-related and rogue data transfers, or flows.

The data flow policy contains rules that specify which data flows are allowed and which are prohibited, thus preventing unauthorized transfers of sensitive information when DLP is enabled in a protection plan and running in Enforcement mode.

Each sensitivity category in the policy contains one default rule (marked with an asterisk) and one or more explicit (non-default) rules that define the data flows for specific users or groups.

The data flow policy is usually created automatically while DLP is running in observation mode. The time required for building a representative data flow policy is approximately one month, but it could differ depending on the business processes in your organization. The policy can also be created, configured, or edited manually.

### Starting Automatic Creation of Data Flow Policy

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Management** > **Protection plans**.
3. Click **Create plan**.
4. Expand the **Data Loss Prevention** section and click the **Mode** row.
5. In the Mode dialog, select **Observation mode**, and select how to process data transfers:

| Option | Description |
|--------|-------------|
| **Allow all** | All transfers of sensitive data from user workloads are treated as necessary for the business process and safe. A new rule is created for every detected data flow that does not match an already defined rule in the policy. |
| **Justify all** | All transfers of sensitive data from user workloads are treated as necessary for the business process, but risky. For every intercepted transfer of sensitive data to any recipient or destination both inside and outside the organization that does not match a previously created data flow rule, the user must provide a one-time business justification. When the justification is submitted, a new data flow rule is created in the data flow policy. |
| **Mixed** | The Allow all logic is applied for all internal sensitive data flows, and the Justify all logic is applied for all external data flows. |

6. Save the protection plan and apply it to the workloads from which you want to collect data to build the policy.

> **Note:** Data leakage is not prevented during observation mode.

### Configuring the Data Flow Policy Manually

1. In the Cyber Protect console, navigate to **Protection** > **Data flow policy**.
2. Click **New data flow rule**. The New data flow rule pane expands on the right.
3. Select a sensitivity category, add a sender and a recipient, and define the permission for data transfers for the selected category, sender, and recipient:

| Option | Description |
|--------|-------------|
| **Allow** | Allow this sender to transfer data of this sensitivity category to this recipient. |
| **Exception** | Do not allow this sender to transfer data of this sensitivity category to this recipient, but allow the sender to submit an exception to the rule for a specific transfer. When this sender tries to transfer data, block the transfer and ask the sender to submit an exception to allow it. All subsequent data transfers between this sender and recipient for this sensitivity category will be allowed for five minutes after the exception is submitted. |
| **Deny** | Do not allow this sender to transfer data of this sensitivity category to this recipient, and do not allow the sender to request an exception to the rule. |

4. (Optional) Select an action that should be executed when the rule is triggered:

| Action | Description |
|--------|-------------|
| **Write in log** | Store an event record in the audit log when the rule is triggered. Recommended for rules with Exception permission. |
| **Generate an alert** | Generate an alert in the Cyber Protect Alerts tab when the rule is triggered. If notifications are enabled for the administrator, an email notification will be sent as well. |
| **Notify the end user when a data transfer is denied** | Notify the user in real time with an on-screen warning when they trigger the rule. |

5. Click **Save**.
6. Repeat steps 2 to 5 to create multiple rules of different sensitivity categories and options.

> **Warning:** When **No action** is selected and the rule is triggered: no event record is added to the audit log; no alert is sent to the administrator; no onscreen notification is displayed to the end user.

## Data Flow Policy Structure

In the **Data flow policy** view, policy rules are grouped according to the category of sensitive data that they control. The sensitivity category identifier is displayed right above the group of policy rules.

- **Sensitive**
  - Protected Health Information (PHI)
  - Personally Identifiable Information (PII)
  - Payment Card Industry Data Security Standard (PCI DSS)
  - Marked as Confidential
- **Non-sensitive**

## Rule Structure

Each policy rule consists of the following elements:

- **Sensitivity Category** -- PHI, PII, PCI DSS, or Marked as Confidential
- **Sender** -- specifies the initiator of a data transfer controlled by this rule. It may be a single user, a list of users, or user group:
  - **Any internal** -- a user group that includes all internal users of the organization
  - **Contact / From organization** -- a Windows account in the organization recognized by DLP, as well as all other accounts (including those used by third-party communication applications)
  - **Contact / Custom identity** -- identifier of an internal user specified in formats such as email, Skype ID, ICQ identifier, IRC identifier, Jabber e-mail, Mail.ru Agent e-mail, Viber phone number, Zoom e-mail. Wildcards `*` (any number of symbols) and `?` (any single symbol) can be used.
- **Recipient** -- specifies the destination. It may be a single user, a list of users, or user group, as well as other types of destinations:
  - **Any** -- any of the recipient types supported by DLP
  - **Contact / Any contact**, **Any internal contact**, **Any external contact**, **From organization**, **Custom identity**
  - **File sharing services** -- identifier of a controlled file sharing service
  - **Social network** -- identifier of a controlled social network
  - **Host / Any host**, **Any internal host**, **Any external host**, **Specific host** (FQDN or IP address)
  - **Device / Any device**, **External storage**, **Encrypted removable**, **Redirected clipboard**
  - **Printers** -- any local or network printer connected to the workload
- **Permission** -- Allow, Exception, or Deny (see "Adjusting the permissions")
- **Action** -- Write in log, Notify the end user when a data transfer is denied, Generate an alert

### What Triggers a Policy Rule?

A data transfer matches a data flow policy rule if all of the following conditions are true:

- All senders of this data transfer are listed or belong to a user group specified in the **Sender** field of the rule.
- All recipients of this data transfer are listed or belong to a user group specified in the **Recipient** field of the rule.
- The data being transferred matches the **Sensitivity category** of the rule.
