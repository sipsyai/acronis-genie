---
title: "Creating Bootable Media to Recover Operating Systems"
section: "Managing the backup and recovery of workloads and files"
subsection: "Bootable media"
page_range: "906-929"
tags: [bootable-media, Linux-based, WinPE, WinRE, Bootable-Media-Builder, ISO, kernel-parameters, scripts, autostart-json, registration, network-settings, VLAN, NIC-teaming, Startup-Recovery-Manager, remote-operations]
acronis_version: "26.02"
---

# Creating Bootable Media to Recover Operating Systems

Bootable media is a CD, DVD, USB flash drive, or other removable media that allows you to run the protection agent in a Linux-based environment or a Windows Preinstallation Environment / Windows Recovery Environment (WinPE/WinRE), without the help of an operating system. The main purpose is to recover an operating system that cannot start.

> **Note:** Bootable media does not support hybrid drives. Running it requires 1.5 GB of RAM.

## Custom or Ready-Made Bootable Media?

**Bootable Media Builder** creates custom bootable media (Linux-based or WinPE-based) for Windows, Linux, or macOS computers. In custom media, you can configure additional settings such as automatic registration, network settings, or proxy server settings. In WinPE/WinRE-based custom media, you can also add additional drivers.

**Ready-made bootable media** (Linux-based only) is available for download from the Cyber Protect console and can be used for recovery and Universal Restore.

## Linux-Based or WinPE/WinRE-Based?

### Linux-Based

Contains a protection agent based on a Linux kernel. It can boot and perform operations on any PC-compatible hardware, including bare metal and machines with corrupted or non-supported file systems.

### WinPE/WinRE-Based

Contains a minimal Windows system (WinPE) and a Cyber Protection plugin for WinPE (a modification of the protection agent). WinRE-based bootable media uses Windows Recovery Environment and does not require installation of additional packages.

**Advantages of WinPE:**
- More functionality than Linux-based media in WinPE environments.
- PE-based media helps overcome Linux-related issues with certain RAID controllers.
- Dynamic loading of device drivers (WinPE 2.x and later).

**Limitation:** Bootable media based on WinPE versions earlier than 4.0 cannot boot on machines that use UEFI.

## Creating Physical Bootable Media

**In Windows or Linux:**
1. Create a custom ISO file using Bootable Media Builder, or download the ready-made ISO from the Cyber Protect console (**Recover** > **More ways to recover...** > **Download ISO image**).
2. [Optional] Generate a registration token for cloud storage access.
3. Create physical media:
   - Burn the ISO to a CD/DVD.
   - Create a bootable USB flash drive (use ISO to USB, RUFUS for UEFI; Win32DiskImager for BIOS; `dd` utility in Linux).
   - For VMs, connect the ISO as a CD/DVD drive.

**In macOS:**
1. Click **Applications** > **Rescue Media Builder**.
2. Select the connected removable media. All data will be erased.
3. Click **Create**.

## Bootable Media Builder

Bootable Media Builder is a dedicated tool installed as an optional component alongside the protection agent. It creates customized Linux-based or WinPE-based bootable media images.

### 32-bit or 64-bit?

Both 32-bit and 64-bit components are included. Use 64-bit media for UEFI machines.

### Creating Linux-Based Bootable Media

1. Start **Bootable Media Builder**.
2. Select **Default (Linux-based media)** as the type.
3. Select volume representation: Linux-like (hda1, sdb2...) or Windows-like (C:, D:...).
4. [Optional] Specify Linux kernel parameters (e.g., `vga=ask`, `acpi=off`, `noapic`, `quiet`, `nousb`, `nodma`, `pci=bios`, `pci=nobios`).
5. [Optional] Select the language.
6. [Optional] Select boot mode (BIOS or UEFI).
7. Select the component: Cyber Protection bootable agent.
8. [Optional] Specify boot menu timeout interval.
9. [Optional] Enable **Use the following script** to automate operations.
10. [Optional] Configure bootable media registration (automatic or token-based).
11. Configure network settings (static IP or DHCP).
12. [Optional] Configure proxy server.
13. [Optional] Configure Wi-Fi authentication (Open, WEP, WPA/WPA2 Personal/Enterprise, IEEE 802.1X).
14. Select file type: ISO image or ZIP file.
15. Specify the file name, review settings, and click **Proceed**.

