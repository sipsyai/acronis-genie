---
title: "Azure failback, runbooks, resources, soft deletion, and workers"
section: "Implementing disaster recovery"
subsection: "Disaster Recovery to Microsoft Azure"
page_range: "1041-1057"
tags: [Azure failback, agent-based failback, agentless failback, manual failback, Azure runbooks, Azure resources, soft deletion, workers, temporary agents]
acronis_version: "26.02"
---

# Failback in Microsoft Azure

Failback is a process of moving the workload from the cloud back to a physical or virtual machine on your local site. You can perform a failback when a recovery server is in the **Failover** state, and then continue using the server on your local site.

You can perform automated failover to a virtual or physical target machine on your local site. During the failback, you can transfer the backup data to your local site while the virtual machine in the cloud continues to run. This technology helps you achieve a very short downtime period, which is estimated and displayed in the Cyber Protect console.

If you perform agent-based failback via bootable media, the downtime is even shorter, as only the delta changes will be transferred to the local site.

> **Note**
> Runbook operations support the failback in manual mode only. If you start the failback process by executing a runbook that includes a **Failback server** step, the procedure will require a manual interaction.

## Failback methods

| Method | Target | Details |
|--------|--------|---------|
| **Agent-based failback via bootable media** | Physical or virtual machine | Transfers only delta changes. Uses flashback technology. Shortest downtime. |
| **Agentless failback via hypervisor agent** | New virtual machine (VMware ESXi or Hyper-V) | Optimized for failback to a new VM. Uses four phases: Planning, Data transfer, Switchover, Validation. |
| **Manual failback** | Physical or virtual machine | Data transfer is manual. Longer downtime. Recommended only when advised by Support team. |

---

# Agent-based failback via bootable media from Microsoft Azure

The agent-based failback via bootable media process is optimized for performing a failback to the original physical or virtual machine. During this process, only the delta changes are transferred to the local site.

The process consists of four phases: **Planning**, **Data transfer**, **Switchover**, and **Validation** -- identical in structure to the failback from Cyber Protect Cloud.

### Prerequisites

- The agent that you will use to perform failback is online and is not currently used for another failback operation.
- Your Internet connection is stable.
- A registered bootable media is available.
- The target machine is the original machine on your local site, or has the same firmware.
- There is at least one full backup of the virtual machine in the cloud.

### To perform a failback to a physical machine

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Failback type** field, select **Agent-based via bootable media**.
5. In the **Target bootable media** field, click **Specify**, select the bootable media, and then click **Done**.
6. [Optional] To change the default disk mapping, in the **Disk mapping** field, click **Specify**, map the disks, and click **Done**.
7. Click **Start data transfer** and then, in the confirmation window, click **Start**.

The data transfer phase starts, displaying **Progress** and **Downtime estimation** fields.

8. Click **Switchover** and confirm. The switchover phase starts, displaying **Progress** and **Estimated time to finish**.

> **Note**
> If no backup plan is applied to the virtual machine in the cloud, a backup will be performed automatically during the switchover phase, which will cause a longer downtime.

9. After the **Switchover** phase completes, reboot the bootable media, and verify that the physical machine is working as expected.
10. Click **Confirm failback** and then click **Confirm** to finalize. The virtual machine in the cloud is deleted, and the recovery server returns to **Standby** state.

> **Note**
> After the failback process completes, apply a protection plan on the recovered server to ensure that it is protected again.

---

# Agentless failback via a hypervisor agent from Microsoft Azure

The agentless failback via a hypervisor agent process is optimized for performing a failback from Microsoft Azure to a new virtual machine. If you want to perform a failback to the original virtual machine, follow the agent-based failback procedure.

The agentless failback via a hypervisor agent consists of four phases: Planning, Data transfer, Switchover, and Validation.

### Prerequisites

- The agent that you will use to perform failback is online and is not currently used for another failback operation.
- Your internet connection is stable.
- There is at least one full backup of the virtual machine in the cloud.

### To perform an agentless failback to a virtual machine via a hypervisor agent

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Failback parameters** section, in the **Failback type** field, select **Agentless via hypervisor agent**, and then configure the other parameters.

