# Browsing the hardware inventory

RMM > Managing your hardware inventory > Browsing the hardware inventory
Browsing the hardware inventory

You can view and browse the data for all hardware components that are available on all devices in your organization.

Prerequisites

The devices use Windows or macOS operating system.

The devices have a license that supports the Hardware inventory feature.

The Hardware inventory feature for virtual machines is not supported in the Cyber Protect legacy editions.

A protection agent is installed on the device.

Hardware inventory scan on the devices has finished successfully.

[If the device is a virtual machine] The machine runs on one of the supported virtualization platforms. For more information, see Managing your hardware inventory.

To view all hardware components that are available on the Windows and macOS devices

In the Cyber Protect console, go to Devices.

In the View: drop-down field, select Hardware.

View is a set of columns that determines what data is visible on the screen. The predefined views are Standard and Hardware. You can create and save custom views that include different sets of columns, and are more convenient for your needs.

The following table describes the data that is visible in the Hardware view.

Column	Description
Name	Device name.
Hardware scan status

Status of the hardware scan.

Completed.

Not started.

Not supported. This status is shown for workloads for which the hardware inventory functionality is not supported. For example, virtual machines, mobile devices, and Linux devices.

Update agent. This status is shown when an outdated version of agent is installed on the device. Clicking on this action will redirect to Settings > Agents page, where administrators can update the agent.

Upgrade license.

Clicking on this status opens a dialog where administrators can change the current license to another of the licenses that are available for the tenant.


Processor	Models of all processors of the device.
Processor cores	Number of cores of all processors of the device.
Disk storage	Used storage, and total storage of all the disks of the device.
Memory	Total RAM capacity of the device.
Scan date	Date and time of the last hardware inventory scan.
Motherboard	Motherboard of the device.
Motherboard serial number	Serial number of the motherboard.
Serial number	System serial number of the device.
BIOS version	Version of the BIOS of the system.
Organization	Organization to which the device belongs.
Owner	Owner of the device.
Domain	Domain of the device.
Operating system	Operating system of the device.
Operating system build	Build of the operating system of the device.

To add columns in the table, click the gear icon, and select the columns that you want to be visible in the table.

To narrow the information displayed on the screen, use one or more filters.

Click Search.

Click the arrow, and then click Hardware.

Select one or a combination of several filters.

The following table describes the Hardware filters.

Filter	Description
Processor model	Multiple selection is possible. Use this filter if you want to view the hardware data of the devices which have the specified processor model.
Processor cores	Use this filter if you want to view the hardware data of the devices which have the specified number of processor cores.
Disk total size	Use this filter if you want to view the hardware data of the devices which have the specified total storage size.
Memory capacity	Use this filter if you want to view the hardware data of the devices which have the specified RAM capacity.

Click Apply.

To sort the data in an ascending order, click a column name.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.