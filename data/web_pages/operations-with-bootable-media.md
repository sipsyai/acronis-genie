# Local operations with bootable media

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Local operations with bootable media
Local operations with bootable media

Operations with bootable media are similar to the recovery operations that are performed under a running operating system. The differences are as follows:

Under bootable media with a Windows-like volume representation, a volume has the same drive letter as in Windows. Volumes that do not have drive letters in Windows (such as the System Reserved volume) are assigned free letters in order of their sequence on the disk.

If the bootable media cannot detect Windows on the machine or detects more than one, all volumes, including those without drive letters, are assigned letters in order of their sequence on the disk. Thus, the volume letters may differ from those seen in Windows. For example, the D: drive under the bootable media might correspond to the E: drive in Windows.

It is advisable to assign unique names to the volumes.

The bootable media with a Linux-like volume representation shows local disks and volumes as unmounted (sda1, sda2...).
Tasks cannot be scheduled. If you need to repeat an operation, configure it from scratch.
The log lifetime is limited to the current session. You can save the entire log or the filtered log entries to a file.
Setting up a display mode

When you boot a machine via Linux-based bootable media, a display video mode is detected automatically based on the hardware configuration (monitor and graphics card specifications). If the video mode is detected incorrectly, do the following:

In the boot menu, press F11.
On the command line, enter vga=ask, and then proceed with booting.
From the list of supported video modes, choose the appropriate mode by typing its number (for example, 318), and then press Enter.

If you do not want to follow this procedure every time you boot a given hardware configuration, recreate the bootable media with the appropriate mode number (in the example above, vga=0x318) specified in the Kernel parameters field.

Recovering data with locally run bootable media

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.