### Kernel Parameters

Common parameters for troubleshooting:

| Parameter | Description |
|---|---|
| `acpi=off` | Disables ACPI (hardware configuration issues) |
| `noapic` | Disables APIC (hardware issues) |
| `vga=ask` | Prompts for video mode selection |
| `vga=<mode_number>` | Sets specific video mode (hex format, e.g., `vga=0x318`) |
| `quiet` | Disables startup messages, starts management console |
| `nousb` | Disables USB subsystem |
| `nousb2` | Disables USB 2.0 (USB 1.1 still works) |
| `nodma` | Disables DMA for IDE drives |
| `nofw` | Disables FireWire support |
| `nopcmcia` | Disables PCMCIA detection |
| `nomouse` | Disables mouse support |
| `module_name=off` | Disables specific module (e.g., `sata_sis=off`) |
| `pci=bios` | Forces PCI BIOS usage |
| `pci=nobios` | Disables PCI BIOS |
| `pci=biosirq` | Uses PCI BIOS for interrupt routing table |
| `LAYOUTS=en-US, de-DE, ...` | Specifies keyboard layouts |

### Scripts in Bootable Media

You can specify a script to automate operations. The script runs every time a machine is booted from the media (no user interface shown).

**Predefined scripts:**
- `entire_pc_cloud` -- Recovery from cloud storage
- `entire_pc_share` -- Recovery from network share

