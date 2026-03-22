# Deploying baseline templates

RMM > Managing and monitoring the Microsoft 365 environment > Managing tenant baseline templates > Deploying baseline templates
Deploying baseline templates

Deploying a template automatically deploys and scans all the constituent baselines to the customer on which the template is deployed. It will overwrite any existing baselines of the same type.

In service-based licensing, this functionality requires the RMM > Microsoft 365 seats service quota to be applied to all the customer's Microsoft 365 seats.

In solution-based licensing, the functionality is enabled with either Security and RMM or Ultimate Protection license.

To deploy a baseline template

Required role: Partner administrator.

In the Cyber Protect console, go to Microsoft 365 management > Baseline templates.

In the list of baseline templates, click the template that you want to deploy.

The template details appear to the right.

Click Deploy template.
In the Deploy template dialog, select a customer to deploy the template to.

[If another template is already deployed to the customer] Because a customer can only be managed by one template at a time, select what to do with the current template settings:

Replace current template baselines

The baselines of the current template will be deleted, and the baselines of the new template will be applied.

Keep current template baselines

Keep the baselines of the current template but stop managing them with that template. The new template will be applied and any overlapping baselines will be replaced with the baselines of the newly deployed template.

Click Deploy.
Deploying a baseline is not the same operation as remediating a baseline. No changes will be made to the customer until you choose to remediate.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.