# Recovering team channels or files in team channels

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering team channels or files in team channels
Recovering team channels or files in team channels

To recover team channels

Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up teams you want to recover. Otherwise, skip this step.
Expand the Teams node, select All teams, select the team whose channels you want to recover, and then click Recovery.
Select a recovery point.
Click Recover > Channels.

Select the channels that you want to recover, and then click Recover. To select a channel in the main pane, select the check box in front of its name.

The following search options are available:

For Conversations: sender, subject, content, language, attachment name, date or date range.

For Files: file name or folder name, file type, size, date or date range of the last change.

You can also download the files locally, instead of recovering them.

If multiple Microsoft 365 organizations were added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

In Recover to team, view, change, or specify the target team.

By default, the original team is selected. If this team does not exist or a non-original organization is selected, you must specify the target team.

In Recover to channel, view, change, or specify the target channel.
Click Start recovery.

Select one of the overwriting options:

Overwrite existing content if it is older
Overwrite existing content

Do not overwrite existing content

When you recover OneNote notebooks, both of the options Overwrite existing content if it is older and Overwrite existing content will result in overwriting the exiting OneNote notebooks.

Click Proceed to confirm your decision.

Conversations are recovered as a single html file in the Files tab of the channel. You can find this file in a folder named according to the following pattern: <Team name>_<Channel name>_conversations_backup_<date of recovery>T<time of recovery>Z.

After recovering a team or team channels, go to Microsoft Teams, select the channels that were recovered, and then click their Files tab. Otherwise, the subsequent backups of these channels will not include this tab's content – due to a Microsoft Teams beta API limitation.

To recover files in a team channel

Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up teams you want to recover. Otherwise, skip this step.
Expand the Teams node, select All teams, select the team whose channels you want to recover, and then click Recovery.
Select a recovery point.
Click Recover > Channels.

Select the desired channel, and then open the Files folder.

Browse to the required items or use search to obtain the list of the required items. The following search options are available: file name or folder name, file type, size, date or date range of the last change.

To download an item, select the item, click Download, select the location in which you want to save the item, and then click Save.

Select the items that you want to recover, and then click Recover

If multiple Microsoft 365 organizations were added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

In Recover to team, view, change, or specify the target team.

By default, the original team is selected. If this team does not exist or a non-original organization is selected, you must specify the target team.

In Recover to channel, view, change, or specify the target channel.
Select whether to recover the sharing permissions of the recovered items.
Click Start recovery.

Select one of the overwriting options:

Overwrite existing content if it is older
Overwrite existing content

Do not overwrite existing content

When you recover OneNote notebooks, both of the options Overwrite existing content if it is older and Overwrite existing content will result in overwriting the exiting OneNote notebooks.

Click Proceed to confirm your decision.

You cannot recover individual conversations. In the main pane, you can only browse the Conversation folder or download its content as a single html file. To do so, click the "recover folders" icon , select the desired Conversations folder, and then click Download.

You can search the messages in the Conversation folder by:

Sender
Content
Attachment name
Date
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.