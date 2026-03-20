---
title: "Managing and Assigning Automation Workflows - Overview"
section: "Managing and assigning automation workflows"
subsection: "Overview, creating, and viewing workflows"
page_range: "1115-1121"
tags: [automation, workflows, MSP, triggers, conditions, actions, templates, alert-management, workflow-creation]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#workflows.html"
---

# Managing and Assigning Automation Workflows

You can use workflows to automate MSP operations so that various predefined actions are triggered when specific events occur in the Cyber Protect Cloud platform. This automation ensures a more efficient use of resources, while simultaneously reducing the risk of human error in step-by-step operations. MSP technicians can also complete their daily tasks more easily and faster, giving them more time to spend on non-standard issues.

## Use Workflows To

- **Reduce alert noise:** Gain greater control over how alerts are triggered and delivered, while filtering out unnecessary notifications, and focusing on those of higher priority. For example, if you have a URL that is blocked for employee access via URL filtering, you can define a workflow to handle any alerts generated when employees access the specified URL.
- **Automate standard procedures:** Defined workflows are triggered by a platform event, and then execute a set of predefined actions.

## Role-based Access

**Important:** Partner or tenant users with the role of Company administrator, Administrator, or Cyber administrator, can create new workflows, and view and update any workflows in the system. These users can also view execution history, and assign workflows to the relevant tenant users.

For propagated workflows or workflows set as templates, the Company administrator, Administrator, or Cyber administrator can enable or disable workflow versions for selected tenants and child tenants, access workflow details in read-only mode, and clone workflows, but not workflow versions.

All other user roles have read-only access to the workflows assigned to them.

## How to Create, Configure, and Enable a Workflow

| Task | Procedure |
|---|---|
| **Accessing and viewing workflows** | Go to **Management > Workflows**. Partner-level admins can view all workflows. Child tenants can view their own workflows and templates from the parent partner. Customer users can view their own workflows and those assigned/enabled for them. |
| **Creating a workflow** | In the main Workflows screen, click **Create**. Define a name and description. Optionally set it as a template. Click **Create**. |
| **Defining triggers, conditions, and actions** | Open the relevant workflow. Select a trigger event (e.g., Failed backup, EDR threat detected). Add conditions with If/Else paths. Click Action to define response actions (e.g., Dismiss alert, Send email, Add comment). |
| **Enabling the workflow** | Go to the **Versions** tab, click the Disabled toggle to enable it. Assign to relevant customer tenants in the **Clients** tab via **Manage clients**. |
| **Managing and monitoring** | Monitor execution history, update the workflow, clone and delete the workflow. Create, update, and manage versions. |

## Viewing Current Workflows

To view all workflows, in the Cyber Protect console, go to **Management > Workflows**.

The following information is displayed for each workflow:

- The name and current enabled version of the workflow
- A user-defined description of the workflow
- The current status (**Enabled**, **Disabled**, or **Draft**)
- The date and time when the workflow was last executed
- The status of the last execution (**Success**, **Error**, or **Not executed**)
- The user who created the workflow

Click on a workflow to view additional details in the right pane: a general overview, the tenants who can work with it (for admins), and the current available versions.

You can click the **My workflows** switch to filter the displayed list to show only workflows relevant for your role.

## Creating a Workflow

As the Company administrator, Administrator, or Cyber administrator, you can create a workflow from scratch, or use one of the predefined workflow templates.

**Note:** You can create workflows for a specific tenant, or for a number of tenants. You can then assign the workflow to the relevant tenants in the **Clients** tab.

### To Create a Workflow

1. In the Cyber Protect console, go to **Management > Workflows**.
2. Click **Create** (or **Create workflow** if no existing workflows).
3. Define a name and description (optional) for the workflow.
4. (Optional) Click the **Template** toggle to save it as a template available to partners and customer tenants.
   - All versions will be visible to customer tenants and child tenants/partners
   - Customer tenants and partners can view and access the propagated workflow, enable any version or create their own version
   - Customer tenants and partners can disable a workflow version they or their child tenants enabled
5. Click **Create**.

### Defining Triggers

6. In the main **Workflows** screen, select the workflow and click **Open**.
7. Click the **Trigger** block and select the relevant trigger (e.g., **Failed backup**, **Alert created**). You can add additional triggers as required.

### Defining Conditions

8. In the **Actions** section, click **Condition** to add a **Condition** block.
   - **Path A (If):** Initially displays an empty block leading to the next step.
   - **Path B (Else):** Defines an Else result which leads to the workflow endpoint.

   Configure the **If** and **Else** paths accordingly. Click **+** to add a condition to the path, select a data source variable with the relevant operator and value, and click **Add**.

   You can combine multiple AND and OR combinations in one block.

   The **Condition** block consists of two block types:
   - **All:** All conditions must be met to proceed.
   - **Any:** At least one condition must be met to proceed.

### Defining Actions

9. Click **Action** to define what happens after the workflow is triggered. Select from available options such as **Dismiss alert**, **Send email**, or **Add comment**.

The changes are saved automatically and cannot be undone.

**Note:** After configuring, you can enable (or disable) a workflow from the main **Workflows** screen by selecting the relevant workflow and then selecting **Enable** or **Disable**.
