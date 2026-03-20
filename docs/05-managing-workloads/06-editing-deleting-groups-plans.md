---
title: "Editing groups, deleting groups, and managing plans for groups"
section: "Managing workloads in the Cyber Protect console"
subsection: "Device groups management"
page_range: "424-426"
tags: [device groups, dynamic groups, plans, apply plan, revoke plan, delete group, edit group]
acronis_version: "26.02"
---

# Editing a dynamic group

You edit a dynamic group by changing the search query that defines the group content. In dynamic groups that are based on Active Directory, you can also change the Active Directory group.

## By changing the search query

1. Click **Devices**, navigate to the dynamic group that you want to edit, and then select it.
2. Click the gear icon next to the name of the group, and then click **Edit**. Alternatively, click **Edit** in the **Actions** pane.
3. Change the search query by modifying the search attributes, their values, or the search operators, and then click **Search**.
4. Click **Save** next to the search field.

## By changing the Active Directory group

> **Note:** This procedure applies to dynamic groups based on Active Directory. Active Directory-based dynamic groups are available only in **Microsoft 365** > **Users**.

1. Click **Devices**, navigate to **Devices** > **Microsoft 365** > your organization > **Users**.
2. Select the dynamic group that you want to edit.
3. Click the gear icon next to the name of the group, and then click **Edit**. Alternatively, click **Edit** in the **Actions** pane.
4. Change the group content by doing any of the following:
   - Change the already selected Active Directory group by clicking its name, and then selecting a new Active Directory group from the list that opens.
   - Edit the search query, and then click **Search**. The search query is limited to the currently selected Active Directory group.
5. Click **Save** next to the search field.

You can also save your edits without overwriting the current group. To save the edited configuration as a new group, click the arrow button next to the search field, and then click **Save as**.

> **Note:** Groups that are created by using the **Save As** option inherit the discovery criteria from the original dynamic group. Thus, the new discovery criteria that you configure are added to the inherited criteria and saved to the new dynamic group. Only groups created from the **All** group category do not inherit criteria.

# Deleting a group

When you delete a device group, all plans that are applied to that group will be revoked. The workloads in the group will become unprotected if no other plans are applied to them.

## To delete a device group

1. Click **Devices**, and then navigate to the group that you want to delete.
2. Click the gear icon next to the name of the group, and then click **Delete**.
3. Confirm your choice by clicking **Delete**.

# Applying a plan to a group

You can apply a plan to a group by selecting the group first, and then assigning a plan to it. Alternatively, you can open a plan for editing, and then add a group to it.

## To apply a plan to a group

1. Click **Devices**, and then navigate to the group to which you want to apply a plan.
2. [For non-cloud-to-cloud workloads] Click **Protect group**.
   A list of plans that can be applied is shown.
3. [For cloud-to-cloud workloads] Click **Group backup**.
   A list of backup plans that can be applied is shown.
4. [To apply an existing plan] Select the plan, and then click **Apply**.
5. [To create a new plan] Click **Create plan**, select the plan type, and then create the new plan. For more information about the available types of plans and how to create them, refer to "Supported plans for device groups."

> **Note:** Backup plans that are applied to cloud-to-cloud device groups are automatically scheduled to run once a day. You cannot run these plans on demand by clicking **Run now**.

# Revoking a plan from a group

You can revoke a plan from a group by selecting the group first, and then revoking the plan from it. Alternatively, you can open the plan for editing, and then remove the group from it.

## To revoke a plan from a group

1. Click **Devices**, and then navigate to the group from which you want to revoke a plan.
2. [For non-cloud-to-cloud workloads] Click **Protect group**.
   A list of plans that are applied to the group is shown.
3. [For cloud-to-cloud workloads] Click **Group backup**.
   A list of backup plans that are applied to the group is shown.
4. Select the plan that you want to revoke.
5. [For non-cloud-to-cloud workloads] Click the ellipsis icon (...), and then click **Revoke**.
6. [For cloud-to-cloud workloads] Click the gear icon, and then click **Revoke**.
