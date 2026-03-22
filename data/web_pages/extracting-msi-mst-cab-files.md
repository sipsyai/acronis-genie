# Extracting the MSI, MST, and CAB files

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Windows > Extracting the MSI, MST, and CAB files
Extracting the MSI, MST, and CAB files

Extract the MSI, MST, and CAB files with the installation packages by running the graphical user interface of the setup program.

To extract the MSI, MST, and CAB files

Run the graphical user interface of the setup program, and then click Create .mst and .msi files for unattended installation.

In What to install, select the components that you want to install, and then click Done.

When modifying an existing installation, select the components that are already installed and the components that you want to add.

The installation packages for these components will be extracted from the setup program as CAB files.

In Registration settings, select Use credentials or Use registration token. Depending on your choice, specify the credentials or the registration token, and then click Done.

For more information on how to generate a registration token, see Generating a registration token.

[Only when installing on a domain controller] In Logon account for the agent service, select Use the following account. Specify the user account under which the agent service will run, and then click Done. For security reasons, the setup program does not automatically create new accounts on a domain controller.

The user account that you specify must be granted the Log on as a service right. This account must have already been used on the domain controller, in order for its profile folder to be created on that machine.

For more information about installing the agent on a read-only domain controller, see this knowledge base article.

Review or modify other installation settings that will be added to the MST file, and then click Proceed.
Select the folder in which the MSI, MST, and CAB files will be extracted, and then click Generate.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.