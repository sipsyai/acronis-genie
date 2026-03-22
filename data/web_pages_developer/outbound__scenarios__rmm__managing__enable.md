---
title: "Enabling"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/managing/enable.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:31.686706"
---

# Enabling

Enabling
The MSP wants to enable the CyberApp between Acronis and the RMM system.

Preconditions

MSP has an account in Acronis Cyber Protect Cloud.
MSP has an account in the RMM system.



Basic flow
In the vendor’s RMM interface, the MSP enters the API credentials from Acronis Cyber Protect Cloud. (For example, client ID, client secret, data center URL, tenant, etc.).


Post conditions
The CyberApp should become active, but is not yet configured (no customer mapping, no product or ticket mapping).

Note
If validation fails, the RMM interface should display an error message.



API endpoints

Fetch Current User Self Info
Create API Client

The integration uses the credentials to authenticate in the Acronis Cyber Protect Cloud by requesting an access token.


Notes
This establishes a connection between the Acronis partner tenant and the RMM tenant.
Many partners use multiple partner tenants across multiple data centres. Our most popular CyberApps support multiple partner tenant mapping.