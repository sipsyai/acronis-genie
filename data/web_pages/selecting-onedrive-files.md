# Selecting OneDrive files

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Selecting OneDrive files
Selecting OneDrive files

Select the files as described below, and then specify other settings of the protection plan as appropriate.

To select OneDrive files

Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose users' data you want to back up. Otherwise, skip this step.

Do one of the following:

To back up the files of all users (including users that will be created in the future), expand the Users node, select All users, and then click Group backup.
To back up the files of individual users, expand the Users node, select All users, select the users whose files you want to back up, and then click Backup.

In the backup plan, configure the following:

[If available] In What to back up, select OneDrive.

If some of the individually selected users do not have the OneDrive service included in their Microsoft 365 plan, you will not be able to select this option.

If some of the selected users for group backup do not have the OneDrive service included in their Microsoft 365 plan, you will be able to select this option, but the protection plan will not be applied to those users.

In Items to back up, do one of the following:

Keep the default setting [All] (all files).

Specify the files and folders to back up by adding their names or paths.

You can use wildcard characters (*, **, and ?). For more details about specifying paths and using wildcards, see File filters (Inclusions/Exclusions).

Specify the files and folders to back up by browsing.

The Browse link is available only when creating a protection plan for a single user.

In Encryption, click Specify password.
Specify and confirm the encryption password, and then select the encryption algorithm.
Click OK.

[Optional] In Items to back up, click Show exclusions to specify the files and folders to skip during the backup.

File exclusions override the file selection. If you specify the same file in both fields, this file will be skipped during a backup.

To back up OneNote notebooks, enable the Include OneNote switch.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.