Scripts are located in:
- Windows: `%ProgramData%\Acronis\MediaBuilder\scripts\`
- Linux: `/var/lib/Acronis/MediaBuilder/scripts/`

**Custom scripts** require three files:
- `<script_file>.sh` -- Bash script using BusyBox commands plus `acrocmd` and `product`.
- `autostart` -- Shell script that sources `variables.sh`, the main script, and `post_actions.sh`.
- `autostart.json` -- JSON file defining script name, description, timeout, and variable controls for Bootable Media Builder.

### Structure of autostart.json

**Top-level object:**

| Name | Type | Required | Description |
|---|---|---|---|
| displayName | string | Yes | Script name shown in Bootable Media Builder |
| description | string | No | Script description |
| timeout | number | No | Boot menu timeout in seconds (default: 10) |
| variables | object | No | Variables configurable via Bootable Media Builder |

**Variable object properties:** displayName, type, order, description, default, min/max/step (for spinner), items (for enum), required.

**Control types:** string, multiString, password, number, spinner, enum, checkbox.

### Creating WinPE or WinRE Bootable Media

**WinRE images** can be created without additional preparation on Windows 7 (64-bit) through Windows Server 2025 (64-bit).

**WinPE images** require Windows Automated Installation Kit (AIK) or Windows Assessment and Deployment Kit (ADK).

1. Run Bootable Media Builder.
2. Select **Windows PE** or **Windows PE (64-bit)**.
3. Select subtype: **WinRE** or **WinPE**.
4. [Optional] Select language, boot mode.
5. Configure network settings.
6. [Optional] Configure registration.
7. [Optional] Add Windows drivers (.inf files).
8. Select file type (ISO or WIM image).
9. Specify file path, review, click **Proceed**.

## Registering the Bootable Media

Registration allows the bootable media to access cloud storage for backups.

**Preconfigure during media creation:**
1. In Bootable Media Builder, navigate to **Bootable media registration**.
2. Specify the Cyber Protection service URL.
3. [Optional] Specify a display name.
4. Select **Register the bootable media automatically**:
   - **Ask for registration token at booting up** -- token required each boot.
   - **Use the following token** -- automatic registration every boot.

**Register after booting:**
1. Boot from media, click **Register media**.
2. Enter the Cyber Protection service URL and registration token.
3. Click **Register**.

## Network Settings

Preconfigure TCP/IP for up to ten NICs. Settings include: IP address, subnet mask, gateway, DNS server, WINS server. The bootable agent assigns settings by MAC address, then by NIC slot order.

### Adding VLANs

In the **Network Settings** window, click **Add VLAN**, select the NIC, specify the VLAN identifier.

## Local and Remote Operations with Bootable Media

### Local Operations

1. Boot from media, click **Manage this machine locally**.
2. Click **Recover**, select backup data, configure recovery, click **OK**.

**Differences from OS-based operations:**
- Windows-like volume representation: volumes may have different drive letters.
- Linux-like representation: disks shown as unmounted (sda1, sda2...).
- Tasks cannot be scheduled; logs are limited to the current session.

### Remote Operations

After registering, media appears on **Devices** > **Bootable media** tab (disappears after 30 days offline).

**Recover files/folders remotely:**
1. Go to **Devices** > **Bootable media**, select the media.
2. Click **Recovery**, select backup location, then **Recover files/folders**.
3. Browse/search, select files, click **Recover**.
4. Specify destination path, click **Start recovery**.
5. Select overwrite options, choose restart behavior, click **Proceed**.

**Recover disks/volumes/entire machines remotely:**
1. Select the media, click **Recovery**.
2. Select backup, click **Recover** > **Entire machine**.
3. Configure target and volume mapping.
4. Click **Start recovery**, confirm.

You can also remotely: **Reboot**, **Shut down**, view **Details/Activities/Alerts**, and **Delete** the bootable media.

## NIC Teaming Support

NIC teaming (bonding) is preserved during recovery and after recovery. To disable NIC teaming during recovery, edit the configuration file:

- **Windows:** `C:\Program Files\Common Files\Acronis\BackupAndRecoveryAgent\bootagent_msp64.config`
- **Linux:** `/usr/lib/Acronis/BackupAndRecoveryAgent/bootagent_msp64.config`

Add `DONT_CREATE_BONDING=1` to the kernel64 value parameter, save, then recover using any supported method.

## Startup Recovery Manager

Startup Recovery Manager is a bootable component that resides on the hard drive. It allows starting the bootable rescue utility without separate bootable media. Press **F11** at boot (or select from the GRUB menu) when the prompt **Press F11 for Acronis Startup Recovery Manager** appears.

Supported for Windows and Linux machines.

> **Important:** Activating on a machine with an encrypted system volume requires at least one non-encrypted volume on the same machine.

### Disk Space Requirements

| Boot mode | Non-encrypted system volume (no Secure Zone) | Encrypted system volume (no Secure Zone) | Machine with Secure Zone |
|---|---|---|---|
| BIOS | 200 MB on system volume | 400 MB on an unencrypted volume | 400 MB on Secure Zone |
| UEFI | 200 MB on EFI system partition (ESP) | 400 MB on ESP, or 200 MB on ESP + 200 MB on an unencrypted boot-accessible partition | 400 MB on Secure Zone |

### Limitations

- Activating Startup Recovery Manager overwrites the MBR with its own boot code. You may need to reactivate third-party boot loaders afterward.
- In Linux, install the boot loader to the root or /boot partition's boot record instead of the MBR before activating.

### Activating Startup Recovery Manager

**On a machine with an agent:**
1. In the Cyber Protect console, select the machine, click **Details**.
2. Enable the **Startup Recovery Manager** switch.

**On a machine without an agent:**
1. Boot from bootable media.
2. Click **Tools** > **Activate Startup Recovery Manager**.
3. Select **Activate**, click **OK**.

### Deactivating Startup Recovery Manager

**On a machine with an agent:** Select the machine > **Details** > disable the **Startup Recovery Manager** switch.

**On a machine without an agent:** Boot from media > **Tools** > **Deactivate Startup Recovery Manager** > **Deactivate** > **OK**.

> **Note:** Backup operations that create One-click recovery backups will fail if Startup Recovery Manager is not activated.
