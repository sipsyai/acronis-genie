---
title: "Device control access settings"
section: "Managing workloads in the Cyber Protect console"
subsection: "Working with the Device control module"
page_range: "432-440"
tags: [device control, access settings, device types, notifications, alerts, peripheral devices]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#dc-ht-settings.html"
---

# Access settings

On the **Access settings** page, you can allow or deny access to devices of certain types, as well as enable or disable OS notification and device control alerts.

> **Note:** The access settings configured in Device control might be overridden when using both Device control and Data Loss Prevention to protect a workload. See "Enabling Data Loss Prevention in protection plans."

## View or change access settings

1. Open the protection plan panel for a protection plan and enable device control in that plan.
2. Click the arrow icon next to the **Device control** switch to expand the settings, and then click the link next to **Access settings**.
3. On the page for managing access settings that appears, view or change access settings as appropriate.

## Device types and ports

The access settings allow you to limit user access to the following device types and ports:

### By device type

- **Removable** -- Devices with any interface for connecting to a computer (USB, FireWire, PCMCIA, IDE, SATA, SCSI, etc.) that are recognized by the operating system as removable storage devices (USB sticks, card readers, magneto-optical drives, etc.). The device control classifies all hard drives connected via USB, FireWire, and PCMCIA as removable devices. You can allow full access, read-only access, or deny access. Access rights do not affect devices encrypted with BitLocker or FileVault (only HFS+ file system). Supported on both Windows and macOS.

- **Encrypted removable** -- Removable devices that are encrypted with BitLocker (on Windows) or FileVault (on macOS) drive encryption. On macOS, only encrypted removable drives using the HFS+ file system are supported. Encrypted removable drives using the APFS file system are treated as removable drives. You can allow full access, read-only access, or deny access. Access rights affect only devices encrypted with BitLocker or FileVault (only HFS+ file system). Supported on both Windows and macOS.

- **Printers** -- Physical printers with any interface for connecting to a computer (USB, LPT, Bluetooth, etc.), as well as printers accessed from a computer on the network. You can allow or deny access to control the printing of documents on any printer on a protected computer. Supported only on Windows.

  > **Note:** When you change the access setting for printers to **Deny**, the applications and processes accessing the printers must be restarted to enforce the newly configured access settings.

- **Clipboard** -- Windows clipboard. You can allow or deny access to the clipboard to control the copy and paste operations through the Windows clipboard on a protected computer. Supported only on Windows.

  > **Note:** When you change the access setting for clipboard to **Deny**, the applications and processes accessing the clipboard must be restarted.

- **Screenshot capture** -- Enables capturing of screenshots of the entire screen, the active window, or of selected portion of the screen. You can allow or deny access to the screenshot capture. Supported only on Windows.

  > **Note:** When you change the access setting for screenshot capture to **Deny**, processes accessing the screenshot capture must be restarted.

- **Mobile devices** -- Devices (such as Android-based smartphones, etc.) that communicate with a computer via Media Transfer Protocol (MTP), with any interface used for connecting (USB, IP, Bluetooth). You can allow full access, read-only access, or deny access. Supported only on Windows.

  > **Note:** When you change the access setting for mobile devices to **Read-only** or **Deny**, the applications and processes accessing the mobile devices must be restarted.

- **Bluetooth** -- External and internal Bluetooth devices with any interface for connecting to a computer (USB, PCMCIA, etc.). This setting controls the use of the devices of this type rather than data exchange using such devices. You can allow or deny access. Supported on both Windows and macOS.

  > **Note:** On macOS, the access rights for Bluetooth do not affect Bluetooth HID devices. The access to these devices is always allowed to prevent wireless HID devices (mice and keyboards) from being disabled on iMac and Mac Pro hardware.

- **Optical drives** -- External and internal CD/DVD/BD drives (including writers) with any interface for connecting (IDE, SATA, USB, FireWire, PCMCIA, etc.). You can allow full access, allow read-only access, or deny access. Supported on both Windows and macOS.

- **Floppy drives** -- External and internal floppy drives with any interface for connecting (IDE, USB, PCMCIA, etc.). Some models of floppy drives that the operating system recognizes as removable drives are also identified as removable devices by the device control. You can allow full access, allow read-only access, or deny access. Supported only on Windows.

### By device interface

- **USB** -- Any devices connected to a USB port, except hubs. You can allow full access, allow read-only access, or deny access. Supported on both Windows and macOS.

- **FireWire** -- Any devices connected to a FireWire (IEEE 1394) port, except hubs. You can allow full access, allow read-only access, or deny access. Supported on both Windows and macOS.

### Redirected devices

- **Redirected devices** -- Mapped drives (hard, removable, and optical drives), USB devices, and the clipboard redirected to virtual application/desktop sessions. The device control recognizes devices redirected via Microsoft RDP, Citrix ICA, VMware PCoIP, and HTML5/WebSockets remoting protocols in Microsoft RDS, Citrix XenDesktop, Citrix XenApp, Citrix XenServer, and VMware Horizon. Supported only on Windows.

  You can configure access to redirected devices as follows:
  - **Mapped drives** -- Allow full access, allow read-only access, or deny access to and from any hard drive, removable drive, or optical drive redirected to the session.
  - **Clipboard incoming** -- Allow or deny access to control data copy operations through the clipboard to the session hosted on a protected computer.
  - **Clipboard outgoing** -- Allow or deny access to control data copy operations through the clipboard from the session hosted on a protected computer.
  - **USB ports** -- Allow or deny access to control data copy operations to and from devices connected to any USB port redirected to the session.

## Access control precedence

When access to a device is controlled by both its type and its interface, denying access at the interface level takes precedence. For example, if access to USB ports is denied (device interface), then access to mobile devices connected to a USB port is denied regardless of whether access to mobile devices is allowed or denied (device type). To allow access to such a device, you must allow both its interface and type.

> **Note:** If the protection plan used on macOS has settings for device types that are supported only on Windows, then the settings for these device types will be ignored on macOS.

> **Important:** When a removable device, an encrypted removable device, a printer, or a Bluetooth device is connected to a USB port, allowing access to that device overrides the access denial set at the USB interface level. If you allow such a device type, access to the device is allowed regardless of whether access to the USB port is denied.

## Enable or disable OS notification and service alerts

### To enable or disable OS notification

1. Follow the steps to view or change access settings.
2. On the page for managing access settings, select or clear the **Show OS notification to end users if they try to use a blocked device type or port** check box.

### To enable or disable service alerts

1. Follow the steps to view or change access settings.
2. On the page for managing access settings, select or clear the **Show alert** check box for the desired device type/s.

The **Show alert** check box is available only for device types with restricted access (Read-only or Denied access), except screenshot capture.
