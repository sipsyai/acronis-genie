---
title: "Disabling"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/managing/disable.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:27.181500"
---

# Disabling

Disabling
MSP wants to temporarily disable (or permanently delete) the CyberApp and stop synchronization, so no updates are made on either side.

Preconditions

CyberApp was previously enabled.



Post conditions

When the MSP disables CyberApp
Usage synchronization stops.
Product mapping configuration is preserved until the feature is enabled again.
Ticket creation configuration is preserved until the feature is enabled again.


When the MSP deletes the CyberApp from within the RMM UI
The CyberApp is deactivated.
All CyberApp settings are removed.
Tenants, workloads and policies are not affected.





API endpoints
None. No need to do this through the Acronis API.