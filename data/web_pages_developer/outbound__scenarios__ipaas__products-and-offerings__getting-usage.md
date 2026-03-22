---
title: "Getting usage report"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/products-and-offerings/getting-usage.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:20.296617"
---

# Getting usage report

Getting usage report
The MSP wants to be able to get usage reporting for one or more customer tenants.

Prerequisite

A customer tenant exists and has usage.



Input fields


Field
Value
Mandatory



Customer tenant name
Text string, or select from a pulldown.






Post conditions

If a customer tenant with this name exists, the integration returns enabled offering items and their usage.
If no customer tenant with this name can be found, the integration will return a message like Customer not found.