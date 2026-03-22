# OS notification and service alerts

Managing workloads in the Cyber Protect console > Working with the Device control module > Access settings > OS notification and service alerts
OS notification and service alerts

You can configure the device control to display OS notification to end users if they try to use a blocked device type on protected computers. When the Show OS notification to end users if they try to use a blocked device type or port check box is selected in the access settings, the agent displays a pop-up message in the notification area of the protected computer if any of the following events occurs:

A denied attempt to use a device on a USB or FireWire port. This notification appears whenever the user plugs in a USB or FireWire device that is denied at the interface level (for example, when denying access to the USB port) or at the type level (for example, when denying the use of removable devices). The notification informs that the user is not allowed to access the specified device/drive.

A denied attempt to copy a data object (such as a file) from a certain device. This notification appears when denying read access to the following devices: floppy drives, optical drives, removable devices, encrypted removable devices, mobile devices, redirected mapped drives, and redirected clipboard incoming data. The notification informs that the user is not allowed to get the specified data object from the specified device.

The denied read notification is also displayed when denying read/write access to Bluetooth, FireWire port, USB port, and redirected USB port.

A denied attempt to copy a data object (such as a file) to a certain device. This notification appears when denying write access to the following devices: floppy drives, optical drives, removable devices, encrypted removable devices, mobile devices, local clipboard, screenshot capture, printers, redirected mapped drives, and redirected clipboard outgoing data. The notification informs that the user is not allowed to send the specified data object to the specified device.

User attempts to access blocked device types on protected computers can raise alerts that are logged in the Cyber Protect console. It is possible to enable alerts for each device type (excluding screenshot capture) or port separately by selecting the Show alert check box in the access settings. For example, if access to removable devices is restricted to read-only, and the Show alert check box is selected for that device type, an alert is logged every time a user on a protected computer attempts to copy data to a removable device. See Device control alerts for further details.

See also steps to enable or disable OS notification and service alerts.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.