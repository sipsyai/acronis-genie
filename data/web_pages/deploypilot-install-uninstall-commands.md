# Installation and uninstallation commands and arguments

RMM > Managing software > Working with software repositories and software packages > Installation and uninstallation commands and arguments
Installation and uninstallation commands and arguments

By providing installation and uninstallation arguments while manually uploading software packages, you can ensure smooth and efficient software deployment across your organization.

You can use Copilot to automatically populate installation and uninstallation arguments.

Installation commands
Command arguments

Command-line arguments are parameters or flags that you can specify for the installation process. Common examples include:

Silent installation (Installs the software without showing any UI):

/s or /quiet

No restart (Prevents the system from restarting automatically after the installation process completes):

/norestart

Log file (Creates a log file to track the installation process):

/l* log.txt

Uninstallation commands
Uninstall path

The uninstall path provides the necessary file path and command to uninstall the software. For example:

%ProgramFiles%\7-Zip\Uninstall.exe

Command arguments

Command-line arguments are parameters or flags that you can specify for the uninstallation process. Common examples include:

Silent uninstallation (Uninstalls the software, without showing any UI):

/s or /quiet

No restart (Prevents the system from restarting automatically after the uninstallation process completes):

/norestart

Log file (Creates a log file to track the uninstallation process):

/l* log.txt

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.