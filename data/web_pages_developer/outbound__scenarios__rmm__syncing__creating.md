---
title: "Creating tickets"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/syncing/creating.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:09.525508"
---

# Creating tickets

Creating tickets
The MSP wants to see tickets created for the mapped alerts in the RMM.

Preconditions

MSP has enabled the integration.
Completed alert mapping scenario successfully.
Ticketing is enabled.
Alerts mapped to tickets.



Basic flow
The integration gets ticket types, categories, statuses, priorities and agents.
MSP defines for which alert type tickets should be created, and sets type, category, status, priority and agent for each.


Post conditions
If the tickets feature is:

Enabled, and a mapped alert is raised for the mapped customer tenant in Acronis, then a linked ticket is generated in RMM and for the respective customer account.
Disabled, then tickets will not be generated.


Automatically create tickets
If the Automatically create ticket feature is:

Enabled and a mapped alert is raised for mapped customer tenant in Acronis, then a linked ticket is generated in the RMM and for the respective customer account.
Disabled, then tickets will not be generated.




API endpoints
No need to do through Acronis API.

Note
This requires development on the CyberApp side.