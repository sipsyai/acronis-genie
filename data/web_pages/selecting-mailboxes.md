# Selecting mailboxes

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Selecting mailboxes
Selecting mailboxes

Select the mailboxes that you want to protect, and then apply a backup plan to them.

You can create a new plan or select an existing plan.

To select Exchange Online mailboxes and apply a backup plan

New plan
Existing plan
In the Cyber Protect console, under Devices, click Microsoft 365.
[If multiple Microsoft 365 organizations are added] Select a Microsoft 365 organization.

Select the mailboxes that you want to back up.

[To back up the mailboxes of all users and all shared mailboxes, including mailboxes that will be created in the future] Expand the Users node, select All users, and then click Group backup.
[To back up individual users or shared mailboxes] Expand the Users node, select All users, select the mailboxes that you want to back up, and then click Backup.

[To back up all group mailboxes, including mailboxes of groups that will be created in the future] Expand the Groups node, select All groups, and then click Group backup.

Starting from Cyber Protect Cloud 25.06, unprotected groups that are part of a team are not shown in Devices > Microsoft 365 > Microsoft 365 organization > Groups. You can protect the SharePoint site and group mailbox of these groups by applying a backup plan to the whole team. For more information, see Protecting Microsoft 365 Teams.

At least one of the group owners must be a licensed Microsoft 365 user with a mailbox. If the group is private or with a hidden membership, the owner must also be a member of the group.

[To back up individual group mailboxes] Expand the Groups node, select All groups, select the mailboxes that you want to back up, and then click Backup.

Starting from Cyber Protect Cloud 25.06, unprotected groups that are part of a team are not shown in Devices > Microsoft 365 > Microsoft 365 organization > Groups. You can protect the SharePoint site and group mailbox of these groups by applying a backup plan to the whole team. For more information, see Protecting Microsoft 365 Teams.

At least one of the group owners must be a licensed Microsoft 365 user with a mailbox. If the group is private or with a hidden membership, the owner must also be a member of the group.

To create a backup plan, click Create new.

In the backup plan, configure the following:

[If available] In What to back up, select Microsoft 365 mailboxes.

If some of the individually selected users do not have the Exchange service included in their Microsoft 365 plan, you will not be able to select this option.

If some of the selected users for group backup do not have the Exchange service included in their Microsoft 365 plan, you will be able to select this option, but the backup plan will not be applied to those users.

In Schedule, select the backup frequency.

In How long to keep, configure the retention rules for the backups.

To include the archive mailboxes in the backup, enable the Archive mailbox switch.

In Encryption, click Specify password.
Specify and confirm the encryption password, and then select the encryption algorithm.
Click OK.

To enable antimalware scan, enable the Backup scan for malware switch.

The availability of this feature depends on the service quotas that are enabled for your account.

For more information, see Antimalware scan of mailboxes.

Click Apply.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.