---
title: "Troubleshooting the connection"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/managing/troubleshoot.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:40.095831"
---

# Troubleshooting the connection

Troubleshooting the connection

Preconditions

MSP has enabled the integration.



Triggers

If the integration cannot connect to Acronis due to invalid credentials, then the vendor’s RMM interface:

Must display an inline error message.
Must show the corresponding integration status in the integration statistics.


If, during period syncs, the integration module cannot connect to Acronis because it is not available,
it should count the number of failed sync tasks and generate an alert after 3 subsequent failed syncs.
Detailed information about the connection to Acronis Cyber Protect Cloud can be obtained with
Acronis Cloud Connection Verification Tool.