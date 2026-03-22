# USB devices database management page

Managing workloads in the Cyber Protect console > Working with the Device control module > USB devices allowlist > USB devices database management page
USB devices database management page

When configuring the allowlist for USB devices, you have the option to add a device from the database. If you choose this option, a management page appears with a list of devices. On this page you can view the list of all devices that are registered with the database, you can select devices to add to the allowlist, and perform the following operations:

Register a device with the database

Click Add to database at the top of the page.
On the Add USB device dialog that appears, choose the machine to which the USB device is connected.

Only machines that are online are displayed in the list of computers.

The list of USB devices is displayed only for machines that have the agent for Data Loss Prevention installed.

The USB devices are listed in tree view. The first level of the tree represents a device model. The second level represents a specific device of that model.

A blue icon next to the description of the device indicates that the device is currently attached to the computer. If the device is not attached to the computer, the icon is grayed out.

Select the check box for the USB device that you want to register, and click Add to database.

Change the description of a device

On the USB devices database page click ellipsis (...) at the end of the list item representing the device and then click Edit.

Make changes to the description in the dialog box that appears.

Remove a device from the database

Click the ellipsis (...) at the end of the list item representing the device.

Click Delete, and confirm the deletion.

For each device, the list on the page provides the following information:

Description - A readable identifier of the device. You can change the description as needed.
Device type - Displays Unique if the list item represents a unique device, or Model if it represents a device model. A unique device must have a serial number along with a vendor ID (VID) and product ID (PID), whereas a device model is identified by a combination of VID and PID.
Vendor ID, Product ID, Serial number - These values together make up the device ID in the form USB\VID_<vendor ID>&PID_<product ID>\<serial number>.
Account - Indicates the tenant to which this device belongs. This is the tenant that contains the user account that was used to register the device with the database.
This column is hidden by default. To display it in the table, click the gear icon in the upper right corner of the table, and then select Account.

The leftmost column is intended to select the devices to add to the allowlist: Select the check box for each device to add, and then click the Add to allowlist button. To select or clear all check boxes, click the check box in the column header.

You can search or filter the list of devices:

Click Search at the top of the page and enter a search string. The list displays devices whose description matches the string you typed.
Click Filter, and then configure and apply a filter in the dialog box that appears. The list is limited to devices with the type, vendor ID, product ID, and account that you selected when configuring the filter. To cancel the filter and list all devices, click Reset to default.

Export the list of USB devices in the database

You can export the list of USB devices that are added to the database.

Open the protection plan of a device for editing.
Click the arrow icon next to the Device control switch to expand the settings, and then click the USB devices allowlist row.
On the USB devices allowlist page, click Add from database.
On the USB devices database management page that appears, click Export.

The standard Browse dialog opens.

Select the location to which you want to save the file, enter a new file name if needed, and click Save.

The list of USB devices is exported to a JSON file.

You can edit the resulting JSON file to add or remove devices from it, and make mass changes of device descriptions.

Import a list of USB devices to the database

Instead of adding USB devices from the Cyber Protect console, you can import a list of USB devices. The list is a file in JSON format.

You can import JSON files to a database that does not contain the devices described in the file. To import a modified file to the database from which it was exported, you must clear the database first because you cannot import duplicate entries. If you export the list of USB devices, modify it, and try to import to the same database without clearing it, the import will fail.
Open the protection plan of a device for editing.
Click the arrow icon next to the Device control switch to expand the settings, and then click the USB devices allowlist row.
On the USB devices allowlist page, click Add from database.
Use drag and drop (or browse) for the file that you want to import.

The Cyber Protect console checks if the list contains duplicate entries that already exist in the database and skips them. The USB devices that are not found in the database are appended to it.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.