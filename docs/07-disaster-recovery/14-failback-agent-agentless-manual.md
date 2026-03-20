---
title: "Failback - agent-based, agentless, and manual"
section: "Implementing disaster recovery"
subsection: "Failback"
page_range: "999-1009"
tags: [failback, agent-based failback, agentless failback, manual failback, bootable media, hypervisor agent, data transfer, switchover, validation, flashback technology]
acronis_version: "26.02"
---

# Failback

A failback is a process of moving the workload from the cloud back to a physical or virtual machine on your local site. You can perform a failback on a recovery server in **Failover** state, and continue using the server on your local site.

You can perform automated failover to a virtual or physical target machine on your local site. During the failback, you can transfer the backup data to your local site while the virtual machine in the cloud continues to run. This technology helps you to achieve a very short downtime period, which is estimated and displayed in the Cyber Protect console.

> **Note**
> Runbook operations support the failback in manual mode only. This means that if you start the failback process by executing a runbook that includes a **Failback server** step, the procedure will require a manual interaction: you must manually recover the machine, and confirm or cancel the failback process from the **Disaster Recovery** > **Servers** tab.

## Failback methods

| Method | Target | Recommended for |
|--------|--------|-----------------|
| **Agent-based failback via bootable media** | Physical or virtual machine | Original physical machine or same firmware. Transfers only delta changes for shorter downtime. |
| **Agentless failback via hypervisor agent** | New virtual machine | Failback to a new VM on VMware ESXi or Microsoft Hyper-V host. |
| **Manual failback** | Physical or virtual machine | When automated procedures cannot be used, as advised by Support team. Longer downtime period expected. |

---

# Agent-based failback via bootable media

The agent-based failback via bootable media process is optimized for performing a failback to the original physical or virtual machine. During this process, only the delta changes are transferred to the local site.

The agent-based failback process via bootable media consists of the following phases:

1. **Planning**. During this phase, you restore the IT infrastructure at your local site (such as the hosts and the network configurations), configure the failback parameters, and plan when to start the data transfer.

2. **Data transfer**. During this phase, the data is transferred from the cloud site to the local site while the virtual machine in the cloud continues to run. You can start the next phase (switchover) at any time during the data transfer phase, but you should consider:
   - The longer you remain in the data transfer phase, the more data will be transferred to your local site.
   - The shorter the downtime period that you will experience during the switchover phase.
   - The higher the cost you will pay (you spend more compute points).
   If you want to minimize the downtime, start the switchover phase after more than 90% of the data is transferred to the local site.

   > **Note**
   > The data transfer process uses a flashback technology. This technology compares the data that is available on the target machine to the data of the virtual machine in the cloud. If part of the data is already available on the target machine, it will not be transferred again. This technology makes the data transfer phase faster. For this reason, we recommend that you restore the server to the original machine on your local site.

3. **Switchover**. During this phase, the virtual machine in the cloud is turned off, and the remaining data -- including the last backup increment -- is transferred to the local site. If no backup plan is applied on the recovery server, a backup will be performed automatically during the switchover phase, which will slow down the process.

4. **Validation**. During this phase, the machine on the local site is ready, and you can reboot it using a Linux-based bootable media. You can verify if the virtual machine is working correctly, and:
   - If everything is working as expected, confirm the failback. After the failback confirmation, the virtual machine in the cloud is deleted, and the recovery server returns to the **Standby** state.
   - If something is wrong, you can cancel the failover and return to the planning phase.

   > **Note**
   > After the bootable media has been rebooted, you will not be able to use it again. If, at the validation phase, you discover something wrong, you must register a new bootable media and start the failback process again. However, as flashback technology will be used, the data that is already on the local site will not be transferred again, and the failback process will be much faster.

## Performing agent-based failback via bootable media

### Prerequisites

- The agent that you will use to perform failback is online and is not currently used for another failback operation.
- Your Internet connection is stable.
- A registered bootable media is available.
- The target machine is the original machine on your local site, or has the same firmware as the original machine.
- There is at least one full backup of the virtual machine in the cloud.

### To perform a failback to a physical machine

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Failback type** field, select **Agent-based via bootable media**.
5. In the **Target bootable media** field, click **Specify**, select the bootable media, and then click **Done**.
6. [Optional] To change the default disk mapping, in the **Disk mapping** field, click **Specify**, map the disks of the backup to the disks of the target machine, and then click **Done**.
7. Click **Start data transfer** and then, in the confirmation window, click **Start**.

The data transfer phase starts. The console displays the following information:

| Field | Description |
|-------|-------------|
| **Progress** | Shows how much data is already transferred to the local site, and the total amount of data that must be transferred. Both values increase with time as the virtual machine continues to generate new backup increments during data transfer. |
| **Downtime estimation** | Shows how much time the virtual machine in the cloud will be unavailable if you start the switchover phase now. The value decreases with time. |

8. Click **Switchover** and then, in the confirmation window, click **Switchover** again. The switchover phase starts with the following displayed information:

