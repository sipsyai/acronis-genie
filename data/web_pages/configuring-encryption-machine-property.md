# Configuring encryption as a machine property

Managing the backup and recovery of workloads and files > Encryption > Configuring encryption as a machine property
Configuring encryption as a machine property

You can configure backup encryption as a machine property. In this case, backup encryption is not configured in the protection plan, but on the protected workload. Encryption as a machine property uses the AES algorithm with a 256-bit key (AES-256).

Using the AES-256 algorithm with a strong password provides quantum-resistant encryption. It is safe against cryptanalytic attacks that rely on quantum computing.

Configuring encryption as a machine property affects the protection plans in the following way:

Protection plans that are already applied to the machine. If the encryption settings in a protection plan are different, the backups will fail.
Protection plans that will be applied to the machine later. The encryption settings saved on the machine will override the encryption settings in the protection plan. Any backup will be encrypted, even if encryption is disabled in the Backup module settings.

For accounts in Compliance mode, only encryption as a machine property is available.

If you have more than one Agent for VMware connected to the same vCenter Server, and you configure encryption as a machine property, you must use the same encryption password on all machines with Agent for VMware, because of the load balancing between the agents.

You can configure encryption as a machine property in the following ways:

On the command line
In Cyber Protect Monitor (Available for Windows and macOS)
There is no way to recover encrypted backups if you lose or forget the password.

To configure encryption as a machine property

On the command line
In Cyber Protect Monitor
Log in as an administrator in Windows or the root user in Linux.

Navigate to the acropsh tool, as follows:

For Windows:

<installation_path>\PyShell\bin\

Where <installation_path> is %ProgramFiles%\BackupClient.

For Linux:

/usr/sbin/

For a virtual appliance:

/./sbin/

[To specify the password in the command-line interface]

Run the following command:

For Windows

acropsh.exe -m manage_creds --set-password

For Linux and virtual appliance

acropsh -m manage_creds --set-password

At the interactive prompt, specify the encryption password.

[To specify the password by using a file]

Prepare a text file, in which you specify the encryption password.

The file must have the following content:

--set-password <password>

Where <password> is the encryption password.

For security reasons, ensure that only you can access this file. Delete the file after you finish this procedure.

On the command line, run the following command:

For Windows

acropsh.exe -m manage_creds @<file_path>

For Linux and virtual appliance

acropsh -m manage_creds @<file_path>

Where <file_path> is the full path to the file in which the password is specified.

For example, /home/JohnDoe/MyFile.txt or C:\Users\JohnDoe\MyFile.txt.

To reset the encryption settings

Log in as an administrator in Windows or root user in Linux.

Navigate to the acropsh tool, as follows:

For Windows:

<installation_path>\PyShell\bin\

Where <installation_path> is %ProgramFiles%\BackupClient.

For Linux:

/usr/sbin/

For a virtual appliance:

/./sbin/

Run the following command:

For Windows

acropsh.exe -m manage_creds --reset

For Linux and virtual appliance

acropsh -m manage_creds --reset
If you reset the encryption as a machine property or change the encryption password after a protection plan creates a backup, the next backup operation will fail. To continue backing up the workload, create a new protection plan.
See also
Compliance mode
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.