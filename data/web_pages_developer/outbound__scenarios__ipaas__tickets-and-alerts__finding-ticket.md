---
title: "Finding a ticket"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tickets-and-alerts/finding-ticket.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:06.611437"
---

# Finding a ticket

Finding a ticket
The MSP wants to be able to find a specific, existing ticket in Acronis PSA, and to return status and other relevant information.

Preconditions

Partner must have Acronis PSA enabled.


Note
If Acronis PSA is not enabled for this partner, the event should be shown in the pulldown list, but be shown as disabled.



Input fields


Field
Value
Mandatory



Ticket number
Number






Post conditions

If the ticket number is found, returns a full list of all ticket fields, as well as ticket status.
If the ticket number is not found, returns an error like Ticket number not found.