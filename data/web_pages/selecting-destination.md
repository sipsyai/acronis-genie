# Selecting a destination

Managing the backup and recovery of workloads and files > Selecting a destination
Selecting a destination

Click Where to back up, and then select one of the following:

Cloud storage

Backups will be stored in the cloud data center.

Backups to public cloud require a Local backup storage quota.

Local folders

If a single machine is selected, browse to a folder on the selected machine or type the folder path.

If multiple machines are selected, type the folder path. Backups will be stored in this folder on each of the selected physical machines or on the machine where the agent for virtual machines is installed. If the folder does not exist, it will be created.

Network folder

This is a folder shared via SMB/CIFS/DFS.

Browse to the required shared folder or enter the path in the following format, where <host> is either a full DNS domain name or an IPv4 address:

For SMB/CIFS shares:

\\<host>\<path>\

smb://<host>/<path>/

For DFS shares:

\\<host>\<DFS root>\<path>

Then, click the arrow button. If prompted, specify the user name and password for the shared folder. You can change these credentials at any time by clicking the key icon next to the folder name.

Backing up to a folder with anonymous access is not supported.

Public cloud

This option is available if the Direct Backup to Public Cloud feature is enabled for your tenant.

It enables you to configure a direct backup to a public cloud compatible storage, without the need to deploy additional components (such as Microsoft Azure or other virtual machines as gateways). Select and connect to the relevant public cloud, as required.

Backups to public cloud require a Local backup storage quota.

For more information, see Backing up workloads to public clouds.

NFS folder (available for machines running Linux or macOS)

Verify that the nfs-utils package is installed on the Linux server where the Agent for Linux is installed.

Browse to the required NFS folder or enter the path in the following format, where <host> is either a full DNS domain name or an IPv4 address:

nfs://<host>/<exported folder>:/<subfolder>

Then, click the arrow button.

It is not possible to back up to an NFS folder protected with a password.

Secure Zone (available if it is present on each of the selected machines)

Secure Zone is a secure partition on a disk of the backed-up machine. This partition has to be created manually prior to configuring a backup. For information about how to create Secure Zone, its advantages and limitations, see About Secure Zone.

Advanced storage option

This functionality is available only in the Advanced edition of the Cyber Protection service.

Defined by a script (available for machines running Windows)

You can store each machine's backups in a folder deﬁned by a script. The software supports scripts written in JScript, VBScript, or Python 3.5. When deploying the protection plan, the software runs the script on each machine. The script output for each machine should be a local or network folder path. If a folder does not exist, it will be created (limitation: scripts written in Python cannot create folders on network shares). On the Backup storage tab, each folder is shown as a separate backup location.

In Script type, select the script type (JScript, VBScript, or Python), and then import, or copy and paste the script. For network folders, specify the access credentials with the read/write permissions.

Examples:

The following JScript script outputs the backup location for a machine in the format \\bkpsrv\<machine name>:

WScript.Echo("\\\\bkpsrv\\" + WScript.CreateObject("WScript.Network").ComputerName);

As a result, the backups of each machine will be saved in a folder of the same name on the server bkpsrv.

The following JScript script outputs the backup location in a folder on the machine where the script runs:

WScript.Echo("C:\\Backup");

As a result, the backups of this machine will be saved in the folder C:\Backup on the same machine.

The location path in these scripts is case-sensitive. Therefore, C:\Backup and C:\backup are displayed as different locations in the Cyber Protect console. Also, use upper case for the drive letter.

About Secure Zone

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.