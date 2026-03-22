# Registering Workloads Registration Token Cli

Installing and deploying Cyber Protection agents > Registration of workloads > Registering and unregistering workloads by using the command-line interface > Registering workloads by using a registration token
Registering workloads by using a registration token

A registration token is a series of 12 characters, separated by hyphens in three segments. The registration token passes the identity of a user to the agent setup program, without storing the user credentials for the Cyber Protect console. This enables users to register workloads under their account or apply protection plans to workloads without logging in to the console.

For more information, see Generating a registration token.

Protection plans are not applied automatically during workload registration. Applying a protection plan is a separate task.

For more information, see this knowledge base article.

When you use a registration token, you must specify the exact data center address. This is the URL that you see after you log in to the Cyber Protection service.

For example, https://eu2.company.cloud.

To register a workload by using a registration token

In Windows
In Linux
In macOS
Virtual appliance
Bootable media

In Command Prompt, run the following command:

"%ProgramFiles%\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a <service address> --token <registration token>

For example:

"C:\Program Files\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a https://au1.company.cloud --token 3B4C-E967-4FBD
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.