# Preparation

Installing and deploying Cyber Protection agents > Before you start > Preparation
Preparation
Step 1

Choose an agent, depending on what you are going to back up. For more information on the possible choices, refer to Which agent do I need?

Step 2

Ensure that there is enough free space on your hard drive to install an agent. For detailed information about the required space, refer to System requirements for agents.

Step 3

Download the setup program. To find the download links, click All devices > Add.

The Add devices page provides web installers for each agent that is installed in Windows. A web installer is a small executable file that downloads the main setup program from the Internet and saves it as a temporary file. This file is deleted immediately after the installation.

If you want to store the setup programs locally, download a package containing all agents for installation in Windows by using the link at the bottom of the Add devices page. Both 32-bit and 64-bit packages are available. These packages enable you to customize the list of components to install. These packages also enable unattended installation, for example, via Group Policy. This advanced scenario is described in Deploying protection agents through Group Policy.

To download the setup program for Agent for Microsoft 365, click the account icon in the top-right corner, and then click Downloads > Agent for Microsoft 365.

Installation in Linux and macOS is performed from ordinary setup programs.

All setup programs require an Internet connection to register the machine in the Cyber Protection service. If there is no Internet connection, the installation will fail.

Step 4

Cyber Protect features require Microsoft Visual C++ 2017 Redistributable. Please ensure that it is already installed on your machine or install it before installing the agent. After the installation of Microsoft Visual C++, a restart may be required. You can find the Microsoft Visual C++ Redistributable package here https://support.microsoft.com/help/2999226/update-for-universal-c-runtime-in-windows.

Step 5

Verify that your firewalls and other components of your network security system (such as a proxy server) allow outbound connections through the following TCP ports.

Ports 443 and 8443

These ports are used for accessing the Cyber Protect console, registering the agents, downloading the certificates, user authorization, and downloading files from the cloud storage.

Ports in the range 7770 – 7800

The agents use these ports to communicate with the management server.

Port 44445

The agents use this port for data transfer during backup and recovery.

If a proxy server is enabled in your network, see Configuring proxy server settings to understand whether you need to configure these settings on each machine that runs a protection agent.

The minimum Internet connection speed required for managing an agent from the cloud is 1 Mbit/s (not to be confused with the data transfer rate acceptable for backing up to the cloud). Consider this if you use a low-bandwidth connection technology such as ADSL.

TCP ports required for backup and replication of VMware virtual machines

Port 443

Agent for VMware (both Windows and Virtual Appliance) connects to this port on the ESXi host/vCenter server to perform VM management operations, such as create, update, and delete VMs on vSphere during backup, recovery, and VM replication operations.

Port 902

Agent for VMware (both Windows and Virtual Appliance) connects to this port on the ESXi host to establish NFC connections to read/write data on VM disks during backup, recovery, and VM replication operations.

Port 2029

Agent for VMware (Virtual Appliance) listens on this port for incoming requests to the NFS server, which is hosted on the agent. Connections via this port are required for running a virtual machine from a backup (Instant Restore).

Port 3333

If the Agent for VMware (Virtual Appliance) is running on the ESXi host/cluster that is the target for VM replication, VM replication traffic does not go directly to the ESXi host on port 902. Instead, the traffic goes from the source Agent for VMware to TCP port 3333 on the Agent for VMware (Virtual Appliance) located on the target ESXi host/cluster.

The source Agent for VMware that reads data from the original VM disks can be anywhere else and can be of any type: Virtual Appliance or Windows.

The service that is responsible for accepting VM replication data on the target Agent for VMware (Virtual Appliance) is called “Replica disk server.” This service is responsible for the WAN optimization techniques, such as traffic compression and deduplication during VM replication, including replica seeding (see Seeding an initial replica). When no Agent for VMware (Virtual Appliance) is running on the target ESXi host, this service is not available, and therefore the replica seeding scenario is not supported.

Ports required by the Downloader component

The Downloader component is responsible for delivering updates to a computer and distributing them to other Downloader instances. It can run in agent mode which turns its computer into Downloader agent. The Downloader agent downloads updates from the internet and serves as the source of updates distribution to other computers. The Downloader requires the following ports to operate.

TCP and UDP (incoming) port 6888

Used by the BitTorrent protocol for torrent peer-to-peer updates.

UDP port 6771

Used as the local peer discovery port. Also takes part in peer-to-peer updates.

TCP port 18018

Used for communication between updaters working in different modes: Updater and UpdaterAgent.

TCP port 18019

Local port, used for communication between the Updater and the protection agent.

Step 6

On the machine where you plan to install the protection agent, verify that the following local ports are not in use by other processes.

127.0.0.1:9999
127.0.0.1:43234
127.0.0.1:9850

You do not have to open them in the firewall.

Changing the ports used by the protection agent

Some of the ports required by the protection agent might be in use by other applications in your environment. To avoid conflicts, you can change the default ports used by the protection agent by modifying the following files.

In Linux: /opt/Acronis/etc/aakore.yaml
In Windows: \ProgramData\Acronis\Agent\etc\aakore.yaml
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.