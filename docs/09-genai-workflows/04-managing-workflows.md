---
title: "Managing Workflows - Enabling, Assigning, Execution History, Cloning, Updating, Deleting"
section: "Managing and assigning automation workflows"
subsection: "Managing your workflows"
page_range: "1125-1128"
tags: [workflow-management, enabling, assigning, execution-history, cloning, updating, deleting, tenant-assignment, role-permissions]
acronis_version: "26.02"
---

# Managing Your Workflows

Depending on your role, certain workflow functionality might not be available. The following table lists the functionality available for all roles:

| Functionality | Company admin / Administrator / Cyber admin | Customer tenant users and all other users |
|---|---|---|
| Enabling a workflow | Yes | Yes, only those workflows which they have been assigned |
| Managing who can access and execute workflows | Yes | No |
| Viewing the workflow execution history | Yes | Yes |
| Cloning a workflow | Yes | No |
| Updating a workflow | Yes | No |
| Deleting a workflow | Yes | No |

## Enabling a Workflow

As a Company administrator, Administrator, or Cyber administrator, you can specify the version of the workflow that you want to enable for your customer tenants.

Customer tenant users can only enable or disable workflows that were assigned to them.

**Note:** Partner-level administrators can have multiple versions enabled. Customer tenant users can have only one version enabled at any time.

### To Enable Workflows

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the main **Workflows** screen, select the relevant workflow, and then click the **Versions** tab.
3. From the displayed list of workflow versions, click the **Disabled** toggle switch to enable the version.

**For Company admin/Administrator/Cyber admin:** The enabled workflow is now available for customer tenants who were previously assigned the workflow. The workflow can also be assigned to additional tenants.

**For customer tenant users:** The enabled workflow will execute according to the defined triggers, conditions, and actions.

To disable a workflow version, click the **Enabled** toggle switch to revert it to **Disabled**.

**Note:** If multiple workflows are triggered by the same event, they are executed one by one according to their priority, and then according to their date and time of execution. If the first workflow fails to execute for whatever reason, the next workflow is automatically executed.

## Assigning Workflows

You can view and assign the currently activated workflows for a selected tenant or customer in the **Clients** tab. When you assign a workflow, it is automatically set as **Enabled** for the selected customer tenant users.

The **Clients** tab is only accessible to users assigned with the Company administrator, Administrator, or Cyber administrator role.

### To Assign Workflows to Selected Tenants or Customers

1. Go to **Management > Workflows**, and then select the relevant workflow.
2. Click the **Clients** tab.
3. Click the **Manage clients** link.
4. Select the **My company** option to expand the list of available customer tenants, and then select the tenants you want to set workflow versions for.
5. In the **Version** column, select the relevant workflow version that you want to assign to each customer tenant. The selected workflow version is the only available version displayed to the customer tenant, and they cannot access any other versions.
6. Click **Next**.
7. Verify the selected versions and tenants, and click **Save**.

The selected workflow versions are now available for each customer tenant when they access the main **Workflows** screen. The workflow versions are automatically set as **Enabled**.

## Viewing the Execution History of a Workflow

The execution history of a selected workflow enables you to see when a workflow was executed, and by which tenant.

### To View the Execution History

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the main **Workflows** screen, select the relevant workflow, and then click the **Execution history** tab.

Each execution of the selected workflow is listed in a separate row. Each row indicates the date and time of execution, the status (**Success** or **Error**) of each execution, and the tenant who executed the workflow. You can also filter the displayed list of executions by **Status** and **Client**.

## Cloning a Workflow

You can clone any existing workflow that is currently set with the **Enabled** status.

**Note:** When logged in as a Company administrator, Administrator, or Cyber administrator, you can clone any workflow, including workflows in **Draft** status.

### To Clone a Workflow

1. In the Cyber Protect console, go to **Management > Workflows**.
2. Ensure that the workflow you want to clone is set with the **Enabled** status.
3. In the relevant workflow row, click the ellipsis (...) icon, and then select **Clone**.

The cloned workflow is saved in **Draft** status, and with the name `Copied + Old workflow name` (e.g., **Copied Alerts workflow**). To change the name, open the cloned workflow, and update the name in the **Settings** tab.

When cloning a workflow, a full copy of the default version of the workflow is cloned, including all triggers, conditions, and actions.

## Updating a Workflow

As a Company administrator, Administrator, or Cyber administrator, you can update all elements of the workflow, including its name and description, and the workflow triggers, conditions, and actions.

Customer tenant users and all non-administrator users cannot update workflows.

### To Update a Workflow

1. In the Cyber Protect console, go to **Management > Workflows**.
2. Click on the relevant workflow row, and then click **Open**.
3. Update the workflow.
4. Click **Update**.

The workflow is automatically updated for the relevant users assigned the workflow.

## Deleting a Workflow

As the Company administrator, Administrator, or Cyber administrator, you can delete workflows that you created or that were assigned to you.

**Note:** You can delete only workflows in **Draft** state.

### To Delete a Workflow

1. In the Cyber Protect console, go to **Management > Workflows**.
2. Click the **My workflows** switch to display the workflows you created, and any workflows assigned to you.
3. In the rightmost column of the relevant workflow row, click the ellipsis (...) icon, and then select **Delete**.
4. In the confirmation message, click **Delete**.
