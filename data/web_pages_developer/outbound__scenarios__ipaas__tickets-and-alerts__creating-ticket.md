---
title: "Creating a ticket"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tickets-and-alerts/creating-ticket.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:58.193698"
---

# Creating a ticket

Creating a ticket
The MSP wants to be able to create a new ticket in Acronis PSA.

Preconditions

Partner must have Acronis PSA enabled.


Note
If Acronis PSA is not enabled for this partner, the event should be shown in the pulldown list, but be shown as disabled.



Input fields


Field
Value
Mandatory



Ticket title
String


Billable

One of:
Yes
No (default)






Email to customer

One of:
Yes
No (default)






End-user
One from a list of end-users in Acronis PSA.


Customer name
One from a list of customers in Acronis PSA.


Phone number
Text string


Superior
Text string


Priority
One from a list of priorities in Acronis PSA.


SLA
One from a list of SLAs in Acronis PSA.


Support agent
One from a list of agent users in Acronis PSA.


Category
One from a list of categories in Acronis PSA.


Support group
One from a list of user groups in Acronis PSA.


Status
One from a list of statuses in Acronis PSA.


Billing activity type
One from a list of billing types in Acronis PSA.


Schedule ticket

Either:
No


or
Date
Time
Duration in hours and minutes






Ticket notes
Text string


Ticket updates
Text string






Post conditions

A ticket is created in Acronis PSA, and the integration returns the ticket.