---
title: "Device control module overview"
section: "Managing workloads in the Cyber Protect console"
subsection: "Working with the Device control module"
page_range: "427-431"
tags: [device control, data loss prevention, DLP, peripheral devices, security, macOS, Windows]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#dc-alerts.html"
---

# Working with the Device control module

A part of the Cyber Protection service protection plans, the device control module leverages a functional subset of the agent for Data Loss Prevention on each protected computer to detect and prevent unauthorized access and transmission of data over local computer channels. It provides fine-grained control over a wide range of data leakage pathways including data exchange using removable media, printers, virtual and redirected devices, and the Windows clipboard.

The module is available for Cyber Protect Essentials, Cyber Protect Standard, and Cyber Protect Advanced editions that are licensed per workload.

> **Note:** On Windows machines, the device control features require the installation of Agent for Data Loss Prevention. It will be installed automatically for protected workloads if the **Device control** module is enabled in their protection plans.

The device control module relies on the data loss prevention functions of the agent to enforce contextual control over data access and transfer operations on the protected computer. These include user access to peripheral devices and ports, document printing, clipboard copy/paste operations, media format and eject operations, as well as synchronizations with locally connected mobile devices.

The device control module controls access to various peripheral devices, whether used directly on protected computers or redirected in virtualization environments hosted on protected computers. It recognizes devices redirected in Microsoft Remote Desktop Server, Citrix XenDesktop/XenApp/XenServer, and VMware Horizon. It can also control data copy operations between the clipboard of the guest operating system running on VMware Workstation/Player, Oracle VM VirtualBox, or Windows Virtual PC, and the clipboard of the host operating system running on the protected computer.

## Supported operating systems

### Device control

- Microsoft Windows 7 Service Pack 1 and later
- Microsoft Windows Server 2008 R2 -- Windows Server 2022
- macOS 10.15 (Catalina)
- macOS 11.2.3 (Big Sur)
- macOS 12 (Monterey)
- macOS 13 (Ventura)
- macOS 14 (Sonoma)
- macOS 15 (Sequoia)

> **Note:** Agent for Data Loss Prevention for macOS supports only x64 processors. Apple silicon ARM-based processors are not supported.

### Data loss prevention

- Microsoft Windows 7 Service Pack 1 and later
- Microsoft Windows Server 2008 R2 -- Windows Server 2022

> **Note:** Agent for Data Loss Prevention might be installed on unsupported macOS systems because it is an integral part of Agent for Mac. In this case, the Cyber Protect console will indicate that Agent for Data Loss Prevention is installed on the computer, but the device control and data loss prevention functionality will not work. Device control functionality will only work on macOS systems that are supported by Agent for Data Loss Prevention.

## Limitation on the use of the agent for Data Loss Prevention with Hyper-V

Do not install Agent for Data Loss Prevention on Hyper-V hosts in Hyper-V clusters because it might cause BSOD issues, mainly in Hyper-V clusters with Clustered Shared Volumes (CSV).

If you use any of the following versions of Agent for Hyper-V, you need to manually remove Agent for Data Loss Prevention:

- 15.0.26473 (C21.02)
- 15.0.26570 (C21.02 HF1)
- 15.0.26653 (C21.03)
- 15.0.26692 (C21.03 HF1)
- 15.0.26822 (C21.04)

To remove Agent for Data Loss Prevention, on the Hyper-V host, run the installer manually and clear the Agent for Data Loss Prevention check box, or run the following command:

```
<installer_name> --remove-components=agentForDlp -quiet
```

## Device control configuration summary

The **Device control** section displays a summary of the module's configuration:

- **Access settings** -- Shows a summary of device types and ports with restricted (denied or read-only) access, if any. Otherwise, indicates that all device types are allowed.
- **Device types allowlist** -- Shows how many device subclasses are allowed by excluding from device access control, if any.
- **USB devices allowlist** -- Shows how many USB devices/models are allowed by excluding from device access control, if any.
- **Exclusions** -- Shows how many access control exclusions have been set for Windows clipboard, screenshot capture, printers, and mobile devices.

## Using device control

This section covers step-by-step instructions for basic tasks when using the device control module.

### Enable or disable device control

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Open the protection plan panel:
   - To create a new protection plan, select a machine to protect, click **Protect**, and then click **Create plan**.
   - To change an existing protection plan, select a protected machine, click **Protect**, click the ellipsis (...) next to the name of the protection plan, and then click **Edit**.
3. In the protection plan panel, navigate to the **Device control** area, and enable or disable **Device control**.
4. Apply changes:
   - If creating a protection plan, click **Create**.
   - If editing a protection plan, click **Save**.

### Enabling the use of the device control module on macOS

The device control settings of a protection plan become effective only after loading the device control driver on the protected workload. This is a one-time operation that requires administrator privileges on the endpoint machine.

Supported macOS versions: macOS 10.15 and later, macOS 11.2.3 and later, macOS 12.2 and later, macOS 13.2 and later, macOS 14 and later, macOS 15 and later.

1. Install Agent for Mac on the machine that you want to protect.
2. Enable device control settings in the protection plan.
3. Apply the protection plan.
4. The "System Extension Blocked" warning will appear on the protected workload. Click **Open Security Preferences**.
5. In the **Security & Privacy** pane that appears, select **App Store and identified developers** and then click **Allow**.
6. In the dialog that appears, click **Restart** to restart the workload and activate the device control settings.

> **Note:** You do not have to repeat these steps if the device control setting are disabled and then enabled again.