| Field | Description |
|-------|-------------|
| **Progress** | Shows the progress of restoring the machine on the local site. |
| **Estimated time to finish** | Shows the approximate time when the switchover phase will be completed. |

> **Note**
> If no backup plan is applied to the virtual machine in the cloud, a backup will be performed automatically during the switchover phase, which will cause a longer downtime.

9. After the **Switchover** phase completes, reboot the bootable media, and then verify that the physical machine on your local site is working as expected.
10. Click **Confirm failback** and then, in the confirmation window, click **Confirm** to finalize the process. The virtual machine in the cloud is deleted, and the recovery server returns to the **Standby** state.

> **Note**
> Applying a protection plan on the recovered server is not part of the failback process. After the failback process completes, apply a protection plan on the recovered server to ensure that it is protected again.

---

# Agentless failback via a hypervisor agent

The agentless failback via a hypervisor agent process is optimized for performing a failback to a new virtual machine. If you want to perform a failback to the original virtual machine, follow the procedure for agent-based failback via bootable media.

The agentless failback via a hypervisor agent consists of four phases: Planning, Data transfer, Switchover, and Validation -- similar to agent-based failback.

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
| **Backup size** | Amount of data that will be transferred to your local site during the failback process. The **Backup size** will be increasing during the data transfer phase because the virtual machine continues to run and generate new data. To calculate the estimated downtime, take 10% of the **Backup size** value and divide it by the value of your Internet speed. |
| **Target machine location** | Failback location: a VMware ESXi host or a Microsoft Hyper-V host. You can select from all hosts that have an agent registered with the Cyber Protection service. |
| **Agent** | Agent which will perform the failback operation. One agent can perform one failback operation at a time. You can install several agents on VMware ESXi hosts, and start a separate failback process using each of them. |
| **Target machine settings** | Virtual machine settings: **Virtual processors**, **Memory**, **Units**, [Optional] **Network adapters**. |
| **Path** | (For Microsoft Hyper-V hosts) Folder on the host where your machine will be stored. |
| **Datastore** | (For VMware ESXi hosts) Datastore on the host where your machine will be stored. |
| **Provisioning mode** | Method of allocation of the virtual disk. For Hyper-V hosts: **Dynamically expanding** (default) or **Fixed size**. For VMware ESXi hosts: **Thin** (default) or **Thick**. |
| **Target machine name** | Name of the target machine. By default, the name is the same as the recovery server name. Must be unique on the selected **Target machine location**. |

5. Click **Start data transfer**, and then in the confirmation window, click **Start**.
6. Click **Switchover** and then, in the confirmation window, click **Switchover** again.
7. After the **Switchover** phase completes and the virtual machine at your local site is started automatically, validate that it is working as expected.
8. Click **Confirm failback** and then, in the confirmation window, click **Confirm** to finalize the process. The virtual machine in the cloud is deleted, and the recovery server returns to the **Standby** state.

---

# Manual failback

> **Note**
> We recommend that you use the failback process in a manual mode only when you are advised to do so by the Support team.

You can also start a failback process in a manual mode. In this case, the data transfer from the backup in the cloud to the local site will not be done automatically. It must be done manually after the virtual machine in the cloud is powered off. This makes the failback process in a manual mode much slower, and you should expect a longer downtime period.

The failback process in a manual mode consists of the following phases:

1. **Planning**. Restore IT infrastructure at your local site, configure failback parameters, and plan data transfer.
2. **Switchover**. The virtual machine in the cloud is turned off, and the newly generated data is backed up. If no backup plan is applied on the recovery server, a backup will be performed automatically. When the backup is complete, you recover the machine to the local site manually using bootable media or from the cloud backup storage.
3. **Validation**. You verify that the physical or virtual machine at the local site is working correctly, and confirm the failback. After the confirmation, the virtual machine on the cloud site is deleted, and the recovery server returns to the **Standby** state.

### To perform a manual failback

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Target** field, select **Physical machine**.
5. Click the gear icon, and then enable the **Use manual mode** switch.
6. [Optional] Calculate the estimated downtime period during the failback process, by dividing the **Backup size** value by the value of your Internet speed.
7. Click **Switchover**, and then in the confirmation window, click **Switchover** again. The virtual machine on the cloud site is turned off.
8. Recover the server from the cloud backup to the physical or virtual machine on your local site.
9. Ensure that the recovery is completed and the recovered machine works properly, and click **Machine is restored**.
10. If everything is working as expected, click **Confirm failback**, and then in the confirmation window, click **Confirm** again.

The recovery server and recovery points become ready for the next failover. To create new recovery points, apply a protection plan to the new local server.

> **Note**
> Applying a protection plan on the recovered server is not part of the failback process. After the failback process completes, apply a protection plan on the recovered server to ensure that it is protected again. You may apply the same protection plan that was applied on the original server, or a new protection plan that has the **Disaster recovery** module enabled.
