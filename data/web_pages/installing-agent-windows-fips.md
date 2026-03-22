# Installing Agent for Windows in FIPS-compliant mode

Installing and deploying Cyber Protection agents > FIPS-compliant mode > Installing Agent for Windows in FIPS-compliant mode
Installing Agent for Windows in FIPS-compliant mode

You can install Agent for Windows in FIPS-compliant mode by using the graphical user interface or command-line interface.

Prerequisites

Your workload has a 64-bit Windows operating system.

The operating system of the workload is working in FIPS mode.

For more information, see System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing in the Microsoft documentation.

You downloaded the installation file for Agent for Windows.

For more information, see Downloading protection agents.

To install Agent for Windows in FIPS-compliant mode

Graphical user interface
Command-line interface

On the machine on which you want to install the agent, run Command Prompt as an administrator.

In Command Prompt, navigate to the installation file.

To run the installation procedure in FIPS-compliant mode, and continue in the graphical user interface, run the following command:

<file path>/<EXE file> --fips=enabled

For example:

C:\Users\Administrator\Downloads\AgentForWindows_web.exe --fips=enabled

[Optional] Click Customize installation settings, and then configure the installation settings.

The following options are available:

Changing the components to install (for example, disabling the installation of Cyber Protect Monitor or the Command-Line Tool, or installing the Agent for Antimalware protection and URL filtering).

On Windows machines, the antimalware protection and URL filtering features require the installation of Agent for Antimalware protection and URL filtering. This agent is installed automatically for protected workloads if the Antivirus & Antimalware protection and/or the URL filtering options are enabled in their protection plans.

Changing the components to install (for example, disabling the installation of Cyber Protect Monitor or the Command-Line Tool, or installing the Agent for Antimalware protection and URL filtering or the SIEM Log Forwarder feature).

On Windows machines, the antimalware protection and URL filtering features require the installation of Agent for Antimalware protection and URL filtering. This agent is installed automatically for protected workloads if the Antivirus & Antimalware protection and/or the URL filtering options are enabled in their protection plans.

Changing the method of registering the workload in the Cyber Protection service. You can switch from Use service console (default) to Use credentials or Use registration token.
Changing the installation path.
Changing the user account under which the agent service will run. For details, see Changing the logon account on Windows machines.

Verifying or changing the host name or IP address of a proxy server, the port, username, and password to access it.

The password can include lowercase and uppercase alphanumeric characters, and the following special characters:

! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` } | { ~
If a proxy server is enabled in Windows, it is automatically detected and used.
Click Install.

[Only when installing Agent for VMware] Specify the address and access credentials for the vCenter Server or the stand-alone ESXi host on which you want to back up and recover virtual machines, and then click Done.

We recommend that you use a dedicated account for accessing vCenter Server or the ESXi host, instead of using an existing account with the Administrator role. For more information, see Required privileges for Agent for VMware.

[Only when installing on a domain controller] Specify the user account under which the agent service will run, and then click Done. For security reasons, the setup program does not automatically create new accounts on a domain controller.

The user account that you specify must be granted the Log on as a service right. This account must have already been used on the domain controller, in order for its profile folder to be created on that machine.

For more information about installing the agent on a read-only domain controller, see this knowledge base article.

[If you selected the default registration method Use service console] Wait until the registration screen appears.

Register the agent under a user account in a customer tenant. For more information about registration, see Registering workloads by using the graphical user interface.

[If you registered the agent in a tenant that uses Compliance mode] Set the encryption password.
To install FIPS-compliant agents on multiple machines, you can use an MSI file that is created by a FIPS-compliant agent. For more information about installing agents with an MSI file, see Unattended installation and uninstallation with an MSI file.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.