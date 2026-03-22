# Mounting volumes from a backup

Managing the backup and recovery of workloads and files > Operations with backups > Mounting volumes from a backup
Mounting volumes from a backup

Mounting volumes from a disk-level backup lets you access the volumes as though they were physical disks.

Mounting volumes in the read/write mode enables you to modify the backup content; that is, save, move, create, delete files or folders, and run executables consisting of one file. In this mode, the software creates an incremental backup that contains the changes you make to the backup content. Note that none of the subsequent backups will contain these changes.

Requirements
This functionality is available only in Windows by using File Explorer.
Agent for Windows must be installed on the machine that performs the mount operation.
The backed-up file system must be supported by the Windows version that the machine is running.
The backup must be stored in a local folder, on a network share (SMB/CIFS), or in the Secure Zone.
Usage scenarios

Sharing data

Mounted volumes can be easily shared over the network.

"Band-aid" database recovery solution

Mount a volume that contains an SQL database from a recently failed machine. This will provide access to the database until the failed machine is recovered. This approach can also be used for granular recovery of Microsoft SharePoint data by using SharePoint Explorer.

Offline virus removal

If a machine is infected, mount its backup, clean it with an antivirus program (or find the latest backup that is not infected), and then recover the machine from this backup.

Error check

If a recovery with volume resize has failed, the reason may be an error in the backed-up file system. Mount the backup in the read/write mode. Then, check the mounted volume for errors by using the chkdsk /r command. After the errors are fixed and a new incremental backup is created, recover the system from this backup.

To mount a volume from a backup

Browse to the backup location by using File Explorer.

Double-click the backup file. The file names are based on the following template:

<machine name> - <protection plan GUID>

If the backup is encrypted, enter the encryption password. Otherwise, skip this step.

File Explorer displays the recovery points.

Double-click the recovery point.

File Explorer displays the backed-up volumes.

Double-click a volume to browse its content. You can copy files and folders from the backup to any folder on the file system.

Right-click a volume to mount, and then select one of the following options:
Mount
Only the last backup in the archive (backup chain) can be mounted in read-write mode.
Mount in read-only mode.

If the backup is stored on a network share, provide access credentials. Otherwise, skip this step.

The software mounts the selected volume. The first unused letter is assigned to the volume.

To unmount a volume

Browse to Computer (This PC in Windows 8.1 and later) by using File Explorer.
Right-click the mounted volume.
Click Unmount.

If the volume was mounted in the read/write mode, and its content was modified, select whether to create an incremental backup containing the changes. Otherwise, skip this step.

The software unmounts the selected volume.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.