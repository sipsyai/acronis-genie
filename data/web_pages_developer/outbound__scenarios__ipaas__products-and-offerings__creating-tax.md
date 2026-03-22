---
title: "Creating a tax"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/products-and-offerings/creating-tax.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:07.697546"
---

# Creating a tax

Creating a tax
The MSP wants to be able to create a new tax in Acronis PSA.

Preconditions

Partner must have Acronis PSA enabled.


Note
If Acronis PSA is not enabled for this partner, the event should be shown in the pulldown list, but be shown as disabled.



Input fields


Field
Value
Mandatory



Active

One of:
Yes (default)
No






Tax code
Text string


Tax name
Text string


Tax rate
Float






Post conditions

A new tax object is created in Acronis PSA.