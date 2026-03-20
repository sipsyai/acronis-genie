---
title: "Dynamic installation of components and macOS permissions"
section: "Installing and deploying Cyber Protection agents"
subsection: "Before you start"
page_range: "54-55"
tags: ["dynamic-installation", "components", "antimalware", "URL-filtering", "DLP", "macOS", "permissions", "Connect-Agent"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#dynamic-installation-uninstallation-components.html"
---

# Dynamic installation of components

For Windows workloads protected by agent version 15.0.26986 (released in May 2021) or later, the following components are installed dynamically — that is, only when required by a protection plan:

- Agent for Antimalware protection and URL filtering — required for antimalware protection and URL filtering.
- Agent for Data Loss Prevention — required for device control.

By default, these components are not installed. The respective component is automatically installed if a workload becomes protected by a plan in which any of the following modules are enabled:

- **Antivirus & Antimalware protection**
- **URL filtering**
- **Device control**

Similarly, if no protection plan requires antimalware protection, URL filtering, or device control, the respective component is automatically uninstalled.

Dynamic installation or uninstallation of components might take up to 10 minutes after you apply, revoke, edit, or delete a protection plan. If any of the following operations is running, dynamic installation or uninstallation will start after the operation completes:

- Backup
- Recovery
- Backup replication
- Virtual machine replication
- Testing a replica
- Running a virtual machine from backup (including finalization)
- Disaster recovery failover
- Disaster recovery failback
- Running a script (for Cyber Scripting functionality)
- Patch installation
- ESXi configuration backup

---

# Granting the required system permissions to the Connect Agent

To enable all features from the remote desktop functionality on macOS workloads, in addition to the full disk access permission, you must grant the following permissions to the Connect Agent:

- **Screen Recording** — enables screen recording of the macOS workload via NEAR. Until this permission is granted, all remote control connections are denied.
- **Accessibility** — enables remote connections in control mode via NEAR.
- **Microphone** — enables sound redirection from the remote macOS workload to the local workload via NEAR. A sound capture driver must be installed on the workload. See "Remote sound redirection" (p. 1346).
- **Automation** — enables the empty recycle bin action.
- **Location Services** — enables the location services on the workload. Until this permission is granted, the agent cannot track the location of the workload.

After you start the agent on the macOS workload, it will check if the agent has these rights and will ask you to grant the permissions, if needed.

## To grant the Screen Recording permission

1. In the **Grant required system permissions to Cyber Protect Agent** dialog, click **Set up system permissions**.
2. In the **System permissions** dialog, on the **Screen Recording** row, click **Acquire**.
3. Click **Open System Settings**.
4. For **Connect Agent**, enable the toggle.

If the agent does not have the permission when you try to access the workload remotely, it will show the Screen Recording permission request dialog. Only the local user may answer the dialog.

## To grant the Accessibility permission

1. In the **Grant required system permissions to Cyber Protect Agent** dialog, click **Set up system permissions**.
2. In the **System permissions** dialog, on the **Accessibility** row, click **Acquire**.
3. Click **Open System Settings**.
4. Click the lock icon in the bottom-left corner of the window so that it changes to an unlocked icon. The system will ask you for an administrator password to make changes.
5. Select **Connect Agent**.

## To grant the Microphone permission

1. In the **Grant required system permissions to Cyber Protect Agent** dialog, click **Set up system permissions**.
2. In the **System permissions** dialog, on the **Microphone** row, click **Acquire**.
3. In the system dialog that opens, click **OK**.
