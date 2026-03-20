---
title: "Organization Map and Known Issues"
section: "Data Loss Prevention"
subsection: "Organization Map"
page_range: "1477-1480"
tags: [dlp, organization-map, user-groups, accounts, incident-investigation, known-issues, limitations]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#advanced-dlp-organization-map.html"
---

# Organization Map and Known Issues

## Organization Map

> **Note:** This functionality is accessible only to Company Administrator users.

The organization map is a database that contains data for users and all their accounts used to transfer data through instant messaging, email, or any other means, that have been intercepted by DLP.

The organization map provides means to create and manage user groups in DLP, and to manage users and accounts associated to users in DLP. User groups can then be used for group-based DLP policy management.

### To Locate the Organization Map

In the Cyber Protect Cloud console, navigate to **Protection** > **Data loss prevention** > **Organization map**.

## How Does It Work?

> **Note:** The organization map is populated while the DLP module operates in Observation mode.

For every data transfer intercepted by the DLP Agent, the following attributes are collected in the back end:

| Attribute | Description | Label in the UI |
|-----------|-------------|-----------------|
| Organization Unit | A manually created group. The Organization unit can have one or more nested Organization Units. | Group name, as defined |
| Security ID | A unique security identifier. | On the user details page > **SID** |
| (display name) | A user-friendly display name derived from the account names for the user. This name is not always available in Organization map. | **Name** |
| PC\UserName | The name of the user of the endpoint (workload). A user name can be assigned to only one Organization Unit. | **User name** |
| Device (Workload) | The name of the endpoint (workload). | **Workload** |
| Account | Accounts that were used by a user for communication via instant messaging and email, and have been intercepted by the DLP Agent. For example, if the agent detects that username 'PC\john' uses john@gmail.com to send an email - this account is linked to PC\john user name. | **Accounts** |

In the organization map, you can view and search accounts, users, and groups, and create, edit, and delete groups.

### Searching for Specific Accounts

As part of incident investigation, Administrator users might need to find the owner of a specific account that was involved in a potential data breach.

1. In the Cyber Protect Cloud console, navigate to **Protection** > **Data loss prevention** > **Organization map**.
2. In the **Search** text box above the users list, start typing or paste the account. The list is filtered as you type.

### Searching for a Specific User Name

1. In the Cyber Protect Cloud console, navigate to **Protection** > **Data loss prevention** > **Organization map**.
2. To search in a specific group, click the group name in the list.
3. In the **Search** text box above the users list, start typing or paste a user name. The list is filtered as you type.

### Viewing the Accounts Used by a Particular User Name

1. Locate the user in the users list.
2. Click the three dots at the end of the user row and select **View**.
3. In the user details dialog, locate the **Associated accounts** section.
4. You can add comments in the Description text box.

### Creating a User Group

1. In the Cyber Protect Cloud console, navigate to **Protection** > **Data loss prevention** > **Organization map**.
2. In the lower left section of the groups list, click **Create group**. The Create organizational unit dialog opens.
3. From the Parent drop-down menu, select the context for the new group.

   > **Note:** You cannot change the parent later. The group will remain nested in this context.

4. Enter a group name and click **Save**.

### Adding a User to a Group

1. In the Cyber Protect Cloud console, navigate to **Protection** > **Data loss prevention** > **Organization map**.
2. In the users list, locate the user that you want to add and select the check box in the beginning of the user row. The **Move selected** and **Delete selected** buttons appear above the users list.
3. Click **Move selected**. The Move user dialog opens.
4. Select a new parent for the selected user and click **Save**.

> **Note:** A user can belong to only one group.

### Deleting an Account Associated to a User

1. Locate the user in the users list.
2. Click the three dots at the end of the user row and select **View**.
3. In the user details dialog, locate the **Associated accounts** section.
4. Locate the account that you want to delete and click the three dots next to it.
5. From the drop-down list, select **Delete**.

### Renaming a User Group

1. In the Cyber Protect Cloud console, navigate to **Protection** > **Data loss prevention** > **Organization map**.
2. Click the three dots next to the name of the group and click **Rename**.

### Deleting a User Group

1. In the Cyber Protect Cloud console, navigate to **Protection** > **Data loss prevention** > **Organization map**.
2. Click the three dots next to the name of the group and click **Delete**. All users from the group are moved to the parent entity.

## Known Issues and Limitations

- [DEVLOCK-4028] There is no control for the group chats in the Zoom desktop agent.
- [DEVLOCK-4016] Friendly name and sender ID are not captured for GMX Web Mail and Web.de Mail in case of draft creation.
- [DEVLOCK-4447] There is no Justification dialog for naver.com WebMail in case of draft creation.
