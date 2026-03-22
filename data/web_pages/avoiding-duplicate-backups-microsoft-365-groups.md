# Avoiding duplicate backups of Microsoft 365 groups

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Avoiding duplicate backups of Microsoft 365 groups
Avoiding duplicate backups of Microsoft 365 groups

Duplicate backups can occur when a Microsoft 365 group that is part of a Microsoft team is backed up under both Teams and Groups:

Teams backup

In Devices > Microsoft 365 > Microsoft 365 organization > Teams, you can configure a team backup. This includes the SharePoint site, group mailbox, and other team-related data.

Groups backup

In Devices > Microsoft 365 > Microsoft 365 organization > Groups, you can configure a backup for SharePoint site and group mailbox.

Group	Groups appears in Devices > Microsoft 365 > Groups	Possibility for duplicate backups
Group not in a team

A group plan* is applied

Yes	No


A group plan is not applied

Yes	No
Group in a team

A group plan is applied



Yes

These groups are marked with a warning icon , because they might be backed up twice, under both Groups and Teams.

If you do not back up such a group as part of a team, you can ignore this warning.

If you back up such a group as part of a team, avoid duplicate backups by configuring protection only in the relevant team.



Yes




A group plan is not applied



No

Starting from Cyber Protect Cloud 25.06, unprotected groups that are part of a team are not shown in Devices > Microsoft 365 > Microsoft 365 organization > Groups. You can protect the SharePoint site and group mailbox of these groups by applying a backup plan to the whole team. For more information, see Protecting Microsoft 365 Teams.



No

* A group plan is a backup plan for SharePoint sites or mailboxes that is applied under Groups.

To avoid duplicate backups of a Microsoft 365 group

Log in to the Cyber Protect console.

Go to Devices > Microsoft 365 > Microsoft 365 organization > Groups > All groups.

Check the Team column.

If the column is blank, the group is not part of a team.

If the column shows a team name, the group is part of a team.

A warning icon  indicates that this group might have duplicate backups, under both Groups and Teams.

[If the backup is configured under both Groups and Teams] Configure the backup only at the team level.

Go to Devices > Microsoft 365 > Microsoft 365 organization > Teams > All teams, and then ensure that a backup plan is applied to the team that includes the group.

Go to Devices > Microsoft 365 > Microsoft 365 organization > Groups > All groups, and then revoke the group backup plans. For more information, see Revoking a backup plan for Microsoft 365 Business – Backup.

Plans that are applied at a group level can only be revoked at the group level. For example, you cannot revoke a plan that is applied to All groups by editing the protection setting for a specific workload in the group. For more information, see To revoke a backup plan > Devices > step 4.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.