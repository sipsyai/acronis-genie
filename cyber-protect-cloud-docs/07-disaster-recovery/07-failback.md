---
title: "Failback to local site"
section: "Implementing disaster recovery"
subsection: "Failback"
page_range: "999-1009"
tags: [failback, agent-based, agentless, bootable media, hypervisor agent, manual failback, data transfer, switchover]
acronis_version: "26.02"
---

# Failback

A failback is a process of moving the workload from the cloud back to a physical or virtual machine on your local site. You can perform a failback on a recovery server in **Failover** state, and continue using the server on your local site.

You can perform automated failover to a virtual or physical target machine on your local site. During the failback, you can transfer the backup data to your local site while the virtual machine in the cloud continues to run. This technology helps you to achieve a very short downtime period, which is estimated and displayed in the Cyber Protect console.

> **Note:** Runbook operations support the failback in manual mode only. If you start the failback process by executing a runbook that includes a **Failback server** step, the procedure will require manual interaction.

## Failback methods

- **Agent-based failback via bootable media** -- Optimized for performing a failback to the original physical or virtual machine. Only the delta changes are transferred to the local site. Best for failback to physical machines or when you want to restore to the original VM.
- **Agentless failback via a hypervisor agent** -- Optimized for performing a failback to a new virtual machine on VMware ESXi or Microsoft Hyper-V hosts.
- **Manual failback** -- Use only when advised by the Support team. Data transfer is done manually after the virtual machine in the cloud is powered off. Results in a longer downtime period.

## Agent-based failback via bootable media

The agent-based failback process consists of four phases:

### 1. Planning

During this phase, you restore the IT infrastructure at your local site (hosts, network configurations), configure the failback parameters, and plan when to start the data transfer.

### 2. Data transfer

During this phase, the data is transferred from the cloud site to the local site while the virtual machine in the cloud continues to run. You can start the switchover at any time during the data transfer phase, but consider the following:

- The longer you remain in the data transfer phase, the more data will be transferred and the shorter the downtime during the switchover phase.
- If you want to minimize the downtime, start the switchover phase after more than 90% of the data is transferred.
- If you can afford a longer downtime period and do not want to spend more compute points, you can start the switchover phase earlier.

> **Note:** The data transfer process uses flashback technology. This technology compares the data on the target machine to the data of the virtual machine in the cloud. If part of the data is already available on the target machine, it will not be transferred again. For this reason, we recommend that you restore the server to the original machine.

### 3. Switchover

During this phase, the virtual machine in the cloud is turned off, and the remaining data -- including the last backup increment -- is transferred to the local site. If no backup plan is applied on the recovery server, a backup will be performed automatically during the switchover phase, which will slow down the process.

### 4. Validation

During this phase, the machine on the local site is ready, and you can reboot it using a Linux-based bootable media. You can verify if the virtual machine is working correctly, and:
- If everything is working as expected, confirm the failback. After the failback confirmation, the virtual machine in the cloud is deleted, and the recovery server returns to the **Standby** state.
- If something is wrong, you can cancel the failover and return to the planning phase.

> **Note:** After the bootable media has been rebooted, you will not be able to use it again. If you discover something wrong at the validation phase, you must register a new bootable media and start the failback process again. However, flashback technology will be used, so the data already on the local site will not be transferred again.

### To perform a failback to a physical machine

**Prerequisites:**
- The agent for failback is online and not currently used for another failback operation.
- Your Internet connection is stable.
- A registered bootable media is available.
- The target machine is the original machine on your local site, or has the same firmware.
- There is at least one full backup of the virtual machine in the cloud.

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Failback type** field, select **Agent-based via bootable media**.
5. In the **Target bootable media** field, click **Specify**, select the bootable media, and then click **Done**.
6. [Optional] To change the default disk mapping, in the **Disk mapping** field, click **Specify**, map the disks, and then click **Done**.
7. Click **Start data transfer** and then, in the confirmation window, click **Start**.

   > **Note:** If there is no backup of the virtual machine in the cloud, the system will perform a backup automatically before the data transfer phase.

   The data transfer phase starts. The console displays: **Progress** (how much data is already transferred vs. total amount) and **Downtime estimation** (how much time the VM in the cloud will be unavailable if you start switchover now).

