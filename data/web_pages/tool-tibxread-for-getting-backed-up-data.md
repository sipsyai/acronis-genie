# The tool \"tibxread\" for getting the backed-up data

Managing the backup and recovery of workloads and files > Backup options > Forensic data > The tool "tibxread" for getting the backed-up data
The tool "tibxread" for getting the backed-up data

Cyber Protection provides the tool, called tibxread, for manual check of the backed-up disk integrity. The tool allows you to get data from a backup and calculate hash of the specified disk. The tool is installed automatically with the following components: Agent for Windows, Agent for Linux, and Agent for Mac.

The installation path: the same folder as the agent has (for example, C:\Program Files\BackupClient\BackupAndRecovery).

The supported locations are:

The local disk

The network folder (CIFS/SMB) that can be accessed without the credentials.

In case of a password-protected network folder, you can mount the network folder to the local folder by using the OS tools and then the local folder as the source for this tool.

The cloud storage

You should provide the URL, port, and certificate. The URL and port can be obtained from the Windows registry key or configuration files on Linux/Mac machines.

For Windows:

HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings\OnlineBackup\FesAddressCache\Default\<tenant_login>\FesUri

For Linux:

/etc/Acronis/BackupAndRecovery.config

For macOS:

/Library/Application Support/Acronis/Registry/BackupAndRecovery.config

The certificate can be found in the following locations:

For Windows:

%allusersprofile%\Acronis\BackupAndRecovery\OnlineBackup\Default

For Linux:

/var/lib/Acronis/BackupAndRecovery/OnlineBackup/Default

For macOS:

/Library/Application Support/Acronis/BackupAndRecovery/OnlineBackup/Default

The tool has the following commands:

list backups
list content
get content
calculate hash
list backups

Lists recovery points in a backup.

SYNOPSIS:

tibxread list backups --loc=URI --arc=BACKUP_NAME --raw

Options

--loc=URI
--arc=BACKUP_NAME
--raw
--utc
--log=PATH
Output template:
GUID Date Date timestamp
----   ------ --------------
<guid> <date> <timestamp>

<guid> – a backup GUID.

<date> – a creation date of the backup. Format is “DD.MM.YYYY HH24:MM:SS”. In local timezone by default (can be changed by using the --utc option).

Output example:

GUID Date Date timestamp
----   ------ --------------
516FCE73-5E5A-49EF-B673-A9EACB4093B8 18.12.2019 16:01:05 1576684865
516FCE73-5E5A-49EF-B673-A9EACB4093B9 18.12.2019 16:02:05 1576684925
list content

Lists content in a recovery point.

SYNOPSIS:

tibxread list content --loc=URI --arc=BACKUP_NAME --password --backup=RECOVERY_POINT_ID --raw --log=PATH

Options

--loc=URI
--arc=BACKUP_NAME
--password
--backup=RECOVERY_POINT_ID
--raw
--log=PATH

Output template:

Disk Size Notarization status
-------- ------ ---------------------
<number> <size> <notarization_status>

<number> – identifier of the disk.

<size> – size in bytes.

<notarization_status> – the following statuses are possible: Without notarization, Notarized, Next backup.

Output example:

Disk Size Notary status
-------- ------ --------------
1 123123465798 Notarized
2 123123465798 Notarized
get content

Writes content of the specified disk in the recovery point to the standard output (stdout).

SYNOPSIS:

tibxread get content --loc=URI --arc=BACKUP_NAME --password --backup=RECOVERY_POINT_ID --disk=DISK_NUMBER --raw --log=PATH --progress

Options

--loc=URI
--arc=BACKUP_NAME
--password
--backup=RECOVERY_POINT_ID
--disk=DISK_NUMBER
--raw
--log=PATH
--progress
calculate hash

Calculates the hash of the specified disk in the recovery point by using the SHA-2 (256-bit) algorithm and writes it to the stdout.

SYNOPSIS:

tibxread calculate hash --loc=URI --arc=BACKUP_NAME --password --backup=RECOVERY_POINT_ID --disk=DISK_NUMBER --raw --log=PATH --progress

Options

--loc=URI
--arc=BACKUP_NAME
--password
--backup=RECOVERY_POINT_ID
--disk=DISK_NUMBER
--raw
--log=PATH
Options description
Option	Description
--arc=BACKUP_NAME	The backup file name that you can get from the backup properties in the Cyber Protect console. The backup file must be specified with the extension .tibx.
--backup=RECOVERY_POINT_ID	The recovery point identifier
--disk=DISK_NUMBER	Disk number (the same as was written to the output of the "get content" command)
--loc=URI

A backup location URI. The possible formats of the "--loc" option are:

Local path name (Windows)

c:/upload/backups

Local path name (Linux)

/var/tmp

SMB/CIFS

\\server\folder

Cloud storage

--loc=<IP_address>:443 --cert=<path_to_certificate> [--storage_path=/1]

<IP_address> – you can find it in the registry key in Windows: HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings\OnlineBackup\FesAddressCache\Default\<tenant_login>\FesUri

<path_to_certificate> – a path to the certificate file to access Cyber Protect Cloud. For example, in Windows this certificate is located in C:\ProgramData\Acronis\BackupAndRecovery\OnlineBackup\Default\<username>.crt where <username> – is your account name to access Cyber Protect Cloud.


--log=PATH	Enables writing the logs by the specified PATH (local path only, format is the same as for --loc=URI parameter). Logging level is DEBUG.
--password=PASSWORD	An encryption password for your backup. If the backup is not encrypted, leave this value empty.
--raw

Hides the headers (2 first rows) in the command output. It is used when the command output should be parsed.

Output example without "--raw":

GUID Date Date timestamp
----   ------ --------------
516FCE73-5E5A-49EF-B673-A9EACB4093B8 18.12.2019 16:01:05 1576684865
516FCE73-5E5A-49EF-B673-A9EACB4093B9 18.12.2019 16:02:05 1576684925

Output with"--raw":

516FCE73-5E5A-49EF-B673-A9EACB4093B8 18.12.2019 16:01:05 1576684865
516FCE73-5E5A-49EF-B673-A9EACB4093B9 18.12.2019 16:02:05 1576684925

--utc	Shows dates in UTC
--progress

Shows progress of the operation.

For example:

1%
2%
3%
4%
...
100%
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.