---
title: "Device control alerts and OS notifications"
section: "Managing workloads in the Cyber Protect console"
subsection: "Working with the Device control module"
page_range: "440-451"
tags: [device control, alerts, notifications, action field, event log, USB]
acronis_version: "26.02"
---

# OS notification and service alerts

You can configure the device control to display OS notification to end users if they try to use a blocked device type on protected computers. When the **Show OS notification to end users if they try to use a blocked device type or port** check box is selected in the access settings, the agent displays a pop-up message in the notification area of the protected computer if any of the following events occurs:

- A denied attempt to use a device on a USB or FireWire port. This notification appears whenever the user plugs in a USB or FireWire device that is denied at the interface level (e.g., when denying access to the USB port) or at the type level (e.g., when denying the use of removable devices).
- A denied attempt to copy a data object (such as a file) from a certain device. This notification appears when denying read access to floppy drives, optical drives, removable devices, encrypted removable devices, mobile devices, redirected mapped drives, and redirected clipboard incoming data. The denied read notification is also displayed when denying read/write access to Bluetooth, FireWire port, USB port, and redirected USB port.
- A denied attempt to copy a data object (such as a file) to a certain device. This notification appears when denying write access to floppy drives, optical drives, removable devices, encrypted removable devices, mobile devices, local clipboard, screenshot capture, printers, redirected mapped drives, and redirected clipboard outgoing data.

# Device control alerts

The device control maintains an event log by tracking user attempts to access controlled device types, ports, or interfaces. Certain events can raise alerts that are logged in the Cyber Protect console. For example, the device control module can be configured to prevent the use of removable devices, with an alert logged whenever a user tries to copy data to or from such a device.

When configuring the device control module, you can enable alerts for most items listed under device Type (except screenshot capture) or Ports. If alerts are enabled, each attempt by a user to perform an operation that is not allowed generates an alert. For example, if access to removable devices is restricted to read-only, and the **Show alert** option is selected for that device type, an alert is generated every time a user on a protected computer attempts to copy data to a removable device.

## Viewing device control alerts

To view alerts in the Cyber Protect console, go to **Monitoring** > **Alerts**. Within each device control alert, the console provides the following information about the respective event:

- **Type** -- Warning.
- **Status** -- Displays "Peripheral device access is blocked".
- **Message** -- Displays "Access to '<device type or port>' on '<computer name>' is blocked". For example, "Access to 'Removable' on 'accountant-pc' is blocked".
- **Date and time** -- The date and time that the event occurred.
- **Device** -- The name of the computer on which the event occurred.
- **Plan name** -- The name of the protection plan that caused the event.
- **Source** -- The device type or port involved in the event. For example, in the event of a denied user attempt to access a removable device, this field reads Removable device.
- **Action** -- The operation that caused the event. For example, in the event of a denied user attempt to copy data to a device, this field reads Write.
- **Name** -- The name of the event target object, such as the file the user attempted to copy or the device the user attempted to use. Not displayed if the target object cannot be identified.
- **Information** -- Additional information about the event target device, such as the device ID for USB devices. Not displayed if no additional information is available.
- **User** -- The name of the user who caused the event.
- **Process** -- The fully qualified path to the executable file of the application that caused the event. In some cases, the process name might be displayed instead. Not displayed if process information is not available.

If an alert applies to a USB device (including removable devices and encrypted removable devices), the administrator can add the device to the allowlist directly from the alert. Clicking **Allow this USB device** adds it to the USB devices allowlist and also adds it to the USB devices database.

## Action field values

Alert **Action** field can contain the following values:

| Action | Description |
|--------|-------------|
| **Read** | Get data from the device or port |
| **Write** | Send data to the device or port |
| **Format** | Direct access (formatting, check disk, etc.) to the device |
| **Eject** | Remove the device from the system or eject the media from the device |
| **Print** | Send a document to the printer |
| **Copy audio** | Copy/paste audio data via the local clipboard |
| **Copy file** | Copy/paste a file via the local clipboard |
| **Copy image** | Copy/paste an image via the local clipboard |
| **Copy text** | Copy/paste text via the local clipboard |
| **Copy unidentified content** | Copy/paste other data via the local clipboard |
| **Copy RTF data (image)** | Copy/paste an image via the local clipboard using Rich Text Format |
| **Copy RTF data (file)** | Copy/paste a file via the local clipboard using Rich Text Format |
| **Copy RTF data (text, image)** | Copy/paste text along with an image via the local clipboard using Rich Text Format |
| **Copy RTF data (text, file)** | Copy/paste text along with a file via the local clipboard using Rich Text Format |
| **Copy RTF data (image, file)** | Copy/paste an image along with a file via the local clipboard using Rich Text Format |
| **Copy RTF data (text, image, file)** | Copy/paste text along with an image and a file via the local clipboard using Rich Text Format |
| **Delete** | Delete data from the device (e.g., removable device, mobile device) |
| **Device access** | Access some device or port (e.g., Bluetooth device, USB port) |
| **Insert** | Connect a USB device or a FireWire device |
| **Rename** | Rename files on a device (e.g., removable devices, mobile devices) |
| **Incoming audio/file/image/text/unidentified content** | Copy/paste data from the client computer to the hosted session via the redirected clipboard |
| **Incoming RTF data (various)** | Copy/paste data from the client to hosted session via redirected clipboard using Rich Text Format |
| **Outgoing audio/file/image/text/unidentified content** | Copy/paste data from the hosted session to the client computer via the redirected clipboard |
| **Outgoing RTF data (various)** | Copy/paste data from the hosted session to client via redirected clipboard using Rich Text Format |
