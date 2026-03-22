# Parameters for unattended installation (MSI)

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Windows > Parameters for unattended installation (MSI)
Parameters for unattended installation (MSI)

The following table summarizes the parameters for unattended installation when you use an MSI file.

You can also use additional msiexec parameters. For example, use /qn to prevent any GUI elements from showing. To learn more about the msiexec parameters, see the Microsoft documentation.

Parameters	Description
General parameters
ADDLOCAL=<component1,component2,...,componentN>

The components to be installed. See the full list of available components in Components for unattended installation (MSI).

When you specify multiple components, separate them with commas. Do not add spaces before or after the comma.

You must extract the installation files for all components that you want to install. For more information about how to extract them, see Extracting the MSI, MST, and CAB files.

TARGETDIR=<path>

The folder in which the selected components will be installed. If the specified folder does not exist, it will be created.

If you do not specify this parameter, a default folder is used: C:\Program Files\BackupClient.


REBOOT=ReallySuppress	Specify this parameter if you want to install components without restarting the machine.
/l*v <log file>	Specify this parameter to save a verbose log. This log is needed if you have to investigate installation issues.
CURRENT_LANGUAGE=<language ID>

The product language.

The following values are available: en, bn, bg, cs, da, de, es, fr, ko, id, it, hi, hu, ms, nl, ja, nb, pl, pt, pt_BR, ru, fi, sr, sv, th, tr, vi, zh, zh_TW.

If you do not specify this parameter, and the system language of the machine on which you perform the installation is listed above, the system language is used. In all other cases, the value is set to en.


SKIP_SHA2_KB_CHECK={0,1}

Use this parameter to either check or to skip the check for the installation of Microsoft update for SHA2 code signing support (KB4474419) on a machine. The check only runs on operating systems that require this update. To see if it is required for your operating system, see Supported operating systems and environments for backup and recovery.

To skip the check, set the parameter value to 1.

If you do not specify the parameter or set its value to 0, and the SHA2 code signing support update is not found on the machine, the installation fails.


FSS_ONBOARDING_AUTO_START={0,1}

Use this parameter with value set to 1 to show the File Sync & Share on-boarding wizard after an unattended installation.

If you do not specify this parameter or set its value to 0, the on-boarding wizard will not be shown.


ENABLE_FIPS_COMPLIANCE_MODE={0,1}	Use this parameter with value set to 1 to install the agent in FIPS-compliant mode.
Registration parameters
REGISTRATION_ADDRESS

The URL of the Cyber Protection service. You can use this parameter either with the REGISTRATION_LOGIN and REGISTRATION_PASSWORD parameters, or with REGISTRATION_TOKEN.

When you use it with REGISTRATION_LOGIN and REGISTRATION_PASSWORD parameters, specify the address that you use to log in to the Cyber Protection service. For example, https://company.cloud:

When you use it with the REGISTRATION_TOKEN parameter, specify the exact datacenter address. This is the URL that you see after you log in to the Cyber Protection service. For example, https://eu2.company.cloud.

Do not use https://company.cloud with the REGISTRATION_TOKEN parameter.




REGISTRATION_LOGIN

REGISTRATION_PASSWORD



The credentials for the account under which the agent will be registered in the Cyber Protection service. This cannot be a partner administrator account.

Do not use these parameters with the REGISTRATION_TOKEN parameter.


REGISTRATION_PASSWORD_ENCODED	The password for the account under which the agent will be registered in the Cyber Protection service, encoded in base64. For more information on how to encode your password, see Using passwords with special characters or blank spaces.
REGISTRATION_TOKEN

The registration token.

The registration token is a series of 12 characters, separated into three segments by hyphens. For more information about how to generate one, see Generating a registration token.

Do not use this parameter with the REGISTRATION_LOGIN and REGISTRATION_PASSWORD parameters.


REGISTRATION_REQUIRED={0,1}

Use this parameter to choose what happens if the registration fails.

If you set the value to 1, the installation also fails. If you set the value to 0 or do not specify the parameter, the installation completes successfully even though the registration fails.




Logon account for the agent service


MMS_USE_SYSTEM_ACCOUNT={0,1}

Use this parameter with value 1, to make the service run under the Local System logon account.

For more information about the logon accounts, see Changing the logon account on Windows machines.


MMS_CREATE_NEW_ACCOUNT={0,1}	Use this parameter with value 1, to make the agent service run under a new logon account, Acronis Agent User, which is created automatically.


MMS_SERVICE_USERNAME=<user name>

MMS_SERVICE_PASSWORD=<password>

Use these parameters to specify an existing logon account under which the agent service will run.
vCenter/ESXi parameters
SET_ESX_SERVER={0,1}

Use this parameter when you install Agent for VMware.

If you set the value to 0, Agent for VMware will not be connected to vCenter Server or an ESXi host.

If you set the value to 1, specify the following parameters: ESX_HOST, EXI_USER, ESX_PASSWORD.


ESX_HOST=<host name>	The host name or IP address of vCenter Server or the ESXi host.


ESX_USER=<user name>

ESX_PASSWORD=<password>

The access credentials to vCenter Server or the ESXi host.
Proxy parameters


HTTP_PROXY_ADDRESS=<IP address>

HTTP_PROXY_PORT=<port>



Use these parameters to specify the HTTP proxy server that the agent will use.

If you do not use a proxy server, do not specify these parameters.




HTTP_PROXY_LOGIN=<login>

HTTP_PROXY_PASSWORD=<password>



The credentials for the HTTP proxy server.

Use these parameters if the proxy server requires authentication.


Uninstallation parameters
REMOVE={<component1,component2,...,componentN>|ALL}

The components to be uninstalled.

When you specify multiple components, separate them with commas. Do not add spaces before or after the comma.

To remove all product components, set the value to ALL.


DELETE_ALL_SETTINGS={0,1}

To delete all product logs, tasks, and configuration settings, set the value to 1.

Use this optional parameter when you use the REMOVE parameter.


ANTI_TAMPER_PASSWORD=<password>	The password required for uninstalling a password-protected Agent for Windows or modifying its components.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.