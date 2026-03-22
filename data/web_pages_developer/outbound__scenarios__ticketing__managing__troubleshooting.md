---
title: "Troubleshooting the connection"
source: "https://developer.acronis.com/doc/outbound/scenarios/ticketing/managing/troubleshooting.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:25.263573"
---

# Troubleshooting the connection

Troubleshooting the connection
The MSP wants to troubleshoot connectivity between Acronis and the ticketing system.

Preconditions

MSP has enabled the CyberApp.



Triggers

If the CyberApp cannot connect to Acronis due to invalid credentials, then the vendor’s ticketing interface:


Must display an inline error message.
Must show the corresponding CyberApp status in the CyberApp statistics.



If, during period syncs, the CyberApp module cannot connect to Acronis because it is not available, it should count the number of failed sync tasks and generate an alert after 3 subsequent failed syncs.



API endpoints
For trigger 1
Use the CyberApp’s API client keys (client ID and secret) and check via request bearer access tokens to define the inline error message and status based on the corresponding response code, status and error message.
For trigger 2
In the case where the integrated Acronis DC is not available, the Acronis Cloud connection verification tool could be implemented and based on the results either fix on CyberApp side or reach Acronis support.