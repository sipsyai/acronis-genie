# Startup Recovery Manager

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Startup Recovery Manager
Startup Recovery Manager

Startup Recovery Manager is a bootable component that resides on the hard drive. With Startup Recovery Manager, you can start the bootable rescue utility without using a separate bootable media.

If a failure occurs, restart the machine, wait for the prompt Press F11 for Acronis Startup Recovery Manager to appear, and then press F11 or select the Startup Recovery Manager from the boot menu (if you use the GRUB boot loader). Startup Recovery Manager starts and you can perform a recovery.

Startup Recovery Manager is supported for Windows and Linux machines.

Activating Startup Recovery Manager on a machine with encrypted system volume requires at least one non-encrypted volume on the same machine.
Disk space requirements

Startup Recovery Manager requires disk space for temporary files. The requirements vary according to the machine on which Startup Recovery Manager is activated.

The table below summarizes the available options.

Boot mode	Machine without Secure Zone	Machine with Secure Zone
With non-encrypted system volume	With encrypted system volume	With encrypted or non-encrypted system volume
BIOS

200 MB on the system volume

400 MB on an unencrypted volume	400 MB on the Secure Zone
UEFI	200 MB on the EFI system partition (ESP)

One of the following:

400 MB on the EFI system partition (ESP)

200 MB on the EFI system partition (ESP) and 200 MB on an unencrypted partition that is accessible during the boot process

400 MB on the Secure Zone
Recovery with restart requires additional disk space. To check how much additional space is required, see Disk space requirements.
Limitations

[Not applicable to GRUB that is installed to the master boot record] Activating Startup Recovery Manager overwrites the master boot record (MBR) with its own boot code. As a result, you might need to reactivate any third-party boot loaders after the activation.

[Not applicable to GRUB] Before activating Startup Recovery Manager in Linux, we recommend that you install the boot loader to the root partition's boot record or to the /boot partitions' boot record instead of installing it to the master boot record. Otherwise, manually reconfigure the boot loader after the activation.

Activating Startup Recovery Manager

Deactivating Startup Recovery Manager

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.