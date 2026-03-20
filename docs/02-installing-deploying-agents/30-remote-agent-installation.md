---
title: "Remote installation of agents and UAC requirements"
section: "Installing and deploying Cyber Protection agents"
subsection: "Remote installation of agents"
page_range: "182-197"
tags: ["remote installation", "UAC", "agent components", "discovery", "GPO", "credentials", "onboarding", "exclusions"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#remote-installation-of-agents.html"
---

# Remote installation of agents and UAC requirements

After the device discovery process, you can remotely install agents on discovered Windows devices.

## Requirements on User Account Control (UAC)

On a machine that is running Windows 7 or later and is not a member of an Active Directory domain, centralized management operations (including remote installation) require that UAC and UAC remote restrictions be disabled.

### To disable UAC

- **In a Windows operating system prior to Windows 8:** Go to **Control panel** > **View by: Small icons** > **User Accounts** > **Change User Account Control Settings**, move the slider to **Never notify**, and restart the machine.
- **In any Windows operating system:** Open Registry Editor, locate `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System`, set the **EnableLUA** value to **0**, and restart the machine.

### To disable UAC remote restrictions

1. Open Registry Editor.
2. Locate `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`.
3. For **LocalAccountTokenFilterPolicy** value, change the setting to **1**. If the value does not exist, create it as DWORD (32-bit).

> **Note:** For security reasons, we recommend reverting both settings to their original state after finishing the management operation: **EnableLUA=1** and **LocalAccountTokenFilterPolicy=0**.

## Agent components

When you add multiple devices discovered by searching the Active Directory, you can select additional components to install.

| Component | Description |
|-----------|-------------|
| **Agent for Windows** | Mandatory. Backs up disks, volumes, files. Always installed, not selectable. |
| **Agent for Data Loss Prevention** | Limits user access to local and redirected peripheral devices, ports, and clipboard. Installed if selected. |
| **Antimalware and URL filtering** | Enables Antivirus & Antimalware protection and URL filtering module. Auto-installed later if any of these modules is enabled in a protection plan. |
| **Antimalware** | Enables Antivirus & Antimalware protection module. Auto-installed later if the module is enabled in a protection plan. |
| **Agent for Hyper-V** | Backs up Hyper-V virtual machines. Installed if selected and Hyper-V role detected. |
| **Agent for SQL** | Backs up SQL Server databases. Installed if selected and application detected. |
| **Agent for Exchange** | Backs up Exchange databases and mailboxes. Installed if selected and Mailbox role of Microsoft Exchange Server detected. |
| **Agent for Active Directory** | Backs up Active Directory Domain Services data. Installed if selected and application detected. |
| **Agent for VMware (Windows)** | Backs up VMware virtual machines on Windows machines with network access to vCenter Server. Installed if selected. |
| **Agent for Microsoft 365** | Backs up Microsoft 365 mailboxes to a local destination. Installed if selected. |
| **Agent for Oracle** | Backs up Oracle databases. Installed if selected. |
| **Cyber Protection Monitor** | Monitors execution of running tasks in the notification area. Supported on Windows 7 SP1+ and Windows Server 2008 R2 SP1+. |
| **Command-line tool** | Supports the `acrocmd` utility command-line interface. Does not contain tools that physically execute commands. |
| **Bootable Media Builder** | Creates bootable media. Supported on Windows and Linux. |

## Remote installation of agents

> **Note:** Remote installation of agents is supported for Windows devices only. Agent installation on multiple devices is only available for devices that are in the same network and discovered by the same discovery method.

The remote installation process:

1. The discovery agent connects to the target machines by using the host name, IP address, and administrator credentials, and uploads the `web_installer.exe` file.
2. The `web_installer.exe` runs on the target machines in unattended mode.
3. The web installer retrieves additional installation packages from the cloud, and installs them via the `msiexec` command.
4. After installation completes, the components are registered in the cloud.

> **Note:** Remote installation of agents is not supported for Domain Controllers, due to the additional permissions required for the agent service to run.

## Preparing machines for remote installation manually

- For Windows 7 or later: **Control panel** > **Folder options** > **View** > **Use Sharing Wizard** must be *disabled*.
- For machines that are *not* members of an Active Directory domain: User Account Control (UAC) must be *disabled*.
- By default, the credentials of the built-in administrator account are required. To use another administrator account, UAC remote restrictions must be *disabled*.
- File and Printer Sharing must be *enabled* on the remote machine.
- Cyber Protection uses TCP ports 445, 25001, and 43234 for remote installation. Port 445 opens with File and Printer Sharing. Ports 43234 and 25001 are automatically opened through Windows Firewall. After the remote installation is complete, port 25001 is automatically closed. Ports 445 and 43234 need to remain open if you want to update the agent remotely.

## Preparing machines for remote installation by using a GPO

You can configure and apply an Active Directory Group Policy object (GPO) to prepare a set of machines for remote installation of the Protection agents.

### Prerequisites

- Member of the Domain Admins group or a domain administrator.
- **Group Policy Management Console** (GPMC) is installed.

### To prepare machines for remote installation by using a GPO

1. Open GPMC: Press **Win + R**, type `gpmc.msc`, press **Enter**.
2. Right-click the domain or OU, and click **Create a GPO in this domain, and Link it here...**.
3. Name the GPO, then click **OK**.
4. Right-click the GPO, and click **Edit...**.
5. Disable **Use Sharing Wizard** by adding a registry item under **User Configuration** > **Preferences** > **Windows Settings** > **Registry**:
   - Hive: `HKEY_CURRENT_USER`, Key Path: `Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced`, Value name: `SharingWizardOn`, Value type: `REG_DWORD`, Value data: `0`
6. Disable User Account Control (UAC) by adding a registry item under **Computer Configuration** > **Preferences** > **Windows Settings** > **Registry**:
   - Hive: `HKEY_LOCAL_MACHINE`, Key path: `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\`, Value name: `EnableLUA`, Value type: `REG_DWORD`, Value Data: `0`
7. Disable UAC Remote restrictions:
   - Hive: `HKEY_LOCAL_MACHINE`, Key path: `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`, Value name: `LocalAccountTokenFilterPolicy`, Value type: `REG_DWORD`, Value Data: `1`
8. Enable **File and Printer Sharing** in the firewall (Inbound and Outbound Rules) via **Computer Configuration** > **Policies** > **Windows Settings** > **Security Settings** > **Windows Defender Firewall with Advanced Security**.
9. Link the GPO to the domain or OU.
10. On target machines, force the Group Policy Update:
    ```
    gpupdate /force
    ```

## Installing agents remotely

### Complete automatic onboarding via Active Directory

1. Go to **Devices** > **Discovered devices** > **Devices without agent**.
2. Select the devices to protect.
3. Click **Install agent**.
4. On the **Select onboarding option** tab, click **Complete automatic onboarding via Active Directory**.
5. Select the **Domain controller** and **Domain administrator credentials**.
7. Select machines to onboard and click **Next**.
8. On the **Select agent components** tab, select components to install, configure installation options (Service logon account, restart behavior), select a user account for registration.
9. (Optional) On the **Select plans** tab, select plans to apply to the machines.
10. Click **Next**.
11. On the **Review and register** screen, check quotas and click **Register**.

### Manual preconfiguration and automatic onboarding

1. Go to **Devices** > **Discovered devices** > **Devices without agent**.
2. Select the devices to protect.
3. Click **Install agent**.
4. On the **Select onboarding option** tab, click **Manual preconfiguration and automatic onboarding**, then click **Next**.
5. On the **Select agent components** tab, select the **Discovery agent**, components to install, and configure installation options.
6. (Optional) On the **Select plans** tab, select plans.
7. Click **Next**.
8. On the **Credentials** tab, add credentials with administrator rights to the selected devices.
9. On the **Connectivity** tab, resolve any connectivity issues or click **Next**.
10. On the **Review and register** screen, check quotas and click **Register**.

## Excluding devices from discovery

When you exclude devices from discovery, they will not be listed in the results of discovered devices when a device discovery scan is run.

1. In the Protection console, go to **Discovered devices**.
2. Click the device that you want to exclude, and then click **Exclude from discovery**. The device is excluded and added to the **Exclusions** page.
