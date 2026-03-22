---
title: "Creating a product"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/products-and-offerings/creating-product.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:03.444320"
---

# Creating a product

Creating a product
The MSP wants to be able to create a new product in Acronis PSA.

Prerequisite

Partner must have Acronis PSA enabled.


Note
If Acronis PSA is not enabled for this partner, the event should be shown in the pulldown list, but be shown as disabled.



Input fields


Field
Value
Mandatory



Product name
Text string


Description
Text string


External id
Text string


Price
Number


Taxable



Cost
Number


Product type

One of:
Contract product
Project product
Activity-based ticket billing






Ticket product

One of:
Yes
No






Ledger
One of a list of ledger names in Acronis PSA.


Active

One of:
Yes
No






VAR product

One of:
Yes
No










Post conditions

A product is created in Acronis PSA with the provided fields and values.