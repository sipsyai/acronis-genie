# Mount Points 36348

Managing the backup and recovery of workloads and files > Backup options > Mount points
Mount points

This option is effective only in Windows for a file-level backup of a data source that includes mounted volumes or cluster shared volumes.

For Linux and macOS, the Backup Mount Points option is ignored, and the behavior will be as follows:
The data in "local" mount points, such as local disks, USB drives, etc., will always be backed up.
The data in "remote" mount points, such as CIFS/NFS shares, etc., will never be backed up.

This option is effective only when you select for backup a folder that is higher in the folder hierarchy than the mount point. (A mount point is a folder on which an additional volume is logically attached.)

If such folder (a parent folder) is selected for backup, and the Mount points option is enabled, all files located on the mounted volume will be included in the backup. If the Mount points option is disabled, the mount point in the backup will be empty.

During recovery of a parent folder, the mount point content will or will not be recovered, depending on whether the Mount points option for recovery is enabled or disabled.

If you select the mount point directly, or select any folder within the mounted volume, the selected folders will be considered as ordinary folders. They will be backed up regardless of the state of the Mount points option and recovered regardless of the state of the Mount points option for recovery.

The preset is: Disabled.

You can back up Hyper-V virtual machines residing on a cluster shared volume by backing up the required files or the entire volume with file-level backup. Just power off the virtual machines to be sure that they are backed up in a consistent state.

Example

Let's assume that the C:\Data1\ folder is a mount point for the mounted volume. The volume contains folders Folder1 and Folder2. You create a protection plan for file-level backup of your data.

If you select the check box for volume C and enable the Mount points option, the C:\Data1\ folder in your backup will contain Folder1 and Folder2. When recovering the backed-up data, be aware of proper using the Mount points option for recovery.

If you select the check box for volume C, and disable the Mount points option, the C:\Data1\ folder in your backup will be empty.

If you select the check box for the Data1, Folder1 or Folder2 folder, the checked folders will be included in the backup as ordinary folders, regardless of the state of the Mount points option.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.