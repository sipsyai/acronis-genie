# Creating WinPE or WinRE bootable media

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Bootable Media Builder > Creating WinPE or WinRE bootable media
Creating WinPE or WinRE bootable media

Bootable Media Builder provides two methods of integrating Cyber Protection with WinPE and WinRE:

Creating an ISO file with the Cyber Protection plugin from scratch.
Adding the Cyber Protection plugin to a WIM file for any future purpose (manual ISO building, adding other tools to the image and so on).

To create WinPE or WinRE bootable media

On the machine where the protection agent is installed, run Bootable Media Builder.

In Bootable media type, select Windows PE or Windows PE (64-bit). A 64-bit media is required to boot a machine that uses Unified Extensible Firmware Interface (UEFI).

Select the subtype of the bootable media: WinRE or WinPE.

Creating WinRE bootable media does not require installation of any additional packages.

To create a 64-bit WinPE media, you must download Windows Automated Installation Kit (AIK) or Windows Assessment and Deployment Kit (ADK). To create 32-bit WinPE media, in addition to downloading the AIK or ADK, you need to do the following:

Click Download the Plug-in for WinPE (32-bit).
Save the plugin to %PROGRAM_FILES%\BackupClient\BootableComponents\WinPE32.

Select the language for the bootable media.

Select the boot mode (BIOS or UEFI) that Windows will use after the recovery.

Specify the network settings for the network adapters of the booted machine or keep the automatic DHCP configuration.

Select how to register the bootable media in the Cyber Protection service on booting up. For more information about the registration settings, refer to Registering the bootable media.

[Optional] Specify the Windows drivers to be added to the bootable media.

After you boot a machine into Windows PE or Windows RE, the drivers can help you access the device where the backup is located. Add 32-bit drivers if you use a 32-bit WinPE or WinRE distribution or 64-bit drivers if you use a 64-bit WinPE or WinRE distribution.

To add the drivers:

Click Add, and then specify the path to the necessary .inf file for a corresponding SCSI, RAID, SATA controller, network adapter, or other device.
Repeat this procedure for each driver that you want to include in the resulting WinPE or WinRE media.

Select the file type of the created bootable media:

ISO image

WIM image

Specify the full path to the resulting image file, including the file name.
Check your settings in the summary screen, and then click Proceed.

To create a PE image (ISO file) from the resulting WIM file

Replace the default boot.wim file in your Windows PE folder with the newly created WIM file. For the above example, type:

copy c:\RecoveryWIMMedia.wim c:\winpe_x86\ISO\sources\boot.wim

Use the Oscdimg tool. For the above example, type:

oscdimg -n -bc:\winpe_x86\etfsboot.com c:\winpe_x86\ISO c:\winpe_x86\winpe_x86.iso

Do not copy and paste this example. Type the command manually, otherwise it will fail.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.