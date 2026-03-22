---
title: "Setting mapped partner and explicit customer enablement"
source: "https://developer.acronis.com/doc/cyberapps/versions/working-with-versions/creating/enablement/mapping-explicit.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:09:22.749679"
---

# Setting mapped partner and explicit customer enablement

Setting mapped partner and explicit customer enablement

To set mapped partner and explicit customer enablement


Select Provide Partner-level acount credentials in the How MSPs will enable the CyberApp subsection of the CyberApp enablement options section.



Select the Work with Acronis data only radio button option in the How the CyberApp will be enabled for Customers subsection.


[Optional] Turn off the Seamless migration of customer tenants toggle switch.

Note

Only turn off this switch if customer tenant migration to another partner tenant is not possible on your side.
This might be the case, for example, because customer migration to another partner tenant requires some credentials update.




The Connection with your platform toggle switch is automatically turned on, and cannot be turned off because callbacks are used to connect and communicate with your cloud service when the CyberApp is enabled.


Important
You must have a callback handler capable of servicing the mapping enablement callbacks.



Enter the Callback handler base URL.