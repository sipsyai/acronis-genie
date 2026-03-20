---
title: "Deploying Agent for Synology"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying Agent for Synology"
page_range: "167-175"
tags: ["Synology", "NAS", "agent", "SPK", "DiskStation Manager", "backup", "installation", "update"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#deploying-agent-synology.html"
---

# Deploying Agent for Synology

## Before you start

With Agent for Synology, you can back up files and folders from and to Synology NAS devices. The NAS-specific properties and access permissions for shares, folders, and files are preserved.

Agent for Synology runs on the NAS device. Thus, you can use the resources of the device for off-host data processing operations, such as backup replication, validation, and cleanup.

> **Note:** Agent for Synology supports only NAS devices with x86_64 processors. ARM processors are not supported.

You can recover a backup to the original or a new location on the NAS device, and to a network folder that is accessible through that device. Backups in the cloud storage can also be recovered to a non-original NAS device on which Agent for Synology is installed.

## Backup sources and destinations

| What to backup | Items to backup (Backup source) | Where to backup (Backup destination) |
|----------------|-------------------------------|-------------------------------------|
| Files/folders | Local folder* | Cloud storage |
| | | Local folder* |
| | Network folder (SMB)** | Network folder (SMB)** |
| | | NFS folder |
| | | Public clouds*** |

\* Including USB drives that are attached to the NAS device.

> **Note:** Encrypted folders are not supported. These folders are not shown in the Cyber Protection graphical user interface.

\*\* Using external network shares as backup source or backup destination via the SMB protocol is only available for agents running on Synology DiskStation Manager 6.2.3 and later. The data hosted on the Synology NAS itself, including in hosted network shares, can be backed up without limitations.

\*\*\* Backup to public clouds, such as Microsoft Azure, Amazon, or S3-compatible storages, is supported only by Agent for Synology 7.x. Agent for Synology 6.x does not support this backup destination due to limitations of the Linux kernel of Synology DSM 6.x.

## Limitations

- Agent for Synology supports only NAS devices with x86_64 processors. ARM processors are not supported.
- Backed-up encrypted shares are recovered as non-encrypted.
- Backed-up shares for which the **File compression** option is enabled are recovered with this option disabled.
- You can recover to a Synology NAS device only backups that are created by Agent for Synology.

## Downloading the setup program

The setup program for Agent for Synology is available as an SPK file.

### Agent for Synology 7.x

1. In the Cyber Protect console, navigate to **Devices** > **All devices**.
2. In the upper-right corner, click **Add**.
3. Under **Network attached storage (NAS)**, click **Synology**. The setup program is downloaded to your machine.

### Agent for Synology 6.x

1. In the Cyber Protect console, navigate to **Devices** > **All devices**.
2. In the upper-right corner, click **Add**.
3. Under **Network attached storage (NAS)**, click **Synology**. The setup program for Agent for Synology 7.x is downloaded.
4. Click **Download Agent for Synology 6.x**. The setup program for Agent for Synology 6.x is downloaded.

## Installing Agent for Synology

### Agent for Synology 7.x

**Prerequisites:**

- The NAS device runs DiskStation Manager 7.x.
- You are a member of the **administrators** group on the NAS device.
- There are at least 200 MB of free space on the NAS volume on which you want to install the agent.
- An SSH client is available on your machine (e.g., Putty).

**Limitations:** You cannot register Agent for Synology via QuickConnect. To register the agent, access the NAS device directly.

**To install Agent for Synology:**

1. Log in to Synology DiskStation Manager.
2. Open **Package Center**.
3. Click **Manual Install**, and then click **Browse**.
4. Select the SPK file that you downloaded from the Cyber Protect console, and then click **Next**. A warning that you will install a third-party software package is shown.
5. To confirm, click **Agree**.
6. Select the volume on which you want to install the agent, and then click **Next**.
7. Check the settings, and then click **Done**.
8. In Synology DiskStation Manager **Package Center**, open Cyber Protect Agent for Synology, and verify that it is running.
9. In Synology DiskStation Manager **Control Panel**, go to **Terminal & SNMP**, and then enable the SSH access to the NAS device.
10. Run the `install` script on the NAS device by using an SSH client (e.g., Putty).
    a. Start Putty, and specify the IP address or host name of your Synology NAS device.
    b. Click **Open**, and then log in as a Synology DSM administrator.
    c. Run the following command:
       ```
       sudo /var/packages/CyberProtectAgent/target/install/install
       ```
       After the script starts, wait for 15 seconds during which the Cyber Protection services initialize.
11. In Synology DiskStation Manager **Control Panel**, go to **Terminal & SNMP**, and then disable the SSH access.
12. In Synology DiskStation Manager **Package Center**, open Cyber Protect Agent for Synology.
13. Select the registration method.
    - **To register by using credentials:** In the **User name** and **Password** fields, specify credentials for the account under which the agent will be registered. This account cannot be a partner administrator account.
    - **To register by using a registration token:** In **Registration address**, specify the exact data center address (e.g., `https://us5.acronis.cloud`). In the **Token** field, specify the registration token.

    > **Note:** Do not use a URL format without the data center address. For example, do not use `https://acronis.cloud`.

14. Click **Register**.

### Agent for Synology 6.x

**Prerequisites:**

- The NAS device runs DiskStation Manager 6.2.x.
- You are a member of the **administrators** group on the NAS device.
- There are at least 200 MB of free space on the NAS volume.

**To install Agent for Synology:**

1. Log in to Synology DiskStation Manager.
2. Open **Package Center**.
3. Click **Manual Install**, and then click **Browse**.
4. Select the SPK file that you downloaded from the Cyber Protect console, and then click **Next**. A warning about installing a package without a digital signature is shown.
5. To confirm, click **Yes**.
6. Select the volume on which you want to install the agent, and then click **Next**.
7. Check the settings, and then click **Apply**.
8. In Synology DiskStation Manager **Package Center**, open Cyber Protect Agent for Synology.
9. Select the registration method (credentials or registration token).
10. Click **Register**.

When the registration completes, the Synology NAS device appears in the Cyber Protect console, on the **Devices** > **Network Attached Storage** tab.

## Updating Agent for Synology

You can update Agent for Synology 6.x to a newer version of Agent for Synology 6.x. Similarly, you can update Agent for Synology 7.x to a newer version of Agent for Synology 7.x. To update the agent, run the newer version of the setup program in Synology DiskStation Manager. The original registration, settings, and plans applied to protected workloads will be preserved.

> **Note:** You cannot update the agent from the Cyber Protect console.

Upgrading Agent for Synology 6.x to Agent for Synology 7.x is supported only by uninstalling the older agent and installing the newer agent. In this case, all protection plans are revoked and you must re-apply them manually.

### Agent for Synology 7.x update

**Prerequisites:**

- You are a member of the **administrators** group on the NAS device.
- At least 200 MB of free space on the NAS volume.
- An SSH client is available.

1. In DiskStation Manager, open **Package Center**.
2. Click **Manual Install**, and then click **Browse**.
3. Select the newer SPK file for Agent for Synology 7.x that you downloaded.
4. To confirm, click **Agree**.
5. Check the settings, and then click **Done**.
6. In **Package Center**, open Cyber Protect Agent for Synology and verify it is running.
7. In **Control Panel**, go to **Terminal & SNMP**, and enable SSH access.
8. Run the `install` script via SSH:
   ```
   sudo /var/packages/CyberProtectAgent/target/install/install
   ```
9. In **Control Panel**, go to **Terminal & SNMP**, and disable SSH access.

### Agent for Synology 6.x update

1. In DiskStation Manager, open **Package Center**.
2. Click **Manual Install**, and then click **Browse**.
3. Select the newer SPK file for Agent for Synology 6.x.
4. To confirm, click **Yes**.
5. Check the settings, and then click **Apply**.

## SSH connections to a virtual appliance

Use a Secure Socket Shell (SSH) connection when you need to remotely access a virtual appliance for maintenance purposes.

### Starting the Secure Shell daemon

1. In the hypervisor software, open the console of the virtual appliance.
2. In the graphical user interface, press CTRL+SHIFT+F2 to open the command-line interface.
3. Run: `/bin/sshd`
4. (Only during the first connection) Set the password for the `root` user.

> **Note:** We recommend that you stop the Secure Shell daemon when you do not use the SSH connection.

### Setting the root password on a virtual appliance

1. Open the console of the virtual appliance.
2. Press CTRL+SHIFT+F2 to open the command-line interface.
3. Run: `passwd`
4. Specify a password (at least nine characters, complexity score of three or more -- use special symbols, uppercase and lowercase symbols, and digits).
5. Confirm the password.

### Accessing a virtual appliance via an SSH client

1. On the remote machine, open WinSCP (or another SSH client).
2. Click **Session** > **New Session**.
3. In **File protocol**, select **SCP**.
4. In **Host name**, specify the IP address of the virtual appliance.
5. In **User name** and **Password**, specify `root` and the password for the root user.
6. Click **Login**.