### Failback parameters

| Parameter | Description |
|-----------|-------------|
| **Backup size** | Amount of data to be transferred. Increases during data transfer as the VM continues generating data. |
| **Target machine location** | VMware ESXi host or Microsoft Hyper-V host with a registered agent. |
| **Agent** | Agent performing the failback operation. One agent per one failback at a time. Multiple agents on VMware ESXi hosts can run parallel failback processes. |
| **Target machine settings** | Virtual processors, Memory, Units, [Optional] Network adapters. |
| **Path** | (For Hyper-V hosts) Folder on the host for the machine. |
| **Datastore** | (For VMware ESXi hosts) Datastore on the host for the machine. |
| **Provisioning mode** | Hyper-V: Dynamically expanding (default) or Fixed size. VMware ESXi: Thin (default) or Thick. |
| **Target machine name** | Name of the target machine. Must be unique on the selected Target machine location. |

5. Click **Start data transfer**, and then confirm.
6. Click **Switchover** and confirm.
7. After the **Switchover** phase completes and the virtual machine is started automatically, validate it is working as expected.
8. Click **Confirm failback** and confirm. The virtual machine in the cloud is deleted, and the recovery server returns to **Standby** state.

---

# Manual failback from Microsoft Azure

> **Note**
> We recommend that you use the failback process in a manual mode only when you are advised to do so by the Support team.

The manual failback process consists of three phases: **Planning**, **Switchover**, and **Validation**.

### To perform a manual failback

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Target** field, select **Physical machine**.
5. Click the gear icon, and then enable the **Use manual mode** switch.
6. [Optional] Calculate the estimated downtime period.
7. Click **Switchover**, and then confirm.
8. Recover the server from the cloud backup to the physical or virtual machine on your local site.
9. Ensure that the recovery is completed and the recovered machine works properly, and click **Machine is restored**.
10. Click **Confirm failback** and confirm.

> **Note**
> If you are performing a failback from a Microsoft Azure virtual machine to the original Azure virtual machine, use the recovery options described in "Failback from Microsoft Azure to an Azure virtual machine."

## Failback from Microsoft Azure to an Azure virtual machine

You can perform a failback from a Microsoft Azure virtual machine to the original Azure virtual machine by following the procedure for manual failback and using one of the following recovery options in step 8:

- **Agentless recovery** -- Supports recovery only to a new Azure VM that is created automatically. Configure the Azure connection in the Cyber Protect console (**Devices** > **Add** > **Microsoft Azure virtual machine**). A backup appliance VM is deployed in the Azure subscription. Recovery flow: On the **Backup storage** screen, select a backup, then recover as an Azure VM. The appliance VM can be powered on only during recovery, then turned off manually to reduce costs.

- **Agent-based recovery** -- Supports recovery to the same Azure VM (if the original VM with the agent is available) or a new Azure VM with a new agent installed. Process: Manually create a clean Windows/Linux VM in Azure, install the protection agent, use the agent to browse and recover backups from Acronis Cloud Storage.

---

# Runbooks in Microsoft Azure

A runbook is a set of instructions describing how to launch the production environment in the cloud. With runbooks, you can:

- Automate the failover of one or multiple servers.
- Automatically check the failover result by pinging the server IP address and checking the connection to the port you specify.
- Set the sequence of operations for servers running distributed applications.
- Include manual operations in the workflow.
- Verify the integrity of your disaster recovery solution, by executing runbooks in the test mode.

Runbooks let you automate a failover of one or multiple servers. You can set the correct sequence of failover operations for servers running distributed applications. You can execute runbooks in either test or production mode, to check the integrity of your disaster recovery solution.

## Creating a runbook in Microsoft Azure

A runbook consists of steps that are executed consecutively. A step consists of actions that start simultaneously.

### To create a runbook in Microsoft Azure

1. In the Cyber Protection console, go to **Disaster Recovery** > **Runbooks**.
2. Click **Create runbook**.
3. Click **Add step**.
4. Click **Add action**, and then select the action:

