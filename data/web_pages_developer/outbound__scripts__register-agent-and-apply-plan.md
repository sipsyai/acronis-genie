---
title: "Register agent and apply plan"
source: "https://developer.acronis.com/doc/outbound/scripts/register-agent-and-apply-plan.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:35:07.491250"
---

# Register agent and apply plan

Register agent and apply plan
This section provides a PowerShell script that is used to install, register an agent, and apply a plan to it. It is recommended the user issue a registration token for security purposes and use the method of installation/registration from a generated registration token. For detailed steps generating a registration token, visit the documentation page for Generating a registration token. It provides options to specify various parameters, such as the data center URL, installation flag, registration token, and installer path. The script will then register the agent and apply the plan to it. The script can also be executed with parameters, in which case the script will register the agent and apply the plan to it using the specified parameters. The script will output the result of the operation to the console. If the agent has not been installed, the user can install the agent, register, and apply the plan. If installation has already been performed, the user can register and apply the plan without reinstalling the agent, which is the default behavior.

Download
You can click to download the script here.


Usage

Download the script to the Windows machine you wish to install or register the agent on.
[Optional] If you have not already done so, and wish to install Acronis Cyber Protect, either download the Acronis Cyber Protect Cloud installer from the Acronis Cyber Cloud console or set Install parameter to 1 and do not pass an InstallerPath parameter. If Acronis Cyber Protect is already installed, you can skip this step.
Open a PowerShell terminal and navigate to the directory where the script is located.
Run the script with the desired parameters. If you do not enter any parameters, the script will prompt you to enter the required parameters. If you enter parameters, the script will register the agent and apply the plan to it using the specified parameters.

Automatically download and install Acronis Cyber Protect (Install is set to 1):
.\RegisterAgentAndApplyPlan.ps1 [-DataCenterUrl] <string> [-RegToken] <string> [-Install] <boolean>


OR
Specify the path to an installer file:
.\RegisterAgentAndApplyPlan.ps1 [-DataCenterUrl] <string> [-RegToken] <string> [-Install] <boolean> [-InstallerPath] <string>


OR
Where the agent is already installed. Only register and apply a plan to an agent (Install is set to 0):
.\RegisterAgentAndApplyPlan.ps1 [-DataCenterUrl] <string> [-RegToken] <string> [-Install] <boolean>



The script will output live updates to the console and create a log file in the execution directory. The log file will contain the HTTP response code and the response body of the requests for more detailed information.



Parameters

-DataCenterUrl: URL of the data center. Example: https://dc1.acronis.cloud
-RegToken: Registration token. Visit the documentation page for Generating a registration token.
-Install: Boolean flag (0 OR 1) to specify if installation is to be performed. Default is false (0).
-InstallerPath: Path to the installer file. The path should end with ‘.exe’. Not required. If Install is set to 1, ensure that AcronisCyberProtect_AgentForWindows_web.exe is in the same directory as the script. If you wish to use a different installer, or if the installer is not in the same directory as the script, you must specify the path to the installer. If Install is set to 0, the default directory used is  ...ProgramFiles\BackupClient\RegisterAgentTool\register_agent.exe. If register_agent.exe is not in the default directory, you must specify the path to register_agent.exe.



Examples
Visit the documentation page for Generating a registration token.
.\RegisterAgentAndApplyPlan.ps1 -DataCenterUrl "https://eu8.acronis.cloud" -RegToken "7D59-6214-4A03" -Install 1


This example registers the agent and applies a plan to it using the specified registration token, and automatically downloads and installs Acronis Cyber Protect.
.\RegisterAgentAndApplyPlan.ps1 -DataCenterUrl "https://eu8.acronis.cloud" -RegToken "7D59-6214-4A03" -Install 1 -InstallerPath "C:\Users\myAccount\Downloads\AcronisCyberProtect_AgentForWindows_web.exe"


This example registers the agent and applies a plan to it using the specified registration token, and installs Acronis Cyber Protect using the specified installer path.
.\RegisterAgentAndApplyPlan.ps1 -DataCenterUrl "https://eu8.acronis.cloud" -RegToken "7D59-6214-4A03" -Install 0


This example is with a machine where the agent is already installed, but not registered. It registers the agent and applies a plan to it using the specified registration token.