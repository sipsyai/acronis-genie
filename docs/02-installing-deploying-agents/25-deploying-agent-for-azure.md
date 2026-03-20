---
title: "Deploying Agent for Azure"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying Agent for Azure"
page_range: "157-162"
tags: ["Azure", "Microsoft Azure", "virtual appliance", "cloud", "agentless", "backup", "deployment", "subscription"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#deploying-agent-azure.html"
---

# Deploying Agent for Azure

You can perform an agentless backup of Microsoft Azure virtual machines by setting up Agent for Azure, a single agent that can access Microsoft Azure virtual machine data transparently.

Agent for Azure ensures:

- Backup and restore functionality for Microsoft Azure virtual machines running Windows or Linux.
- Reduced Microsoft Azure virtual machine overheads, with only one agent to manage.
- Transparent migration of any on-premise or cloud machine backups to Microsoft Azure virtual machines, configurable via the Cyber Protect console.
- Reduced Microsoft Azure resource costs, with CPU and RAM overheads for only one agent inside the virtual machine.

## System requirements for the agent

By default, the virtual appliance is assigned the **Standard_B2s** size (4 GiB of RAM and 2 CPUs), which is optimal and sufficient for operations with up to ten virtual machines backed up in parallel. To improve backup performance, we recommend changing the size to get 4 vCPUs and 8 GB of RAM in more demanding cases -- for example, when you back up more than ten virtual machines in parallel or if you simultaneously back up multiple virtual machines with large hard drives (500 GB or more).

## Deploying the Agent for Azure virtual appliance

You deploy the Agent for Azure virtual appliance by first connecting to the relevant Microsoft Azure subscription, and then defining the Azure deployment settings.

> **Note:** Connection to a Microsoft Azure subscription can be configured when creating a backup location via the **Devices** or **Backup storage** menu.

### To deploy the Agent for Azure virtual appliance

1. In the Cyber Protect console, go to **Devices** > **All machines**.
2. Click **Add**.
3. Under the **Cloud workloads** section, select **Microsoft Azure virtual machines**.
   - If you have existing Microsoft Azure subscriptions in use, the Add Microsoft Azure virtual machines wizard is displayed, with your existing subscriptions listed. Select the relevant subscription and click **Next**. Then proceed to step 8.
   - If you have existing subscriptions but want to add a new subscription, click **Add subscription**.
   - If you have no existing subscriptions, click **Add** to add a subscription.
4. In the displayed dialog, click **Sign in**. You are redirected to the Microsoft login page.

> **Note:** You must be assigned one of the following roles in Microsoft Entra ID to complete the connection to the subscription: Cloud Application Administrator, Application Administrator, or Global Administrator. You must also be assigned the Owner role for each selected subscription.

5. Enter your Microsoft login credentials and accept the requested permissions. The connection process starts, and may take several minutes.
6. When the connection is complete:
   - If you have multiple subscriptions, select the relevant subscription from the drop-down list in the displayed dialog, and click **Add subscription**.
   - If you are adding your first subscription, you are redirected to the main wizard screen.
7. Select the relevant subscription, and click **Next**.
8. From the **Azure region** drop-down list, select the relevant region for the subscription. You should select an Azure region where most of the virtual machines to be protected are deployed in order to optimize backup performance. The estimated cost for the region is calculated and displayed. These costs will be charged to your Microsoft Azure subscription and are billed by Microsoft.
9. Click **Done**. You are redirected to the **Devices** > **Microsoft Azure** screen, where progress of the deployment is displayed. When complete, you can begin defining protection plans with the newly added subscription.

## Viewing and updating a deployed Agent for Azure

You can view and update your Agent for Azure deployment in the following ways:

- View current deployments via the **Devices > Microsoft Azure** menu. The current list of deployments is displayed, with each subscription showing the relevant resource groups below it in the hierarchical tree.
- View, update, access, and redeploy current deployments via the **Infrastructure > Public clouds** menu.

### To view and update current deployments via the Infrastructure > Public clouds menu

1. In the Cyber Protect console, go to **Infrastructure** > **Public clouds**. The current list of public cloud connections is displayed.
2. Select the relevant Microsoft Azure subscription where the Agent for Azure is deployed.
3. In the right pane, click the **Agent for Azure** tab.
4. You can:
   - View the current status of the deployment.
   - Click the link in the **Instance name** field to access the instance where the Agent for Azure is deployed (you will need to be logged into your Microsoft Azure account).
   - Click the gear icon to redeploy the Agent for Azure.
   - Click **Update** if an update is available.

## Removing the Agent for Azure virtual appliance

The Agent for Azure virtual appliance is automatically removed when you remove the corresponding Microsoft Azure subscription.

### To remove the Agent for Azure virtual appliance

1. In the Cyber Protect console, go to **Devices** > **Microsoft Azure**.
2. Click the **Subscriptions** node in the hierarchical tree, and then select the relevant subscription in the displayed list to the right.
3. In the right pane, click **Delete**.
4. In the displayed confirmation dialog, click **Remove**. When the subscription is removed, the Agent for Azure virtual appliance is de-provisioned and does not use Microsoft Azure resources.

> **Note:** You cannot remove a subscription if it is currently in use by Microsoft Azure virtual machines.
