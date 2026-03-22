# Access settings

Managing workloads in the Cyber Protect console > Working with the Device control module > Access settings
Access settings

On the Access settings page, you can allow or deny access to devices of certain types, as well as enable or disable OS notification and device control alerts.

The access settings configured in Device control might be overridden when using both Device control and Data Loss Prevention to protect a workload. See Enabling Data Loss Prevention in protection plans.

The access settings allow you to limit user access to the following device types and ports:

Removable (access control by device type) - Devices with any interface for connecting to a computer (USB, FireWire, PCMCIA, IDE, SATA, SCSI, etc.) that are recognized by the operating system as removable storage devices (for example, USB sticks, card readers, magneto-optical drives, etc.). The device control classifies all hard drives connected via USB, FireWire, and PCMCIA as removable devices. It also classifies some hard drives (usually with SATA and SCSI) as removable devices if they support the hot-plug function and do not have the running operating system installed on them.

You can allow full access, read-only access, or deny access to removable devices to control data copy operations to and from any removable device on a protected computer. Access rights do not affect devices that are encrypted with BitLocker or FileVault (only HFS+ file system).

This device type is supported on both Windows and macOS.

Encrypted removable (access control by device type) - Removable devices that are encrypted with BitLocker (on Windows) or FileVault (on macOS) drive encryption.

On macOS, only encrypted removable drives using the HFS+ (also known as HFS Plus or Mac OS Extended, or HFS Extended) file system are supported. Encrypted removable drives using the APFS file system are treated as removable drives.

You can allow full access, read-only access, or deny access to encrypted removable devices to control data copy operations to and from any encrypted removable device on a protected computer. Access rights affect only devices that are encrypted with BitLocker or FileVault (only HFS+ file system).

This device type is supported on both Windows and macOS.


Printers (access control by device type) - Physical printers with any interface for connecting to a computer (USB, LPT, Bluetooth, etc.), as well as printers accessed from a computer on the network.

You can allow or deny access to printers to control the printing of documents on any printer on a protected computer.

When you change the access setting for printers to Deny, the applications and processes accessing the printers must be restarted to enforce the newly configured access settings. To ensure that access settings are enforced correctly, restart the protected workloads.

This device type is supported only on Windows.

Clipboard (access control by device type) - Windows clipboard.

You can allow or deny access to the clipboard to control the copy and paste operations through the Windows clipboard on a protected computer.

When you change the access setting for clipboard to Deny, the applications and processes accessing the clipboard must be restarted to enforce the newly configured access settings. To ensure that access settings are enforced correctly, restart the protected workloads.

This device type is supported only on Windows.

Screenshot capture (access control by device type) - Enables capturing of screenshots of the entire screen, the active window, or of selected portion of the screen.

You can allow or deny access to the screenshot capture to control the screenshot capturing on a protected computer.

When you change the access setting for screenshot capture to Deny, the applications and processes accessing the screenshot capture must be restarted to enforce the newly configured access settings. To ensure that access settings are enforced correctly, restart the protected workloads.

This device type is supported only on Windows.

Mobile devices (access control by device type) - Devices (such as Android-based smartphones, etc.) that communicate with a computer via Media Transfer Protocol (MTP), with any interface used for connecting to a computer (USB, IP, Bluetooth).

You can allow full access, allow read-only access, or deny access to mobile devices to control data copy operations to and from any MTP-based mobile device on a protected computer.

When you change the access setting for mobile devices to Read-only or Deny, the applications and processes accessing the mobile devices must be restarted to enforce the newly configured access settings. To ensure that access settings are enforced correctly, restart the protected workloads.

This device type is supported only on Windows.

Bluetooth (access control by device type) - External and internal Bluetooth devices with any interface for connecting to a computer (USB, PCMCIA, etc.). This setting controls the use of the devices of this type rather than data exchange using such devices.

You can allow or deny access to Bluetooth to control the use of any Bluetooth devices on a protected computer.

On macOS, the access rights for Bluetooth do not affect Bluetooth HID devices. The access to these devices is always allowed to prevent wireless HID devices (mice and keyboards) from being disabled on iMac and Mac Pro hardware.

