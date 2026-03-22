# Backup options

Managing the backup and recovery of workloads and files > Backup options
Backup options

To modify the backup options of a protection plan, in the Backup module, in the Backup options field, click Change.

Availability of the backup options

The set of available backup options depends on:

The environment the agent operates in (Windows, Linux, macOS).
The type of the data being backed up (disks, files, virtual machines, application data).
The backup destination (the cloud storage, local or network folder).

The following table summarizes the availability of backup options.

The column "Other" under "Virtual machines (agentless backup)" contains aggregated information for all supported hypervisors that do not have a dedicated column in the table:

Virtuozzo Hybrid Server
Virtuozzo Hybrid Infrastructure
Scale Computing
oVirt
Proxmox VE
Nutanix AHV

Exceptions in feature support are listed as footnotes under the table.

Option	Disk-level backup	File-level backup

Virtual machines

(agentless backup)

SQL and Exchange


Windows



Linux



macOS



Windows



Linux



macOS



ESXi



Hyper-V



Azure



Other



Windows




Alerts



+



+



+



+



+



+



+



+

-

+



+


Azure restore points: Retention	-	-	-	-	-	-	-	-	+	-	-
Azure restore points: Consistency level	-	-	-	-	-	-	-	-	+	-	-
Azure restore points: Handling unsupported disks	-	-	-	-	-	-	-	-	+	-	-


Backup consolidation



+



+



+



+



+



+



+



+

-

+



-




Backup file name



+



+



+



+



+



+



+



+

+

+



+




Backup format



+



+



+



+



+



+



+



+

-

+



+




Backup validation



+



+



+



+



+



+



+



+

-

+



+




Changed block tracking (CBT)



+



-



-



-



-



-



+



+

+

+ 1



-




Cluster backup mode



-



-



-



-



-



-



-



-

-

-



+




Compression level



+



+



+



+



+



+



+



+

+

+



+


Error handling
Re-attempt, if an error occurs

+



+



+



+



+



+



+



+

+

+



+


Do not show messages and dialogs while processing (silent mode)

+



+



+



+



+



+



+



+

+

+



+


Ignore bad sectors

+



-



+



+



-



+



+



+

+

+



-


Re-attempt, if an error occurs during VM snapshot creation

-



-



-



-



-



-



+



+

+

+



-




Fast incremental/differential backup



+



+



+



-



-



-



-



-

-

-



-




File-level backup snapshot



-



-



-



+



+



+



-



-

-

-



-




File filters



+



+



+



+



+



+



+



+

+

+



-




Forensic data



+



-



-



-



-



-



-



-

-

-



-




Log truncation



-



-



-



-



-



-



+



+

-

-



SQL only




LVM snapshotting



-



+



-



-



-



-



-



-

-

-



-




Mount points



-



-



-



+



-



-



-



-

-

-



-




Multi-volume snapshot



+



+



-



+



+



-



-



-

-

-



-


One-click recovery

+



+



-



-



-



-



-



-

-

-



-




Performance and backup window



+



+



+



+



+



+



+



+

-

+



+




Physical Data Shipping



+



+



+



+



+



+



+



+

-

+



-




Pre/Post commands



+



+



+



+



+



+



+2



+

-

+



+




Pre/Post data capture commands



+



+



+



+



+



+



+



-

-

-



+




Scheduling


Distribute start times within a time window

+



+



+



+



+



+



+



+

-

+



+


Limit the number of simultaneously running backups

-



-



-



-



-



-



+



+

-

+



-




Sector-by-sector backup



+



+



-



-



-



-



+



+

+

+



-




Splitting



+



+



+



+



+



+



+



+

-

+



+




Task failure handling



+



+



+



+



+



+



+



+

-

+



+




Task start conditions



+



+



-



+



+



-



+



+

-

+



+




Volume Shadow Copy Service (VSS)



+



-



-



+



-



-



-



+

-

-



+




Volume Shadow Copy Service (VSS) for virtual machines



-



-



-



-



-



-



+



+

-

+



-




Weekly backup



+



+



+



+



+



+



+



+

+

+



+




Windows event log



+



-



-



+



-



-



+



+

-

-



+

1 Supported for all hypervisors except oVirt.

2 Supported only when Agent for VMware is installed directly on the ESXi host. Not supported in appliance-based setups, such as when using with Agent for VMware (Virtual Appliance).

Alerts

Azure restore points

Backup consolidation

Backup file name

Backup format

Backup validation

Changed block tracking (CBT)

Cluster backup mode

Compression level

Error handling

Fast incremental/differential backup

File filters (Inclusions/Exclusions)

File-level backup snapshot

Forensic data

Log truncation

LVM snapshotting

Mount points

Multi-volume snapshot

One-click recovery

Performance and backup window

Physical Data Shipping

Pre/Post commands

Pre/Post data capture commands

Scheduling

Sector-by-sector backup

Splitting

Task failure handling

Task start conditions

Volume Shadow Copy Service (VSS)

Volume Shadow Copy Service (VSS) for virtual machines

Weekly backup

Windows event log

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.