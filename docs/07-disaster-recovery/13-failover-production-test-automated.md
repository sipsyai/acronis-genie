---
title: "Failover - production, test, and automated test failover"
section: "Implementing disaster recovery"
subsection: "Failover"
page_range: "991-998"
tags: [failover, production failover, test failover, automated test failover, finalization, recovery server, DHCP, DNS, failover process]
acronis_version: "26.02"
---

# Failover

When a recovery server is created, it stays in the **Standby** state. The corresponding virtual machine does not exist until you start a failover. Before starting a failover process, you must create at least one disk image backup (with bootable volume) of the original machine.

When starting the failover process, you select the recovery point (backup) of the original machine from which a virtual machine with the predefined parameters will be created. The failover operation uses the "run VM from a backup" functionality. The recovery server gets the transition state **Finalization**. This process implies transferring the server's virtual disks from the backup storage ('cold' storage) to the disaster recovery storage ('hot' storage).

> **Note**
> During the **Finalization**, the server is accessible and operable, although the performance is lower than normal. You can open the server console by clicking the **Console is ready** link. The link is available in the **VM State** column on the **Disaster Recovery** > **Servers** screen and in the server's **Details** view.

When the **Finalization** is completed, the server performance reaches its normal value. The server state changes to **Failover**. The workload is now switched from the original machine to the recovery server in the cloud site.

If the recovery server has a protection agent inside, the agent service is stopped in order to avoid interference (such as starting a backup or reporting outdated statuses to the backup component).

For Windows machines, if the `DeviceInstallDisabled` parameter is set to 1 (`HKLM\SYSTEM\CurrentControlSet\Services\DeviceInstall\Parameters\DeviceInstallDisabled = 1`), the disaster recovery service will set the value to 0 or remove the parameter completely during failover. This is required because Windows must be allowed to install and configure the necessary drivers and devices for the failover process to complete successfully. If you want to keep the original setting, you can manually restore it after the failover operation is complete.

> **Warning!**
> Setting the `DeviceInstallDisabled` parameter to 1 might impact subsequent disaster recovery operations, including failback and the re-validation steps that are required before initiating failback.

---

# Performing a failover

A failover is a process of moving a workload from your premises to the cloud, and also the state when the workload remains in the cloud.

When you start a failover, the recovery server starts in the production network. To avoid interference and unwanted issues, ensure that the original workload is not online and cannot be accessed via VPN.

To avoid a backup interference into the same cloud archive, manually revoke the protection plan from the workload that is currently in **Failover** state.

> **Important**
> You must create a recovery server in advance to protect your devices from a disaster. You can perform failover only from recovery points (backups) that were created after the recovery server of the device was created. At least one recovery point must be created before failing over to a recovery server. The maximum number of recovery points that is supported is 100.

### To perform a failover

1. Ensure that the original machine is not available on the network.
2. In the Cyber Protect console, go to **Disaster Recovery** > **Servers** > **Recovery servers**, and then select the recovery server.
3. Click **Failover**.
4. Select **Production failover**.
5. Select the recovery point (backup), and then click **Start**.
6. [If the backup that you selected is encrypted by using encryption as a machine property]
   a. Enter the encryption password for the backup set.
   b. [Optional] To save the password for the backup set and use it in subsequent failover operations, select the **Store the password in a secure credentials store...** check box and then, in the **Credentials name** field, enter a name for the credentials.
   c. Click **Done**.

When the recovery server starts, its state changes to **Finalization**, and after some time to **Failover**.

7. Ensure that the recovery server is started by viewing its console. Click **Disaster Recovery** > **Servers**, select the recovery server, and then click **Console**.
8. Ensure that the recovery server can be accessed using the production IP address that you specified when creating the recovery server.

Once the recovery server is finalized, a new protection plan is automatically created and applied to it, based on the protection plan that was used for creating the recovery server, with certain limitations. In this plan, you can change only the schedule and retention rules.

## How to perform failover of servers using local DNS

If your local site uses DNS servers to resolve machine names, recovery servers might fail to communicate after a failover. This happens because the DNS servers in the cloud are different from those on the local site. By default, newly created cloud servers use the DNS servers of the cloud site, but you can configure custom DNS settings.

## How to perform failover of a DHCP server

When a DHCP server on a Windows or Linux host is failed over to the cloud site, the DHCP server duplication issue occurs because the VPN gateway in the cloud also performs the DHCP role. To resolve this issue:

- If only the DHCP host was failed over to the cloud, log in to the DHCP host in the cloud and turn off the DHCP server on it. Only the VPN gateway will work as the DHCP server.
- If your cloud servers already got IP addresses from the DHCP host, log in to the DHCP host in the cloud and turn off the DHCP server on it. Also log in to the cloud servers and renew the DHCP lease to assign new IP addresses from the correct DHCP server (hosted on the VPN gateway).

