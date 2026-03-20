---
title: "Recovery with restart, Universal Restore, and recovery options"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery"
page_range: "663-676"
tags: ["recovery-with-restart", "WinRE", "Universal-Restore", "recovery-options", "boot-mode", "BIOS", "UEFI", "flashback", "SID-changing", "VM-power-management", "safe-recovery", "malware-scan", "file-exclusions", "file-level-security", "mount-points", "performance"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#universal-restore-in-windows.html"
---

# Recovery with restart

A restart is required when you recover an operating system (e.g., entire machine or system volume) or encrypted volumes (e.g., BitLocker-encrypted or CheckPoint-encrypted volumes).

> **Important:** Backed-up encrypted volumes are recovered as non-encrypted.

A recovery environment is automatically prepared on the recovered machine. When the environment is ready, the machine restarts, the recovery environment opens, and when the recovery completes, the operating system starts.

## Recovery environments

| Recovered machine | WinRE | Linux |
|---|---|---|
| Windows | Yes (Default)* | Yes |
| Linux | N/A | Yes |

*If the default WinRE recovery environment cannot start, the recovery operation will automatically switch to the Linux environment.

### Disk space requirements

| Boot mode | Non-encrypted system volume | Encrypted system volume |
|---|---|---|
| BIOS | 1 GB in Windows\Temp + 200 MB on system volume | 1 GB in Windows\Temp + 400 MB on an unencrypted volume |
| UEFI | 1 GB in Windows\Temp + 200 MB on EFI system partition (ESP) | 1 GB in Windows\Temp + 400 MB on ESP (or 200 MB on ESP + 200 MB on an unencrypted partition accessible during boot) |

### Changing the recovery environment

You can change the default recovery environment on Windows workloads via registry:

**To set WinRE:**
1. Open **Regedit**.
2. Go to `HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings`.
3. Create a new string value named `RebootEnvironmentType`.
4. Set value data to `Windows`.

**To set Linux:** Same steps, but set value data to `Linux`.

**To reset to default:** Delete the `RebootEnvironmentType` string value.

### Troubleshooting

If a recovery fails and the error "Cannot get file from partition" is shown after restart, disable Secure Boot.

# Using Universal Restore

Most recent operating systems remain bootable when recovered to dissimilar hardware, including VMware or Hyper-V platforms. If a recovered operating system does not boot, use the Universal Restore tool to update the drivers and modules critical for startup.

Universal Restore is applicable to Windows and Linux.

## To apply Universal Restore

1. Boot the machine from the bootable media.
2. Click **Apply Universal Restore**.
3. If there are multiple operating systems, choose the one to apply Universal Restore to.
4. [For Windows only] Configure the additional settings.
5. Click **OK**.

## Universal Restore in Windows

### Preparation

Prepare drivers for the new HDD controller and chipset (critical for OS startup). Driver files should have the `.inf` extension. If downloaded in `.exe`, `.cab`, or `.zip` format, extract them first.

Best practice: maintain a single driver repository sorted by device type or hardware configuration.

### Universal Restore settings

- **Automatic driver search** -- Specify where to search for HAL, HDD controller, and network adapter drivers:
  - Turn on **Search removable media** if drivers are on vendor's disc/removable media.
  - Click **Add folder** to specify a path to a networked folder or bootable media location.
  - Universal Restore also searches the Windows default driver storage folder (typically `WINDOWS/inf`).
- **Mass storage drivers to install anyway** -- Use this when:
  - Hardware has a specific mass storage controller (e.g., NVIDIA RAID, fibre channel adapter).
  - You migrated a system to a virtual machine with a SCSI hard drive controller.
  - Automatic driver search does not help boot the system.
  - Click **Add driver** to specify drivers that will be forcibly installed.

### Universal Restore process

If Universal Restore cannot find a compatible driver, it will display a prompt. You can:
- Add the driver to the previously specified locations and click **Retry**.
- Click **Ignore** to continue. Reapply Universal Restore if the result is not satisfactory.

Once Windows boots, it will initialize the standard procedure for installing new hardware.

## Universal Restore in Linux

Universal Restore can be applied to Linux operating systems with a kernel version of 2.6.8 or later.

It updates a temporary file system known as the initial RAM disk (initrd). This ensures that the operating system can boot on the new hardware. Universal Restore adds modules for the new hardware (including device drivers) to the initial RAM disk. It finds the necessary modules in the `/lib/modules` directory.

Universal Restore may modify the GRUB boot loader configuration to ensure system bootability. Universal Restore never modifies the Linux kernel.

### Reverting to the original initial RAM disk

The initial RAM disk is stored on the machine in a file. Before updating, Universal Restore saves a copy with the `_acronis_backup.img` suffix. To revert, rename the backup copy accordingly or specify it in the `initrd` line of the GRUB boot loader configuration.

# Recovery options

The set of available recovery options depends on the environment (Windows, Linux, macOS, bootable media) and the type of data being recovered (disks, files, VMs, application data).

## Recovery options summary

| Option | Disks (Win/Linux/Media) | Files (Win/Linux/macOS/Media) | VMs (ESXi/Hyper-V/etc.) | Azure | SQL/Exchange |
|---|---|---|---|---|---|
| Backup validation | + / + / + | + / + / + / + | + | - | + |
| Boot mode | + / - / - | - | + | - | - |
| Date and time for files | - | + / + / + / + | - | - | - |
| Error handling | + / + / + | + / + / + / + | + | + | + |
| File exclusions | - | + / + / - / + | - | - | - |
| File-level security | + / - / - | + / - / - / - | - | - | - |
| Flashback | + / + / + | - | + | - | - |
| Full path recovery | + / - / - | + / + / + / + | - | - | - |
| Mount points | - | + / - / - / - | - | - | - |
| Performance | + / + / - | + / + / + / - | + | - | + |
| Pre/Post commands | + / + / - | + / + / + / - | + | - | + |
| SID changing | + / - / - | - | - | - | - |
| VM power management | - | - | + | + | - |
| Windows event log | + / - / - | + / - / - / - | Hyper-V only | - | + |

## Key recovery options

### Boot mode

Preset: **As on the target machine.** Options: As on the target machine, As on the backed-up machine, BIOS, UEFI.

This option enables you to select the boot mode (BIOS or UEFI) that Windows will use after recovery. If the boot mode of the original machine differs from the selected boot mode, the software initializes the disk (MBR for BIOS, GPT for UEFI) and adjusts the OS accordingly.

Transferring between UEFI and BIOS is supported for 64-bit Windows starting with Windows 7 / Windows Server 2008 SP1. BIOS does not allow using more than 2 TB of disk space.

### Flashback

Preset: **Disabled** (physical machines), **Enabled** (virtual machines).

Works only if the volume layout of the disk being recovered exactly matches that of the target disk. If enabled, only the differences are recovered, which accelerates disk and volume recovery.

### Safe recovery

Use safe recovery with **Entire machine** or **Disks/volumes** backups of Windows workloads to ensure you recover only malware-free data. During a safe recovery, the backup is automatically scanned for malware, the protection agent recovers the backup on the target workload, and deletes any infected files.

Statuses assigned to backups: **Malware detected**, **No malware**, **Not scanned**.

**Limitations:**
- Supported for physical and virtual Windows machines with a protection agent installed.
- Supported for **Entire machine** and **Disks/volumes** backups only.
- Only NTFS volumes are scanned. Non-NTFS volumes are recovered without antimalware scanning.
- Not supported for CDP backups. To recover CDP data, run an additional **Files/folders** recovery.

### VM power management

- **Power off target virtual machines when starting recovery** -- Preset: **Enabled**. Recovery to an existing running VM is not possible, so the VM is powered off automatically.
- **Power on the target virtual machine when recovery is complete** -- Preset: **Disabled**. Power on manually after taking necessary precautions (e.g., to prevent network conflicts with the original machine's replica).

### SID changing

Preset: **Disabled**. Effective when recovering Windows 8.1/Windows Server 2012 R2 or earlier. Generates a unique security identifier (Computer SID) for the recovered OS. Microsoft does not officially support changing SID on a deployed or recovered system -- use at your own risk.
