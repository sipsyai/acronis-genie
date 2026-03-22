# Installing and uninstalling agents and components (MSI and direct selection)

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Windows > Installing and uninstalling agents and components (MSI and direct selection)
Installing and uninstalling agents and components (MSI and direct selection)

Run the MSI file, manually select the components to install, and specify their installation parameters on the command line. In this case, you do not need the MST file.

To install agents and components
To remove an installed component
To uninstall an agent

Extract the MSI file and the installation packages (CAB files) as described in Extracting the MSI, MST, and CAB files.

For this installation method, you only need the MSI and CAB files. You do not need the MST file.

In the command-line interface of the machine, run the following command:

msiexec /i <MSI file><PARAMETER 1>=<value 1> ... <PARAMETER N>=<value n>

Use spaces to separate the parameters, and commas without spaces to separate the values for a parameter. For example:

msiexec.exe /i BackupClient64.msi ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,CommandLineTool,TrayMonitor TARGETDIR="C:\Program Files\BackupClient" REGISTRATION_ADDRESS=https://eu2.company.cloud REGISTRATION_TOKEN=34F6-8C39-4A5C

To check the available parameters and their values, see Parameters for unattended installation (MSI).

Examples

Installing Agent for Windows, Agent for Antimalware and URL filtering, Command-Line Tool, and Cyber Protect Monitor. Registering the workload in the Cyber Protection service by using a user name and password.

msiexec.exe /i BackupClient64.msi /l*v my_log.txt /qn ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,AmpAgentFeature,CommandLineTool,TrayMonitor TARGETDIR="C:\Program Files\BackupClient" REBOOT=ReallySuppress MMS_USE_SYSTEM_ACCOUNT=1 REGISTRATION_ADDRESS=https://company.cloud REGISTRATION_LOGIN=johndoe REGISTRATION_PASSWORD=johnspassword

Installing Agent for Windows, Command-Line Tool, and Cyber Protect Monitor. Creating a new logon account for the agent service in Windows. Registering the workload in the Cyber Protection service by using a token.

msiexec.exe /i BackupClient64.msi /l*v my_log.txt /qn ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,CommandLineTool,TrayMonitor TARGETDIR="C:\Program Files\BackupClient" REBOOT=ReallySuppress MMS_CREATE_NEW_ACCOUNT=1 REGISTRATION_ADDRESS=https://eu2.company.cloud REGISTRATION_TOKEN=34F6-8C39-4A5C

Installing Agent for Windows, Command-Line Tool, Agent for Oracle and Cyber Protect Monitor. Registering the machine in the Cyber Protection service by using a user name and encoded in base64 password. You might need to encode your password if it contains special characters or blank spaces. For more information about how to encode a password, see Using passwords with special characters or blank spaces.

msiexec.exe /i BackupClient64.msi /l*v my_log.txt /qn ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,CommandLineTool,OracleAgentFeature,TrayMonitor TARGETDIR="C:\Program Files\BackupClient" REBOOT=ReallySuppress CURRENT_LANGUAGE=en MMS_USE_SYSTEM_ACCOUNT=1 REGISTRATION_ADDRESS=https://company.cloud REGISTRATION_LOGIN=johndoe REGISTRATION_PASSWORD_ENCODED=am9obnNwYXNzd29yZA==

Installing Agent for Windows, Command-Line Tool, and Cyber Protect Monitor. Registering the machine in the Cyber Protection service by using a token. Setting an HTTP proxy.

msiexec.exe /i BackupClient64.msi /l*v my_log.txt /qn ADDLOCAL=MmsMspComponents,BackupAndRecoveryAgent,CommandLineTool,TrayMonitor TARGETDIR="C:\Program Files\BackupClient" REBOOT=ReallySuppress CURRENT_LANGUAGE=en MMS_USE_SYSTEM_ACCOUNT=1 REGISTRATION_ADDRESS=https://eu2.company.cloud REGISTRATION_TOKEN=34F6-8C39-4A5C HTTP_PROXY_ADDRESS=https://my-proxy.company.com HTTP_PROXY_PORT=80 HTTP_PROXY_LOGIN=tomsmith HTTP_PROXY_PASSWORD=tomspassword



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.