---
title: "Compute points, failover, and test failover"
section: "Implementing disaster recovery"
subsection: "Failover"
page_range: "990-998"
tags: [compute points, failover, test failover, automated test failover, production failover, recovery server]
acronis_version: "26.02"
---

# Compute points

In Disaster Recovery to Cyber Protect Cloud, compute points are used for primary servers and recovery servers during test failover and production failover. Compute points reflect the compute resources used for running the servers (virtual machines) in the cloud.

The consumption of compute points during disaster recovery depends on the server's parameters, and the duration of the time period in which the server is in failover state. The more powerful the server and the longer the time period, the more compute points will be consumed.

All servers that are running in Cyber Protect Cloud will be charged for compute points, depending on their configured flavor, and regardless of their state (powered on or powered off). Recovery servers that are in the **Standby** state do not consume compute points and will not be charged.

| Type | CPU | RAM | Compute points |
|------|-----|-----|----------------|
| F1 | 1 vCPU | 2 GB | 1 |
| F2 | 1 vCPU | 4 GB | 2 |
| F3 | 2 vCPU | 8 GB | 4 |
| F4 | 4 vCPU | 16 GB | 8 |
| F5 | 8 vCPU | 32 GB | 16 |
| F6 | 16 vCPU | 64 GB | 32 |
| F7 | 16 vCPU | 128 GB | 64 |
| F8 | 16 vCPU | 256 GB | 128 |

For example, if you want to protect with Disaster Recovery one virtual machine with 4 vCPU and 16 GB RAM, and one virtual machine with 2 vCPU and 8 GB RAM, the first will consume 8 compute points per hour, and the second 4 compute points per hour. If both are in failover, the total consumption will be 12 compute points per hour, or 288 compute points for the whole day.

> **Note:** If the overage for the **Compute points** quota is reached, all primary and recovery servers will be shut down. It will not be possible to use these servers until the beginning of the next billing period, or until you increase the quota. The default billing period is a full calendar month.

# Failover

When a recovery server is created, it stays in the **Standby** state. The corresponding virtual machine does not exist until you start a failover. Before starting a failover process, you must create at least one disk image backup (with bootable volume) of the original machine.

When starting the failover process, you select the recovery point (backup) of the original machine from which a virtual machine with the predefined parameters will be created. The failover operation uses the "run VM from a backup" functionality. The recovery server gets the transition state **Finalization**, during which the server's virtual disks are transferred from the backup storage ('cold' storage) to the disaster recovery storage ('hot' storage).

> **Note:** During the **Finalization**, the server is accessible and operable, although the performance is lower than normal. You can open the server console by clicking the **Console is ready** link.

When the **Finalization** is completed, the server performance reaches its normal value. The server state changes to **Failover**. The workload is now switched from the original machine to the recovery server in the cloud site.

If the recovery server has a protection agent inside, the agent service is stopped to avoid interference (such as starting a backup or reporting outdated statuses to the backup component).

# Performing a failover

A failover is a process of moving a workload from your premises to the cloud, and also the state when the workload remains in the cloud.

When you start a failover, the recovery server starts in the production network. To avoid interference, ensure that the original workload is not online and cannot be accessed via VPN. To avoid backup interference into the same cloud archive, manually revoke the protection plan from the workload that is currently in **Failover** state.

> **Important:** You must create a recovery server in advance. You can perform failover only from recovery points (backups) that were created after the recovery server of the device was created. At least one recovery point must be created. The maximum number of recovery points that is supported is 100.

## To perform a failover

1. Ensure that the original machine is not available on the network.
2. In the Cyber Protect console, go to **Disaster Recovery** > **Servers** > **Recovery servers**, and then select the recovery server.
3. Click **Failover**.
4. Select **Production failover**.
5. Select the recovery point (backup), and then click **Start**.
6. [If the backup is encrypted by using encryption as a machine property]
   a. Enter the encryption password for the backup set.
   b. [Optional] To save the password for subsequent failover operations, select the **Store the password in a secure credentials store...** check box and enter a credentials name.
   c. Click **Done**.

When the recovery server starts, its state changes to **Finalization**, and after some time to **Failover**.

