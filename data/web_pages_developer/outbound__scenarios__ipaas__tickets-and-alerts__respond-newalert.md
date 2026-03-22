---
title: "Responding to a new alert"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tickets-and-alerts/respond-newalert.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:15.014665"
---

# Responding to a new alert

Responding to a new alert
The MSP wants to be able to trigger an automation every time an alert is created in Acronis.

Input fields


Field
Value
Mandatory



Customer name
Text string, or select from a pulldown (allow for multiples).


Device

MSP can select one or more devices that belong to selected customer tenants.
By default, all devices are selected.




Severity

Select one or more severities.
By default, all severities are selected.




Alert types

Select one or more alert types.
By default, no types are selected.








Output fields


Field
Example value



Alert ID
1234

Alert type
Backup failed

Alert category
Antimalware protection

Alert severity
Critical

Alert date
Mar 01, 2023, 06:24

DC
us5-cloud

Partner tenant name
MSP Inc

Customer tenant name
macShop

Device name
my-macbook.local

Device url
URL that links to device in management console.

Registered to
John Doe

Alert title
Automatic update has failed

Alert body
Automatic update of the agent installed on ‘My-MacBook.local’ has failed, and it is now suspended. You can update this agent manually, by using an installation file from the ‘Downloads’ section.

KB link
URL to kb.acronis.com





Post conditions

When a new alert exists on Acronis, the integration is triggered and the output fields are supplied as information.