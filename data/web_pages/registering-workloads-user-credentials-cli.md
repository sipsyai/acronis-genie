# Registering Workloads User Credentials Cli

Installing and deploying Cyber Protection agents > Registration of workloads > Registering and unregistering workloads by using the command-line interface > Registering workloads by using user credentials
Registering workloads by using user credentials

Use the user name and password for the account under which you want to register the workload. This account must be an account in a customer tenant. If the password contains special characters or blank spaces, see Using passwords with special characters or blank spaces.

The service address is the URL that you use to log in to the Cyber Protection service.

For example, https://company.cloud.

To register a workload by using a user name and password

In Windows
In Linux
In macOS

In Command Prompt, run the following command:

"%ProgramFiles%\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a <service address> -u <user name> -p <password>

For example:

"C:\Program Files\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a https://company.cloud -u johndoe -p johnspassword

Using passwords with special characters or blank spaces




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.