# Recovering an entire team

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering an entire team
Recovering an entire team
Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up teams you want to recover. Otherwise, skip this step.

Expand the Teams node, select All teams, select the team that you want to recover, and then click Recovery.

You can search teams by name. Wildcards are not supported.

Select a recovery point.

Click Recover > Entire Team.

If multiple Microsoft 365 organizations were added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

In Recover to team, view the target team or select another.

By default, the original team is selected. If this team does not exist (for example, it was deleted) or you selected an organization that does not contain the original team, you must select a target team from the drop-down list.

You can recover a team only into an existing team. You cannot create teams during recovery operations.

Click Start recovery.

Select one of the overwriting options:

Overwrite existing content if it is older
Overwrite existing content

Do not overwrite existing content

When you recover OneNote notebooks, both of the options Overwrite existing content if it is older and Overwrite existing content will result in overwriting the exiting OneNote notebooks.

Click Proceed to confirm your decision.

When you delete a channel in Microsoft Teams' graphic interface, it is not immediately removed from the system. Thus, when you recover the whole team, this channel's name cannot be used and a postfix will be added to it.

Conversations are recovered as a single html file in the Files tab of the channel. You can find this file in a folder named according to the following pattern: <Team name>_<Channel name>_conversations_backup_<date of recovery>T<time of recovery>Z.

After recovering a team or team channels, go to Microsoft Teams, select the channels that were recovered, and then click their Files tab. Otherwise, the subsequent backups of these channels will not include this tab's content – due to a Microsoft Teams beta API limitation.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.