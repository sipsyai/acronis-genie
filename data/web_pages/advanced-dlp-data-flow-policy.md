# Creating the data flow policy and policy rules

Data Loss Prevention > Creating the data flow policy and policy rules
Creating the data flow policy and policy rules

The key principle of data loss prevention demands that users of a corporate IT system should be allowed to handle sensitive data only to the extent necessary to perform their job duties. Any other sensitive data transfers - irrelevant to the business processes - should be blocked. Therefore it is crucial to distinguish between business-related and rogue data transfers, or flows.

The data flow policy contains rules that specify which data flows are allowed and which are prohibited, thus preventing unauthorized transfers of sensitive information when the Data Loss Prevention module is enabled in a protection plan and running in Enforcement mode.

Each sensitivity category in the policy contains one default rule, marked with an asterisk (*) and one or more explicit (non-default) rules that define the data flows for specific users or groups. Read more about the types of policy rules in the Fundamentals guide.

The data flow policy is usually created automatically while Data Loss Prevention is running in observation mode. The time required for building a representative data flow policy is approximately one month, but it could differ, depending on the business processes in your organization. The data flow policy can also be created, configured, or edited manually by a company or unit administrator.

To start the automatic creation of data flow policy

Log in to the Cyber Protect console as an administrator.
Navigate to Management > Protection plans.
Click Create plan.
Expand the Data Loss Prevention section and click the Mode row.
In the Mode dialog, select Observation mode, and select how to process data transfers:
Option	Description
Allow all	All transfers of sensitive data from user workloads are treated as necessary for the business process and safe. A new rule is created for every detected data flow that does not match an already defined rule in the policy.
Justify all	All transfers of sensitive data from user workloads are treated as necessary for the business process, but risky. Therefore, for every intercepted transfer of sensitive data to any recipient or destination both inside and outside the organization that does not match a previously created data flow rule, the user must provide a one-time business justification. When the justification is submitted, a new data flow rule is created in the data flow policy.
Mixed	The Allow all logic is applied for all internal sensitive data flows, and the Justify all logic is applied for all external data flows.
For more information about internal and external data see Automated detection of destination
Save the protection plan and apply it to the workloads from which you want to collect data to build the policy.
Data leakage is not prevented during observation mode.

To configure the data flow policy manually

In the Cyber Protect console, navigate to Protection > Data flow policy.
Click New data flow rule.
The New data flow rule pane expands on the right.
Select a sensitivity category, add a sender and a recipient, and define the permission for data transfers for the selected category, sender, and recipient.
Option	Description
Allow	Allow this sender to transfer data of this sensitivity category to this recipient.
Exception

Do not allow this sender to transfer data of this sensitivity category to this recipient, but allow the sender to submit an exception to the rule for a specific transfer.

When this sender tries to transfer data of this sensitivity category to this recipient, block the transfer and ask the sender to submit an exception to allow this transfer. When the exception is submitted, the data transfer is allowed to proceed.

All subsequent data transfers between this sender and recipient for this sensitivity category will be allowed for five minutes after the exception is submitted.

Deny	Do not allow this sender to transfer data of this sensitivity category to this recipient, and do not allow the sender to request an exception to the rule.
(Optional) Select an action that should be executed when the rule is triggered.
Action	Description
Write in log	Store an event record in the audit log when the rule is triggered. We recommend to select this action for rules with Exception permission.
Generate an alert	Generate an alert in the Cyber Protect Alerts tab when the rule is triggered. If notifications are enabled for the administrator, an email notification will be sent as well.
Notify the end user when a data transfer is denied	Notify the user in real time with an on-screen warning when they trigger the rule.
Click Save.
Repeat steps 2 to 5 to create multiple rules of different sensitivity categories and options, and verify that the resulting rules correspond to the options that you selected.

Data flow policy structure

Rule structure

Adjusting the permissions in data flow policy rules

Combining data flow policy rules

Policy review and management

Data flow policy renewal

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.