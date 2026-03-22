# Recovery environments

Managing the backup and recovery of workloads and files > Recovery > Recovery with restart > Recovery environments
Recovery environments

You can use WinRE or Linux recovery environment.

The table below summarizes the available options.

Recovered machine	Recovery environment
WinRE	Linux
Windows	Yes (Default)*	Yes
Linux	N/A	Yes

* If the default WinRE recovery environment cannot start, the recovery operation will automatically switch to the Linux environment. If you explicitly set the recovery environment either to WinRE or Linux, only the selected environment will be used. For more information, see Changing the recovery environment.

Preparing the WinRE recovery environment might take up to three minutes.

Disk space requirements

The recovery environment requires disk space for temporary files. The requirements vary depending on the recovered machine.

The table below summarizes the available options.

Boot mode	Machine with non-encrypted system volume	Machine with encrypted system volume
BIOS	1 GB in the Windows\Temp folder	1 GB in the Windows\Temp folder
UEFI	1 GB in the Windows\Temp folder	1 GB in the Windows\Temp folder
BIOS

200 MB on the system volume

400 MB on an unencrypted volume
UEFI	200 MB on the EFI system partition (ESP)

One of the following:

400 MB on the EFI system partition (ESP)

200 MB on the EFI system partition (ESP) and 200 MB on an unencrypted partition that is accessible during the boot process

* Recovery of a machine with encrypted system volume requires at least one non-encrypted volume on the same machine.

Limitations

Before recovery, you must lock all encrypted non-system volumes. You can lock a volume by opening a file that resides on it. If the volume is not locked, the recovery will continue without restart, and the volume might not be recognized by the operating system.

You do not need to lock an encrypted system volume.

Troubleshooting

If a recovery fails and the error Cannot get file from partition is shown after restart, disable Secure Boot. For more information, see Disabling Secure Boot in the Microsoft documentation.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.