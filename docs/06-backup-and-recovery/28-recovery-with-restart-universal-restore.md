---
title: "Recovery with Restart and Universal Restore"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery with restart and Universal Restore"
page_range: "663-668"
tags: [recovery-with-restart, recovery-environment, WinRE, universal-restore, drivers, bootable-media, BIOS, UEFI, Linux, Windows]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#recovery-with-restart.html"
---

# Recovery with Restart

A restart is required when you recover the following:

- **An operating system** -- for example, when you recover an entire machine or the system volume of a machine.
- **Encrypted volumes** -- for example, when you recover BitLocker-encrypted or CheckPoint-encrypted volumes.

> **Important:** Backed-up encrypted volumes are recovered as non-encrypted.

A recovery environment is automatically prepared on the recovered machine. When the environment is ready, the machine restarts, and then the recovery environment opens. When the recovery completes, the operating system starts.

> **Note:** Preparing the WinRE recovery environment might take up to three minutes.

## Recovery Environments

You can use WinRE or Linux recovery environment.

| Recovered machine | WinRE | Linux |
|---|---|---|
| Windows | Yes (Default)* | Yes |
| Linux | N/A | Yes |

> **Note:** * If the default WinRE recovery environment cannot start, the recovery operation will automatically switch to the Linux environment. If you explicitly set the recovery environment to either WinRE or Linux, only the selected environment will be used.

## Disk Space Requirements

The recovery environment requires disk space for temporary files. The requirements vary depending on the recovered machine.

| Boot mode | Machine with non-encrypted system volume | Machine with encrypted system volume |
|---|---|---|
| BIOS | 1 GB in the `Windows\Temp` folder | 1 GB in the `Windows\Temp` folder |
| UEFI | 1 GB in the `Windows\Temp` folder | 1 GB in the `Windows\Temp` folder |
| BIOS | 200 MB on the system volume | 400 MB on an unencrypted volume |
| UEFI | 200 MB on the EFI system partition (ESP) | 400 MB on the EFI system partition (ESP), or 200 MB on ESP and 200 MB on an unencrypted partition accessible during boot |

* Recovery of a machine with encrypted system volume requires at least one non-encrypted volume on the same machine.

## Limitations

- Before recovery, you must lock all encrypted non-system volumes. You can lock a volume by opening a file that resides on it. If the volume is not locked, the recovery will continue without restart, and the volume might not be recognized by the operating system.
- You do not need to lock an encrypted system volume.

## Troubleshooting

If a recovery fails and the error `Cannot get file from partition` is shown after restart, disable Secure Boot.

## Changing the Recovery Environment

You can change the default recovery environment on Windows workloads. On Linux workloads, only the Linux recovery environment is available.

### To set WinRE

1. In Windows, open **Regedit**.
2. Go to `HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings`.
3. Create a new string value, and then name it **RebootEnvironmentType**.
4. Open the string value for editing.
5. In **Value data**, specify `Windows`.
6. Click **OK**.

### To set Linux

1. In Windows, open **Regedit**.
2. Go to `HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings`.
3. Create a new string value, and then name it **RebootEnvironmentType**.
4. Open the string value for editing.
5. In **Value data**, specify `Linux`.
6. Click **OK**.

### To reset the default settings

1. In Windows, open **Regedit**.
2. Go to `HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings`.
3. Delete the **RebootEnvironmentType** string value.
4. To confirm your choice, click **Yes**.

# Using Universal Restore

The most recent operating systems remain bootable when recovered to dissimilar hardware, including the VMware or Hyper-V platforms. If a recovered operating system does not boot, use the Universal Restore tool to update the drivers and modules that are critical for the operating system startup.

Universal Restore is applicable to Windows and Linux.

## To Apply Universal Restore

1. Boot the machine from the bootable media.
2. Click **Apply Universal Restore**.
3. If there are multiple operating systems on the machine, choose the one to apply Universal Restore to.
4. [For Windows only] Configure the additional settings.
5. Click **OK**.

## Universal Restore in Windows

### Preparation -- Prepare Drivers

Before applying Universal Restore to a Windows operating system, make sure that you have the drivers for the new HDD controller and the chipset. These drivers are critical to start the operating system. Use the CD or DVD supplied by the hardware vendor or download the drivers from the vendor's website. The driver files should have the `*.inf` extension.

The best practice is to store drivers for all the hardware used in your organization in a single repository sorted by device type or by hardware configurations. Keep a copy of the repository on a DVD or flash drive, pick some drivers and add them to the bootable media, or create the custom bootable media with the necessary drivers for each of your servers. Or simply specify the path to the repository every time Universal Restore is used.

### Universal Restore Settings

**Automatic driver search:** Specify where the program will search for the Hardware Abstraction Layer (HAL), HDD controller driver, and network adapter driver(s):

- If the drivers are on a vendor's disc or other removable media, turn on the **Search removable media**.
- If the drivers are in a networked folder or on the bootable media, specify the path by clicking **Add folder**.

Universal Restore will also search the Windows default driver storage folder (`WINDOWS/inf`).

Universal Restore searches recursively in all sub-folders of the specified folder, finds the most suitable HAL and HDD controller drivers of all those available, and installs them into the system. Universal Restore also searches for the network adapter driver; the path to the found driver is then transmitted to the operating system.

**Mass storage drivers to install anyway:** Use this setting if:

- The hardware has a specific mass storage controller such as RAID (especially NVIDIA RAID) or a fibre channel adapter.
- You migrated a system to a virtual machine that uses a SCSI hard drive controller.
- If the automatic drivers search does not help to boot the system.

Specify the appropriate drivers by clicking **Add driver**. The drivers defined here will be installed with appropriate warnings, even if the program finds a better driver.

### Universal Restore Process

After you have specified the required settings, click **OK**. If Universal Restore cannot find a compatible driver in the specified locations, it will display a prompt about the problem device. Do one of the following:

- Add the driver to any of the previously specified locations and click **Retry**.
- If you do not remember the location, click **Ignore** to continue the process. If the result is not satisfactory, reapply Universal Restore, specifying the necessary driver.

Once Windows boots, it will initialize the standard procedure for installing new hardware. The network adapter driver will be installed silently if the driver has the Microsoft Windows signature. Otherwise, Windows will ask for confirmation to install the unsigned driver.

## Universal Restore in Linux

Universal Restore can be applied to Linux operating systems with a kernel version of 2.6.8 or later.

When Universal Restore is applied to a Linux operating system, it updates a temporary file system known as the initial RAM disk (initrd). This ensures that the operating system can boot on the new hardware.

Universal Restore adds modules for the new hardware (including device drivers) to the initial RAM disk. As a rule, it finds the necessary modules in the `/lib/modules` directory. If Universal Restore cannot find a module it needs, it records the module's file name into the log.

Universal Restore may modify the configuration of the GRUB boot loader. This may be required, for example, to ensure the system bootability when the new machine has a different volume layout than the original machine. Universal Restore never modifies the Linux kernel.

### Reverting to the Original Initial RAM Disk

You can revert to the original initial RAM disk if necessary. The initial RAM disk is stored on the machine in a file. Before updating the initial RAM disk for the first time, Universal Restore saves a copy of it to the same directory. The name of the copy is the name of the file, followed by the **_acronis_backup.img** suffix. This copy will not be overwritten if you run Universal Restore more than once.

To revert to the original initial RAM disk, do any of the following:

- Rename the copy accordingly. For example:
  ```
  mv initrd-2.6.16.60-0.21-default_acronis_backup.img initrd-2.6.16.60-0.21-default
  ```
- Specify the copy in the **initrd** line of the GRUB boot loader configuration.
