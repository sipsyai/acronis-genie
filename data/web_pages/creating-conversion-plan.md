# Creating a conversion plan

Working with plans > Off-host data protection plans > Conversion to a virtual machine > Creating a conversion plan
Creating a conversion plan

To convert a disk-level backup to a virtual machine, you must create a conversion plan.

You can use this plan to migrate a virtual machine to a non-original hypervisor. For example, you can convert a backup of a VMware virtual machine to a Proxmox virtual machine.

Also, with a conversion plan, you can update the resulting virtual machine after each incremental or differential backup.

Incremental updates are not available for virtual machines that are created by VMware Workstation and VHDX files options. For more information, see Types of conversion to virtual machine.

To create a conversion plan

VMware ESXi
Microsoft Hyper-V
Scale Computing HC3
Virtuozzo Hybrid Infrastructure
VMware Workstation
VHDX files
Proxmox VE
In the Cyber Protect console, go to Management > Conversion to VM.
Click Create plan.

To rename the plan, click the pencil icon, enter a new name, and then click OK.

In Convert to, select VMware ESXi.
In Host, select the target host, specify the virtual machine name, and then click OK.
In Agent, select the agent that will perform the conversion.

In Items to convert, select one or more backups to convert, and then click Done.

To switch between selecting individual backups and backup locations, click Locations / Backups.

If the selected backups are encrypted, all of them must use the same encryption password. For backups that use different encryption passwords, create separate plans.

[If prompted] Specify the credentials to access the backup location, and then click OK.
In Datastore, select the storage for the virtual machine.
In Provisioning mode, select the disk provisioning mode.
In VM settings, change the memory size, the number of processors, or the network connections of the virtual machine, and then click OK.

In Schedule, change the plan schedule, and then click OK.

[If the selected backups are encrypted] Turn on the Backup password switch, provide the encryption password, and then click OK.

To change error handling, performance, pre-post commands or task failure handling, click the gear icon, update the settings, and then click Done.

Click Create.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.