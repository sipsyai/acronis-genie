---
title: "Orchestration (runbooks) and removing the DR site"
section: "Implementing disaster recovery"
subsection: "Orchestration (runbooks)"
page_range: "1010-1015"
tags: [runbooks, orchestration, automation, failover automation, execution, DR site removal]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#orchestration-runbooks.html"
---

# Failback from Cyber Protect Cloud to an Azure virtual machine

You can perform a failback from Cyber Protect Cloud to the original Azure virtual machine by following the procedure for "Performing manual failback" and using one of the following recovery options in step 8:

## Recovery options

- **Agentless recovery** -- Supports recovery only to a new Azure VM that is created automatically. Configure the Azure connection in the Cyber Protect console (**Devices** > **Add** > **Microsoft Azure virtual machine**). A backup appliance VM is deployed in the Azure subscription to manage the recovery. Recovery flow: select a backup on the **Backup storage** screen, then recover as an Azure virtual machine. To reduce incurred costs, the appliance VM can be powered on only during recovery and then turned off manually.

- **Agent-based recovery** -- Supports recovery to the same Azure virtual machine (if the original VM with the agent is available) or a new Azure virtual machine that has a new agent installed. The process consists of: manually create a clean Windows or Linux VM in Azure, install the protection agent, and use the agent to browse and recover backups from Acronis Cloud Storage.

# Orchestration (runbooks)

A runbook is a set of instructions describing how to launch the production environment in the cloud. You can create runbooks in the Cyber Protect console.

With runbooks, you can:

- Automate the failover of one or multiple servers.
- Automatically check the failover result by pinging the server IP address and checking the connection to the port you specify.
- Set the sequence of operations for servers running distributed applications.
- Include manual operations in the workflow.
- Verify the integrity of your disaster recovery solution, by executing runbooks in the test mode.

To access the **Runbooks** screen, go to **Disaster Recovery** > **Runbooks**.

## Creating a runbook

A runbook consists of steps that are executed consecutively. A step consists of actions that start simultaneously.

### To create a runbook

1. In the Cyber Protection console, go to **Disaster Recovery** > **Runbooks**.
2. Click **Create runbook**.
3. Click **Add step**.
4. Click **Add action**, and then select the action that you want to add to the step.

### Available actions

| Action | Description |
|--------|-------------|
| **Failover server** | Performs a failover of a cloud server. You must select a cloud server and configure the runbook parameters. If the backup is encrypted, the **Failover server** action will be paused and changed to **Interaction required**. You will have to provide the password for the encrypted backup. |
| **Failback server** | Performs a failback of a cloud server. Runbook operations support the failback in manual mode only. You must manually recover the machine, and confirm or cancel the failback process from the **Disaster Recovery** > **Servers** tab. |
| **Start server** | Starts a cloud server. Not applicable for test failover operations in runbooks. |
| **Stop server** | Stops a cloud server. Not applicable for test failover operations in runbooks. |
| **Manual operation** | A manual operation requires an interaction from a user. When a runbook sequence reaches a manual operation, the runbook will be paused and will not proceed until a user performs the required manual operation, such as clicking the confirmation button. |
| **Execute runbook** | Executes another runbook. A runbook can include only one execution of a given runbook (e.g., you can add "execute Runbook A" and "execute Runbook B", but cannot add "execute Runbook A" twice). |

5. Define the runbook parameters for the action.
6. [Optional] To add a description of the step, click the ellipsis icon, then click **Description**, enter the description, and click **Done**.
7. Repeat steps 3-6 until you create the desired sequence of steps and actions.
8. [Optional] To change the default name of the runbook, click the ellipsis icon, enter the name and description, and click **Done**.
9. Click **Save**.
10. Click **Close**.

## Runbook parameters

Runbook parameters are specific settings that you must configure to define a runbook action. There are two categories: action parameters and completion check parameters.

- **Action parameters** define the runbook behavior depending on the action initial state or result.
- **Completion check parameters** ensure that the server is available and provides the necessary services. If a completion check fails, the action is considered failed.

| Parameter | Category | Available for action | Description |
|-----------|----------|---------------------|-------------|
| **Continue if already done** | Action parameter | Failover server, Start server, Stop server, Failback server | Defines the runbook behavior when the required action is already done (e.g., a failover has already been performed or a server is already running). When enabled, the runbook issues a warning and proceeds. When disabled, the action fails, and then the runbook fails too. Default: enabled. |
| **Continue if failed** | Action parameter | Failover server, Start server, Stop server, Failback server | Defines the runbook behavior when the required action fails. When enabled, the runbook issues a warning and proceeds. When disabled, the action and runbook fail. Default: disabled. |
| **Ping IP address** | Completion check | Start server | The software will ping the production IP address of the cloud server until the server replies or the timeout expires, whichever comes first. |
| **Connect to port** (443 by default) | Completion check | Failover server, Start server | The software will try to connect to the cloud server by using its production IP address and the port you specify, until the connection is established or the timeout expires. This way, you can check if the application that listens on the specified port is running. |
| **Timeout in minutes** | Completion check | Failover server, Start server | The default timeout is 10 minutes. |

## Operations with runbooks

When a runbook is not running, the following operations are available: **Execute**, **Edit**, **Clone**, **Delete**.

### Executing a runbook

Every time you click **Execute**, you are prompted for the execution parameters. These parameters apply to all failover and failback operations included in the runbook.

- **Failover and failback mode** -- Choose whether you want to run a test failover (by default) or a real (production) failover. The failback mode will correspond to the chosen failover mode.
- **Failover recovery point** -- Choose the most recent recovery point (by default) or select a point in time in the past. If the latter, the recovery points closest before the specified date and time will be selected for each server.

### Stopping a runbook execution

During a runbook execution, you can select **Stop** in the list of operations. The software will complete all of the already started actions except for those that require user interaction.

### Viewing the execution history

When you select a runbook on the **Runbooks** tab, the software displays the runbook details and execution history. Click the line corresponding to a specific execution to view the execution log.

# Removing the disaster recovery site

You can remove the disaster recovery site. This action will automatically delete the VPN gateway, VPN connections, and all runbooks that were configured on the site.

**Prerequisites:** No cloud servers are available on the disaster recovery site.

### To remove the disaster recovery site

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**.
3. Click **Remove the disaster recovery site**.
4. Confirm your choice.
