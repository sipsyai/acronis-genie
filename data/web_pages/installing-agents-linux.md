# Installing protection agents in Linux

Installing and deploying Cyber Protection agents > Installing protection agents by using the graphical user interface > Installing protection agents in Linux
Installing protection agents in Linux

You can install Agent for Linux by running its installation file on a local machine.

Prerequisites

You downloaded the installation file for Agent for Linux. See Downloading protection agents.

The 64-bit installation package contains additional agents, such as Agent for Virtuozzo, Agent for Oracle, Agent for MySQL/MariaDB, and Agent for Proxmox. These agents depend on Agent for Linux and are installed with it.

You installed the required Linux packages.
At least 2 GB of free disk space is available on the machine on which you want to install the agent.
When installing the agent in SUSE Linux, ensure that you use su - instead of sudo. Otherwise, the following error occurs when you try to register the agent via the Cyber Protect console: "Failed to launch the web browser. No display available". Some Linux distributions, such as SUSE, do not pass the DISPLAY variable when using sudo, and the installer cannot open the browser in the graphical user interface (GUI).

Limitations

Some Linux distributions do not allow the installation of packages that are signed with SHA-1. In such cases, the installation fails with the following message: 'Cannot find package Backup and Recovery Agent.' For more information about how to resolve this issue, see this knowledge base article.

To install Agent for Linux

Ensure that the machine is connected to the Internet.

As the root user, navigate to directory with the installation file, make the file executable, and then run it.

chmod +x <installation file name>
./<installation file name>

If a proxy server is enabled in your network, when running the installation file, specify the server host name/IP address and port in the following format: --http-proxy-host=ADDRESS --http-proxy-port=PORT --http-proxy-login=LOGIN --http-proxy-password=PASSWORD.

If you want to change the default method of registering the machine in the Cyber Protection service, run the installation file with one of the following parameters:

--register-with-credentials – to ask for a user name and password during the installation
--token=STRING – to use a registration token
--skip-registration – to skip the registration

Select the check boxes for the agents that you want to install. The following agents are available in the 64-bit installation package:

Agent for Linux
Agent for Virtuozzo
Agent for Oracle
Agent for MySQL/MariaDB
Agent for Proxmox
If you kept the default registration method in step 2, proceed to the next step. Otherwise, enter the user name and password for the Cyber Protection service, or wait until the machine will be registered by using the token.

Register the agent under a user account in a customer tenant. For more information about registration, see Registering workloads by using the graphical user interface.

[If you registered the agent in a tenant that uses Compliance mode] Set the encryption password.

If the UEFI Secure Boot is enabled on the machine, you are informed that you need to restart the system after the installation. When prompted for a password, use the password for the root user. If this password is not accepted, use the word "acronis" as a password.

The installation generates a new key that is used for signing the kernel modules. You must enroll this new key to the Machine Owner Key (MOK) list by restarting the machine. Without enrolling the new key, your agent will not be operational. If you enable the UEFI Secure Boot after the agent is installed, you need to reinstall the agent.

After the installation completes, do one of the following:

Click Restart, if you were prompted to restart the system in the previous step.

During the system restart, opt for MOK (Machine Owner Key) management, select Enroll MOK, and then enroll the key by using the password recommended in the previous step.

Otherwise, click Exit.

Troubleshooting information is provided in the file: /usr/lib/Acronis/BackupAndRecovery/HOWTO.INSTALL

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.