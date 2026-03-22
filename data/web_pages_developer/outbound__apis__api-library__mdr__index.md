---
title: "Endpoint Detection and Response API"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/mdr/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:48.606632"
---

# Endpoint Detection and Response API

Endpoint Detection and Response API
This document covers the Endpoint Detection and Response (EDR) application programming interface (Endpoint Detection and Response API).

What can I do with the Endpoint Detection and Response API?
This interface enables integration developers to programmatically leverage the following functionality:

Fetch information about incidents.
Manage the incident investigation state.
Perform a response action on the incident.
Perform batch update of the investigation states.

For more details on the Endpoint Detection and Response (EDR) functionality, see the product documentation.


Data format
The API uses HTTP/1.1 protocol and operates mostly with JSON-formatted messages.


Location
The Acronis Endpoint Detection and Response API is available at a specific URL (the base URL): <datacenter_url>/api/mdr/v<version>, where:


<datacenter_url> is the URL of the Acronis data center where the client using the API is registered.

<version> is the API version number.
The Endpoint Detection and Response API is currently version 1.





In this section

Fetching incidents
Fetching incident details and response actions
Performing and monitoring response actions
Updating incident investigation state
Updating a batch of investigation states