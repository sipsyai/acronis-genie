# Required user rights for application-aware backups

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Application-aware backup > Required user rights for application-aware backups
Required user rights for application-aware backups

An application-aware backup contains metadata of VSS-aware applications that are present on the disk. To access this metadata, the agent needs an account with the appropriate rights, which are listed below. You are prompted to specify this account when enabling application backup.

For SQL Server:

The account must be a member of the Backup Operators or Administrators group on the machine and a member of the sysadmin role on each of the instances that you are going to back up.

Only Windows authentication is supported.

For Exchange Server:

Exchange 2007: The account must be a member of the Administrators group on the machine, and a member of the Exchange Organization Administrators role group.

Exchange 2010 and later: The account must be a member of the Administrators group on the machine, and a member of the Organization Management role group.

For Active Directory:

The account must be a domain administrator.

Additional requirement for virtual machines

If the application runs on a virtual machine that is backed up by Agent for VMware or Agent for Hyper-V, ensure that User Account Control (UAC) is disabled on the machine.

If you do not want to disable UAC, you must provide the credentials of the built-in domain administrator (DOMAIN\Administrator) when enabling application backup.

Use the built-in domain administrator account that was configured as part of the creation of the domain. Accounts created later are not supported.
Additional requirements for machines running Windows

For all Windows versions, you must disable the User Account Control (UAC) policies to allow application-aware backups.

If you do not want to disable UAC, you must provide the credentials of the built-in domain administrator (DOMAIN\Administrator) when enabling application backup.

Use the built-in domain administrator account that was configured as part of the creation of the domain. Accounts created later are not supported.

To disable the UAC policies in Windows

In the Registry Editor, locate the following registry key:

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System

Change the EnableLUA value to 0.
Restart the machine.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.