# Deploying the Agent for Azure virtual appliance

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Azure > Deploying the Agent for Azure virtual appliance
Deploying the Agent for Azure virtual appliance

You deploy the Agent for Azure virtual appliance by first connecting to the relevant Microsoft Azure subscription, and then defining the Azure deployment settings.

Connection to a Microsoft Azure subscription can be configured when creating a backup location via the Devices or Backup storage menu, as described in Defining a backup location in Microsoft Azure.

To deploy the Agent for Azure virtual appliance

In the Cyber Protect console, go to Devices > All machines.
Click Add.

Under the Cloud workloads section, select Microsoft Azure virtual machines.

If you have existing Microsoft Azure subscriptions in use, the Add Microsoft Azure virtual machines wizard is displayed, with your existing subscriptions listed. You can select the relevant subscription and click Next. Then proceed to step 8.

If you have existing Microsoft Azure subscriptions in use but want to add a new subscription, click Add subscription.
If you have no existing subscriptions, click Add to add a subscription.

In the displayed dialog, click Sign in. You are redirected to the Microsoft login page.

You must be assigned with one of the following roles in Microsoft Entra ID in order to complete the connection to the subscription: Cloud Application Administrator, Application Administrator, or Global Administrator. You must also be assigned the Owner role for each selected subscription.

Enter your Microsoft login credentials and accept the requested permissions. The connection process starts, and may take several minutes.

For more information about securely accessing your Microsoft Azure subscription, see article Microsoft Azure connection security and audit (72684).

When the connection is complete:

If you have multiple subscriptions, select the relevant subscription from the drop-down list in the displayed dialog, and click Add subscription. You are then redirected to the main wizard screen.
If you are adding your first subscription, you are redirected to the main wizard screen.
Select the relevant subscription, and click Next.

From the Azure region drop-down list, select the relevant region for the subscription. You should select an Azure region where most of the virtual machines to be protected are deployed in order to optimize backup performance.

The estimated cost for the region is calculated and displayed. These costs will be charged to your Microsoft Azure subscription and are billed by Microsoft.

The deployed Agent for Azure uses the Standard_B2s size.

Click Done.

You are redirected to the Devices > Microsoft Azure screen, where progress of the deployment is displayed. When complete, you can begin defining protection plans with the newly added subscription.

For more information about the additional Microsoft Azure backup and recovery options, see Azure restore points and Recovery of virtual machines.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.