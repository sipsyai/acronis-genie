---
title: "Deactivating an outbound integration"
source: "https://developer.acronis.com/doc/outbound/deactivation.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:21.278940"
---

# Deactivating an outbound integration

Deactivating an outbound integration

Note
This section is only valid if the outbound integration is listed on the Acronis integration catalogs, the MSP has previously activated the integration, and you have activated the integration for the MSP tenant.

Acronis integrations are listed on data center integration catalogs. When an MSP has previously activated an integration, and decides to stop using it, they must deactivate it for their tenant.
When they do this, the integration must register the deactivation using an API, so that:

the integration catalog card displays no longer appears as IN USE for the MSP.
the integration use statistics are recorded correctly.


To deactivate an outbound integration

The MSP locates the integration catalog card in the IN USE tab of the integration catalog.
The MSP clicks Deactivate on the catalog card.
When the MSP verifies deactivation by clicking Delete, the integration must send a deactivation API query to update and correctly display the integration status in Acronis Cyber Protect Cloud Console.