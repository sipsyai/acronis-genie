---
title: "Mapping tickets"
source: "https://developer.acronis.com/doc/outbound/scenarios/ticketing/syncronizing/mapping.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:54.797192"
---

# Mapping tickets

Mapping tickets
The MSP wants to see existing mapping between Acronis alerts and ticketing system tickets.
The MSP wants only to receive alerts for selected alert types.

Preconditions

MSP has enabled the CyberApp.



Basic flow

The CyberApp can fetch a list of all Acronis alerts using the GET /alerts
endpoint, and process it based on the alerts mapping.
For each enabled alert type, the MSP can select default options that would help the MSP prioritize the ticket and get the tickets assigned to the right team/person.
The ticket may include the following information, and it’s up to the vendor to determine what to display:

Acronis alert.
Ticketing type.
Ticketing category (if available).
Ticketing status (if available).
Ticketing SLA (if available).
Ticketing priority (if available).



The MSP needs to be able to edit the alert information.
The MSP defines for which alert type tickets should be created, and sets type, category, status, priority, and agent for each:


Ticket type.
Category.
Status.
SLA.
Priority (depends on SLA).





API endpoints

Fetch all alerts


Note
Specific scenarios and grouping can be achieved with other endpoints found and listed at the same page.

Blog article

Advanced monitoring automation with Acronis Cyber Protect Cloud.