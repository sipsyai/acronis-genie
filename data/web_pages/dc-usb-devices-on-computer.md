# List of USB devices on a computer

Managing workloads in the Cyber Protect console > Working with the Device control module > USB devices allowlist > List of USB devices on a computer
List of USB devices on a computer

The Inventory panel of a computer in the Cyber Protect console includes the USB Devices tab. If the computer is online and the agent for Data Loss Prevention is installed on it, the USB Devices tab displays a list all USB devices that have ever been connected to that computer.

The USB devices are listed in tree view. The first level of the tree represents a device model. The second level represents a specific device of that model.

For each device, the list provides the following information:

Description - The operating system assigns a description when connecting the USB device. This description can serve as a readable identifier of the device.

A blue icon next to the description of the device indicates that the device is currently attached to the computer. If the device is not attached to the computer, the icon is grayed out.

Device ID - The identifier that the operating system assigned to the device. This identifier has the following format: USB\VID_<vendor ID>&PID_<product ID>\<serial number> where <serial number> is optional. Examples: USB\VID_0FCE&PID_ADDE\D55E7FCA (device with a serial number); USB\VID_0FCE&PID_ADDE (device without serial number).

To add devices to the USB devices database, select the check boxes of the desired devices, and then click the Add to database button.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.