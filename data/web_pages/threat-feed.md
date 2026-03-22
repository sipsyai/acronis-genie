# Threat feed

Understanding your current level of protection > Monitoring > Smart protection > Threat feed
Threat feed

Acronis Cyber Protection Operations Center (CPOC) generates security alerts that are sent only to the related geographic regions. These security alerts provide information about malware, vulnerabilities, natural disasters, public health, and other types of global events that may affect your data protection. The threat feed informs you about all the potential threats and allows you to prevent them.

The availability of this feature depends on the service quotas that are enabled for your account.

Some security alerts can be resolved by following a set of specific actions that are provided by the security experts. Other security alerts just notify you about the upcoming threats but no recommended actions are available.

Malware alerts are generated only for machines that have the Agent for Antimalware protection and URL filtering installed.
How it works

Acronis Cyber Protection Operations Center monitors external threats and generates alerts about malware, vulnerability, natural disaster, and public health threats. You will be able to see all these alerts in the Cyber Protect console, in the Threat feed section. You can perform respective recommended actions depending on the type of alert.

The main workflow of the threat feed is illustrated in the diagram below.

To run the recommended actions on received alerts from Acronis Cyber Protection Operations Center, do the following:

In the Cyber Protect console, go to Monitoring> Threat feed to review if there are any existing security alerts.
Select an alert in the list and review the provided details.
Click Start to launch the wizard.

Enable the actions that you want to be performed and machines to which these actions must be applied. The following actions can be suggested:

Vulnerability assessment – to scan machines for vulnerabilities
Patch management – to install patches on the selected machines
Antimalware Protection – to run full scan of the selected machines
This action is available only for machines that have the agent for Anitmalware protection installed.
Backup of protected or unprotected machines – to back up protected and unprotected workloads.

If there are no backups yet for the workload (in all accessible locations, cloud and local), or the existing backups are encrypted, the system creates a full backup with the following name format:

%workload_name%-Remediation

By default, the destination for the backup is the Cyber Protect Cloud storage, but you can configure another location before you start the operation.

If a non-encrypted backup already exists, the system will create an incremental backup in the existing archive.

Click Start.
On the Activities page, verify that the activity was successfully performed.

Deleting all alerts

Automatic clean-up from the threat feed is made after the following time periods:

Natural disaster – 1 week
Vulnerability – 1 month
Malware – 1 month
Public health – 1 week
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.