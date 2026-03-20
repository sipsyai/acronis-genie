---
title: "Uninstalling agents"
section: "Installing and deploying Cyber Protection agents"
subsection: null
page_range: "69-70"
tags: ["uninstall", "remove", "agent", "Windows", "Linux", "macOS", "VMware"]
acronis_version: "26.02"
---

# Uninstalling agents

When you uninstall an agent from a workload, the workload is automatically removed from the Cyber Protect console. If the workload is still shown after you uninstall the agent, for example, due to a network problem, manually remove this workload from the console. For more information about how to do it, refer to "Removing workloads from the Cyber Protect console" (p. 385).

> **Note:** Uninstalling an agent does not delete any plans or backups.

## Windows

> **Note:** [For protection plans created after November 2024] The uninstallation and modification of the protection agents for Windows is prohibited by default. Agent for Windows can be modified only during a maintenance window or through the agent auto update functionality. For instructions on how to enable the one-time uninstallation or modification of an agent, see "To allow the modification of an agent with uninstallation protection enabled" (p. 201). To disable the agent uninstallation protection, see "To disable agent uninstallation protection" (p. 201).

1. Sign in as an administrator to the machine with the agent.
2. In **Control panel**, go to **Programs and Features** (**Add or Remove Programs** in Windows XP).
3. Right-click **Acronis Cyber Protect**, and then select **Uninstall**.
4. [For password-protected agents] Specify the password that is required to uninstall the agent, and then click **Next**.
5. [Optional] Select the **Remove the logs and configuration settings** check box. If you are planning to install the agent again, keep this check box cleared. If you select the check box and then install the agent again, this workload might be duplicated in the Cyber Protect console and its old backups might not be associated with it.
6. Click **Uninstall**.

## Linux

1. On the machine with the agent, run `/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall` as the root user.
2. [Optional] Select the **Clean up all product traces (Remove the product's logs, tasks, vaults, and configuration settings)** check box. If you are planning to install the agent again, keep this check box cleared.
3. Confirm your decision.

## macOS

1. On the machine with the agent, double-click the installation .dmg file.
2. Wait until the operating system mounts the installation disk image.
3. Inside the image, double-click **Uninstall**.
4. If prompted, provide administrator credentials.
5. Confirm your decision.

## To uninstall components that are bundled with Agent for Windows

You can uninstall individual components that are bundled with Agent for Windows, such as Cyber Protect Monitor, Agent for Data Loss Prevention, or Bootable Media Builder, without uninstalling Agent for Windows.

1. Sign in as an administrator to the machine with the agent.
2. Run the setup program, and then click **Modify installed components**.
3. Clear the check boxes next to the components that you want to uninstall, and then click **Done**.

## To remove Agent for VMware (Virtual appliance)

1. By using the vSphere Client, log in to vCenter Server.
2. [If the virtual appliance is powered on] Right-click the virtual appliance, and then click **Power** > **Power Off**. Confirm your decision.
3. [If the virtual appliance uses locally attached storage on a virtual disk and you want to preserve data on that disk] Remove the virtual storage from the virtual appliance:
   a. Right-click the virtual appliance, and then click **Edit Settings**.
   b. Select the disk with the storage, and then click **Remove**.
   c. Under **Removal Options**, click **Remove from virtual machine**.
   d. Click **OK**.
   As a result, the disk remains in the datastore. You can attach the disk to another virtual appliance.
4. Right-click the virtual appliance, and then click **Delete from Disk**. Confirm your decision.
5. [Optional] [If you are not planning to use this appliance again] In the Cyber Protect console, go to **Backup storage** > **Locations**, and then delete the location corresponding to the locally attached storage.
