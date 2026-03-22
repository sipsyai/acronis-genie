# How to  create, configure, and enable a workflow

Managing and assigning automation workflows > How to create, configure, and enable a workflow
How to create, configure, and enable a workflow

You can create and configure a workflow when logged in as a Company administrator, Administrator, or Cyber administrator. When the workflow is configured, it can then be enabled for the relevant customer tenants.

The table below includes the steps involved in a typical workflow configuration, with links to the relevant sections for further information.

Task	Procedure
Accessing and viewing workflows

As the Company administrator, Administrator, or Cyber administrator at the highest partner level, you can view all workflows in the system. Their child tenants can view their own workflows, and workflows that were defined as a template by the parent partner. Customer users can view their own workflows, and workflows that were assigned to them or enabled for them.

To access the Workflows module in the Cyber Protect console, go to Management > Workflows.

In the main Workflows screen, you can view and update existing workflows, and create new workflows.

For more information, see Viewing current workflows.


Creating a workflow
Company administrator, Administrator, or Cyber administrator.
In the main Workflows screen, click Create.
In the Create workflow dialog, define a name and description for the workflow.

Use the toggle to set the workflow as a template, which will be propagated to the selected tenant and its child tenants.

Click Create.

For more information, see Creating a workflow.


Defining the workflow triggers, conditions, and actions

In the main Workflows screen, open the relevant workflow, and then:

Select a trigger event to initiate the workflow, such as Failed backup, or EDR threat detected. You can add additional triggers, as required.

In the Actions section, click Condition to add a Condition block. Then, configure the If and Else paths accordingly:

Click + to add an element to the path, then select a data source variable with the relevant operator and value, and click Add.

Configure the Else path (and any additional paths) in the same way.

Click Action in the workflow to define what happens after the workflow is triggered. Select the relevant action from the available options, such as Dismiss alert, Send email, or Add comment.

The changes you make to the workflow are saved automatically and cannot be undone.

For more information, see Creating a workflow.


Enabling the workflow

When the workflow is configured, go to the Versions tab, and then click the Disabled toggle switch to enable it. You can then assign it to the relevant customer tenants (in the Clients tab, click Manage clients to select the relevant tenant(s), and then select the required workflow version).

When enabled, the workflow will be executed according to the defined triggers, conditions, and actions.

For more information, see Enabling a workflow.


Managing and monitoring the workflow

When enabled for the relevant customer tenants, you can monitor the execution history of the workflow, update the workflow, and clone and delete the workflow. For more information, see Managing your workflows.

You can also create, update, and manage versions of the workflow. For more information, see Workflow versions.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.