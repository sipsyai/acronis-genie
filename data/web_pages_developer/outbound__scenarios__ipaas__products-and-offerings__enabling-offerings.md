---
title: "Enabling an offering item"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/products-and-offerings/enabling-offerings.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:11.899869"
---

# Enabling an offering item

Enabling an offering item
The MSP wants to be able to enable offering items.

Preconditions

Customer tenant exists.



Input fields


Field
Value
Mandatory



Customer tenant name
Text string, or select from a pulldown.


Offering item
Text string


Quota
Int






Post conditions


If a customer tenant with this name exists, the offering item will be enabled:
Quota will be set to value given. If no value is given, quota will be set to Unlimited.




If a customer tenant with this name exists, and the offering item is already enabled, its state will not change.
If no customer tenant with this name can be found, the integration will return a message like Customer not found.