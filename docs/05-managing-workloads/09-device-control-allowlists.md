---
title: "Device types allowlist and USB devices allowlist"
section: "Managing workloads in the Cyber Protect console"
subsection: "Working with the Device control module"
page_range: "441-446"
tags: [device control, allowlist, USB devices, device subclasses, exclusions, USB database]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#dc-exclude-device-types.html"
---

# Device types allowlist

On the **Device types allowlist** page, you can choose device subclasses to exclude from device access control. As a result, access to those devices is allowed regardless of the access settings in the device control module.

The device control module provides the option to allow access to devices of certain subclasses within a denied device type. This option allows you to deny all devices of a certain type, except for some subclasses of devices of this type. It can be useful, for example, when you need to deny access to all USB ports while allowing the use of a USB keyboard and mouse at the same time.

When configuring the device control module, you can specify which device subclasses to exclude from device access control. When a device belongs to an excluded subclass, access to that device is allowed regardless of whether or not the device type or port is denied.

## Available device subclasses

You can selectively exclude the following device subclasses from device access control:

- **USB HID (mouse, keyboard, etc.)** -- Allows access to Human Interface Devices (mouse, keyboard, and so on) connected to a USB port even if USB ports are denied. By default, this item is selected so that denying access to the USB port does not disable the keyboard or mouse. Supported on both Windows and macOS.

- **USB and FireWire network cards** -- Allows access to network cards connected to a USB or FireWire (IEEE 1394) port even if USB ports and/or FireWire ports are denied. Supported on both Windows and macOS.

- **USB scanners and still image devices** -- Allows access to scanners and still image devices connected to a USB port even if USB ports are denied. Supported only on Windows.

- **USB audio devices** -- Allows access to audio devices, such as headsets and microphones, connected to a USB port even if USB ports are denied. Supported only on Windows.

- **USB cameras** -- Allows access to Web cameras connected to a USB port even if USB ports are denied. Supported only on Windows.

- **Bluetooth HID (mouse, keyboard, etc.)** -- Allows access to Human Interface Devices (mouse, keyboard, and so on) connected via Bluetooth even if Bluetooth is denied. Supported only on Windows.

- **Clipboard copy/paste within application** -- Allows copying/pasting of data through the clipboard within the same application even if the clipboard is denied. Supported only on Windows.

> **Note:** Settings for unsupported device subclasses are ignored if these settings are configured in the applied protection plan.

## Considerations when allowlisting device types

- With the device types allowlist, you can only allow a whole subclass of device. You cannot allow a specific device model, while denying all other devices of the same subclass. For example, by excluding USB cameras from device access control, you allow the use of any USB camera, no matter their model and vendor. To allow individual devices/models, see USB devices allowlist.
- Device types can only be selected from a closed list of device subclasses. If the device to allow is of a different subclass, then it cannot be allowed by using the device types allowlist. For example, USB smartcard readers cannot be added to the allowlist.
- The device types allowlist only works for devices that use standard Windows drivers. The device control may not recognize the subclass of some USB devices with proprietary drivers. In this case, you could allow access on a per-device/model basis using the USB devices allowlist.

## To exclude device subclasses from access control

1. Open the protection plan panel for a protection plan and enable device control in that plan.
2. Click the arrow icon next to the **Device control** switch to expand the settings, and then click the link next to **Device types allowlist**.
3. On the page for managing the allowlist that appears, view or change the selection of device subclasses to exclude from access control.

# USB devices allowlist

The allowlist is intended to allow using certain USB devices regardless of any other device control settings. You can add individual devices or device models to the allowlist to disable the access control for those devices. For example, if you add a mobile device with a unique ID to the allowlist, you allow the use of that particular device even though any other USB devices are denied.

## Identifying devices

There are two ways to identify devices in the allowlist:

- **Model of device** -- Collectively identifies all devices of a certain model, identified by vendor ID (VID) and product ID (PID), such as `USB\VID_0FCE&PID_E19E`. This combination does not identify a specific device but an entire device model. Adding a device model to the allowlist allows access to any device of that model.

- **Unique device** -- Identifies a certain device by vendor ID (VID), product ID (PID), and serial number, such as `USB\VID_0FCE&PID_E19E\D55E7FCA`. Not all USB devices are assigned a serial number. You can add a device to the allowlist as a unique device only if the device has been assigned a serial number during production.

## Allowlist fields

Each item in the allowlist represents a device or device model and has the following fields:

- **Description** -- The operating system assigns a certain description when connecting the USB device. You can modify the description in the USB devices database.
- **Device type** -- Displays Unique if the list item represents a unique device, or Model if it represents a device model.
- **Read-only** -- When selected, allows only receiving data from the device. If the device does not support read-only access, then access to the device is blocked. Clear this check box to allow full access to the device.
- **Reinitialize** -- When selected, causes the device to simulate disconnecting/reconnecting when a new user logs in. Some USB devices require reinitialization in order to function, so this is recommended for mouse, keyboard, etc. Recommend clearing this check box for data storage devices (USB sticks, optical drives, external hard drives, etc.).

  > **Note:** The **Reinitialize** field is hidden by default. To display it in the table, click the gear icon in the upper right corner of the table, and then select the **Reinitialize** check box.

  > **Note:** The **Read-only** and **Reinitialize** fields are not supported on macOS. If these fields are configured in the applied protection plan, they will be ignored.

