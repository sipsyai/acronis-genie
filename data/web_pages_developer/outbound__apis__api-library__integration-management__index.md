---
title: "Integration Management"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/integration-management/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:31.803302"
---

# Integration Management

Integration Management

Introduction

You can use the Acronis Integration Management API to report an Acronis partner tenant integration status to Acronis platform.

The Acronis Integration Management API is commonly used for outbound integrations which have a ‘proxy’ CyberApp deployed as a catalog-only deployment.
When an outbound integration is activated, the CyberApp catalog card status is set to IN USE for the tenant.
If the integration is deactivated, the CyberApp catalog card status is cleared for the tenant.



Data format
The API uses the secure HTTP/1.1 over TLS 1.2 protocol, and operates mostly with JSON-formatted messages.


Location
The Acronis Integration Management API is available at a specific URL (the base URL): <datacenter_url>/api/integration_management/v<version>, where:


<datacenter_url> is the URL of the Acronis data center where the client using the API is registered.

<version> is the API version number.
The Integration Management API is currently version 2.





In this section

API endpoint
Activating an integration
Deactivating an integration