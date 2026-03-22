---
title: "Switching customer tenant to production"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tenant-mapping/switching2production.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:53.980315"
---

# Switching customer tenant to production

Switching customer tenant to production
The MSP wants to be able to switch a customer tenant to production when usage billing starts.

Preconditions
A customer tenant exists in trial mode.


Input fields


Field
Value
Mandatory



Customer tenant name
Text string, or select from a pulldown.


Production start date
Defaults to today.






Suggested default values to be used by the integration


Field
Value



Mode
Production





Post conditions

Customer tenant that matches the name of the customer tenant input field is switched to production.
Production start timestamp is returned to the integration.