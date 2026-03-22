---
title: "Enabling the integration"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/enabling.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:42.279320"
---

# Enabling the integration

Enabling the integration
The MSP wants to configure Acronis API credentials to enable the integration.

Preconditions
The MSP has:

An account in Acronis Cyber Protect Cloud.
An account on the Workflow Automation platform.



Basic flow
The MSP starts the authentication process, and is asked to provide the following:


Acronis datacenter URL
API key
API secret




Post conditions

Credentials are tested before the window closes.


Note
If credentials are invalid, an Invalid credentials error must be raised in the window.


The window closes, and the MSP is returned to workflow building flow.
Integration activation is reported via API, and the integration tile in the Application Catalog is set to In use.