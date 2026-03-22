# Linux-based bootable media

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Bootable Media Builder > Linux-based bootable media
Linux-based bootable media

To create a Linux-based bootable media

Start Bootable Media Builder.

In Bootable media type, select Default (Linux-based media).

Select how volumes and network resources will be represented:
Bootable media with a Linux-like volume representation displays the volumes as, for example, hda1 and sdb2. It tries to reconstruct MD devices and logical volumes (LVM) before starting a recovery.
Bootable media with Windows-like volume representation displays the volumes as, for example, C: and D:. It provides access to dynamic volumes (LDM).

[Optional] Specify the parameters of the Linux kernel. Separate multiple parameters with spaces.

For example, to be able to select a display mode for the bootable agent each time the media starts, type: vga=ask. For more information about the available parameters, refer to Kernel parameters.

Select the language for the bootable media.

Select the boot mode (BIOS or UEFI) that Windows will use after the recovery.

Select the component to be placed on the media – the Cyber Protection bootable agent.

Specify the timeout interval for the boot menu. If this setting is not configured, the loader will wait for you to select whether to boot the operating system (if present) or the component.

If you want to automate the bootable agent operations, select the Use the following script check box. Then, select one of the scripts and specify the script parameters. For more information about the scripts, refer to Scripts in bootable media.

Select how to register the bootable media in the Cyber Protection service on booting up. For more information about the registration settings, refer to Registering the bootable media.

Specify the network settings for the network adapters of the booted machine or keep the automatic DHCP configuration.

If a proxy server is enabled in your network, specify its host name/IP address and port.

To specify the network authentication method, click Wi-Fi settings, and then select one of the following:

Open authentication
WEP
WEP Shared
IEEE 802.1X
WPA Personal
WPA Enterprise
WPA2 Personal
WPA2 Enterprise

Select the file type of the created bootable media:

ISO image
ZIP file
Specify a file name for the bootable media file.
Check your settings in the summary screen, and then click Proceed.

Kernel parameters

Scripts in bootable media

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.