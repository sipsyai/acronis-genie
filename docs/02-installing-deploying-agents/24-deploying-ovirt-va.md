---
title: "Deploying Agent for oVirt (Virtual Appliance)"
section: "Installing and deploying Cyber Protection agents"
subsection: "Deploying virtual appliances"
page_range: "151-157"
tags: ["oVirt", "Red Hat Virtualization", "virtual appliance", "OVA", "deployment", "required roles", "required ports"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#deploying-agent-ovirt-virtual-appliance.html"
---

# Deploying Agent for oVirt (Virtual Appliance)

## Before you start

This appliance is a preconfigured virtual machine that you deploy in a Red Hat Virtualization/oVirt environment. The appliance contains a protection agent that can back up and recover the virtual machines in the environment.

## System requirements for the agent

By default, the virtual appliance uses 2 vCPUs and 4 GiB of RAM. These settings are sufficient for most operations. To improve backup performance, increase the number of vCPUs to four, and the RAM to 8 GiB in more demanding cases.

The size of the appliance virtual disk is 8 GiB.

## How many agents do I need?

One virtual appliance can back up and recover all virtual machines in the environment. You can use multiple virtual appliances if you want to distribute the bandwidth load of the backup traffic.

If more than one virtual appliance is deployed, the automatic redistribution of the backed-up virtual machines occurs when the load imbalance among the appliances reaches 20 percent. Redistribution occurs only if you remove the virtual appliance from the Cyber Protect console. It will not start if you remove the virtual appliance from the Red Hat Virtualization/oVirt Administration Portal or if the appliance gets corrupted.

### Limitations

The following operations are not supported for Red Hat Virtualization/oVirt virtual machines:

- Application-aware backup
- Running a virtual machine from a backup
- Replication of virtual machines
- Changed block tracking

## Deploying the OVA template

1. Log in to the Cyber Protect console.
2. Click **Devices** > **All devices** > **Add** > **Red Hat Virtualization (oVirt)**. A ZIP archive is downloaded.
3. Unpack the ZIP archive and extract the OVA image file.
4. Upload the OVA file to a host in the Red Hat Virtualization/oVirt environment that you want to protect.
5. Log in to Red Hat Virtualization/oVirt Administration Portal as an administrator.
6. From the navigation menu, select **Compute** > **Virtual machines**.
7. Click the vertical ellipsis icon above the main table, and then click **Import**.
8. In the **Import Virtual Machine(s)** window:
   a. In **Data center**, select the data center that you want to protect.
   b. In **Source**, select **Virtual Appliance (OVA)**.
   c. In **Host**, select the host on which you uploaded the OVA file.
   d. In **File Path**, specify the path to the directory that contains the OVA file.
   e. Click **Load**.
   f. In **Virtual Machines on Source**, select the oVirt virtual appliance template, and then click the right arrow.
   g. Click **Next**.
9. In the new window, click the appliance name, and then configure:
   - On the **Network interfaces** tab, configure the network interfaces.
   - On the **General** tab, change the default name of the virtual machine with the agent.
10. (Optional) To hide the virtual appliance in the Cyber Protect console, assign the tag `acronis_virtual_appliance` to the virtual appliance.

> **Note:** If you use an oVirt virtual appliance with Oracle Linux Virtualization Manager, you might receive the error: "VM <name> is down with error. Exit message: unsupported configuration: domain configuration does not support video model 'qxl'." To resolve this error, change the graphics adapter to **CIRRUS**.

## Configuring the virtual appliance

1. Log in to Red Hat Virtualization/oVirt Administration Portal.
2. Select the virtual appliance that you want to configure, and then click the **Console** icon.
3. In the **eth0** field, configure the network interfaces of the appliance. Ensure that automatically assigned DHCP addresses are valid or assign them manually.
4. In the **oVirt** field, click **Change** to specify the oVirt Engine address and credentials:
   a. In the **Server name/IP** field, enter the DNS name or IP address of the engine.
   b. In the **User name** and **Password** fields, enter the administrator credentials. Ensure that this administrator account has the roles required for operations with Red Hat Virtualization/oVirt virtual machines. If Keycloak is the Single-Sign-On (SSO) provider for the oVirt Engine (default in oVirt 4.5.1), use the Keycloak format (e.g., `admin@ovirt@internalsso` instead of `admin@internal`).
   c. (Optional) Click **Check connection** to verify the credentials.
   d. Click **OK**.
5. Register the appliance in the Cyber Protection service (via GUI or command-line interface).
6. (Optional) In the **Name** field, click **Change** to edit the default name (which is **localhost**).
7. (Optional) In the **Time** field, click **Change** to set the time zone.
8. (Optional) Configure the proxy server if enabled in your network.

## Changing the graphics adapter of a virtual appliance

If you receive the unsupported video model 'qxl' error, change the graphics adapter to **CIRRUS**:

1. Log in to Oracle Linux Administration Portal as an administrator.
2. Go to **Compute** > **Virtual machines**.
3. (If powered on) Right-click the virtual appliance and select **Shutdown**.
4. Right-click the virtual appliance and select **Edit**.
5. (If you see only the **General** tab) Click **Show Advanced Options**.
6. Click **Console**.
7. In **Graphical Console**, for **Video Type**, select **CIRRUS**.
8. Click **OK**.
9. Power on the virtual appliance.

## Agent for oVirt -- required roles and ports

### Required roles

**oVirt/Red Hat Virtualization 4.2 and 4.3/Oracle Virtualization Manager 4.3:**
- DiskCreator
- UserVmManager
- TagManager
- UserVmRunTimeManager
- VmCreator

**oVirt/Red Hat Virtualization 4.4, 4.5:**
- SuperUser

### Required ports

Agent for oVirt connects to the oVirt Engine by using the URL that you specify when you configure the virtual appliance. Usually, the engine URL has the format: `https://ovirt.company.com` (HTTPS, port 443).

| oVirt Engine URL | Port | Protocol |
|------------------|------|----------|
| `https://ovirt.company.com/` | 443 | HTTPS |
| `http://ovirt.company.com/` | 80 | HTTP |
| `https://ovirt.company.com:1234/` | 1234 | HTTPS |

No additional ports are required for disk Read/Write operations, because the backup is performed in the HotAdd mode.
