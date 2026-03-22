---
title: "Enabling"
source: "https://developer.acronis.com/doc/outbound/scenarios/ticketing/managing/enabling.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:16.852630"
---

# Enabling

Enabling
The MSP wants to enable the integration between Acronis Cyber Platform and the ticketing system.

Preconditions

MSP has an account in Acronis Cyber Protect Cloud.
MSP has an account in the vendor’s ticketing system.
Exchange of API keys and specific scripts between Acronis Cyber Protect and ticketing system.



Basic flow

In the vendor’s ticketing interface, the MSP enters the API credentials from Acronis Cyber Protect Cloud.
(For example, client ID, client secret, data center URL, tenant, etc.).
The CyberApp uses the credentials to authenticate in the Acronis Cyber Protect Cloud
by requesting an access token.



Post conditions

If the CyberApp is enabled successfully, the CyberApp becomes active, but is not yet configured (no customer mapping, no product or ticket mapping).
If the request fails, an error message is displayed in the vendor’s ticketing interface.



API endpoints

Fetch current user info.
Create API client.
Request bearer access tokens.

Postman collection
Authorization flow.