# Remote installation of agents

Installing and deploying Cyber Protection agents > Device discovery > Remote installation of agents
Remote installation of agents

After the device discovery process, you can remotely install agents on discovered Windows devices.

The remote installation of agents is performed in the following way:

The discovery agent connects to the target machines by using the host name, IP address, and administrator credentials specified in the discovery wizard, and then uploads the web_installer.exe file to these machines.
The web_installer.exe file runs on the target machines in the unattended mode.
The web installer retrieves additional installation packages from the cloud, and then installs them to the target machines via the msiexec command.
After the installation completes, the components are registered in the cloud.
Remote installation of agents is not supported for Domain Controllers, due to the additional permissions required for the agent service to run.

Preparing machines for remote installation manually

Preparing machines for remote installation by using a GPO

Installing agents remotely




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.