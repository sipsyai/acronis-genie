# Installing agents and components (MSI and MST combination)

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Windows > Installing agents and components (MSI and MST combination)
Installing agents and components (MSI and MST combination)

Use the MST file to customize the installation setting for the MSI file. Use the MSI and MST combination when you install agents on multiple machines through a Windows Group Policy. For more information, see Deploying protection agents through Group Policy.

To install components with MSI and MST files

Extract the MSI and MST files as described in Extracting the MSI, MST, and CAB files.

On the command-line interface of the machine on which you want to install components, run the following command:

msiexec /i <MSI file> TRANSFORMS=<MST file>

For example:

msiexec /i BackupClient64.msi TRANSFORMS=BackupClient64.msi.mst



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.