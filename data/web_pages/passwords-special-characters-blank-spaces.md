# Using passwords with special characters or blank spaces

Installing and deploying Cyber Protection agents > Registration of workloads > Registering and unregistering workloads by using the command-line interface > Using passwords with special characters or blank spaces
Using passwords with special characters or blank spaces

If a password contains special characters or blank spaces, enclose it in quotation marks when you type it on the command line.

For example, in Windows, run this command in Command Prompt:

Command template

"%ProgramFiles%\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a <service address> -u <user name> -p <"password">

Command examples

Windows

"C:\Program Files\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a https://company.cloud -u johndoe -p "johnspassword"

Linux

sudo "/usr/lib/Acronis/RegisterAgentTool/RegisterAgent" -o register -t cloud -a https://company.cloud -u johndoe -p "johnspassword"

macOS

sudo "/Library/Application Support/BackupClient/Acronis/RegisterAgentTool/RegisterAgent" -o register -t cloud -a https://company.cloud -u johndoe -p "johnspassword"

If this command fails, encode your password into base64 format at https://www.base64encode.org/. Then, at the command line, specify the encoded password by using the -b or --base64 parameter.

For example, in Windows, run this command in Command Prompt:

Command template

"%ProgramFiles%\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a <service address> -u <user name> -b -p <encoded password>

Command examples

Windows

"C:\Program Files\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a https://company.cloud -u johndoe -b -p am9obnNwYXNzd29yZA==

Linux

sudo "/usr/lib/Acronis/RegisterAgentTool/RegisterAgent" -o register -t cloud -a https://company.cloud -u johndoe -b -p am9obnNwYXNzd29yZA==

macOS

sudo "/Library/Application Support/BackupClient/Acronis/RegisterAgentTool/RegisterAgent" -o register -t cloud -a https://company.cloud -u johndoe -b -p am9obnNwYXNzd29yZA==
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.