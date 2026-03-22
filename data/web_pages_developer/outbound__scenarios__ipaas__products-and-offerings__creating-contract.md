---
title: "Creating a contract"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/products-and-offerings/creating-contract.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:50.826116"
---

# Creating a contract

Creating a contract
The MSP wants to be able to create a new contract in Acronis PSA in Acronis.

Preconditions

Partner must have Acronis PSA enabled.


Note
If Acronis PSA is not enabled for this partner, the event should be shown in the pulldown list, but be shown as disabled.



Input fields


Field
Value
Mandatory



Reference number
Text string


Contract name
Text string


Organization
One of a list of companies in Acronis PSA.


Contact email
Text string


Billing entity
One of a list of billing entities in Acronis PSA.


Invoice interval

One of:
Every month (default)
Quarterly
Semi-annually
Every year






When to bill

One of:
Upfront (default)
Afterwards






Payment method

One of:
Manually (default)
Via authorized debit






Start date
Date (without time).


End date

One of:
“Bill forever”
Date (without time)






Send invoice

One of:
By mail (default)
By email










Post conditions

A contract is created with the values provided.