---
title: "Software Management and Inventory"
section: "RMM"
subsection: "Software Management"
page_range: "1273-1277"
tags: [rmm, software-management, software-inventory, scanning, applications, deploypilot, vulnerability-assessment, patch-management]
acronis_version: "26.02"
---

# Managing Software

To access this functionality, you must have one of the following roles for Cyber Protection: Company administrator, Cyber administrator, or Read-only administrator.

The software management features of Cyber Protection cover the full software lifecycle:

- **Software deployment by using DeployPilot**: Add software packages to the software repository and quickly deploy software on remote workloads.
- **Inventory scanning**: Run automatic or manual inventory scans on devices and gain complete visibility about the software installed on them.
- **Vulnerability assessment**: Run vulnerability scans to identify vulnerabilities in the operating systems and software installed on devices.
- **Patch management**: Manage patches (updates) for applications and operating systems installed on devices, and keep systems up to date.

## Managing Your Software Inventory

The feature enables you to view all the software applications that are installed on all Windows and macOS devices. To obtain the software inventory data, you can run automatic or manual scans on the devices.

Use the software inventory to:
- Browse and compare the information about all applications installed on company devices
- Determine if an application needs to be updated
- Determine if an unused application needs to be removed
- Ensure that the software version on multiple company devices is the same
- Monitor changes in the software status between consecutive scans

## Enabling or Disabling the Software Inventory Scanning

When software inventory scanning is enabled on devices, the system automatically collects the software data every 12 hours. The feature is enabled by default for all devices that have the required license.

### To Enable/Disable

1. In the Cyber Protect console, go to **Settings**.
2. Click **Management**.
3. Click **Inventory scanning**.
4. Enable or disable the **Software inventory scanning** module.

## Starting a Software Inventory Scan Manually

### From Software Inventory

1. In the Cyber Protect console, go to **Software management**.
2. Click **Software inventory**.
3. In the **Group by** dropdown menu, select **Devices**.
4. Find the device and click **Scan now**.

### From Devices

1. In the Cyber Protect console, go to **Devices**.
2. Click the device, and then click **Inventory**.
3. In the **Software** tab, click **Scan now**.

## Browsing the Software Inventory

1. In the Cyber Protect console, go to **Software Management**.
2. Click **Software inventory**.

By default, data is grouped by device. The Software inventory screen shows:

| Column | Description |
|--------|-------------|
| Name | Name of the application |
| Version | Version of the application |
| Status | New, Updated, Removed, or No Change |
| Vendor | Vendor of the application |
| Date installed | When the application was installed |
| Last run | For macOS devices only: when the application was last active |
| Location | Directory where the application is installed |
| User | User for whom the application was installed |
| System type | For Windows: X86 (32-bit) or X64 (64-bit) |

To group by application, select **Applications** in the **Group by** dropdown.

### Filters Available

| Filter | Description |
|--------|-------------|
| Device Name | Compare software on specific devices |
| Application | Compare data for a specific application |
| Vendor | View applications from a specific vendor |
| Status | View applications in selected status |
| Date installed | View applications installed on a specific date |
| Scan date | View software scanned on a specific date |

The list might contain information about deleted machines. The current retention policy is to keep data for deleted machines for up to 35 days.
