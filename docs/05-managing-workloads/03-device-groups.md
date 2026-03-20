---
title: "Device groups"
section: "Managing workloads in the Cyber Protect console"
subsection: "Device groups"
page_range: "401-407"
tags: ["device-groups", "static-groups", "dynamic-groups", "cloud-to-cloud", "search-operators", "Azure-AD"]
acronis_version: "26.02"
---

# Device groups

With device groups, you can protect multiple similar workloads with a group plan. The plan is applied to the group as a whole and cannot be revoked from a member of the group.

A workload can be a member of more than one group. A workload that is included in a device group can still be protected by individual plans.

You can add only workloads of the same type to a device group. For example, under **Hyper-V**, you can only create groups of Hyper-V virtual machines. Under **Machines with agents**, you can only create groups of machines with installed agents.

You cannot create device groups within any **All**-type group, such as the root group **All devices**, or built-in groups like **Machines with agents** > **All**, **Microsoft 365** > your organization > **Users** > **All users**.

## Built-in groups and custom groups

### Built-in groups

After you register a workload in the Cyber Protect console, the workload appears in one of the built-in root groups on the **Devices** tab, such as **Machines with agents**, **Microsoft 365**, or **Hyper-V**.

All registered non-cloud-to-cloud workloads are also listed in the **All devices** root group. A separate built-in root group named after your tenant contains all non-cloud-to-cloud workloads and all units in this tenant.

You cannot delete or edit the root groups, or apply plans to them.

Some root groups contain one or more levels of built-in subgroups, for example:
- **Machines with agents** > **All**
- **Microsoft 365** > your organization > **Teams** > **All teams**
- **Google Workspace** > your organization > **Shared Drives** > **All Shared Drives**

You cannot edit or delete built-in subgroups.

### Custom groups

Protecting all workloads in a built-in group might not be convenient, because there might be workloads that need different protection settings or a different protection schedule.

In some of the root groups, for example **Machines with agents**, **Microsoft 365**, or **Google Workspace**, you can create custom subgroups. These subgroups can be static or dynamic.

You can edit, rename, or delete any custom group.

## Static groups and dynamic groups

### Static groups

Static groups contain manually added workloads. The content of a static group changes only when you explicitly add or remove a workload.

**Example:** You create a static group for the accounting department in your company, and then manually add the accountants' machines to this group. When you apply a group plan, the machines in that group become protected. If a new accountant is hired, you will have to add the new machine to the static group manually.

### Dynamic groups

Dynamic groups contain workloads that match specific criteria. You define these criteria in advance by creating a search query that includes attributes (for example, `osType`), their values (for example, `Windows`), and search operators (for example, `IN`).

All workloads that have the required attributes and values are automatically added to the group, and any workload that loses a required attribute or value is automatically removed from the group.

**Example 1:** The host names of the accounting department machines contain the word "accounting". You search for machines whose names contain "accounting", save the search results as a dynamic group, and apply a protection plan. If a new accountant's machine has "accounting" in its name, it will be automatically added to the dynamic group and protected.

**Example 2:** The accounting department forms a separate Active Directory organizational unit (OU). You specify the accounting OU as a required attribute, save as a dynamic group, and apply a plan. New accountant machines added to the AD OU will automatically join the group.

## Cloud-to-cloud groups and non-cloud-to-cloud groups

- **Cloud-to-cloud groups** contain Microsoft 365 or Google Workspace workloads that are backed up by a cloud agent.
- **Non-cloud-to-cloud groups** contain all other workload types.

### Supported plans for device groups

| Group | Available plans | Plan location |
|-------|----------------|---------------|
| Cloud-to-cloud workloads (Microsoft 365 and Google Workspace) | Backup plan | **Management** > **Cloud applications backup** |
| Non-cloud-to-cloud workloads | Protection plan | **Management** > **Protection plans** |
| | Remote management plan | **Management** > **Remote management plans** |
| | Scripting plan | **Management** > **Scripting plans** |

