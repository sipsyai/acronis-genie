---
title: "Workflow Versions - Creating, Viewing, Setting Default, Cloning, and Deleting"
section: "Managing and assigning automation workflows"
subsection: "Workflow versions"
page_range: "1129-1131"
tags: [workflow-versions, version-management, draft, active, disabled, default-version, cloning-version, deleting-version]
acronis_version: "26.02"
---

# Workflow Versions

Each workflow can consist of multiple versions, with one version always set as the default version.

The Company administrator, Administrator, or Cyber administrator can edit, enable, or delete all workflow versions, as and when required. All other users cannot manage workflow versions.

**Note:** When you create a new workflow, it is automatically set as version 1. Subsequent new versions of the workflow are automatically incremented by +1 when the version is created. For example, the second version is set as version 2, the third is version 3, and so on.

## Version States

Each workflow version can be in one of the following states:

- **Draft** -- An editable version of the workflow that was not previously activated on any tenant. Only versions in this state can be edited.
- **Active** -- The version is enabled for at least one tenant. A version in this state can only be set to Disabled.
- **Disabled** -- The version was previously enabled, but is currently disabled for all tenants.

## Viewing a Workflow Version

You can view and open any workflow that is assigned to you.

**Note:** The Company administrator, Administrator, or Cyber administrator can open and view the versions of any workflow.

### To View a Workflow Version

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the main **Workflows** screen, select the relevant workflow, and then click the **Versions** tab.
3. In the relevant version row, click the ellipsis (...) icon, and then select **Open**.

The workflow version is opened. View and verify the version triggers, conditions and actions, as required. The Company administrator, Administrator, or Cyber administrator can update any of the workflow components.

## Creating a New Version of a Workflow

The Company administrator, Administrator, or Cyber administrator can create a new version of any workflow.

### To Create a New Workflow Version

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the main **Workflows** screen, select the relevant workflow, and then click **New version**.

   The workflow configuration screen is displayed, with the default workflow version open.

3. Modify the version triggers, conditions and actions, as required.

   When done, the new workflow version is automatically saved with a version number that is automatically incremented by 1. For example, the second version is set as version 2, and a subsequent third version is set as version 3.

The new workflow version is set as **Draft**, and is automatically disabled.

## Setting the Default Version of a Workflow

Only one version of a workflow can be set as the default version. The default version is the workflow version that is automatically executed according to the defined triggers, conditions, and actions.

When a workflow version is set as the default version, all your customer and child tenant users with this specific workflow enabled will automatically use this default version.

**Note:** When a workflow is first enabled, the original first version is automatically set as the default version. After subsequent versions are created, you can then define which version is the default at any time.

### To Set the Default Workflow Version

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the main **Workflows** screen, select the relevant workflow, and then click the **Versions** tab.
3. In the relevant version row, click the ellipsis (...) icon, and then select **Set as default**.

The workflow version is set as the default version.

## Cloning a Workflow Version

You can clone any existing workflow version that is currently set as **Enabled**.

**Note:** When logged in as a Company administrator, Administrator, or Cyber administrator, you can clone any workflow version, including the versions of workflows in **Draft** status.

### To Clone a Workflow Version

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the main **Workflows** screen, select the relevant workflow, and then click the **Versions** tab.
3. In the relevant version row, click the ellipsis (...) icon, and then select **Clone**.

The cloned version is automatically set as **Draft** and is also disabled (even if you cloned a workflow set as **Enabled**).

## Deleting a Workflow Version

As the Company administrator, Administrator, or Cyber administrator, you can delete workflow versions of workflows that you created or that were assigned to you.

**Note:** You can delete only workflow versions in **Draft** state.

### To Delete a Workflow Version

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the main **Workflows** screen, select the relevant workflow, and then click the **Versions** tab.
3. In the relevant version row, click the ellipsis (...) icon, and then select **Delete**.
4. In the confirmation dialog, click **Delete**.
