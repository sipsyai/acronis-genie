# Requirements for application-aware backups

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Requirements for application-aware backups
Requirements for application-aware backups

Before configuring the application backup, ensure that the requirements listed below are met.

To check the VSS writers state, use the vssadmin list writers command.

Common requirements

For Microsoft SQL Server, ensure that:

At least one Microsoft SQL Server instance is started.
The SQL writer for VSS is turned on.

For Microsoft Exchange Server, ensure that:

The Microsoft Exchange Information Store service is started.
Windows PowerShell is installed. For Exchange 2010 or later, the Windows PowerShell version must be at least 2.0.

Microsoft .NET Framework is installed.

For Exchange 2007, the Microsoft .NET Framework version must be at least 2.0.

For Exchange 2010 or later, the Microsoft .NET Framework version must be at least 3.5.

The Exchange writer for VSS is turned on.
Agent for Exchange needs a temporary storage to operate. By default, the temporary files are located in %ProgramData%\Acronis\Temp. Ensure that you have at least as much free space on the volume where the %ProgramData% folder is located as 15 percent of an Exchange database size. Alternatively, you can change the location of the temporary files before creating Exchange backups as described in Changing Temp Files and Folder Location (40040).

On a domain controller, ensure that:

The Active Directory writer for VSS is turned on.

When creating a protection plan, ensure that:

For physical machines and machines with the agent installed inside, the Volume Shadow Copy Service (VSS) backup option is enabled.
For virtual machines, the Volume Shadow Copy Service (VSS) for virtual machines backup option is enabled.
Additional requirements for application-aware backups

When creating a protection plan, ensure that Entire machine is selected for backup. The Sector-by-sector backup option must be disabled in a protection plan. Otherwise, recovery of application data from such backups will be impossble. If the plan is executed in the Sector-by-sector mode due to an automatic switch to this mode, then recovery of application data will also be impossible.

Requirements for ESXi virtual machines

If the application runs on a virtual machine that is backed up by Agent for VMware, ensure that:

The virtual machine being backed up meets the requirements for application-consistent backup and restore listed in the article "Windows Backup Implementations" in the VMware documentation: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/virtual-disk-development-kit-programming-guide/backing-up-virtual-disks-in-vsphere/windows-backup-implementations/working-with-microsoft-shadow-copy.html.
VMware Tools is installed and up-to-date on the machine.
User Account Control (UAC) is disabled on the machine. If you do not want to disable UAC, you must provide the credentials of the built-in domain administrator (DOMAIN\Administrator) when enabling application backup.

If you do not want to disable UAC, you must provide the credentials of the built-in domain administrator (DOMAIN\Administrator) when enabling application backup.

Use the built-in domain administrator account that was configured as part of the creation of the domain. Accounts created later are not supported.
Requirements for Hyper-V virtual machines

If the application runs on a virtual machine that is backed up by Agent for Hyper-V, ensure that:

The guest operating system is Windows Server 2008 or later.
For Hyper-V 2008 R2: the guest operating system is Windows Server 2008/2008 R2/2012.
The virtual machine has no dynamic disks.
The network connection exists between the Hyper-V host and the guest operating system. This is required to execute remote WMI queries inside the virtual machine.
User Account Control (UAC) is disabled on the machine. If you do not want to disable UAC, you must provide the credentials of the built-in domain administrator (DOMAIN\Administrator) when enabling application backup.

If you do not want to disable UAC, you must provide the credentials of the built-in domain administrator (DOMAIN\Administrator) when enabling application backup.

Use the built-in domain administrator account that was configured as part of the creation of the domain. Accounts created later are not supported.

The virtual machine configuration matches the following criteria:

Hyper-V Integration Services is installed and up-to-date. The critical update is https://support.microsoft.com/en-us/help/3063109/hyper-v-integration-components-update-for-windows-virtual-machines
In the virtual machine settings, the Management > Integration Services > Backup (volume checkpoint) option is enabled.
For Hyper-V 2012 and later: the virtual machine has no checkpoints.
For Hyper-V 2012 R2 and later: the virtual machine has a SCSI controller (check Settings > Hardware).
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.