---
title: "Mapping tickets"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/syncing/mapping-tickets.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:17.951883"
---

# Mapping tickets

Mapping tickets

The MSP wants to be able to see existing mapping between Acronis alerts and RMM tickets.
The MSP wants to receive only alerts for selected alert types.


Preconditions

MSP has enabled the integration.



Basic flow

The integration can fetch a list of all Acronis alerts using the GET /alerts
endpoint and process it based on the alerts mapping.
For each enabled alert type, MSP can select default options that would help the MSP prioritize the ticket and get the tickets assigned to the right team/person.
The ticket may include the following information and it’s up to the vendor to determine what to display:

Acronis alert.
RMM type.
RMM category (if available).
RMM status (if available).
RMM SLA (if available).
RMM priority (if available).


The MSP needs to be able to edit the alert information. The MSP defines for which alert type tickets should be created, and sets type, category, status, priority and agent for each:

Ticket type.
Category.
Status.
SLA.
Priority (depends on SLA).





API endpoints
Get all alerts

Fetch all alerts.


Note
Specific scenarios and grouping can be achieved with other endpoints found and listed on the same page.

Blog article

Advanced monitoring automation with Acronis Cyber Protect Cloud.