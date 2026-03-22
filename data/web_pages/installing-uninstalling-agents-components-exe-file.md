# Installing and uninstalling agents and components (EXE)

Installing and deploying Cyber Protection agents > Installing and uninstalling protection agents by using the command-line interface > Installing and uninstalling protection agents in Windows > Installing and uninstalling agents and components (EXE)
Installing and uninstalling agents and components (EXE)

To perform unattended installation with an EXE file, run the setup program and specify the installation parameters on the command line.

To download the setup program, in the Cyber Protect console, click the account icon in the top-right corner, and then click Downloads. The download link is also available in the Add devices pane.

To install agents and components
To remove an installed component
To uninstall an agent

Start the command-line interface as administrator, and then navigate to the EXE file of the setup program.

To start the setup program and specify the installation parameters, run the following command:

<file path>/<EXE file><PARAMETER 1>=<value 1> ... <PARAMETER N>=<value n>

Use spaces to separate the parameters, and commas without spaces to separate the values for a parameter. For example:

C:\Users\Administrator\Downloads\AgentForWindows_web.exe --add-components=agentForWindows,agentForSql,commandLine --install-dir="C:\Program Files\BackupClient" --reg-address=https://eu2.company.cloud --reg-token=34F6-8C39-4A5C --quiet

To check the available parameters and their values, see Parameters for unattended installation (EXE).

Examples

Installing Agent for Windows, Agent for Antimalware protection and URL filtering, Command-Line Tool, and Cyber Protect Monitor. Registering the workload in the Cyber Protection service by using a user name and password.

C:\Users\Administrator\Downloads\AgentForWindows_web.exe --add-components=agentForWindows,agentForAmp,commandLine,trayMonitor --install-dir="C:\Program Files\BackupClient" --agent-account=system --reg-address=https://company.cloud --reg-login=johndoe --reg-password=johnspassword

Installing Agent for Windows, Command-Line Tool, and Cyber Protect Monitor. Creating a new logon account for the agent service in Windows. Registering the workload in the Cyber Protection service by using a token.

C:\Users\Administrator\Downloads\AgentForWindows_web.exe --add-components=agentForWindows,commandLine,trayMonitor --install-dir="C:\Program Files\BackupClient" --agent-account=new --reg-address=https://eu2.company.cloud --reg-token=34F6-8C39-4A5C

Installing Agent for Windows, Command-Line Tool, Agent for Oracle and Cyber Protect Monitor. Registering the machine in the Cyber Protection service by using a user name and password.

C:\Users\Administrator\Downloads\AgentForWindows_web.exe --add-components=agentForWindows,commandLine,agentForOracle,trayMonitor --install-dir="C:\Program Files\BackupClient" --language=en --agent-account=system --reg-address=https://company.cloud --reg-login=johndoe --reg-password=johnspassword

Installing Agent for Windows, Command-Line Tool, and Cyber Protect Monitor. Setting the user interface language to German. Registering the machine in the Cyber Protection service by using a token. Setting an HTTP proxy.

C:\Users\Administrator\Downloads\AgentForWindows_web.exe --add-components=agentForWindows,commandLine,agentForOracle,trayMonitor --install-dir="C:\Program Files\BackupClient"--language=de --agent-account=system --reg-address=https://eu2.company.cloud --reg-token=34F6-8C39-4A5C --http-proxy-address=https://my-proxy.company.com:80 --http-proxy-login=tomsmith --http-proxy-password=tomspassword



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.