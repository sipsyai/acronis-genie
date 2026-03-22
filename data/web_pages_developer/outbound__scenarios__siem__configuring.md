---
title: "Configuring"
source: "https://developer.acronis.com/doc/outbound/scenarios/siem/configuring.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:47.416168"
---

# Configuring

Configuring
The MSP wants to be able to test and troubleshoot the connectivity between Acronis and SIEM.

Preconditions
Within the SIEM, the MSP needs to have a Test CyberApp connection button (test API endpoint connection attempt).


Basic flow


Clicking the Test CyberApp connection button gives the following information:If the call to the test endpoint:


Succeeds
Display a “Connection successful” message.



Fails
Display a “Connection failed” message.






If the CyberApp cannot connect to Acronis system due to invalid credentials:


Display an inline error message.
The corresponding status should be shown in the CyberApp summary view.



If, during period syncs, the CyberApp cannot connect to Acronis because it is not available, it should count the number of failed sync tasks and generate an alert after 3 subsequent failed syncs.



API endpoints
None.