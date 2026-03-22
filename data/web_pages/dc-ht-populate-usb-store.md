# Add or remove USB devices from the database

Managing workloads in the Cyber Protect console > Working with the Device control module > Using device control > Add or remove USB devices from the database
Add or remove USB devices from the database

To exclude a particular USB device from access control, you need to add it to the USB devices database. Then, you can add devices to the allowlist by selecting from that database.

The following procedures apply to protection plans that have the device control feature enabled.

To add USB devices to the database

Open the protection plan of a device for editing:

Click the ellipsis (...) next to the name of the protection plan and select Edit.

Device control must be enabled in the plan, so you can access the Device control settings.
Click the arrow icon next to the Device control switch to expand the settings, and then click the link next to USB devices allowlist.
On the USB devices allowlist page that appears, click Add from database.
On the USB devices database management page that appears, click Add to database.
On the Add USB device dialog that appears, click the machine to which the USB device is connected.

Only machines that are online are displayed in the list of computers.

The list of USB devices is displayed only for machines that have the agent for Data Loss Prevention installed.

The USB devices are listed in tree view. The first level of the tree represents a device model. The second level represents a specific device of that model.

A blue icon next to the description of the device indicates that the device is currently attached to the computer. If the device is not attached to the computer, the icon is grayed out.

Select the check boxes for the USB devices that you want to add to the database, and then click Add to database.

The selected USB devices are added to the database.

Close or save the protection plan.

To add USB devices to the database from the computer Details panel

This procedure applies only for devices that are online and have the agent for Data Loss Prevention installed on them. You cannot view the list of USB devices for a computer that is offline or does not have the Data Loss Prevention agent installed.
In the Cyber Protect console, go to Devices > All devices.

Select a computer to which the desired USB device has ever been connected, and, in the menu to the right, click Inventory.

The computer details panel opens.

On the computer details panel, click the USB Devices tab.

The list of USB devices that are known on the selected computer opens.

The USB devices are listed in tree view. The first level of the tree represents a device model. The second level represents a specific device of that model.

A blue icon next to the description of the device indicates that the device is currently attached to the computer. If the device is not attached to the computer, the icon is grayed out.

Select the check boxes for the USB devices that you want to add to the database and click Add to database.

To add USB devices to the database from service alerts

In the Cyber Protect console, go to Monitoring > Alerts.
Locate a device control alert that informs of denying access to the USB device.

In the alert simple view, click Allow this USB device.

This excludes the USB device from access control, and adds it to the database for further reference.

To add USB devices by importing a list of devices to the database

You can import a JSON file with a list of USB devices to the database. See Import a list of USB devices to the database.

To remove USB devices from the database

Open the protection plan of a device for editing:

Click the ellipsis (...) next to the name of the protection plan and select Edit.

Device control must be enabled in the plan, so you can access the Device control settings.
Click the arrow next to the Device control switch to expand the settings, and then click the USB devices allowlist row.
On the page for managing the allowlist that appears, click Add from database.
On the page for selecting USB devices from the database, click ellipsis (...) at the end of the list item representing the device, click Delete, and confirm the deletion.

The USB devices are deleted from the database.

Close or save the protection plan.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.