Cloud resources (Microsoft 365 or Google Workspace users, OneDrive, Google Drive shares, Microsoft Teams, or Azure AD groups) are synchronized to the Cyber Protect console right after you add an organization. Further changes in an organization are synchronized once a day. To synchronize immediately, navigate to **Devices** > **Microsoft 365** or **Google Workspace**, select the required organization, and then click **Refresh**.

## Creating a static group

You can create an empty static group and add workloads to it, or select workloads and create a new static group from your selection.

### In the main window

1. Click **Devices**, and then select the root group.
2. [Optional] Navigate to an existing static group for nesting.
3. Click **+ New static group** below the group tree or click **New static group** in the **Actions** pane.
4. Specify a name for the new group.
5. [Optional] Add a comment.
6. Click **OK**.

### From selection

1. Click **Devices**, and then select the root group.
2. Select the check boxes next to the workloads, and then click **Add to group**.
3. In the folder tree, select the parent level, and then click **New static group**.
4. Specify a name, optionally add a comment, and click **OK**.
5. Click **Done**.

> **Note:** Creating nested static groups is not available for cloud-to-cloud workloads.

## Adding workloads to a static group

### Selecting the target group first

1. Click **Devices**, navigate to your target group.
2. Select the target group, and then click **Add devices**.
3. In the folder tree, select the group that contains the required workloads.
4. Select the check boxes next to the workloads, and then click **Add**.

### Selecting the workloads first

1. Click **Devices**, and then select the root group.
2. Select the check boxes next to the workloads, and then click **Add to group**.
3. In the folder tree, select the target group, and then click **Done**.

## Creating a dynamic group

You create a dynamic group by searching for workloads that have specific attributes and saving the search results as a dynamic group.

The attributes differ for cloud-to-cloud workloads and non-cloud-to-cloud workloads. Dynamic groups are created in their respective root groups. Nested dynamic groups are not supported.

### For non-cloud-to-cloud workloads

1. Click **Devices**, and then select the group for which you want to create a dynamic group.
2. Search for workloads by using the supported search attributes and operators.
3. Click **Save as** next to the search field.
4. Specify a name for the new group.
5. [Optional] Add a description.
6. Click **OK**.

> **Note:** The **Save as** button is not available when you are not allowed to create a dynamic group on a specific level (e.g., in root group **Devices** > **All devices**). Select another level, such as **Devices** > **Machines with agents** > **All**.

### For cloud-to-cloud workloads

1. Click **Devices**, and then select **Microsoft 365** or **Google Workspace**.
2. Select the group (e.g., **Users** > **All users**).
3. Search for workloads by using the supported search attributes and operators, or by selecting Microsoft 365 users from a specific Active Directory group.
4. [Only for **Microsoft 365** > **Users**] To select from a specific AD group:
   a. Navigate to **Users** > **All users**.
   b. Click **Select an Azure AD Group**.
   c. Select the Active Directory group, and click **Add**.
   d. [Optional] Create a search query to include or exclude specific users from the selected group.
5. Click **Save as** next to the search field.
6. Specify a name and optionally add a description.
7. Click **OK**.

## Search operators

You can use the following operators in your search queries:

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equal to | `osType = Windows` |
| `<>` | Not equal to | `osType <> Linux` |
| `>` | Greater than | `#cyberFitScore > 500` |
| `<` | Less than | `#cyberFitScore < 300` |
| `>=` | Greater than or equal to | |
| `<=` | Less than or equal to | |
| `LIKE` | Pattern matching (use `%` as wildcard) | `name LIKE %server%` |
| `IN` | Value is in a list | `osType IN (Windows, Linux)` |
| `NOT IN` | Value is not in a list | `osType NOT IN (macOS)` |
| `AND` | Logical AND | `osType = Windows AND name LIKE %prod%` |
| `OR` | Logical OR | `osType = Windows OR osType = Linux` |
| `HAS` | Contains (for multi-value attributes) | |
| `HAS NOT` | Does not contain | |

You can use more than one operator in a single query.
