# Device types allowlist

Managing workloads in the Cyber Protect console > Working with the Device control module > Device types allowlist
Device types allowlist

On the Device types allowlist page, you can choose device subclasses to exclude from device access control. As a result, access to those devices is allowed regardless of the access settings in the device control module.

The device control module provides the option to allow access to devices of certain subclasses within a denied device type. This option allows you to deny all devices of a certain type, except for some subclasses of devices of this type. It can be useful, for example, when you need to deny access to all USB ports while allowing the use of a USB keyboard and mouse at the same time.

When configuring the device control module, you can specify which device subclasses to exclude from device access control. When a device belongs to an excluded subclass, access to that device is allowed regardless of whether or not the device type or port is denied. You can selectively exclude the following device subclasses from device access control:

USB HID (mouse, keyboard, etc.) - When selected, allows access to Human Interface Devices (mouse, keyboard, and so on) connected to a USB port even if USB ports are denied. By default, this item is selected so that denying access to the USB port does not disable the keyboard or mouse.

Supported on both Windows and macOS.

USB and FireWire network cards - When selected, allows access to network cards connected to a USB or FireWire (IEEE 1394) port even if USB ports and/or FireWire ports are denied.

Supported on both Windows and macOS.

USB scanners and still image devices - When selected, allows access to scanners and still image devices connected to a USB port even if USB ports are denied.
Supported only on Windows.
USB audio devices - When selected, allows access to audio devices, such as headsets and microphones, connected to a USB port even if USB ports are denied.
Supported only on Windows.
USB cameras - When selected, allows access to Web cameras connected to a USB port even if USB ports are denied.
Supported only on Windows.
Bluetooth HID (mouse, keyboard, etc.) - When selected, allows access to Human Interface Devices (mouse, keyboard, and so on) connected via Bluetooth even if Bluetooth is denied.
Supported only on Windows.
Clipboard copy/paste within application - When selected, allows copying/pasting of data through the clipboard within the same application even if the clipboard is denied.
Supported only on Windows.

Settings for unsupported device subclasses are ignored if these settings are configured in the applied protection plan.

When allowlisting device types, consider the following:

With the device types allowlist, you can only allow a whole subclass of device. You cannot allow a specific device model, while denying all other devices of the same subclass. For example, by excluding USB cameras from device access control, you allow the use of any USB camera, no matter their model and vendor. On how to allow individual devices/models, see USB devices allowlist.
Device types can only be selected from a closed list of device subclasses. If the device to allow is of a different subclass, then it cannot be allowed by using device types allowlist. For example, such a subclass as USB smartcard readers cannot be added to the allowlist. To allow a USB smartcard reader when USB ports are denied, follow the instructions in USB devices allowlist.
The device types allowlist only works for devices that use standard Windows drivers. The device control may not recognize the subclass of some USB devices with proprietary drivers. As a result, you cannot allow access to such USB devices by using the device types allowlist. In this case, you could allow access on a per-device/model basis (see USB devices allowlist).
See also
Exclude device subclasses from access control
Enabling the use of the device control module on macOS
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.