# Configuring automatic patch approval

RMM > Managing software > Assessing vulnerabilities and managing patches > Configuring automatic patch approval
Configuring automatic patch approval

You can configure automatic patch approval and ensure that the installation of patches is not delayed by the manual patch approval process.

You might not be allowed to change the settings that your partner administrator configured at the partner level.

To configure automatic patch approval

In the Cyber Protect console, go to Software management > Patches.
Click Settings.
Enable Automatic patch approval.

Configure the settings for automatic patch approval.

Select the automatic patch approval option.

Option	Description
Automatic patch approval and testing	The approval status of the patch will change to Approved when the selected number of days passes after a successful installation of the patch. We recommend that you use this setting if you want to test the patches by installing them on a test machine first, ensure that everything is working as expected, and then install the patches in your production environment.
Automatic patch approval without testing	The approval status of the patch will change to Approved when the selected number of days passes after the patch was found.

Select the number of days that must pass after the condition from the automatic patch approval option is met. After this period, the approval status of the patches will automatically change from Pending approval to Approved.

Select Automatically accept the license agreements.
Click Apply.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.