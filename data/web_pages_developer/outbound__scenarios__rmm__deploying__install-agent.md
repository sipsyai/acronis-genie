---
title: "Installing the Acronis agent"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/deploying/install-agent.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:10.368616"
---

# Installing the Acronis agent

Installing the Acronis agent
The MSP wants to deploy/uninstall/upgrade the Acronis agent to endpoints managed by the RMM.

Preconditions

The MSP has enabled the CyberApp.
Successful customer mapping.
Data center URL where the customer is located has been fetched from the mapping.



Basic flow
These tasks are done using scripts:

The MSP selects the workloads and clicks an option to install or deploy the Acronis agent.
Option for vendor #1: Create a new registration token
for the selected workloads.
Option for vendor #2: Create a new registration token,
refresh the token every 30 minutes and get it from local storage when required.

RMM service sends an agent installation script, along with the registration token and the Acronis data center URL to the RMM agent on the workload.
The RMM agent executes the script, passing the token and URL as arguments.
The script:

Fetches a list of installers from the Acronis data center using the GET /agent_update_references endpoint.
Parses that list to find the installer for the current OS.
Downloads the installer.
Executes the installer.
Once the installation completes, it registers the agent and passes the token as an argument.




Note
The agent installation script can be found in Register agent and apply plan.


Note

If the option uninstall agent is selected, then the script runs the uninstall command, which uninstalls the agent from the workload and unregisters it from Acronis.
If the upgrade agent option is selected, then the script runs the upgrade command, which runs agent update.




API endpoints
Blogs

Base for all flows: Automate Acronis agent installations.
Installation on Windows: Customize unattended Acronis Cyber agent installation on Windows.
Installation on Linux: Customize Unattended Acronis Cyber Agent Installation on Linux.
Installation on MacOS : Customize Unattended Acronis Agent Installation on macOS.

Request agent registration token via API

Create registration token.
Fetch registration tokens.

Postman examples

Note
There are 2 ways to use this endpoint.


Create registration token using a user personal tenant.
Create registration token using a customer tenant and a user personal tenant.

Download agent for Windows, Linux, macOS via API

Fetch agent update reference by attributes.

Remove agent and registration from a tenant

Delete resources.

Update agent

Run agent update now.

Blogs

Automate agents update management using API.
Update agent automatically and monitor update statuses using API.