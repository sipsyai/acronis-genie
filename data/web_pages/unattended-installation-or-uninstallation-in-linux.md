# Installing and uninstalling protection agents in Linux

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Linux
Installing and uninstalling protection agents in Linux

This section describes how to install or uninstall protection agents in the unattended mode on a machine running Linux, by using the command line.

Prerequisites

You downloaded the installation file for Agent for Linux. See Downloading protection agents.

The 64-bit installation package contains additional agents, such as Agent for Virtuozzo, Agent for Oracle, Agent for MySQL/MariaDB, and Agent for Proxmox. These agents depend on Agent for Linux and are installed with it.

You installed the required Linux packages.
At least 2 GB of free disk space is available on the machine on which you want to install the agent.
When installing the agent in SUSE Linux, ensure that you use su - instead of sudo. Otherwise, the following error occurs when you try to register the agent via the Cyber Protect console: "Failed to launch the web browser. No display available". Some Linux distributions, such as SUSE, do not pass the DISPLAY variable when using sudo, and the installer cannot open the browser in the graphical user interface (GUI).

Limitations

Some Linux distributions do not allow the installation of packages that are signed with SHA-1. In such cases, the installation fails with the following message: 'Cannot find package Backup and Recovery Agent.' For more information about how to resolve this issue, see this knowledge base article.
To install an agent
To uninstall an agent
Open Terminal.

Do one of the following:

To start the installation by specifying the parameters on the command line, run the following command:

<package name> -a <parameter 1> ... <parameter N>

Here, <package name> is the name of the installation package (32-bit or 64-bit). See the available parameters and their values in Unattended installation or uninstallation parameters.

To start the installation with parameters that are specified in a separate text file, run the following command:

<package name> -a --options-file=<path to the file>

This approach might be useful if you do not want to enter sensitive information on the command line. In this case, you can specify the configuration settings in a separate text file and ensure that only you can access it. Put each parameter on a new line, followed by the value for that parameter. For example:

--rain=https://company.cloud
--login=johndoe
--password=johnspassword
--auto

or

-C
https://company.cloud
-g
johndoe
-w
johnspassword
-a
--language
en

If the same parameter is specified both on the command line and in the text file, the command-line value precedes.

If UEFI Secure Boot is enabled on the machine, you are prompted to restart the system after the installation. When prompted for a password, use the password for the root user. If this password is not accepted, use the word "acronis" as a password. During the system restart, opt for MOK (Machine Owner Key) management, select Enroll MOK, and then enroll the key by using the recommended password.

If you enable UEFI Secure Boot after installing the agent, repeat the installation, including this step. Otherwise, backups will fail.

Unattended installation or uninstallation parameters

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.