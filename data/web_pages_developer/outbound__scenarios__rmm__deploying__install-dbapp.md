---
title: "Installing the agent for DB application backup"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/deploying/install-dbapp.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:14.572917"
---

# Installing the agent for DB application backup

Installing the agent for DB application backup
The MSP wants to install Acronis agent for DB application backup to customer’s server, so they can apply DB protection plan.

Preconditions

MSP has enabled the integration.
Successful customer mapping.
A registration token has been fetched via Acronis API.
The URL for the data center where the customer data is located has been fetched from the mapping.
Has administrator credentials for the DB.



Basic flow

The MSP selects whether they want to install, update or uninstall the Acronis Cyber Protect Cloud agent.
Selects a device from the list with DB (without the agent installed yet).
RMM system recognizes devices with a DB and initiates the corresponding agent installation.
If there is a DB installed on a device, the agent is provided with the DB module.



Post-conditions

Agent installation is initiated.



API endpoints
The same flow using scripts for Installing the Acronis agent can be used, downloading the agent’s installer for specific application aware or DB agent is possible by providing the value for the required agent component.