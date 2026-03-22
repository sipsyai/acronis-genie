# Unattended installation or uninstallation parameters

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Linux > Unattended installation or uninstallation parameters
Unattended installation or uninstallation parameters

This section describes parameters that are used during unattended installation or uninstallation in Linux.

The minimal configuration for unattended installation includes -a and registration parameters (for example, --login and --password parameters; --rain and --token parameters). You can use more parameters to customize you installation.

Installation parameters
Basic parameters

{-i |--id=}<list of components>

The components to be installed, separated by commas and without space characters. The following components are available in the 64-bit (x86_64) installation package:

Component	Component description
BackupAndRecoveryAgent	Agent for Linux
AgentForPCS	Agent for Virtuozzo
OracleAgentFeature	Agent for Oracle
MySQLAgentFeature	Agent for MySQL/MariaDB
AgentForProxmox	Agent for Proxmox

Without this parameter, all of the above components will be installed.

Agent for Virtuozzo, Agent for Oracle, Agent for MySQL/MariaDB, and Agent for Proxmox require that Agent for Linux is also installed.

The 32-bit installation package contains only BackupAndRecoveryAgent.

{-a|--auto}

The installation and registration process will complete without any further user interaction. When using this parameter, you must specify the account under which the agent will be registered in the Cyber Protection service, either by using the --token parameter, or by using the --login and --password parameters.

{-t|--strict}

If the parameter is specified, any warning that occurs during the installation results in installation failure. Without this parameter, the installation completes successfully even in the case of warnings.

{-n|--nodeps}

The absence of required Linux packages will be ignored during the installation.

{-d|--debug}

Writes the installation log in the verbose mode.

--options-file=<location>

The installation parameters will be read from a text file instead of the command line.

--language=<language ID>

The product language. Available values are as follows: en, bg, cs, da, de, es, fr, hu, id, it, ja, ko, ms, nb, nl, pl, pt, pt_BR, ru, fi, sr, sv, tr, vi, zh, zh_TW.
If this parameter is not specified, the product language will be defined by your system language on the condition that it is in the list above. Otherwise, the product language will set to English (en).

Registration parameters

Specify one of the following parameters:

{-g|--login=}<user name> and {-w|--password=}<password>

Credentials for the account under which the agent will be registered in the Cyber Protection service. This cannot be a partner administrator account.

--token=<token>

The registration token is a series of 12 characters, separated by hyphens in three segments. For more information, see Generating a registration token.

When you use the --token parameter, you must also include the {-C|--rain=} parameter and specify the exact datacenter address.

You cannot use the --token parameter with --login, --password, and --register-with-credentials parameters.

{-C|--rain=}<service address>

The URL of the Cyber Protection service.

You must use the {-C|--rain=} parameter and specify the exact datacenter address when you use the --token parameter. The exact datacenter address is the URL that you see after you log in to the Cyber Protection console. For example:


You can skip the {-C|--rain=} parameter when you use the --login and --password parameters for registration because the installer uses the correct address by default.


--register-with-credentials

If this parameter is specified, the installer's graphical interface will start. To finish the registration, enter the user name and password for the account under which the agent will be registered in the Cyber Protection service. This cannot be a partner administrator account.

--skip-registration

Use this parameter if you want to install the agent but you plan to register it in the Cyber Protection service later. For more information on how to do this, see Registering and unregistering workloads by using the command-line interface.

Additional parameters

--http-proxy-host=<IP address> and --http-proxy-port=<port>

The HTTP proxy server that the agent will use for backup and recovery from the cloud, and for connection to the management server. Without these parameters, no proxy server will be used.

--http-proxy-login=<login> and --http-proxy-password=<password>

The credentials for the HTTP proxy server. Use these parameters if the server requires authentication.

--tmp-dir=<location>

Specifies the folder where the temporary files are stored during the installation. The default folder is /var/tmp.

{-s|--disable-native-shared}

Redistributable libraries will be used during the installation, even though they might have already been present on your system.

--skip-prereq-check

There will be no check of whether the packages required for compiling the snapapi module are already installed.

--force-weak-snapapi

The installer will not compile a snapapi module. Instead, it will use a ready-made module that might not match the Linux kernel exactly. We do not recommend that you use this option.

--skip-svc-start

The services will not start automatically after the installation. Most often, this parameter is used with the --skip-registration one.

Information parameters

{-?|--help}

Shows the description of parameters.

--usage

Shows a brief description of the command usage.

{-v|--version}

Shows the installation package version.

--product-info

Shows the product name and the installation package version.

--snapapi-list

Shows the available ready-made snapapi modules.

--components-list

Shows the installer components.

Parameters for legacy features

These parameters relate to a legacy component, agent.exe.

{-e|--ssl=}<path>

Specifies the path to a custom certificate file for SSL communication.

{-p|--port=}<port>

Specifies the port on which agent.exe listens for connections. The default port is 9876.

Uninstallation parameters

{-u|--uninstall}

Uninstalls the product.

--purge

Uninstalls the product and removes its logs, tasks, and configuration settings. You don't need to specify the --uninstall parameter explicitly when you use the --purge one.

Examples

Installing Agent for Linux without registering it.

./Cyber_Protection_Agent_for_Linux_x86_64.bin -i BackupAndRecoveryAgent -a --skip-registration

Installing Agent for Linux, Agent for Virtuozzo, and Agent for Oracle, and registering them by using credentials.

./Cyber_Protection_Agent_for_Linux_x86_64.bin -a --login=johndoe --password=johnspassword

Installing Agent for Oracle and Agent for Linux, and registering them by using a registration token.

./Cyber_Protection_Agent_for_Linux_x86_64.bin -i BackupAndRecoveryAgent,OracleAgentFeature -a --rain=https://eu2.company.cloud --token=34F6-8C39-4A5C

Installing Agent for Linux, Agent for Virtuozzo, and Agent for Oracle with configuration settings in a separate text file.

./Cyber_Protection_Agent_for_Linux_x86_64.bin -a --options-file=/home/mydirectory/configuration_file

Uninstalling Agent for Linux, Agent for Virtuozzo, and Agent for Oracle, and removing all their logs, tasks, and configuration settings.

./Cyber_Protection_Agent_for_Linux_x86_64.bin -a --purge
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.