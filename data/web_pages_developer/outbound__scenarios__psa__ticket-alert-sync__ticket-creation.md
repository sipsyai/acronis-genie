---
title: "Creating tickets"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/ticket-alert-sync/ticket-creation.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:31:49.332743"
---

# Creating tickets

Creating tickets
The MSP wants to see tickets created in PSA for the mapped alerts.

Preconditions

The MSP has enabled the CyberApp.
Completed alert mapping scenario successfully.
Ticketing is enabled.
Alerts mapped to tickets.



Basic flow
The CyberApp gets ticket types, categories, statuses, priorities and agents.
The MSP defines which alert type tickets should be created for, then sets type, category, status, priority, and agent for each.


Post conditions
If the tickets feature is:


Enabled and a mapped alert is raised for the mapped customer tenant in Acronis
A linked ticket is generated in PSA and for the respective customer account.



Disabled
Tickets will not be generated.





API endpoints
None.