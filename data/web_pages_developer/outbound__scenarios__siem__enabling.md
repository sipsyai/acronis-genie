---
title: "Enabling the integration"
source: "https://developer.acronis.com/doc/outbound/scenarios/siem/enabling.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:51.621821"
---

# Enabling the integration

Enabling the integration
The MSP want to enable an CyberApp between Acronis and the SIEM.

Preconditions
The MSP has:

An account in Acronis Cyber Protect Cloud.
An account in the vendor’s SIEM system.



Basic flow

The MSP enables the CyberApp.


Provides API credentials, where needed. (For example, Client ID/Name, Client Secret, Tenant, etc.).
Clicks the Save button.



The CyberApp validates the settings by making a test API call.



Post conditions
If the validation:


Succeeds
The CyberApp is enabled, but it is not yet configured (no customer mapping).



Fails
An error message is displayed.





API endpoints

Fetch Current User Self Info.
Create API Client.
Request Bearer Access Tokens.

Postman collection
Authorization flow.