---
title: "Ticket options"
source: "https://developer.acronis.com/doc/outbound/scenarios/ticketing/syncronizing/options.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:59.037391"
---

# Ticket options

Ticket options

Creating tickets automatically
MSP needs to have the Automatically create ticket option:

If the Automatically create ticket feature is enabled, and a mapped alert is raised for the mapped customer tenant in Acronis, then a linked ticket is generated in Ticketing and for the respective customer account.
If the Automatically create ticket feature is disabled, then tickets will not be automatically generated.

The CyberApp can use the GET /alerts
to fetch multiple alerts for multiple re-opened tickets.


Resolving tickets automatically
MSP needs to have the Automatically resolve tickets option:

If the option Automatically resolve tickets is enabled, and a linked alert is cleared manually or automatically in Acronis, then the linked ticket status in Ticketing is set to the selected value from the dropdown.
If the option Automatically resolve tickets is disabled, then the Ticketing ticket is not updated. This is the default option.

The CyberApp can use DELETE /alerts/{id}
to delete a single alert for the ticket or use DELETE /alerts
to delete multiple alerts for multiple tickets.


Re-opening tickets
If a ticketing ticket for a certain Acronis alert is already created and then closed, then MSP needs to have the option to reopen it when an Acronis alert is re-raised in a short period of time:

The option must be disabled by default.
The Days field is set to “1” by default.
If Automatically reopen ticket option is disabled, then a new ticket is created always when the alert is raised.
If Automatically reopen ticket option is enabled, and the same alert is raised before the number of days has passed, then the last linked closed ticket is reopened and alert detail is added to it.
If Automatically reopen ticket option is enabled, and the same alert is raised after the number of days has passed, then a new ticket is created and alert detail is added to it.

The CyberApp can use the GET /alerts/{id}
endpoint to fetch the alert for the re-opened ticket or use the GET /alerts
endpoint to fetch multiple alerts for multiple re-opened tickets.


Clearing alerts automatically
MSP needs to have the option Automatically clear alert:

The option must be disabled by default.
If the Automatically clear alert option is enabled, and a ticket status in ticketing is set to the selected dropdown value, then the linked alert is cleared on Acronis side.
If the Automatically clear alert option is disabled, then the linked alert is not cleared.



API endpoints
Clear/dismiss/delete alerts

Dismiss an alert by ID.
Dismiss alerts by filter.


Note

CyberApp’s ticket that originated from the Acronis alert requires development with ticket auto-closure feature on the CyberApp side.
Closing the ticket from the CyberApp should trigger the clear alerts endpoints on Acronis side.


Re-open tickets by fetching all alerts

Fetch all alerts.
Fetch an alert by ID.


Note

If an Acronis alert re-opens, it will be re-opened with the same alert_id value with updated details.
The CyberApp side should preserve - for a short period of time - the old IDs and their relations with the corresponding ticket to assure re-opening the same ticket with same ticket ID.
Specific scenarios and grouping can be achieved with other endpoints found and listed at the same page.