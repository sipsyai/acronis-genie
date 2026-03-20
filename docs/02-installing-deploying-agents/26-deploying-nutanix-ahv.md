---
title: "Deploying Agent for Nutanix AHV"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying Agent for Nutanix AHV"
page_range: "162-167"
tags: ["Nutanix", "AHV", "virtual appliance", "QCOW2", "Prism Element", "deployment", "backup"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#deploying-agent-nutanix-ahv-virtual-appliance.html"
---

# Deploying Agent for Nutanix AHV

## Before you start

This appliance is a pre-configured virtual machine that you can deploy to a Nutanix cluster. The appliance contains a protection agent that can back up and recover the virtual machines in the cluster.

## System requirements for the virtual appliance

We recommend configuring the virtual appliance with 4 vCPUs (4 single-core vCPUs or 2 vCPUs with 2 cores each) and 8 GiB of RAM. These settings are sufficient for most operations.

To improve backup performance and avoid failures related to insufficient RAM memory, you can increase the RAM memory to 16 GiB in more demanding cases -- for example, when backup traffic exceeds 100 MB per second (in 10-Gigabit networks) or if you back up simultaneously multiple virtual machines with large hard drives (500 GiB or more).

The size of the appliance virtual disk is 8 GiB.

## How many virtual appliances do I need?

One virtual appliance can back up and recover all virtual machines in the cluster. You can use multiple virtual appliances per cluster if you want to distribute the bandwidth load of the backup traffic.

If more than one virtual appliance is deployed in the cluster, the automatic redistribution of the backed-up virtual machines occurs when the load imbalance among the appliances reaches 20 percent. Redistribution occurs only if you remove the virtual appliance from the Cyber Protect console. It will not start if you remove the virtual appliance from the Nutanix Prism Element console or if the appliance gets corrupted.

### Limitations

The following operations are not supported:

- Application-aware backup
- Running a virtual machine from a backup
- Replication of virtual machines
- Backups of Nutanix volume groups

## Deploying the QCOW2 template

You must deploy at least one virtual appliance per cluster.

1. Log in to the Cyber Protect console.
2. Click **Devices** > **All devices** > **Add** > **Nutanix AHV**. A ZIP archive is downloaded.
3. Unpack the ZIP archive and extract the QCOW2 image file.
4. Log in to the Nutanix Prism Element console as an administrator.
5. Upload the QCOW2 image file to the Nutanix Prism Element console.
   a. Go to **Settings** and then, under **General**, select **Image configuration**.
   b. Click **Upload image**.
   c. Specify a name for the image.
   d. In **Image Type**, select **Disk**.
   e. Click **Upload a file**, and then click **Choose file**.
   f. Select the QCOW2 image that you downloaded from the Cyber Protect console.
   g. Click **Save**.
6. In the Nutanix Prism Element console, create a new virtual machine by using the QCOW2 image.
   a. Go to **VM**, and then click **Create VM**.
   b. Specify a name for the virtual machine.
   c. In **Compute Details**, specify 4 vCPUs (single core) or 2 vCPUs with 2 cores each, and 8 GiB of memory.
   d. In **Disks**, click **Add New Disk**.
   e. In **Operation**, select **Clone from Image Service**.
   f. In **Image**, select the image that you uploaded to the Nutanix Prism Element console.
   g. Click **Add**.
   h. In **Network adapters (NIC)**, click **Add New NIC**.
   i. Configure the network settings, and then click **Add**.
   j. (Optional) To hide the virtual appliance in the Cyber Protect console, in **Description**, specify: `{AB53A0F1-AD54-480f-80BB-FC72DC41DF53}`
   k. Click **Save**.
7. On the **VM** > **Table tab**, right-click the virtual machine that you created, and then select **Power on**.

## Configuring the Nutanix virtual appliance

After deploying the virtual appliance, you must configure its access to the Nutanix cluster and the Cyber Protect console.

### Prerequisites

- You have deployed and powered on the Nutanix virtual appliance.

### To configure the Nutanix virtual appliance

1. Log in to the Nutanix Prism Element console as an administrator.
2. Go to **VM** > **Table**.
3. Right-click the virtual machine that you deployed, and then select **Launch Console**.
4. In the **eth0** field, configure the network interfaces of the appliance. Ensure DHCP addresses are valid or assign them manually.
5. Specify the IP address of the Nutanix cluster (Nutanix Prism Element) and credentials for accessing it.

> **Note:** You cannot configure Agent for Nutanix AHV with the IP address of Nutanix Prism Central. Even if you manage the cluster through Nutanix Prism Central, Agent for Nutanix AHV can only access it through Nutanix Prism Element.

   a. Under **Agent options**, in the **Nutanix** field, click **Change**.
   b. In the **Server name/IP** field, enter the IP address of the cluster.
   c. In the **User name** and **Password** fields, enter the credentials for a Nutanix administrator account. This account must have the **User Admin** and **Cluster Admin** roles in the Nutanix cluster.
   d. To verify that the settings are correct, click **Check connection**.
   e. Click **OK**.
6. Register the appliance in the Cyber Protection service (via GUI or command-line interface).
7. (Optional) Edit the default name for the virtual appliance (which is **localhost**).
8. (Optional) Configure the time zone of the virtual appliance.
9. (If a proxy server is enabled) Configure the proxy server via `/opt/acronis/etc/aakore.yaml`.

> **Note:** To update a virtual appliance deployed behind a proxy, edit the appliance `config.yaml` file (`/opt/acronis/etc/va-updater/config.yaml`), by adding: `httpProxy: http://<proxy_login>:<proxy_password>@<proxy_address>:<port>`

## Backing up Nutanix virtual machines

### Prerequisites

- You have deployed and configured the Nutanix virtual appliance.

### To protect Nutanix virtual machines

1. Log in to the Cyber Protect console.
2. Go to **Devices** > **Nutanix** > <your cluster>.
3. Select virtual machines and apply a protection plan to them.
