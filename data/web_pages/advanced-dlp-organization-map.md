# Organization map

Data Loss Prevention > Organization map
Organization map
This functionality is accessible only to Company Administrator users.

The organization map is a database that contains data for users and all their accounts used to transfer data through instant messaging, email, or any other means, that have been intercepted by DLP.

The organization map provides means to create and manage user groups in DLP, and to manage users and accounts associated to users in DLP. User groups can then be used for group-based DLP policy management.

To locate the Organization map

In the Cyber Protect Cloud console, navigate to Protection > Data loss prevention > Organization map.
How does it work?
The organization map is populated while the DLP module operates in Observation mode.

For every data transfer intercepted by the DLP Agent, the following attributes are collected in the back end.

Attribute	Description	Label in the UI
Organization Unit	A manually created group. The Organization unit can have one or more nested Organization Units.	Group name, as defined
Security ID	A unique security identifier.	On the user details page > SID


A user-friendly display name derived from the account names for the user. This name is not always available in Organization map.

Name
PC\UserName	The name of the user of the endpoint (workload).

A user name can be assigned to only one Organization Unit.

User name
Device (Workload)	The name of the endpoint (workload).	Workload
Account

Accounts that were used by a user for communication via instant messaging and email, and have been intercepted by the DLP Agent. For example, if the agent detects that username 'PC\John' uses john@gmail.com to send an email - this account is linked to PC\John user name.

Accounts

In the organization map, you can view and search accounts, users, and groups, and create, edit, and delete groups.

To search for specific accounts

As part of incident investigation, Administrator users might need to find the owner of a specific account that was involved in a potential data breach.

In the Cyber Protect Cloud console, navigate to Protection > Data loss prevention > Organization map.

In the Search text box above the users list, start typing or paste the account.

The list is filtered as you type.

To search for a specific user name

In the Cyber Protect Cloud console, navigate to Protection > Data loss prevention > Organization map.

To search in a specific group, click the group name in the list.
In the Search text box above the users list, start typing or paste a user name.

The list is filtered as you type.

To view the accounts used by a particular user name

Locate the user in the users list.
Click the three dots at the end of the user row and select View.
In the user details dialog, locate the Associated accounts section.
You can add comments in the Description text box.

To create a user group

In the Cyber Protect Cloud console, navigate to Protection > Data loss prevention > Organization map.

In the lower left section of the groups list, click Create group.

The Create organizational unit dialog opens.

From the Parent drop-down menu, select the context for the new group.
You cannot change the parent later. The group will remain nested in this context.
Enter a group name and click Save.

To add a user to a group

In the Cyber Protect Cloud console, navigate to Protection > Data loss prevention > Organization map.

In the users list, locate the user that you want to add and select the check box in the beginning of the user row.

The Move selected and Delete selected buttons appear above the users list.

Click Move selected.

The Move user dialog opens.

Select a new parent for the selectet user and click Save.
A user can belong to only one group.

To delete an account associated to a user

Locate the user in the users list.
Click the three dots at the end of the user row and select View.
In the user details dialog, locate the Associated accounts section.
Locate the account that you want to delete and click the three dots next to it.
From the drop-down list, select Delete.

To rename a user group

In the Cyber Protect Cloud console, navigate to Protection > Data loss prevention > Organization map.

Click the three dots next to the name of the group and click Rename.

To delete a user group

In the Cyber Protect Cloud console, navigate to Protection > Data loss prevention > Organization map.

Click the three dots next to the name of the group and click Delete.

All users from the goup are moved to the parent entity.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.