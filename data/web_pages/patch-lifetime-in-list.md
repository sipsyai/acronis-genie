# Configuring the patch lifetime in the list

RMM > Managing software > Assessing vulnerabilities and managing patches > Configuring the patch lifetime in the list
Configuring the patch lifetime in the list

You can keep the list of patches up to date by configuring the patch lifetime in the list on the Patches screen. This setting defines how long the detected available patch will be visible in the list of patches. The patch will be removed from the list after it is successfully installed on all the machines on which it was indicated as missing, or after the lifetime in the list passes.

To configure the patch lifetime in the list

In the Cyber Protect console, go to Software management > Patches.
Click Settings.

In Lifetime in list, select the appropriate option.

Option	Description
Forever	The patch will always stay in the list.
7 days

The patch will be removed from the list seven days after its first installation.

For example, let us assume that you have two machines on which patches must be installed. One of them is online, and the other one is offline. The patch was installed on the first machine. After 7 days, the patch will be removed from the list of patches, even if it is not installed on the second machine (because it was offline).


30 days	The patch is removed from the list 30 days after its first installation.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.