8. Click **Switchover** and then, in the confirmation window, click **Switchover** again.

   The switchover phase starts. The console displays: **Progress** (progress of restoring the machine) and **Estimated time to finish** (approximate time when the switchover phase will be completed).

   > **Note:** If no backup plan is applied to the virtual machine in the cloud, a backup will be performed automatically during the switchover phase, which will cause a longer downtime.

9. After the **Switchover** phase completes, reboot the bootable media, and then verify that the physical machine on your local site is working as expected.

10. Click **Confirm failback** and then, in the confirmation window, click **Confirm** to finalize the process. The virtual machine in the cloud is deleted, and the recovery server returns to the **Standby** state.

> **Note:** Applying a protection plan on the recovered server is not part of the failback process. After the failback process completes, apply a protection plan to ensure the server is protected again.

## Agentless failback via a hypervisor agent

The agentless failback via a hypervisor agent is optimized for performing a failback to a new virtual machine. If you want to perform a failback to the original virtual machine, use the agent-based failback via bootable media.

The agentless failback also consists of four phases (Planning, Data transfer, Switchover, Validation) with the same considerations as agent-based failback.

**Prerequisites:**
- The agent for failback is online and not currently used for another failback operation.
- Your Internet connection is stable.
- There is at least one full backup of the virtual machine in the cloud.

### To perform an agentless failback to a virtual machine

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Failback parameters** section, in the **Failback type** field, select **Agentless via hypervisor agent**, and then configure the other parameters:

| Parameter | Description |
|-----------|-------------|
| **Backup size** | Amount of data that will be transferred. Will increase during the data transfer phase as the VM in the cloud continues generating new data. To estimate downtime: take 10% of the Backup size value (after 90% is transferred) and divide it by your Internet speed. |
| **Target machine location** | Failback location: a VMware ESXi host or a Microsoft Hyper-V host. You can select from all hosts that have an agent registered with the Cyber Protection service. |
| **Agent** | Agent which will perform the failback operation. You can use one agent to perform one failback operation at the same time. You can install several agents on VMware ESXi hosts to run separate failback processes in parallel. |
| **Target machine settings** | Virtual processors, Memory, Units, and [Optional] Network adapters. |
| **Path** | (For Microsoft Hyper-V hosts) Folder on the host where your machine will be stored. |
| **Datastore** | (For VMware ESXi hosts) Datastore on the host where your machine will be stored. |
| **Provisioning mode** | For Hyper-V: Dynamically expanding (default) or Fixed size. For VMware: Thin (default) or Thick. |
| **Target machine name** | Name of the target machine. Must be unique on the selected Target machine location. |

5. Click **Start data transfer**, and then in the confirmation window, click **Start**.
6. Click **Switchover** when ready, and then confirm.
7. After the **Switchover** phase completes and the virtual machine at your local site is started automatically, validate that it is working as expected.
8. Click **Confirm failback**, and then click **Confirm** to finalize the process.

## Manual failback

> **Note:** We recommend that you use the failback process in a manual mode only when you are advised to do so by the Support team.

In manual mode, the data transfer from the backup in the cloud to the local site will not be done automatically. The virtual machine in the cloud must be powered off first. This makes the failback process much slower, and you should expect a longer downtime period.

### Phases of manual failback

1. **Planning** -- Restore your IT infrastructure, configure failback parameters.
2. **Switchover** -- The virtual machine in the cloud is turned off, and the newly generated data is backed up. You then recover the machine to the local site manually (recover the disk by using bootable media, or recover the entire machine from the cloud backup storage).
3. **Validation** -- Verify that the machine at the local site is working correctly, and confirm the failback.

### To perform a manual failback

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Select the recovery server that is in the **Failover** state.
3. Click the **Failback** tab.
4. In the **Target** field, select **Physical machine**.
5. Click the gear icon, and then enable the **Use manual mode** switch.
6. Click **Switchover**, and then in the confirmation window, click **Switchover** again. The virtual machine on the cloud site is turned off.
7. Recover the server from the cloud backup to the physical or virtual machine on your local site.
8. Ensure that the recovery is completed and the recovered machine works properly, and click **Machine is restored**.
9. If everything is working as expected, click **Confirm failback**, and then click **Confirm** again.

The recovery server and recovery points become ready for the next failover. To create new recovery points, apply a protection plan to the new local server.
