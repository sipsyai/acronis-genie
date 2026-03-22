---
title: "Dismissing an alert"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tickets-and-alerts/dismiss-alert.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:02.392740"
---

# Dismissing an alert

Dismissing an alert
The MSP wants to be able to dismiss an existing alert in Acronis.

Preconditions

Customer tenant exists with open alerts.
Get Alert ID with new alert trigger.



Input fields


Field
Value
Mandatory



Customer tenant name
Text string, or select from a pulldown.


Alert ID
Int






Post conditions

If the alert ID is found, the alert on Acronis gets dismissed.
If the alert ID matches no alert on Acronis, an error message is returned like Alert was not found.