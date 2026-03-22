---
title: "Creating contract parts"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/products-and-offerings/creating-contractparts.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:55.034722"
---

# Creating contract parts

Creating contract parts
The MSP wants to be able to create new contract parts in Acronis PSA.

Preconditions

Partner must have Acronis PSA enabled.


Note
If Acronis PSA is not enabled for this partner, the event should be shown in the pulldown list, but be shown as disabled.



Input fields


Field
Value
Mandatory



Contract part type

One of:
Default type (default)
ICT services
Managed service






Product
One of a list of contract products in Acronis PSA.


Quantity
Int


Price
Number


Discount percentage
Number


Description
Text


Start date
Date. Equal to contract start date, if left empty.


End date
Date. sets ‘Bill forever’ to True, if left empty.


Trial

One of:
Yes
No (default)






SLA
One from a list of SLAs in Acronis PSA.






Post conditions

A new contract parts object is created in Acronis PSA.