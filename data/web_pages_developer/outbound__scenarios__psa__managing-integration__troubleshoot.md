---
title: "Troubleshooting the connection"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/managing-integration/troubleshoot.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:40.270529"
---

# Troubleshooting the connection

Troubleshooting the connection
The MSP wants to troubleshoot the connectivity between Acronis and PSA.

Preconditions

The MSP has enabled the CyberApp.



Triggers

If the CyberApp cannot connect to Acronis due to invalid credentials, then the vendor’s PSA interface:

Must display an inline error message.
Must show the corresponding CyberApp status in the CyberApp statistics.


If, during periodic syncs, the CyberApp module cannot connect to Acronis because it is not available,
it should count the number of failed sync tasks and generate an alert after 3 subsequent failed syncs.



API endpoints
For Trigger 1
Use the CyberApp’s API Client keys (client ID and secret) and check via request bearer access tokens to define the inline error message and status based on the corresponding response code, status and error message.
For Trigger 2
In the case where the integrated Acronis DC is not available, the Acronis Cloud connection verification tool could be implemented and - based on the results - either fix on CyberApp side or reach Acronis support.