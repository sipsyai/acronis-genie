---
title: "Activating an outbound integration"
source: "https://developer.acronis.com/doc/outbound/activation.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:13:53.941886"
---

# Activating an outbound integration

Activating an outbound integration

Note
This section is only valid if the outbound integration is listed on the Acronis integration catalogs.

Acronis integrations are listed on data center integration catalogs. When an MSP wants to use an integration, they must activate it for their tenant.
When they do this, the integration must register the activation using an API, so that:

the integration catalog card displays as IN USE for the MSP.
the use of your integration can be recorded correctly.


Important

The reverse applies for deactivating an outbound integration.



To activate an outbound integration for an MSP

The MSP finds the integration on the integration catalog and decides to activate it.

The MSP clicks Configure on the catalog card to activate the integration.
The exact process will vary, depending on the platform the integration was built into, but will always include a step where the MSP must provide:




The URL of the data center (DC) where the tenant for the MSP is provisioned.
The MSP can find this by logging into Acronis Cyber Protect Cloud and looking at the browser address bar. An example of such a URL is eu8.acronis.cloud.



An API client, which consists of an ID and a Secret.
To find out how to create an API client, see the Managing API clients chapter of the Partner Administrator help guide..






When the API credentials are validated, and the integration is correctly activated for the MSP, the integration must send an activation API query to Acronis.