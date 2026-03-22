# Requirements on User Account Control (UAC)

Installing and deploying Cyber Protection agents > Device discovery > Discovering multiple devices > Requirements on User Account Control (UAC)
Requirements on User Account Control (UAC)

On a machine that is running Windows 7 or later and is not a member of an Active Directory domain, centralized management operations (including remote installation) require that UAC and UAC remote restrictions be disabled.

To disable UAC

Do one of the following depending on the operating system:

In a Windows operating system prior to Windows 8:

Go to Control panel > View by: Small icons > User Accounts > Change User Account Control Settings, and then move the slider to Never notify. Then, restart the machine.

In any Windows operating system:

Open Registry Editor.
Locate the following registry key: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System
For the EnableLUA value, change the setting to 0.
Restart the machine.

To disable UAC remote restrictions

Open Registry Editor.
Locate the following registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System

For LocalAccountTokenFilterPolicy value, change the setting to 1.

If the LocalAccountTokenFilterPolicy value does not exist, create it as DWORD (32-bit). For more information about this value, refer to the Microsoft documentation: https://support.microsoft.com/en-us/help/951016/description-of-user-account-control-and-remote-restrictions-in-windows.

For security reasons, we recommend that after finishing the management operation (for example, remote installation), you revert both settings to their original state: EnableLUA=1 and LocalAccountTokenFilterPolicy = 0

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.