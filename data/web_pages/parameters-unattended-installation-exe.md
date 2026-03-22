# Parameters for unattended installation (EXE)

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Windows > Parameters for unattended installation (EXE)
Parameters for unattended installation (EXE)

The following table summarizes the parameters for unattended installation with an EXE file.

Parameters	Description
General parameters
--add-components=<component1,component2,...,componentN>

The components to be installed. See the full list of available components in Components for unattended installation (EXE).

When you specify multiple components, separate them with commas. Do not add spaces before or after the comma.

If you specify components that are already installed, these components will be repaired or updated, depending on version of the setup program and the version of the installed components.

If you do not specify this parameter, a default set of components will be installed, depending on the machine on which you perform the installation. For example, Agent for SQL is only installed on machines that run MS SQL Server.


--install-dir=<path>

The folder in which the selected components will be installed. If the specified folder does not exist, it will be created.

If you do not specify this parameter, a default folder is used: C:\Program Files\BackupClient.


--log-dir=<path>

The folder in which the installation logs will be saved.

If you do not specify this parameter, a default folder is used: %ProgramData%\Acronis\InstallationLogs.


--language=<code>

The product language.

The following values are available: en, bn, bg, cs, da, de, es, fr, ko, id, it, hi, hu, ms, nl, ja, nb, pl, pt, pt_BR, ru, fi, sr, sv, th, tr, vi, zh, zh_TW.

If you do not specify this parameter, and the system language of the machine on which you perform the installation is listed above, the system language is used. In all other cases, the value is set to en.


--quiet

Use this parameter to run the setup program without showing the graphical user interface.

Do not use it together with the --register-only parameter.


--help	Use this parameter to see a list of all available parameters that you can use on the command line and their descriptions.
--fss-onboarding-auto-start

Use this parameter together with the --quiet parameter to show the File Sync & Share on-boarding wizard after an unattended installation.


--fips={enabled | disabled}	Use this parameter with value enabled to install the agent in FIPS-compliant mode.
Registration parameters
--registration={skip | by-credentials | by-token | device-flow}

Use this parameter to choose how to register the agent after the installation.

To skip the registration, specify skip. You can register the agent later, by using the --register-only parameter.

To register the agent by using credentials, specify by-credentials, and then use the --reg-login and --reg-password parameters. Also, you can use only --reg-login and --reg-password parameters, which makes specifying --registration=by-credentials optional.

To register the agent with a registration token, specify by-token, and then use the --reg-token parameter. Also, you can use only the --reg-token parameter, which makes specifying --registration=by-token optional.

To register the agent by using the OAuth 2.0 protocol, specify device-flow. After the installation completes, the registration page opens automatically.

When you use --registration=device-flow, specify the exact data center address as a value for the --reg-address parameter. This is the URL that you see after you log in to the Cyber Protection service. For example, https://eu2.company.cloud.

Do not use --registration=device-flow with the --quiet parameter.


--reg-address=<url>

The URL of the Cyber Protection service. You can use this parameter either with the --reg-login and --reg-password parameters, or with the --reg-token parameter.

When you use it with --reg-login and --reg-password parameters, specify the address that you use to log in to the Cyber Protection service. For example,https://company.cloud:

When you use it with the --reg-token parameter, specify the exact data center address. This is the URL that you see after you log in to the Cyber Protection service. For example, https://eu2.company.cloud.

Do not use https://company.cloud with the --reg-token parameter.




--reg-login=<login>

--reg-password=<password>



The credentials for the account under which the agent will be registered in the Cyber Protection service. This cannot be a partner administrator account.

When you use these parameters, specifying the --registration parameter is optional.

Do not use these parameters with the --reg-token parameter.


--reg-token=<token>

The registration token.

The registration token is a series of 12 characters, separated into three segments by hyphens. For more information about how to generate one, see Generating a registration token.

When you use this parameter, specifying the --registration parameter is optional.

Do not use this parameter with the --reg-login and --reg-password parameters.


--register-only

Use this parameter to skip the installation and register the agent by using the OAuth 2.0 protocol (device-flow).

After the installation completes, the registration page opens automatically.

Do not use --register-only with the --quiet parameter.




Logon account for the agent service




--agent-account={system | new | custom}

or

--agent-account-login=<login>

--agent-account-password=<password>



Use this parameter to specify the logon account under which agent service will run. For more information about the logon accounts, see Changing the logon account on Windows machines.

To use the Local System account, specify --agent-account=system or do not use the --agent-account parameter in your command.

To make the agent service run under a new logon account, Acronis Agent User, which is created automatically, specify new.

To make the agent service run under an existing account, specify the account credentials by using the --agent-account-login and --agent-account-password parameters. In this case, specifying the --agent-account=custom parameter is optional.


vCenter/ESXi parameters
--esxi-address=<host>

The host name or IP address of vCenter Server or the ESXi host.

Use this parameter when you install Agent for VMware.




--esxi-login=<login>

--esxi-password=<password>



The access credentials to vCenter Server or the ESXi host.

Use these parameters when you install Agent for VMware.


Proxy parameters


--http-proxy={none | system | custom}



Use this parameter to specify the HTTP proxy server that you want to use for backup to and recovery from the cloud storage.

If disable the proxy server connections, specify --http-proxy=none.

To use a system-wide proxy server, specify --http-proxy=system or do not use the --http-proxy parameter in your command.

To use another proxy server, specify the proxy server address and credentials by using the --http-proxy-address, --http-proxy-login, and --http-proxy-password parameters. In this case, specifying --http-proxy=custom parameter is optional.




--http-proxy-address=<host>:<port>



The hostname or IP address, and the port of the custom HTTP proxy server.


--http-proxy-login=<login>

Login for the custom HTTP proxy server.


--http-proxy-password=<password>

Password for the custom HTTP proxy server.


Uninstallation parameters
--remove-components=<component1,component2,...,componentN>

The components to be uninstalled. See the full list of available components in Components for unattended installation (EXE).

When you specify multiple components, separate them with commas. Do not add spaces before or after the comma.

By using this parameter, you can uninstall only components. To uninstall the product completely, go to Windows Control Panel > Programs and Features, select the product, and then click Uninstall.


--delete-all-settings

Use this optional parameter when you use the --remove-components parameter to delete all product logs, tasks, and configuration settings.


--anti-tamper-password=<password>	The password required for uninstalling a password-protected Agent for Windows or modifying its components.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.