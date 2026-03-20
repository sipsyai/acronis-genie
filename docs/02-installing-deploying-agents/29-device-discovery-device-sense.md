---
title: "Device discovery by using Device Sense"
section: "Installing and deploying Cyber Protection agents"
subsection: "Device discovery by using Device Sense"
page_range: "184-190"
tags: ["Device Sense", "passive discovery", "active discovery", "network scan", "ports", "device information", "filters"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#device-discovery-device-sense.html"
---

# Device discovery by using Device Sense

Device Sense uses a sophisticated combination of techniques to scan the local networks of organizations to discover and identify devices. In addition to discovering physical and virtual machines and tablets, Device Sense also discovers other network devices, such as routers, switches, printers, smartphones, and IP cameras.

## Benefits of Device Sense

- **Comprehensive network visibility** -- Identification of every device connected to a client's network, helping maintain accurate asset inventory for asset tracking and lifecycle management, and ensuring compliance with licensing agreements.
- **Security and compliance** -- Detection of unauthorized or rogue devices that could pose security risks. Device Sense helps you ensure each device complies with security policies and regulatory requirements.
- **Efficient allocation of resources** -- Understanding of the scope and scale of a client's network, enabling more efficient resource allocation and better service planning.

## Device Sense features

- Automatic smart selection of discovery agents and networks to scan
- Prevention of device discovery in home or non-corporate networks
- On-demand active device discovery
- Device categorization by types
- Advanced search and filtering options for browsing discovered devices
- Comprehensive details of discovered devices
- Remote installation of protection agent on discovered devices, with application of different plan types
- Extended report about discovered devices

> **Note:** The retention period of the information about discovered devices in the database is 3 months.

## Passive device discovery by using Device Sense

Passive device discovery is a non-intrusive method to identify and catalog devices within a network environment without actively probing or sending requests to those devices in the organization's network.

Passive device discovery collects the following device data:

- Device name
- Device type
- OS family
- Manufacturer
- Model
- MAC address
- IP address

The settings for passive discovery are preconfigured on a data center level. A company administrator can customize these settings for all devices in a company or a unit. If no custom settings are applied, settings from the upper level are used, in this order:

1. Cyber Protection data center
2. Company (customer tenant)
3. Unit

> **Note:** Passive discovery by using Device Sense will not scan networks that have a smaller number of agents than the number specified in the **Prevent device discovery in non-corporate networks** setting. The preconfigured value on the data center lever is 3, but the value inherited by the upper-value tenant can differ.

### Configuring passive device discovery

1. In the Cyber Protect console, go to **Settings** > **Management**.
2. Click the **Passive device discovery** tab.
3. Ensure that the **Enable passive device discovery** switch is enabled. The system automatically assigns Windows agents as discovery agents.
4. (Optional) Change the default settings.

| Setting | Description |
|---------|-------------|
| **Smart auto-selection of discovery agents** | Number of agents automatically selected to perform passive device discovery in the local network. Default: 1. Maximum: 3. |
| **Prevent device discovery in non-corporate networks** | Minimum number of agents that must be present in a network to classify it as a corporate environment and enable its scan. Default: 3. Maximum: 1000. |
| **Enhanced identification of devices in a network** | Enable or disable the use of multicast signals for more precise identification of device types joining the local network. Disabled by default. |

5. Click **Save**.

## Active device discovery by using Device Sense

Active device discovery is a method used in network management in which a system actively probes or communicates with devices on a network to identify and gather information about them.

Active device discovery collects the following device data:

- Device name
- Device type
- OS family
- Manufacturer
- Model
- IP address
- MAC address

### Running an active device discovery scan

1. In the Protection console, go to **Devices** > **Discovered devices**.
2. Click the **Local network** tab.
3. Click **Run active scan**.
4. Select the network in which to run active scan, and then click **Run**.
5. In the **Tenant** field, select the tenant.
6. In the **Discovery agent** field, select a workload that is registered in the tenant. The protection agent installed on this workload will be used as a discovery agent.
7. Click **Run**. Active device discovery scan starts. When the scan completes, a notification shows the number of devices discovered with a link to view additional details.

> **Note:** You cannot run multiple active scans simultaneously. If an active scan is in progress, you must cancel it or wait for it to complete before starting a new scan.

## Ports used by Device Sense

### Passive device discovery ports

| Name | Port | Comment |
|------|------|---------|
| DHCP | udp/67 | Listens for REQUEST messages |
| NBNS | udp/137 | Listens for NAME REGISTRATION REQUEST and NAME REFRESH REQUEST packets |
| NBDS (Browser) | udp/138 | Listens for announcement messages |
| SSDP | udp/1900 | Listens for M-SEARCH and NOTIFY messages |
| WSD | udp/3702 | Listens for wsd:Probe messages |
| MDNS | udp/5353 | Listens for various service info announcements |
| LLMNR | udp/5355 | Listens for queries |
| TUYA | udp/6668 | Listens for discovery packets |

### Enhanced identification ports (when enabled)

| Name | Ports | Comment |
|------|-------|---------|
| SSDP | udp/1900 | Sends M-SEARCH requests |
| WSD | udp/3702 | Sends wsd:Probe requests |

### Active device discovery (on-demand scan) ports

| Name | Ports | Comment |
|------|-------|---------|
| FTP | tcp/21 | Reads service banners |
| SSH | tcp/22 | Reads service banners |
| TELNET | tcp/23 | Reads banners |
| SMTP | tcp/25, tcp/587 | Reads EHLO messages |
| RDNS | udp/53 | Makes a reverse DNS request |
| HTTP | tcp/80, tcp/8080, and other common HTTP ports | Sends GET requests |
| NBNS | udp/135 | Sends NBSTAT requests |
| SNMP | udp/161 | Reads MIBs: Versions: v1, v2c; Communities: public |
| HTTPS | tcp/443, tcp/8443 | Sends GET requests |
| SMB | tcp/445 | Extracts data from NTLMv2 auth messages |
| RTSP | tcp/554 | Sends OPTIONS requests |
| SSDP | udp/1900 | Sends M-SEARCH |
| ARD | udp/3283 | Sends Start packets |
| RDP | tcp/3389 | Sends Connection Request and reads Connection Confirm |
| WSD | udp/3702 | Sends wsd:Probe messages |
| AirPlay | tcp/5000, tcp/7000 | Sends wsd:Probe messages |
| MDNS | udp/5353 | Sends PTR messages |
| iRobot | udp/5678 | Sends iRobot discover packets |
| VNC | udp/5900 | Sends RFB ProtocolVersion and Security messages |
| MIIO | udp/54321 | Sends Hello packets |

## Viewing information about discovered devices

### To find a discovered device and view its details

1. In the Protection console, click **Discovered devices**. By default, the **Devices without agent** tab opens.
2. (Optional) To search for devices from a specific category, click the corresponding tab.

| Tab | Description |
|-----|-------------|
| **Devices without agent** | All discovered machines on which a protection agent can be installed, regardless of discovery method. |
| **Active Directory** | Machines discovered by scanning the Active Directory. |
| **Local network** | Machines and network devices discovered by scanning the local corporate networks using Device Sense. |
| **Manual / From text file** | Machines discovered manually or from a text file. |
| **Exclusions** | Devices excluded from discovery. |

3. (Optional) To search by device name, enter it in the **Search** field.
4. (Optional) To search by using filters, click **Filter**, select one or several filters, and click **Apply**.

| Filter | Description |
|--------|-------------|
| **Device type** | Search by one or several device types from the list. Not available on the Manual / From text file tab. |
| **Discovery type** | Filter by: Active Directory, Manual, Local network passive, Local network active. Available on the Devices without agent tab only. |
| **MAC address** | Search by a specific MAC address. Not available on the Manual / From text file tab. |
| **IP address range** | Filter by start IP and end IP address. |
| **First discovered** | Filter by the date the device was initially discovered (predefined or custom range). |
| **Last discovered** | Filter by the date the device was last discovered (predefined or custom range). |
| **Organizational unit** | The organizational unit in Active Directory. Available on the Active Directory tab only. |

5. Click the device, and then click **Details**.
6. In the **Raw data** pane, click the arrow icon.
7. To download the raw data in a JSON file, click **Download**.
