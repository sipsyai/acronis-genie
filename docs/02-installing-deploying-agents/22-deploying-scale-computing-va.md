---
title: "Deploying Agent for Scale Computing HC3 (Virtual Appliance)"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying virtual appliances"
page_range: "135-139"
tags: ["Scale Computing", "HC3", "virtual appliance", "QCOW2", "deployment", "HyperCore", "required roles"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#deploying-agent-for-scale-computing-hc3-virtual-appliance.html"
---

# Deploying Agent for Scale Computing HC3 (Virtual Appliance)

## Before you start

This appliance is a pre-configured virtual machine that you deploy in a Scale Computing HC3 cluster. It contains a protection agent that enables you to administer cyber protection for all virtual machines in the cluster.

## System requirements for the agent

By default, the virtual machine with the agent uses 2 vCPUs and 4 GiB of RAM. These settings are sufficient for most operations but you can change them by editing the virtual machine in the Scale Computing HC3 web interface.

To improve backup performance and avoid failures related to insufficient RAM memory, we recommend increasing resources to 4 vCPUs and 8 GiB of RAM in more demanding cases -- for example, when backup traffic exceeds 100 MB per second (in 10-Gigabit networks) or if you simultaneously back up multiple virtual machines with large hard drives (500 GB or more).

The size of the appliance virtual disk is about 9 GB.

## How many agents do I need?

One agent can protect the entire cluster. However, you can have more than one agent in the cluster if you need to distribute the backup traffic bandwidth load.

If you have more than one agent in a cluster, the virtual machines are automatically evenly distributed between the agents, so that each agent manages a similar number of machines.

Automatic redistribution occurs when the load imbalance among the agents reaches 20 percent. This may happen after you add or remove a machine or an agent. The management server will assign the most appropriate machines to the new agent. The old agents' load will reduce. When you remove an agent from the management server, the machines assigned to the agent are redistributed among the remaining agents. However, this will not happen if an agent gets corrupted or is deleted manually from the Scale Computing HC3 cluster. Redistribution will start only after you remove such an agent from the Cyber Protect console.

### To check which agent manages a specific machine

1. In the Cyber Protect console, click **Devices**, and then select **Scale Computing**.
2. Click the gear icon in the upper right corner of the table, and under **System**, select the **Agent** check box.
3. Check the name of the agent in the column that appears.

## Deploying the QCOW2 template

1. Log in to your Cyber Protection account.
2. Click **Devices** > **All devices** > **Add** > **Scale Computing HyperCore**. The .zip archive is downloaded to your machine.
3. Unpack the .zip archive, and then save the .qcow2 file and the .xml file to a folder named **ScaleAppliance**.
4. Upload the **ScaleAppliance** folder to a network share and ensure that the Scale Computing HC3 cluster can access it.
5. Log in to the Scale Computing HC3 cluster as an administrator who has the **VM Create/Edit** role assigned.
6. In the Scale Computing HC3 web interface, import the virtual machine template from the **ScaleAppliance** folder.
   a. Click the **Import HC3 VM** icon.
   b. In the **Import HC3 VM** window, specify:
      - A name for the new virtual machine.
      - The network share on which the **ScaleAppliance** folder is located.
      - The user name and password required for accessing this network share.
      - (Optional) A domain tag for the new virtual machine.
      - The path to the **ScaleAppliance** folder on the network share.
   c. Click **Import**.

> **Note:** If you need more than one virtual appliance in your cluster, repeat the steps above and deploy additional virtual appliances. Do not clone an existing virtual appliance by using the **Clone VM** option in the Scale Computing HC3 web interface.

## Configuring the virtual appliance

After deploying the virtual appliance, you need to configure it so that it can reach both the Scale Computing HC3 cluster that it will protect and the Cyber Protection service.

1. Log in to your Scale Computing HC3 account.
2. Select the virtual appliance that you want to configure, and then click the **Console** icon.
3. In the **eth0** field, configure the network interfaces of the appliance. Ensure that automatically assigned DHCP addresses (if any) are valid within the networks that your virtual machine uses or assign them manually.
4. In the **Scale Computing** field, click **Change** to specify the Scale Computing HC3 cluster address and credentials for accessing it.
   a. In the **Server name/IP** field, enter the DNS name or IP address of the cluster.
   b. In the **User name** and **Password** fields, enter the credentials for the Scale Computing HC3 administrator account. Ensure that this account has the roles required for operations with Scale Computing HC3 virtual machines.
   c. Click **Check connection** to verify that the settings are correct.
   d. Click **OK**.
5. Register the appliance in the Cyber Protection service:
   - **Via the graphical interface:** Under **Agent options**, in the **Management Server** field, click **Change**. In the **Server name/IP** field, select **Cloud**. Enter your Cyber Protect credentials and (if 2FA is enabled) the TOTP code. Click **OK**.
   - **Via the command-line interface:** Press CTRL+SHIFT+F2, then run: `register_agent -o register -t cloud -a <service address> --token <registration token>`
6. (Optional) In the **Name** field, click **Change** to edit the default name for the virtual appliance (which is **localhost**).
7. (Optional) In the **Time** field, click **Change** to set the time zone for your location.
8. (Optional) Add local backup storage to the virtual appliance (minimum 10 GB disk).
9. (If a proxy server is enabled) Configure the proxy server via `/opt/acronis/etc/aakore.yaml`.

### To protect virtual machines in the Scale Computing HC3 cluster

1. Log in to your Cyber Protection account.
2. Navigate to **Devices** > **Scale Computing HyperCore** > <your cluster> or find your machines in **Devices** > **All devices**.
3. Select machines and apply a protection plan to them.

## Agent for Scale Computing HC3 -- required roles

| Operation | Role |
|-----------|------|
| Back up a virtual machine | Backup, VM Create/Edit, VM Delete |
| Recover to an existing virtual machine | Backup, VM Create/Edit, VM Power Control, VM Delete, Cluster Settings |
| Recover to a new virtual machine | Backup, VM Create/Edit, VM Power Control, VM Delete, Cluster Settings |
