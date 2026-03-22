# Boot mode

Managing the backup and recovery of workloads and files > Recovery > Recovery options > Boot mode
Boot mode

This option is effective when recovering a physical or a virtual machine from a disk-level backup that contains a Windows operating system.

This option enables you to select the boot mode (BIOS or UEFI) that Windows will use after the recovery. If the boot mode of the original machine is different from the selected boot mode, the software will:

Initialize the disk to which you are recovering the system volume, according to the selected boot mode (MBR for BIOS, GPT for UEFI).
Adjust the Windows operating system so that it can start using the selected boot mode.

The preset is: As on the target machine.

You can choose one of the following:

As on the target machine

The agent that is running on the target machine detects the boot mode currently used by Windows and makes the adjustments according to the detected boot mode.

This is the safest value that automatically results in bootable system unless the limitations listed below apply. Since the Boot mode option is absent under bootable media, the agent on media always behaves as if this value is chosen.

As on the backed-up machine

The agent that is running on the target machine reads the boot mode from the backup and makes the adjustments according to this boot mode. This helps you recover a system on a different machine, even if this machine uses another boot mode, and then replace the disk in the backed-up machine.

BIOS

The agent that is running on the target machine makes the adjustments to use BIOS.

UEFI

The agent that is running on the target machine makes the adjustments to use UEFI.

Once a setting is changed, the disk mapping procedure will be repeated. This will take some time.

Recommendations

If you need to transfer Windows between UEFI and BIOS:

Recover the entire disk where the system volume is located. If you recover only the system volume on top of an existing volume, the agent will not be able to initialize the target disk properly.
Remember that BIOS does not allow using more than 2 TB of disk space.
Limitations

Transferring between UEFI and BIOS is supported for:

64-bit Windows operating systems starting with Windows 7
64-bit Windows Server operating systems starting with Windows Server 2008 SP1

When transferring a system between UEFI and BIOS is not supported, the agent behaves as if the As on the backed-up machine setting is chosen. If the target machine supports both UEFI and BIOS, you need to manually enable the boot mode corresponding to the original machine. Otherwise, the system will not boot.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.