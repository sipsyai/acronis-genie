---
title: "Creating tickets"
source: "https://developer.acronis.com/doc/outbound/scenarios/ticketing/syncronizing/creating.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:46.360410"
---

# Creating tickets

Creating tickets
The MSP wants to see tickets created in the ticketing system for the mapped alerts.

Preconditions

MSP has enabled the CyberApp.
Completed alert mapping scenario successfully.
Ticketing is enabled.
Alerts mapped to tickets.



Basic flow
The CyberApp gets ticket types, categories, statuses, priorities, and agents.
The MSP defines which alert type tickets should be created for, and sets type, category, status, priority, and agent for each.


Post conditions
If the tickets feature is:
*   Enabled, and a mapped alert is raised for the mapped customer tenant in Acronis, then a linked ticket is generated in ticketing, and for the respective customer account.
*   Disabled, then tickets will not be generated.

Automatically create tickets
If the Automatically create ticket feature is:
*   Enabled, and a mapped alert is raised for mapped customer tenant in Acronis, then a linked ticket is generated in XX Ticketing and for the respective customer account.
*   Disabled, then tickets will not be generated.



API endpoints
None