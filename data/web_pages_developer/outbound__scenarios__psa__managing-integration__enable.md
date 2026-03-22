---
title: "Enabling"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/managing-integration/enable.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:31.861696"
---

# Enabling

Enabling
The MSP wants to to enable the CyberApp between Acronis and PSA.

Preconditions

MSP has an account in Acronis Cyber Protect Cloud.
MSP has an account in the PSA system.



Basic flow

In the vendor’s PSA interface, the MSP enters the API credentials from Acronis Cyber Protect Cloud.
(For example, client ID, client secret, data center URL, tenant, etc.).
The CyberApp uses the credentials to authenticate in the Acronis Cyber Protect Cloud
by requesting an access token.



Post conditions
If the request:


Is successful
The CyberApp should become active, but not yet configured (no customer mapping, no product or ticket mapping).



Fails
An error message is displayed in the vendor’s PSA interface.





API endpoints

Fetch current user info.
Create API client.
Request bearer access tokens.

Postman collection
Authorization flow.