---
title: "Automating tasks"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/tasks/automating.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:26.395954"
---

# Automating tasks

Automating tasks
The MSP wants to schedule and automate tasks for one or multiple devices.

Preconditions

MSP has enabled the integration.
MSP has already configured Acronis agents authentication.
MSP has deployed the Acronis agents to the target workloads.

Tasks include:

Run a backup by starting the backup policy execution.
Stop backup.
Run an antimalware scan starting the antimalware policy execution.
Apply or revoke a default protection plan by applying the policy to the workload.



Basic flow to run a script
These are scripts that are sent to the endpoint and talk to the agents.

MSP selects one of the available Remote Management scripts (Windows, Linux or Mac version):

Acronis_install_agent
Acronis_uninstall_agent
Acronis_manage_protection_plan
Acronis_scans


Enters the parameter values required by the script.
MSP runs the automation script.



Post conditions
The script is executed and the correct task is performed according to the script type and the script parameters specified by the MSP for the selected devices.


API endpoints
Run backup

Start policy execution

Stop backup

Possible with non-public API.

Run antimalware scan

Note
Input the sub-policy UUID to policy_id parameter in JSON body/payload.


Start Policy Execution

Apply plan

Create an application

Revoke plan

Revoke applications