---
title: "Installing and uninstalling protection agents in macOS via CLI"
section: "Installing and deploying Cyber Protection agents"
subsection: "Installing and uninstalling protection agents by using the command-line interface"
page_range: "94-105"
tags: ["installation", "CLI", "command-line", "macOS", "unattended", "PPPC", "permissions", "kernel-extensions"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#unattended-installation-and-uninstallation-in-macos.html"
---

# Installing and uninstalling protection agents in macOS via CLI

This section describes how to install and uninstall the protection agent in the unattended mode on a machine running macOS, by using the command line.

## Required permissions

Before you initiate an unattended installation on a Mac workload, you must modify the Privacy Preferences Policy Control to allow App access and kernel and system extensions in the macOS of the workload to enable the installation of the Cyber Protection agent. You can do this by deploying a custom PPPC payload or by configuring the preferences in the graphical user interface of the workload.

### Requirements for macOS 11 (Big Sur) or later

The following permissions must be configured in Privacy Preferences Policy Control:

**App Access entries** (all require `SystemPolicyAllFiles` service and `Allow` access):

| Identifier | Identifier Type |
|------------|----------------|
| `com.acronis.backup` | Bundle ID |
| `com.acronis.backup.aakore` | Bundle ID |
| `com.acronis.backup.activeprotection` | Bundle ID |
| `cyber-protect-service` | Bundle ID |

**System Extensions:**
- Allow users to approve system extensions: Enabled
- Display Name: Acronis Cyber Protection Agent System Extensions
- System Extension Types: Allowed Team Identifiers
- Team Identifier: `ZU2TV78AA6`

### Requirements for macOS versions prior to version 11

**App Access entries** (same as above) plus:

**Approved Kernel Extensions:**
- Allow users to approve kernel extensions: Enabled
- Allow standard users to approve legacy kernel extensions (macOS 11 or later): Enabled
- Approved Team ID - Display Name: Acronis Cyber Protection Agent Kernel Extensions
- Team ID: `ZU2TV78AA6`
- Kernel Extension Bundle IDs:
  - `com.acronis.systeminterceptors`
  - `com.acronis.ngscan`
  - `com.acronis.notifyframework`

**System Extensions:** (same as macOS 11+)

## To download the installation file (.dmg)

1. Log in to the Cyber Protect console.
2. [To download the web installer for Mac] Click the account icon in the upper-right corner > **Downloads**, and then click **Agent for Mac OS**. Alternatively, go to **Devices** > **All devices**, click **Add**, and then click **Mac**.
3. [To download the full installer for Mac] Click the account icon in the upper-right corner > **Downloads**, and then click **Agent for Mac OS (64-bit)** or **Agent for Mac OS (ARM)**, according to your needs.

## To install an agent

1. Open Terminal.
2. Create a temporary directory where you will mount the installation file (.dmg).

   ```
   mkdir <dmg_root>
   ```

3. Mount the .dmg file.

   ```
   hdiutil attach <dmg_file> -mountpoint <dmg_root>
   ```

4. Run the installer.
   - If you use a full installer for Mac:

     ```
     sudo installer -pkg <dmg_root>/Install.pkg -target LocalSystem
     ```

   - If you use a web installer for Mac:

     ```
     sudo <dmg_root>/Install.app/Contents/MacOS/cyber_installer -a
     ```

5. Detach the installation file (.dmg).

   ```
   hdiutil detach <dmg_root>
   ```

### Example

```
mkdir mydirectory
hdiutil attach /Users/JohnDoe/Cyber_Protection_Agent_for_MAC_x64.dmg -mountpoint mydirectory
sudo installer -pkg mydirectory/Install.pkg -target LocalSystem
hdiutil detach mydirectory
```

## To uninstall an agent

1. Open Terminal.
2. Do one of the following:
   - To uninstall the agent:

     ```
     sudo /Library/Application\ Support/BackupClient/Acronis/Cyber\ Protect\ Agent\ Uninstall.app/Contents/MacOS/AgentUninstall /confirm
     ```

   - To uninstall the agent and remove all logs, tasks and configuration settings:

     ```
     sudo /Library/Application\ Support/BackupClient/Acronis/Cyber\ Protect\ Agent\ Uninstall.app/Contents/MacOS/AgentUninstall /confirm /purge
     ```

## Troubleshooting permission issues on macOS

The 'System Extension Blocked' message might appear during the installation of Agent for macOS on the screen of the protected Mac machine. The following procedures are performed on the protected machine.

### To approve the Acronis Cyber Protection Agent system extension

1. Click **Open System Settings**. If you dismiss the dialog accidentally, you can access the **System Settings/Preferences** from the **Apple** menu.
2. Navigate to **Privacy & Security**.
3. Scroll down to find the message indicating the system extension was blocked.
4. Click the **Allow** button next to the blocked extension.
5. Restart the Mac machine for the changes to take effect.

> **Note:** If the **Allow** button does not appear, you might need to adjust the security settings in recovery mode.

### To adjust the security settings in recovery mode

1. Shut down the Mac.
2. Press and hold the power button until you see the startup options.
3. Click **Options** and then continue to the next screen.
4. From the **Utilities** menu, select **Startup Security Utility**.
5. In the Startup Security Utility, click the **Security Policy** button.
6. Select **Reduce Security** and then select the check box **Allow user management of kernel extensions from identified developers**.
7. Click **OK**, enter your administrator password, and wait for the changes to be applied.
8. In the menu bar, click **Startup Disk**, and then click **Quit Startup Disk**.
9. Click the Apple icon and select **Restart**.
