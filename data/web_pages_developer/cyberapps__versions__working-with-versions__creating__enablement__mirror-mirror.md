---
title: "Setting mirrored partner and customer enablement"
source: "https://developer.acronis.com/doc/cyberapps/versions/working-with-versions/creating/enablement/mirror-mirror.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:09:53.751234"
---

# Setting mirrored partner and customer enablement

Setting mirrored partner and customer enablement

To set mirrored partner and customer enablement

Select Create a new Partner-level record in the How MSPs will enable the CyberApp subsection of the CyberApp enablement options section.
In the How the CyberApp will be enabled for Customers subsection, select Mirror Acronis Customer tenants.
[Optional] Turn off the Seamless migration of customer tenants toggle switch.

Note

Only turn off this switch if customer tenant migration to another partner tenant is not possible on your side.
This might be the case, for example, because customer migration to another partner tenant requires some credentials update.



The Connection with your platform toggle switch is automatically turned on, and cannot be turned off.
The Connection with your platform toggle switch is automatically turned on, and cannot be turned off because callbacks are used to connect and communicate with your cloud service when the CyberApp is enabled.

Important
You must have a callback handler capable of servicing the mirrored partner enablement callbacks and the the mirrored customer enablement callbacks.


Enter the Callback handler base URL.