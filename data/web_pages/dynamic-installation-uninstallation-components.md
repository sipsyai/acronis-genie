# Dynamic installation of components

Installing and deploying Cyber Protection agents > Before you start > Dynamic installation of components
Dynamic installation of components

For Windows workloads protected by agent version 15.0.26986 (released in May 2021) or later, the following components are installed dynamically – that is, only when required by a protection plan:

Agent for Antimalware protection and URL filtering – required for antimalware protection and URL filtering.
Agent for Data Loss Prevention – required for device control.

By default, these components are not installed. The respective component is automatically installed if a workload becomes protected by a plan in which the Antivirus & Antimalware protection module are enabled.

By default, these components are not installed. The respective component is automatically installed if a workload becomes protected by a plan in which any of the following modules are enabled:

Antivirus & Antimalware protection
URL filtering
Device control

Similarly, if no protection plan requires antimalware protection, URL filtering, or device control, the respective component is automatically uninstalled.

Similarly, if no protection plan requires antimalware protection, the respective component is automatically uninstalled.

Dynamic installation or uninstallation of components might take up to 10 minutes after you apply, revoke, edit, or delete a protection plan. If any of the following operations is running, dynamic installation or uninstallation will start after the operation completes:

Backup
Recovery
Backup replication
Virtual machine replication
Testing a replica
Running a virtual machine from backup (including finalization)
Disaster recovery failover
Disaster recovery failback
Running a script (for Cyber Scripting functionality)
Patch installation
ESXi configuration backup
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.