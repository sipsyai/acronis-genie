---
title: "Getting a list of available offering items"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/products-and-offerings/getting-offerings.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:16.093057"
---

# Getting a list of available offering items

Getting a list of available offering items
The MSP wants to be able to get a list of available offering items for a specific customer tenant.

Preconditions

One or more customer tenants exist.
Customer tenants have services and offering items that are enabled.



Input fields


Field
Value
Mandatory



Customer tenant name
Text string, or select from a pulldown.






Post conditions

If a customer tenant with this name exists, a list of available offering items and their status (enabled/disabled) will be returned.
If no customer tenant with this name exists, the integration will return an error message like Customer not found.
If the customer tenant exists, but no offering items are enabled, the integration will return a message like No Offering Items are enabled.