> **Note**
> The instructions are not valid when your cloud DHCP server is configured with the **Custom DHCP** option, and some of the recovery or primary servers get their IP address from this DHCP server.

---

# Stopping a failover

You can stop a production failover at any moment, during each phase of the process.

> **Note**
> Stopping a failover reverts all changes that were made from the moment the failover was started, except the recovery server backups.

### To stop a production failover

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers** > **Recovery servers**.
2. Select the recovery server that is in status **Failover**.
3. Click the recovery server.
4. Click **Stop failover**.
5. In the confirmation window that appears, select the check box, and then click **Stop failover**. The failover is stopped. The recovery server returns to the **Standby** state.

---

# Test failover

Performing a test failover means starting a recovery server in a test VLAN that is isolated from your production network. You can test several recovery servers at a time and check their interaction. In the test network, the servers communicate using their production IP addresses, but they cannot initiate TCP or UDP connections to the workloads in your local network.

During test failover, the virtual machine (recovery server) is not finalized. The agent reads the content of the virtual disks directly from the backup and randomly accesses different parts of the backup. This might make the performance of the recovery server in the test failover state slower than its normal performance.

## Performing a test failover

Though performing a test failover is optional, we recommend that you make it a regular process with a frequency that you find adequate in terms of cost and safety. A good practice is creating a runbook -- a set of instructions describing how to spin up the production environment in the cloud.

### To perform a test failover

1. Select the original machine or select the recovery server that you want to test.
2. Click **Disaster Recovery**. The description of the recovery server opens.
3. Click **Failover**.
4. Select the failover type **Test failover**.
5. Select the recovery point (backup), and then click **Start**.
6. If the backup is encrypted, enter the encryption password for the backup set.
   [Optional] Save the password to a secure credentials store for subsequent operations.
   c. Click **Done**.

When the recovery server starts, its state changes to **Testing failover**.

7. Test the recovery server by using any of the following methods:
   - In **Disaster Recovery** > **Servers**, select the recovery server, and then click **Console**.
   - Connect to the recovery server by using RDP or SSH, and the test IP address that you specified when creating the recovery server.
   - Run a script within the recovery server to check the login screen, application startup, Internet connection, and the ability of other machines to connect.
   - If the recovery server has access to the Internet and a public IP address, you may want to use TeamViewer.

8. When the test is complete, click **Stop testing**. The recovery server is stopped. All changes made to the recovery server during the test failover are not preserved.

---

# Automated test failover

With automated test failover, the recovery server is tested automatically once a week or once a month, without any manual interaction.

The automated test failover process consists of the following parts:

1. Creating a virtual machine from the last recovery point
2. Taking a screenshot of the virtual machine
3. Analyzing if the operating system of the virtual machine starts successfully
4. Notifying you about the test failover status

> **Note**
> Automated test failover consumes compute points.

Note that, in very rare cases, automated test failover might be skipped and might not be performed at the scheduled time. This is because production failover has higher priority than automated test failover, so the hardware resources (CPU and RAM) allocated for automated test failover might be temporarily limited.

If automated test failover is skipped for some reason, an alert will be raised.

> **Note**
> Automated test failover will fail if the backups of the original machine are encrypted by using encryption as a machine property, and the encryption password is not specified when creating the recovery server.

## Configuring automated test failover

### To configure automated test failover

1. In the console, go to **Disaster recovery** > **Servers** > **Recovery servers**, and then select the recovery server.
2. Click **Edit**.
3. On the **Automated test failover** tab, in the **Schedule** field, select how often automated test failover should be performed.

| Option | Description |
|--------|-------------|
| **Monthly** | Automated test failover is performed at the beginning of each month. |
| **Weekly** | Automated test failover is performed every week. |

4. [Optional] In **Screenshot timeout**, change the default value of the maximum time period (in minutes) for the system to try performing automated test failover.
5. [Optional] If you want to save the **Screenshot timeout** value as the default, select **Set as default timeout**.
6. Click **Save**.

## Viewing the automated test failover status

1. In the console, go to **Disaster recovery** > **Servers** > **Recovery servers**, and then select the recovery server.
2. In the **Automated test failover** section, check the details of the last automated test failover.
3. [Optional] To view the screenshot of the virtual machine, click **Show screenshot**.

> **Note**
> The screenshot of the virtual machine is kept until automated test failover runs again and generates a new screenshot.

## Disabling automated test failover

1. In the console, go to **Disaster Recovery** > **Servers** > **Recovery servers**, and then select the recovery server.
2. Click **Edit**.
3. In the wizard, click the **Automated test failover** tab.
4. Turn off the **Automated test failover** switch.
5. Click **Save**.
