# Creating a workflow

Managing and assigning automation workflows > Creating a workflow
Creating a workflow

As the Company administrator, Administrator, or Cyber administrator, you can create a workflow from scratch, or use one of the predefined workflow templates, according to your requirements.

You can create workflows for a specific tenant, or for a number of tenants. You can then assign the workflow to the relevant tenants in the Clients tab. For more information, see Assigning workflows.

To create a workflow

In the Cyber Protect console, go to Management > Workflows.

Click Create.

If there are no existing workflows, click Create workflow.

Define a name and description (optional) for the workflow.

Click the Template toggle switch to enable it. This ensures the workflow is saved as a template, and is automatically available to your partners and customer tenants, who can use the template to create their own workflows.

When Template is enabled, note the following:

All versions of the workflow will be visible to your customer tenants, and their child tenants and partners.

Your customer tenants and their child tenants and partners can view and access the propagated workflow, and can enable any version of the workflow or create their own version.

Your customer tenants and their child tenants and partners can disable a workflow version that they enabled or their child tenants enabled.

Click Create.

The workflow is added to the current list of available workflows, and accessed from the main Workflows screen. You can now add triggers, conditions, and actions, as required.

In the main Workflows screen, select the relevant workflow, and then click Open.

When a workflow is initially created, it contains two preliminary steps, a trigger and an endpoint. The trigger must be selected from the library of available triggers, as described below.

To define a trigger, click the Trigger block, and then select the relevant trigger, such as Failed backup, or Alert created. You can add additional triggers, as required.

In the Actions section, click Condition to add a Condition block.

Each new block contains two output paths, which determine the direction and actions to apply to the workflow:

Path A (If): Initially displays an empty block leading to the next step.
Path B (Else): Defines an Else result which leads to the workflow endpoint.

Configure the If and Else paths accordingly. Click + to add a condition to the path, then select a data source variable with the relevant operator and value, and click Add.

You can combine multiple AND and OR combinations of conditions in one block.

Configure any additional paths in the same way. You can also delete a condition, by clicking the trash can icon next to it.

The Condition block defines a set of conditions that must be executed as part of the workflow, and consists of two block types:

All: All of the conditions in this block should be met to proceed with the next step of the workflow.

Any: At least one of the conditions in this block must be met to proceed with the next step of the workflow.

Click Action in the workflow to define what happens after the workflow is triggered. Select the relevant action from the available options, such as Dismiss alert, Send email, or Add comment.

For example, click the action Send email, and then modify the selected recipients, body, and subject of the email that is sent as part of this workflow.

The available actions are filtered according to the defined trigger you selected in step 7. Some actions might require additional input parameters in order to be applied to the workflow, depending on the trigger selected.

The changes you make to the workflow as you configure it are saved automatically.

After you have configured the workflow, you can enable (and disable) a workflow from the main Workflows screen by selecting the relevant workflow, and then selecting Enable or Disable. For more information, see Enabling a workflow.

Workflow components and templates

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.