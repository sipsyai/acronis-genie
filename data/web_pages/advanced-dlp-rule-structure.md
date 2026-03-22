# Rule structure

Data Loss Prevention > Creating the data flow policy and policy rules > Rule structure
Rule structure

Each policy rule consists of the following elements.

Sensitivity Category
Protected Health Information (PHI)
Personally Identifiable Information (PII)
Payment Card Industry Data Security Standard (PCI DSS)
Marked as Confidential

See Sensitive data definitions

Sender - specifies the initiator of a data transfer controlled by this rule. It may be a single user, a list of users, or user group.
Any internal - a user group that includes all internal users of the organization.
Contact / From organization - a Windows account in the organization, recognized by Data Loss Prevention, as well as all other accounts (including those used by third-party communication applications) that a given Windows account has used earlier.
Contact / Custom identity - identifier of an internal user specified in one of the following formats: email, Skype ID, ICQ identifier, IRC identifier, Jabber e-mail, Mail.ru Agent e-mail, Viber phone number, Zoom e-mail.

The following wild cards can be used for specifying a group of contacts:

* - any number of symbols
? - any single symbol
Recipient - specifies the destination of a data transfer controlled by this rule. It may be a single user, a list of users, or user group, as well as other types of destinations specified below.
Any - any of the recipient types supported by DLP.
Contact / Any contact - any internal or external contact.
Contact / Any internal contact - any contact of an internal user (see Automated detection of destination).
Contact / Any external contact - any contact of an external person or entity.
Contact / From organization - the same principle as described in the Sender field.
Contact / Custom identity - the same principle as described in the Sender field.
File sharing services - the identifier of a controlled file sharing service.
Social network - the identifier of a controlled social network.
Host / Any host - any computer recognized by DLP as internal or external.
Host / Any internal host - any computer recognized by DLP as internal.
Host / Any external host - any computer recognized by DLP as external.
Host / Specific host - a computer identifier specified as a host name (e.q. FQDN) or IP address (IPv4 or IPv6).
Device / Any device - any peripheral device connected to the workload.
Device / External storage - a removable storage or redirected mapped drive connected to the workload.
Device / Encrypted removable - a removable storage device encrypted with BitLocker To Go.
Device / Redirected clipboard - a redirected clipboard connected to the workload.
Printers - any local or network printer connected to the workload.
Permission - a preventive control enforced over a data transfer controlled by this rule. Described in more detail in topic Permissions in data flow policy rules.
Action - a non-preventive action performed when this rule is triggered. By default this field is set to "No action". The options are:
Write in log - store an event record in the audit log when the rule is triggered.
Notify the end user when a data transfer is denied - notify user with a real-time onscreen warning when they trigger the rule.
Generate an alert - alert the administrator when the rule is triggered.
When No action is selected and the rule is triggered:
no event record is added to the audit log;
no alert is sent to the administrator;
no onscreen notification is displayed to the end user.
What triggers a policy rule?

A data transfer matches a data flow policy rule if all of the following conditions are true:

All senders of this data transfer are listed or belong to a user group specified in the Sender field of the rule.
All recipients of this data transfer are listed or belong to a user group specified in the Recipient field of the rule.
The data being transferred matches the Sensitivity category of the rule.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.