## Managing the allowlist

You can add or remove devices/models from the allowlist as follows:

- Click **Add from database** above the list and then select the desired device/s from those registered with the USB devices database. The selected device is added to the list, where you can configure its settings and confirm the changes.
- Click **Allow this USB device** in an alert informing that access to the USB device is denied (see Device control alerts). This adds the device to the allowlist and to the USB devices database.
- Click the delete icon at the end of a list item. This removes the respective device/model from the allowlist.

## To exclude a USB device from access control

1. Open the protection plan panel for a protection plan and enable device control in that plan.
2. Click the arrow icon next to the **Device control** switch to expand the settings, and then click the link next to **USB devices allowlist**.
3. On the page for managing the allowlist that appears, click **Add from database**.
4. On the page for selecting USB devices that appears, select the desired device/s from those registered with the USB devices database.
5. Click the **Add to allowlist** button.

## To stop excluding a USB device from access control

1. Open the protection plan panel for a protection plan and enable device control in that plan.
2. Click the arrow icon next to the **Device control** switch to expand the settings, and then click the link next to **USB devices allowlist**.
3. On the page for managing the allowlist that appears, click the delete icon at the end of list item representing the desired USB device.

# USB devices database

The device control module maintains a database of USB devices from which you can add devices to the list of exclusions (see USB devices allowlist). A USB device can be registered with the database in any of these ways:

- Add a device on the page that appears when adding a device to the exclusion list (USB devices database management page).
- Add a device from the USB Devices tab of a computer's Inventory pane in the Cyber Protect console (List of USB devices on a computer).
- Allow the device from an alert on denying access to the USB device (see Device control alerts).

## Add or remove USB devices from the database

### To add USB devices to the database

1. Open the protection plan of a device for editing. Click the ellipsis (...) next to the name of the protection plan and select **Edit**. Device control must be enabled in the plan.
2. Click the arrow icon next to the **Device control** switch to expand the settings, and then click the link next to **USB devices allowlist**.
3. On the **USB devices allowlist** page that appears, click **Add from database**.
4. On the USB devices database management page that appears, click **Add to database**.
5. On the **Add USB device** dialog that appears, click the machine to which the USB device is connected. Only machines that are online are displayed. The list of USB devices is displayed only for machines that have the agent for Data Loss Prevention installed.
6. Select the check boxes for the USB devices that you want to add to the database, and then click **Add to database**.
7. Close or save the protection plan.

### To add USB devices to the database from service alerts

1. In the Cyber Protect console, go to **Monitoring** > **Alerts**.
2. Locate a device control alert that informs of denying access to the USB device.
3. In the alert simple view, click **Allow this USB device**. This excludes the USB device from access control, and adds it to the database for further reference.

### Export and import USB devices

You can export the list of USB devices in the database to a JSON file, edit it to add or remove devices and make mass changes, and then import it back.

**To export:** Open a protection plan for editing, expand **Device control** > **USB devices allowlist**, click **Add from database**, and then on the USB devices database management page click **Export**.

**To import:** On the USB devices allowlist page, click **Add from database**, and then use drag and drop (or browse) for the JSON file that you want to import. The Cyber Protect console checks for duplicate entries and skips them. USB devices not found in the database are appended.

> **Note:** You can import JSON files to a database that does not contain the devices described in the file. To import a modified file to the database from which it was exported, you must clear the database first because you cannot import duplicate entries.

# Excluding processes from access control

The access to Windows clipboard, screenshot capture, printers, and mobile devices is controlled through hooks injected into processes. If processes are not hooked, the access to these devices will not be controlled.

> **Note:** Excluding processes from access control is not supported on macOS. If a list of excluded processes is configured in the applied protection plan, it will be ignored.

On the **Exclusions** page, you can specify a list of processes that will not be hooked. This means that clipboard (local and redirected), screenshot capture, printer, and mobile device access controls will not be applied to such processes.

For example, if you applied a protection plan that denies access to printers, then started Microsoft Word, an attempt to print from this application will be blocked. But if you add the Microsoft Word process to the list of exclusions, then the application will not be hooked. As a result, printing from Microsoft Word will not be blocked, while printing from other applications will still be blocked.

## To add processes to exclusions

1. Open the protection plan of a device for editing. Device control must be enabled.
2. Click the arrow next to the **Device control** switch to expand the settings, and then click the **Exclusions** row.
3. On the **Exclusions** page, in the **Processes and folders** row, click **+Add**.
4. Add the processes that you want to exclude from the access control. For example, `C:\Folder\subfolder\process.exe`. You can use wildcards: `*` replaces any number of characters; `?` replaces one character. Examples: `C:\Folder\*`, `*\Folder\SubFolder?\*`, `*\process.exe`
5. Click the check mark, and then click **Done**.
6. In the protection plan, click **Save**.
7. Restart the processes that you excluded to ensure that the hooks are properly removed.

The excluded processes will have access to clipboard, screenshot capture, printers, and mobile devices regardless of the access settings for those devices.
