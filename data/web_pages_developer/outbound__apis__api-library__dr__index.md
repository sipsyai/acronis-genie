---
title: "Disaster Recovery API"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:49.688830"
---

# Disaster Recovery API

Disaster Recovery API
This document covers the Disaster Recovery application programming interface (Disaster Recovery API).

What can I do with the Disaster Recovery API?
This interface enables system administrators to programmatically leverage the following functionality:

Manage recovery servers.
Perform test or production failover and stop it.
Check the connectivity status.
Navigate to DR site connectivity page and cloud server configuration page.
Navigate to remote console of cloud server.

For more details on the disaster recovery functionality, refer to the product documentation.


Data format
The API uses HTTP/1.1 protocol and operates mostly with JSON-formatted messages.


Location
The Acronis Disaster Recovery API is available at a specific URL (the base URL): <datacenter_url>/api/dr/v<version>, where:


<datacenter_url> is the URL of the Acronis data center where the client using the API is registered.

<version> is the API version number.
The Disaster Recovery API is currently version 2.





In this section

Before you start
API error codes
Managing cloud servers