# Excluding processes from access control

Managing workloads in the Cyber Protect console > Working with the Device control module > Excluding processes from access control
Excluding processes from access control

The access to Windows clipboard, screenshot capture, printers, and mobile devices is controlled through hooks injected into processes. If processes are not hooked, the access to these devices will not be controlled.

Excluding processes from access control is not supported on macOS. If a list of excluded processes is configured in the applied protection plan, it will be ignored.

On the Exclusions page, you can specify a list of processes that will not be hooked. This means that clipboard (local and redirected), screenshot capture, printer, and mobile device access controls will not be applied to such processes.

For example, you applied a protection plan that denies access to printers, then started the Microsoft Word application. An attempt to print from this application will be blocked. But if you add the Microsoft Word process to the list of exclusions, then the application will not be hooked. As a result, printing from Microsoft Word will not be blocked, while printing from other applications will still be blocked.

To add processes to exclusions

Open the protection plan of a device for editing:

Click the ellipsis (...) next to the name of the protection plan and select Edit.

Device control must be enabled in the plan, so you can access the Device control settings.
Click the arrow next to the Device control switch to expand the settings, and then click the Exclusions row.
On the Exclusions page, in the Processes and folders row, click +Add.
Add the processes that you want to exclude from the access control.

For example, C:\Folder\subfolder\process.exe.

You can use wildcards:

* replaces any number of characters.
? replaces one character.

For example:

C:\Folder\*

*\Folder\SubFolder?\*

*\process.exe

Click the check mark, and then click Done.
In the protection plan, click Save.
Restart the processes that you excluded to ensure that the hooks are properly removed.

The excluded processes will have access to clipboard, screenshot capture, printers, and mobile devices regardless of the access settings for those devices.

To remove a process from exclusions

Open the protection plan of a device for editing:

Click the ellipsis (...) next to the name of the protection plan and select Edit.

Device control must be enabled in the plan, so you can access the Device control settings.
Click the arrow next to the Device control switch to expand the settings, and then click the Exclusions row.
On the Exclusions page, click the trash can icon next to the process that you want to remove from the exclusions.
Click Done.
In the protection plan, click Save.
Restart the process to ensure that hooks are properly injected.

The access settings from the protection plan will be applied to the processes that you removed from the exclusions.

To edit a process in exclusions

Open the protection plan of a device for editing:

Click the ellipsis (...) next to the name of the protection plan and select Edit.

Device control must be enabled in the plan, so you can access the Device control settings.
Click the arrow next to the Device control switch to expand the settings, and then click the Exclusions row.
On the Exclusions page, click the Edit icon next to the process that you want to edit.
Apply the changes and click the check mark to confirm.
Click Done.
In the protection plan, click Save.
Restart the affected processes to ensure that your changes are applied correctly.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.