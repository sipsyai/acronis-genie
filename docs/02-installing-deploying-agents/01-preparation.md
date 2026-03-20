---
title: "Preparation - Before you start"
section: "Installing and deploying Cyber Protection agents"
subsection: "Before you start"
page_range: "36-38"
tags: ["installation", "preparation", "ports", "firewall", "network", "requirements", "prerequisites"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#preparation.html"
---

# Before you start - Preparation

## Step 1 - Choose an agent

Choose an agent, depending on what you are going to back up. For more information on the possible choices, refer to [Which agent do I need?](./03-which-agent-do-i-need.md).

## Step 2 - Check disk space

Ensure that there is enough free space on your hard drive to install an agent. For detailed information about the required space, refer to [System requirements for agents](./04-system-requirements.md).

## Step 3 - Download the setup program

To find the download links, click **All devices** > **Add**.

The **Add devices** page provides web installers for each agent that is installed in Windows. A web installer is a small executable file that downloads the main setup program from the Internet and saves it as a temporary file. This file is deleted immediately after the installation.

If you want to store the setup programs locally, download a package containing all agents for installation in Windows by using the link at the bottom of the **Add devices** page. Both 32-bit and 64-bit packages are available. These packages enable you to customize the list of components to install. These packages also enable unattended installation, for example, via Group Policy. See [Deploying protection agents through Group Policy](./25-deploying-group-policy.md).

To download the setup program for Agent for Microsoft 365, click the account icon in the top-right corner, and then click **Downloads** > **Agent for Microsoft 365**.

Installation in Linux and macOS is performed from ordinary setup programs.

All setup programs require an Internet connection to register the machine in the Cyber Protection service. If there is no Internet connection, the installation will fail.

## Step 4 - Install prerequisites

Cyber Protect features require Microsoft Visual C++ 2017 Redistributable. Please ensure that it is already installed on your machine or install it before installing the agent. After the installation of Microsoft Visual C++, a restart may be required.

## Step 5 - Configure firewall ports

Verify that your firewalls and other components of your network security system (such as a proxy server) allow outbound connections through the following TCP ports:

| Port(s) | Purpose |
|---------|---------|
| **443** and **8443** | Accessing the Cyber Protect console, registering the agents, downloading the certificates, user authorization, and downloading files from the cloud storage. |
| **7770 – 7800** | Agent communication with the management server. |
| **44445** | Data transfer during backup and recovery. |

### TCP ports required for backup and replication of VMware virtual machines

| Port | Purpose |
|------|---------|
| **443** | Agent for VMware connects to ESXi host/vCenter server for VM management operations (create, update, delete VMs on vSphere), backup, recovery, and VM replication. |
| **902** | Agent for VMware connects to ESXi host for NFC connections to read/write data on VM disks during backup, recovery, and VM replication. |
| **2029** | Agent for VMware (Virtual Appliance) listens for incoming requests to the NFS server for running a VM from a backup (Instant Restore). |
| **3333** | If Agent for VMware (VA) is on the target ESXi host/cluster for VM replication, traffic goes to TCP port 3333 on the target VA instead of port 902 on ESXi. The service is called "Replica disk server" and handles WAN optimization. |

### Ports required by the Downloader component

The Downloader component delivers updates and distributes them via peer-to-peer:

| Port | Protocol | Purpose |
|------|----------|---------|
| **6888** | TCP and UDP (incoming) | BitTorrent protocol for torrent peer-to-peer updates. |
| **6771** | UDP | Local peer discovery port; also used for peer-to-peer updates. |
| **18018** | TCP | Communication between updaters (Updater and UpdaterAgent). |
| **18019** | TCP | Local port for communication between the Updater and the protection agent. |

## Step 6 - Check local ports

On the machine where you plan to install the protection agent, verify that the following local ports are not in use by other processes:

- 127.0.0.1:**9999**
- 127.0.0.1:**43234**
- 127.0.0.1:**9850**

> **Note:** You do not have to open them in the firewall.

### Changing the ports used by the protection agent

To avoid port conflicts, you can change the default ports by modifying the following files:

- In Linux: `/opt/Acronis/etc/aakore.yaml`
- In Windows: `\ProgramData\Acronis\Agent\etc\aakore.yaml`