| Action | Description |
|--------|-------------|
| **Failover server** | Performs a failover of a recovery server. If the backup is encrypted, the action will be paused and changed to **Interaction required**. |
| **Failback server** | Performs a failback of a cloud server. Runbook operations support failback in manual mode only. |
| **Start server** | Starts a cloud server. Not applicable for test failover operations. |
| **Stop server** | Stops a cloud server. Not applicable for test failover operations. |
| **Manual operation** | A manual operation requires user interaction. The runbook will be paused until the user performs the required action. |
| **Execute runbook** | Executes another runbook. A runbook can include only one execution of a given runbook. |

5. Define the runbook parameters for the action.
6-10. Add descriptions, repeat steps, rename the runbook, click **Save**, then **Close**.

## Runbook parameters in Microsoft Azure

| Runbook parameter | Available for action | Description |
|-------------------|---------------------|-------------|
| **Continue if already done** | Failover server, Start server, Stop server, Failback server | Defines behavior when the required action is already done. When enabled, the runbook issues a warning and proceeds. When disabled, the action fails and the runbook fails too. Default: enabled. |
| **Continue if failed** | Failover server, Start server, Stop server, Failback server | Defines behavior when the required action fails. When enabled, the runbook issues a warning and proceeds. When disabled, both the action and runbook fail. Default: disabled. |

## Operations with runbooks in Microsoft Azure

When a runbook is not running, the following operations are available: execute, edit, clone, view details, and delete.

### Execute

Every time you click **Execute**, you are prompted for the execution parameters:

| Parameter | Description |
|-----------|-------------|
| **Failover and failback mode** | Select whether you want to run a test failover (by default) or a real (production) failover. |
| **Failover recovery point** | Select the most recent recovery point (by default) or select a point in time in the past. |

### Edit, Clone, View details, Delete

Available via **Disaster Recovery** > **Runbooks**. When you clone a runbook, the history of the original runbook is not cloned. To view the execution log, click the line corresponding to a specific execution.

---

# Azure resources that are created during the DR site configuration and failover

When you add a connection to your Azure subscription, the system creates a resource group with the prefix `cyber-protect-rg*` in the Azure region. This resource group has the following tag: **Application:CyberProtect**.

When the (DR) site configuration is completed, a resource group with the prefix `dr-rg*` is created to aggregate the resources for failover. This resource group has the following tag: **Application:DisasterRecovery**.

During disaster recovery operations, temporary workers (agents) are deployed to orchestrate failover, failback, and post-failover backup operations. These are temporary Azure VMs that are running in the `cyber-protect-rg*` resource group. All Azure resources that are required for a disaster recovery failover, such as storage accounts, and failed-over VMs are created in the `dr-rg*` resource group.

---

# Soft deletion of tenants that have a disaster recovery site in Microsoft Azure

The soft deletion of a tenant feature (Recycle bin) is supported for the Microsoft Azure DR site configuration.

To ensure business continuity during the soft and hard deletion, Azure VMs in failover will not be stopped or deleted.

### Corner case

If you disable the **DR and direct backup to Azure** offering item (either intentionally or accidentally), a soft delete of the Azure DR configuration is triggered. This means that the configuration is removed but remains in the Recycle bin for 30 days. If during this period you configure a new DR site in a different location (not Microsoft Azure), to recover the initial DR configuration to Microsoft Azure, you must enable the **DR and direct backup to Azure** offering item, remove the new configuration, and then recover the initial one.

---

# Workers in Microsoft Azure

Workers are temporary, on-demand agents that run in your Azure subscription in the system resource group (with the prefix "cyber-protect-rg*") during disaster recovery operations, such as test failover, back up after failover, and failback. One worker is deployed for each operation and is deleted after operation completes. This on-demand model helps reduce costs by automatically deploying workers only during active DR operations and removing them afterward.

The initial deployment of the worker for a test or production failover might take several minutes. Starting workers for the subsequent failovers should be faster.

To monitor the status of active workers, go to **Public clouds**, click the connection to your Microsoft Azure subscription, and then click the **Workers** tab.

If a disaster recovery operation fails because of an error with the worker, you can generate a report and view more information about the error. To do this, go to the **Workers** tab, turn on the **Troubleshooting** switch, click the **Instructions** link, and then follow the instructions.
