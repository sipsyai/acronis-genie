---
title: "Hardware Inventory"
section: "RMM"
subsection: "Hardware Inventory"
page_range: "1267-1272"
tags: [rmm, hardware-inventory, scanning, devices, processors, memory, storage, motherboard, network]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#monitoring-hardware-inventory.html"
---

# Managing Your Hardware Inventory

When you enable the hardware inventory feature, you can view all the hardware components available on:

- Physical Windows and macOS devices with a license that supports the Hardware inventory feature.
- Virtual Windows and macOS machines running on supported virtualization platforms: VMware, Hyper-V, Citrix, Parallels, Oracle, Nutanix, Virtuozzo, and Virtuozzo Hybrid Infrastructure.

The hardware inventory feature is supported only for devices on which a protection agent is installed. You can obtain hardware inventory data by running automatic or manual scans on the devices.

Use hardware inventory data to:
- Discover all hardware assets of the organization
- Browse through the hardware inventory of all devices
- Compare the hardware components on multiple devices
- View detailed information about a hardware component

## Enabling or Disabling the Hardware Inventory Scanning

When hardware inventory scanning is enabled on physical devices and virtual machines, the system automatically collects the hardware data every 12 hours. The feature is enabled by default but can be changed.

Customer tenants can enable or disable the hardware inventory scanning. Unit tenants can only view the settings but cannot change them.

### To Enable/Disable

1. In the Cyber Protect console, go to **Settings**.
2. Click **Management**.
3. Click **Inventory scanning**.
4. Enable or disable the **Hardware inventory scanning** module by clicking the switch.

## Starting a Hardware Inventory Scan Manually

Prerequisites:
- The device uses Windows or macOS operating system
- The device has a license that supports the Hardware inventory feature
- A protection agent is installed on the device
- For virtual machines: must run on a supported virtualization platform

### Steps

1. In the Cyber Protect console, go to **Devices**.
2. Click the device which you want to scan, and then click **Inventory**.
3. On the **Hardware** tab, click **Scan now**.

Hardware inventory scanning of virtual machines is supported only when the current date and time of the virtual machine corresponds to the current date and time in UTC.

## Browsing the Hardware Inventory

To view all hardware components on all Windows and macOS devices:

1. In the Cyber Protect console, go to **Devices**.
2. In the **View** drop-down field, select **Hardware**.

The **Hardware** view shows the following columns:

| Column | Description |
|--------|-------------|
| Name | Device name |
| Hardware scan status | Status: Completed, Not started, Not supported, Update agent, or Upgrade license |
| Processor | Models of all processors |
| Processor cores | Number of cores |
| Disk storage | Used and total storage of all disks |
| Memory | Total RAM capacity |
| Scan date | Date/time of last hardware inventory scan |
| Motherboard | Motherboard of the device |
| Motherboard serial number | Serial number of the motherboard |
| Serial number | System serial number |
| BIOS version | Version of the BIOS |
| Organization | Organization the device belongs to |
| Owner | Owner of the device |
| Domain | Domain of the device |
| Operating system | Operating system of the device |
| Operating system build | Build of the operating system |

### Hardware Filters

| Filter | Description |
|--------|-------------|
| Processor model | Filter by specified processor model |
| Processor cores | Filter by number of processor cores |
| Disk total size | Filter by total storage size |
| Memory capacity | Filter by RAM capacity |

## Viewing the Hardware of a Single Device

You can view detailed information about the motherboard, processors, memory, graphics, storage drives, network, and system of a specific device.

1. In the Cyber Protect console, go to **Devices > All Devices**.
2. In the **View** drop-down field, select **Hardware**.
3. Find the device and click the row listing the device, and click **Inventory**.
4. Click the **Hardware** tab.

| Hardware Component | Information Displayed |
|-------------------|---------------------|
| Motherboard | Name, manufacturer, model, and serial number |
| Processors | Manufacturer, model, max clock speed, and number of cores |
| Memory | Capacity, manufacturer, and serial number |
| Graphics | Manufacturer and model of the GPUs |
| Storage drives | Model, media type, available space and size |
| Network | Mac address, IP address, and type of network adapters |
| System | Product ID, original install date, system boot time, system manufacturer, system model, serial number, BIOS version, boot device, system locale, and time zone |
