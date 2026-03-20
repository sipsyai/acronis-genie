---
title: "Device discovery overview and methods"
section: "Installing and deploying Cyber Protection agents"
subsection: "Device discovery"
page_range: "176-181"
tags: ["device discovery", "Active Directory", "manual discovery", "Device Sense", "network scan", "multiple devices"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#device-discovery.html"
---

# Device discovery overview and methods

By using the device discovery functionality, you can:

- Gain complete visibility of the network devices that are available in the organization's networks.
- Use synchronization with Active Directory to reduce the efforts for provisioning resources and managing machines in a large Active Directory domain.
- Automate the installation of protection agents and the registration of machines by detecting the machines in your Active Directory domain or local network.
- Install protection agents on multiple workloads.

## Discovery methods

You can use one of the following methods to perform device discovery:

- **Active Directory discovery** -- During an Active Directory discovery, the discovery agent collects information about the organizational unit (OU) of the machines and detailed information about their names and operating systems. However, the IP and MAC addresses are not collected.
- **Local network discovery by using Device Sense** -- Scans local corporate networks to discover physical and virtual machines, as well as network devices such as routers, switches, printers, smartphones, and IP cameras.
- **Manual discovery** -- By using a machine IP address or host name, or by importing a list of machines from a file. During a manual discovery, the existing protection agents are updated and re-registered.

## Discovering multiple devices

The flow of discovering multiple devices can be summarized in the following steps:

1. **Selecting the discovery method:**
   - Active Directory discovery -- By using a domain controller for the complete automated flow or a discovery agent for the flow with manual preconfiguration.
   - Local network discovery by using Device Sense.
   - Manual discovery -- By using a machine IP address or host name, or by importing a list of machines from a file.
2. (For Active Directory discovery with manual preconfiguration and Manual discovery) Selecting the machines that you want to add to your tenant.
3. Selecting how to add these machines:
   - Install a protection agent and additional components, and register them in the Cyber Protect console.
   - Register the machines in the Cyber Protect console (if a protection agent was already installed).
   - Add the machines to the Cyber Protect console as unmanaged devices, without installing a protection agent.
   You can also apply a protection plan, monitoring plan, and a remote management plan to machines on which you install a protection agent or which you register.
4. (For Active Directory discovery with manual preconfiguration and Manual discovery) Providing administrator credentials for the selected machines.
5. Verifying that you can connect to the machines by using the provided credentials.

## Device categories in the Cyber Protect console

- **Discovered devices** -- Machines that are discovered, but a protection agent is not installed on them.
- **Machines with agents** -- Machines on which a protection agent is installed.
- **Discovered devices / Devices without agent** -- Machines on which a protection agent can be installed.
- **Discovered devices / Local network** -- Machines and network devices discovered by scanning local networks using Device Sense.
- **Discovered devices / Active Directory** -- Machines discovered by searching the Active Directory.
- **Discovered devices / Manual / From text file** -- Machines that were added manually or from a text file.

## Device discovery requirements

Before using the device discovery functionality, ensure that the following requirements are met:

- For the **Complete automatic onboarding via Active Directory** flow, at least one domain controller with an installed protection agent must be available in your local network or Active directory domain.
- For the **Manual preconfiguration and automatic onboarding** flow, at least one machine with an installed protection agent must be available in your local network or Active directory domain. This agent will be used as a discovery agent.
- You must be assigned one of the following roles for the Cyber Protection service: Cyber administrator or Administrator.

> **Important:** Only agents that are installed on Windows machines can be discovery agents. If there are no discovery agents in your environment, you will not be able to use the **Multiple devices** option in the **Add devices** panel.

Remote installation of agents is supported only for machines running Windows (Windows XP is not supported). For remote installation on a machine running Windows Server 2012 R2, you must have Windows update KB2999226 installed.

## Adding multiple devices

### Search Active Directory

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Click **Add**.
3. In **Multiple devices**, click **Discover devices**. The discovery wizard opens.
4. Select the discovery agent that will perform the scan to detect machines.
5. Select **Search Active Directory**, and then click **Next**.
6. In the **Search Active Directory** window, select how to search for the machines:

| Option | Description |
|--------|-------------|
| **In organizational unit list** | Select the group of machines to be added. |
| **By LDAP dialect query** | Use the LDAP dialect query to select the machines. **Search base** defines where to search, while **Filter** allows you to specify the criteria for machine selection. |

7. In the list of discovered machines, select the machines that you want to add, and then click **Next**. The **Select onboarding option** tab opens with available options.

| Option | Description |
|--------|-------------|
| **Complete automatic onboarding via Active Directory** | Uses a domain controller with a discovery agent installed to onboard discovered devices from Active Directory. No manual preconfiguration required. |
| **Manual preconfiguration and automatic onboarding** | Requires manual preconfiguration of the devices and uses a discovery agent to onboard discovered devices. |
| **Add as unmanaged machines** | Adds the discovered devices to the console as unmanaged devices, without installing a protection agent on them. |

8. Depending on the onboarding option, follow the corresponding procedure steps.

### Scan local network

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Click **Add**.
3. In **Multiple devices**, click **Discover devices**.
4. Click **Scan**. The active device discovery scan starts. You are redirected to the **Discovered devices** > **Local Area Network** screen. When the scan completes, a notification shows the number of devices discovered with a link to view additional details.

### Manually or by importing a file

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Click **Add**.
3. In **Multiple devices**, click **Discover devices**.
4. Click **Specify manually or import from file**.
5. Add machines using one of the following options:
   - **To add machines manually:** In the **Add machine** field, enter the IPv4 address or hostname. Repeat for each machine.
   - **To add machines by importing a file:** Click **Import machine list from file**. Drop the text file or click **Browse** to select it. The file must contain IP addresses or hostnames, one per line.

Example file content:
```
156.85.34.10
156.85.53.32
156.85.53.12
EN-L00000100
EN-L00000101
```

6. Click **Next** and select the onboarding option. Follow the corresponding procedure steps.
