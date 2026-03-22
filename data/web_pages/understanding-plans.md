# Understanding plans

Working with plans > Understanding plans
Understanding plans

The availability of some of the features depends on the offering items that are enabled for your account, and the administration level in the Cyber Protect console.

A plan is a set of configurations and rules that you can apply on one or several workloads to achieve different goals, such as backing up a workload, protecting a workload from malware, monitoring the workload performance, etc.

A plan consists of modules that you can enable or disable. Each module contains settings that are related to a specific functionality.

All plans that you created are visible on the Management tab.

Plan	  Description	Available at administration level


Partner

(All customers)



Customer

Unit
Protection plan

Protects the data on the workload.

At the partner level, a protection plan includes the following modules:

Antivirus and Antimalware protection

Limitations apply. For more information, see Creating a global antivirus and antimalware exclusions plan.

Vulnerability assessment

For more information, see Vulnerability assessment and patch management at partner level.

Patch management

For more information, see Vulnerability assessment and patch management at partner level.

At the customer and unit level, a protection plan includes the following modules:

Backup
Implementing disaster recovery
Endpoint Detection and Response (EDR)
Antivirus and Antimalware protection
URL filtering
Windows Defender Antivirus
Microsoft Security Essentials
Vulnerability assessment
Patch management
Data protection map
Device control

Data Loss Prevention

For more information about the protection plans, see Protection plans and modules.



Yes, with limitations



Yes	Yes
Remote management plan	Enables the remote desktop and assistance functionality on your managed workloads. For more information, see Remote management plans.	Yes	Yes	Yes
Scripting plan	Enables the script execution on multiple workloads, the scheduled script execution, and the configuration of additional script settings. For more information, see Scripting plans.	Yes	Yes	Yes
Monitoring plan	Monitors the performance, hardware, software, system, and security parameters of your managed workloads. For more information, see Monitoring plans.	Yes	Yes	Yes
Software deployment plan	Automates the software deployment process and ensures that the software distribution across your managed workloads is consistent.	Yes	Yes	Yes
Cloud applications backup	Backs up applications running in the cloud by means of agents that run in the cloud and uses the cloud storage as a backup location. For more information, see Backup plans for cloud applications	No	Yes	Yes
Archiving plan

With email archiving, all emails in a Microsoft 365 organization are retained in an external archive that is stored in the cloud. New emails are added to the archive continuously, as they are sent or received. For more information, see Email archiving.

Yes	Yes	No
Backup scanning plan	Scans backups for malware (including ransomware). For more information, see Backup scanning plans.	No	Yes	Yes
SIEM forwarding plan

Configures how Acronis alerts, events, tasks, and audit log information are forwarded for consumption by third-party Security Event and Incident Management (SIEM) platforms.
For more information, see SIEM forward plans.

Yes	No	No
Backup replication	Replicates a backup to another location. For more information, see Backup replication.	No	Yes	Yes
Validation	Validates a backup and verifies that the data from the backup can be recovered. For more information, see Validation.	No	Yes	Yes
Cleanup	Deletes outdated backups according to the retention rules. This plan is only applicable to agents and workloads, and not cloud to cloud backups. For more information, see Cleanup.	No	Yes	Yes
Conversion to VM

This plan is applicable only for disk-level backups.

Checks if a backup includes the system volume and contains all of the information necessary for the operating system to start so that the resulting virtual machine can start on its own. For more information, see Conversion to a virtual machine.

No	Yes	Yes
VM replication	Scans backups for malware (including ransomware). For more information, see Replication of virtual machines.	No	Yes	Yes

Built-in plans

Default plans

Favorite plans

Preselected plans

Plans at different administration levels

Plan status

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.