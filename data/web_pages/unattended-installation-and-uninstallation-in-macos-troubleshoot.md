# Troubleshooting permission issues on macOS

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in macOS > Troubleshooting permission issues on macOS
Troubleshooting permission issues on macOS

The 'System Extension Blocked' message might appear during the installation of Agent for macOS on the screen of the protected Mac machine. The following procedures are performed on the protected machie.

To approve the Acronis Cyber Protection Agent system extension

Click Open System Settings.

If you dismiss the dialog accidentally, you can access the System Settings/Preferences from the Apple menu.

Navigate to Privacy & Security.
Scroll down to find the message indicating the system extension was blocked.
Click the Allow button next to the blocked extension.
Restart the Mac machine for the changes to take effect.
If the Allow button does not appear, you might need to adjust the security settings in recovery mode.

To adjust the security settings in recovery mode

Shut down the Mac.
Press and hold the power button until you see the startup options.
Click Options and then continue to the next screen.
From the Utilities menu, select Startup Security Utility.
In the Startup Security Utility, click the Security Policy button.
Select Reduce Security and then select the check box Allow user management of kernel extensions from identified developers.
Click OK, enter your administrator password, and wait for the changes to be applied.
In the menu bar, click Startup Disk, and then click Quit Startup Disk.

This will take you to the previous screen.

Click the Apple icon and select Restart.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.