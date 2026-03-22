# Application-aware backup

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Application-aware backup
Application-aware backup

Application-aware disk-level backup is available for individual physical machines, ESXi virtual machines, and Hyper-V virtual machines. It is not available for device groups.

When you back up a machine running Microsoft SQL Server, Microsoft Exchange Server, or Active Directory Domain Services, enable Application backup for additional protection of these applications' data.

Why use application-aware backup?

By using application-aware backup, you ensure that:

The applications are backed up in a consistent state and thus will be available immediately after the machine is recovered.
You can recover the SQL and Exchange databases, mailboxes, and mailbox items without recovering the entire machine.
The SQL transaction logs are truncated after each successful backup. SQL log truncation can be disabled in the protection plan options. The Exchange transaction logs are truncated on virtual machines only. You can enable the VSS full backup option if you want to truncate Exchange transaction logs on a physical machine.
If a domain contains more than one domain controller, and you recover one of them, a nonauthoritative restore is performed and a USN rollback will not occur after the recovery.
What do I need to use application-aware backup?

On a physical machine, Agent for SQL and/or Agent for Exchange must be installed, in addition to Agent for Windows.

On a virtual machine, no agent installation is required. It is presumed that the machine is backed up by Agent for VMware or Agent for Hyper-V.

Agentless application-aware backup is not supported for Hyper-V and VMware ESXi virtual machines that are running Windows Server 2022 or Windows Server 2025. To protect Microsoft applications on these machines, install the protection agent inside the guest operating system. For more information, see Configuring application-aware backup of virtual machines running Windows Server 2022 and later.

Agent for VMware (Virtual Appliance) can create application-aware backups, but cannot recover application data from them. To recover application data from backups created by this agent, you need Agent for VMware (Windows), Agent for SQL, or Agent for Exchange on a machine that has access to the location where the backups are stored. When configuring recovery of application data, select the recovery point on the Backup storage tab, and then select this machine in Machine to browse from.

Additional requirements are listed in Requirements for application-aware backups and Required user rights for application-aware backups.

Application-aware backups of Hyper-V virtual machines may fail with the error "WMI 'ExecQuery' failed executing query." or "Failed to create a new process via WMI" if the backups are performed on a host under high load, due to no or delayed response from Windows Management Instrumentation. Retry these backups in a time slot when the load on the host is lower.

Configuring application-aware backup of virtual machines running Windows Server 2022 and later

Required user rights for application-aware backups

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.