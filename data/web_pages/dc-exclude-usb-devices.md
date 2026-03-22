# USB devices allowlist

Managing workloads in the Cyber Protect console > Working with the Device control module > USB devices allowlist
USB devices allowlist

The allowlist is intended to allow using certain USB devices regardless of any other device control settings. You can add individual devices or device models to the allowlist to disable the access control for those devices. For example, if you add a mobile device with a unique ID to the allowlist, you allow the use of that particular device even though any other USB devices are denied.

On the USB devices allowlist page, you can specify individual USB devices or USB device models to exclude from device access control. As a result, access to those devices is allowed regardless of the access settings in the device control module.

There are two ways to identify devices in the allowlist:

Model of device - Collectively identifies all devices of a certain model. Each device model is identified by vendor ID (VID) and product ID (PID), such as USB\VID_0FCE&PID_E19E.

This combination of VID and PID does not identify a specific device, but an entire device model. By adding a device model to the allowlist, you allow access to any device of that model. For example, this way you can allow the use of USB printers of a particular model.

Unique device - Identifies a certain device. Each unique device is identified by vendor ID (VID), product ID (PID), and serial number, such as USB\VID_0FCE&PID_E19E\D55E7FCA.

Not all USB devices are assigned a serial number. You can add a device to the allowlist as a unique device only if the device has been assigned a serial number during production. For example, a USB stick that has a unique serial number.

To add a device to the allowlist, you first need to add it to the USB devices database. Then, you can add devices to the allowlist by selecting from that database.

The allowlist is managed on a separate configuration page called USB devices allowlist. Each item in the list represents a device or device model and has the following fields:

Description - The operating system assigns a certain description when connecting the USB device. You can modify the description of the device in the USB devices database (see USB database management page).
Device type - Displays Unique if the list item represents a unique device, or Model if it represents a device model.
Read-only - When selected, allows only receiving data from the device. If the device does not support read-only access, then access to the device is blocked. Clear this check box to allow full access to the device.
Reinitialize - When selected, causes the device to simulate disconnecting/reconnecting when a new user logs in. Some USB devices require reinitializing in order to function, so we recommend that you select this check box for such devices (mouse, keyboard, etc.). We also recommend that you clear this check box for data storage devices (USB sticks, optical drives, external hard drives, etc.).

The device control may not be able to reinitialize some USB devices with proprietary drivers. If there is no access to such a device, you must remove the USB device from the USB port, and then insert it back.

The Reinitialize field is hidden by default. To display it in the table, click the gear icon in the upper right corner of the table, and then select the Reinitialize check box.

The Read-only and Reinitialize fields are not supported on macOS. If these fields are configured in the applied protection plan, they will be ignored.

You can add or remove devices/models from the allowlist as follows:

Click Add from database above the list and then select the desired device/s from those registered with the USB devices database. The selected device is added to the list, where you can configure its settings and confirm the changes.
Click Allow this USB device in an alert informing that access to the USB device is denied (see Device control alerts). This adds the device to the allowlist and to the USB devices database.
Click the delete icon at the end of a list item. This removes the respective device/model from the allowlist.
See also
Exclude individual USB devices from access control
Enabling the use of the device control module on macOS

USB devices database

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.