This device type is supported on both Windows and macOS.

Optical drives (access control by device type) - External and internal CD/DVD/BD drives (including writers) with any interface for connecting to a computer (IDE, SATA, USB, FireWire, PCMCIA, etc.).

You can allow full access, allow read-only access, or deny access to optical drives to control data copy operations to and from any optical drive on a protected computer.

This device type is supported on both Windows and macOS.

Floppy drives (access control by device type) - External and internal floppy drives with any interface for connecting to a computer (IDE, USB, PCMCIA, etc.). There are some models of floppy drives that the operating system recognizes as removable drives, in which case the device control also identifies these drives as removable devices.

You can allow full access, allow read-only access, or deny access to floppy drives to control data copy operations to and from any floppy drive on a protected computer.

This device type is supported only on Windows.

USB (access control by device interface) - Any devices connected to a USB port, except hubs.

You can allow full access, allow read-only access, or deny access to USB port to control data copy operations to and from devices connected to any USB port on a protected computer.

This device type is supported on both Windows and macOS.

FireWire (access control by device interface) - Any devices connected to a FireWire (IEEE 1394) port, except hubs.

You can allow full access, allow read-only access, or deny access to FireWire port to control data copy operations to and from devices connected to any FireWire port on a protected computer.

This device type is supported on both Windows and macOS.

Redirected devices (access control by device interface) - Mapped drives (hard, removable and optical drives), USB devices, and the clipboard redirected to virtual application/desktop sessions.

The device control recognizes devices redirected via the Microsoft RDP, Citrix ICA, VMware PCoIP, and HTML5/WebSockets remoting protocols in the Microsoft RDS, Citrix XenDesktop, Citrix XenApp, Citrix XenServer, and VMware Horizon virtualization environments hosted on protected Windows computers. It can also control data copy operations between the Windows clipboard of the guest operating system running on VMware Workstation, VMware Player, Oracle VM VirtualBox, or Windows Virtual PC, and the clipboard of the host operating system running on a protected Windows computer.

This device type is supported only on Windows.

You can configure access to redirected devices as follows:

Mapped drives - Allow full access, allow read-only access, or deny access to control data copy operations to and from any hard drive, removable drive, or optical drive redirected to the session hosted on a protected computer.
Clipboard incoming - Allow or deny access to control data copy operations through the clipboard to the session hosted on a protected computer.
When you change the access setting for clipboard incoming to Deny, the applications and processes accessing the clipboard must be restarted to enforce the newly configured access settings. To ensure that access settings are enforced correctly, restart the protected workloads.
Clipboard outgoing - Allow or deny access to control data copy operations through the clipboard from the session hosted on a protected computer.
When you change the access setting for clipboard outgoing to Deny, the applications and processes accessing the clipboard must be restarted to enforce the newly configured access settings. To ensure that access settings are enforced correctly, restart the protected workloads.
USB ports - Allow or deny access to control data copy operations to and from devices connected to any USB port redirected to the session hosted on a protected computer.

Device control settings affect all users equally. For example, if you deny access to removable devices, you prevent any user from copying data to and from such devices on a protected computer. It is possible to selectively allow access to individual USB devices by excluding them from access control (see Device types allowlist and USB devices allowlist).

When access to a device is controlled by both its type and its interface, denying access at the interface level takes precedence. For example, if access to USB ports is denied (device interface), then access to mobile devices connected to a USB port is denied regardless of whether access to mobile devices is allowed or denied (device type). To allow access to such a device, you must allow both its interface and type.

If the protection plan used on macOS has settings for device types that are supported only on Windows, then the settings for these device types will be ignored on macOS.

When a removable device, an encrypted removable device, a printer, or a Bluetooth device is connected to a USB port, allowing access to that device overrides the access denial set at the USB interface level. If you allow such a device type, access to the device is allowed regardless of whether access to the USB port is denied.
See also
View or change access settings
Enabling the use of the device control module on macOS

OS notification and service alerts

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.