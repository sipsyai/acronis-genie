# Limitations for recovering files in the Cyber Protect console

Managing the backup and recovery of workloads and files > Recovery > Recovering files > Limitations for recovering files in the Cyber Protect console
Limitations for recovering files in the Cyber Protect console
Tenants in Compliance mode

In the Cyber Protect console, you cannot recover backups in tenants in Compliance mode. See Recovering backups in tenants in Compliance mode.

Recovery to Virtuozzo containers or Virtuozzo virtual machines

QEMU Guest Agent must be installed on the target virtual machine.

[Only applicable when recovering to containers] Mount points inside containers cannot be used as target for recovery. For example, you cannot recover files to a second hard disk or an NFS share mounted to a container.

When recovering files to a Windows virtual machine, and if the File-level security recovery option is enabled, the archive bit attribute is set to the recovered files.

Files with non-ANSI characters in their names are recovered with incorrect names on machines running Windows Server 2012 or older and machines running Windows 7 or older.

To recover files to CentOS or Red Hat Enterprise Linux virtual machines that run on Virtuozzo Hybrid Server, you must edit the qemu-ga file, as follows:

On the target virtual machine, navigate to /etc/sysconfig/, and then open the qemu-ga file for editing.

Navigate to the following line, and then delete everything after the equals sign (=):

BLACKLIST_RPC=

Restart QEMU Guest Agent by running the following command:

systemctl restart qemu-guest-agent
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.