7. Ensure that the recovery server is started by viewing its console (**Disaster Recovery** > **Servers**, select the recovery server, and then click **Console**).
8. Ensure that the recovery server can be accessed using the production IP address that you specified when creating it.

Once the recovery server is finalized, a new protection plan is automatically created and applied to it based on the protection plan that was used for creating the recovery server.

### How to perform failover of servers using local DNS

If your local site uses DNS servers to resolve machine names, recovery servers might fail to communicate after a failover. You can configure custom DNS settings.

### How to perform failover of a DHCP server

When a DHCP server is failed over to the cloud site, a duplication issue occurs because the VPN gateway in the cloud also performs the DHCP role. To resolve: log in to the DHCP host in the cloud and turn off the DHCP server on it. Then renew the DHCP lease on cloud servers if needed.

## Stopping a failover

You can stop a production failover at any moment, during each phase of the process.

> **Note:** Stopping a failover reverts all changes that were made from the moment the failover was started, except the recovery server backups.

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers** > **Recovery servers**.
2. Select the recovery server that is in status **Failover**.
3. Click the recovery server.
4. Click **Stop failover**.
5. In the confirmation window, select the check box, and then click **Stop failover**.

The recovery server returns to the **Standby** state.

# Test failover

Performing a test failover means starting a recovery server in a test VLAN that is isolated from your production network. You can test several recovery servers at a time and check their interaction. In the test network, the servers communicate using their production IP addresses, but they cannot initiate TCP or UDP connections to the workloads in your local network.

During test failover, the virtual machine (recovery server) is not finalized. The agent reads the content of the virtual disks directly from the backup. This might make the performance of the recovery server in the test failover state slower than its normal performance.

## Performing a test failover

1. Select the original machine or select the recovery server that you want to test.
2. Click **Disaster Recovery**. The description of the recovery server opens.
3. Click **Failover**.
4. Select the failover type **Test failover**.
5. Select the recovery point (backup), and then click **Start**.
6. [If the backup is encrypted] Enter the password and optionally store it.

When the recovery server starts, its state changes to **Testing failover**.

7. Test the recovery server by using any of the following methods:
   - In **Disaster Recovery** > **Servers**, select the recovery server, and then click **Console**.
   - Connect to the recovery server by using RDP or SSH, and the test IP address.
   - Run a script within the recovery server.
   - If the recovery server has access to the Internet and a public IP address, use TeamViewer.

8. When the test is complete, click **Stop testing**. The recovery server is stopped. All changes made to the recovery server during the test failover are not preserved.

## Automated test failover

With automated test failover, the recovery server is tested automatically once a week or once a month, without any manual interaction. The process consists of:

1. Creating a virtual machine from the last recovery point.
2. Taking a screenshot of the virtual machine.
3. Analyzing if the operating system of the virtual machine starts successfully.
4. Notifying you about the test failover status.

> **Note:** Automated test failover consumes compute points. Production failover has higher priority than automated test failover.

### Configuring automated test failover

1. In the console, go to **Disaster recovery** > **Servers** > **Recovery servers**, and then select the recovery server.
2. Click **Edit**.
3. On the **Automated test failover** tab, in the **Schedule** field, select how often automated test failover should be performed:

   | Option | Description |
   |--------|-------------|
   | **Monthly** | Automated test failover is performed at the beginning of each month. |
   | **Weekly** | Automated test failover is performed every week. |

4. [Optional] In **Screenshot timeout**, change the default value of the maximum time period for the system to try performing automated test failover.
5. [Optional] Select **Set as default timeout** if you want to save the **Screenshot timeout** value as the default.
6. Click **Save**.

### Viewing the automated test failover status

1. In the console, go to **Disaster recovery** > **Servers** > **Recovery servers**, and then select the recovery server.
2. In the **Automated test failover** section, check the details of the last automated test failover.
3. [Optional] To view the screenshot of the virtual machine, click **Show screenshot**.

### Disabling automated test failover

1. Select the recovery server.
2. Click **Edit**.
3. Click the **Automated test failover** tab.
4. Turn off the **Automated test failover** switch.
5. Click **Save**.
