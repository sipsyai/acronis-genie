# Selecting files or folders

Managing the backup and recovery of workloads and files > Selecting data to back up > Selecting files or folders
Selecting files or folders

Use file-level backup to protect only specific data, for example, the files in your current project. File-level backups are smaller than disk-level backups and save storage space.

You cannot recover an operating system from a file-level backup.

You can select the files and folders to back up for each individual workload in the protection plan (direct selection) or you can configure policy rules for multiple workloads. Additionally, you can exclude specific files from a backup, or include only specific files in it, by configuring the filters. For more information, see File filters (Inclusions/Exclusions).

To select files or folders

Direct selection
By policy rules
In What to back up, select Files/folders.
In Items to back up, click Specify.
In Select items for backup, select Directly.

Specify the files or folders to back up for each workload in the protection plan.

Click Select files and folders.

Click Local folder or Network folder.

Network folders must be accessible from the selected machine.

When you select Network folder as a source, you can back up data from network-attached storages (NAS), such as NetApp devices. NAS devices from all vendors are supported.

Select the files and folders that you want to back up.

You can select a combination of up to 1,000 files and folders.

Alternatively, you can specify the path to a file or folder, and then click the arrow button.

[For shared folders] Specify the user name and password for the shared folder.

Backing up folders with anonymous access is not supported.

Click Done.
Limitations
You can select files and folders when you back up physical machines or virtual machines on which an agent is installed (agent-based backup). File-level backup is not available for virtual machines that you back up in the agentless mode. For more information about the differences between these types of backup, see Agent-based and agentless backup.

You cannot recover the content of the OneDrive root folder from an Entire machine or Disk/volumes backup, even though the OneDrive folder is shown when browsing the backup archive in a file manager app, such as File Explorer. When browsing the archive in the Cyber Protect console, the OneDrive folder is not shown. When browsing the archive in the Web Restore console, the OneDrive folder is shown as a file but recovery from this backup is not possible.

To be able to recover the content of the OneDrive folder, create a Files/folders backup. Files that are not available on the device will be shown in the archive, but cannot be recovered.

You can back up files and folders that are located on disks connected via the iSCSI protocol to a physical machine. Some limitations apply if you use Agent for VMware or Agent for Hyper-V for backing up the data on the iSCSI-connected disks.

Policy rules for files and folders

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.