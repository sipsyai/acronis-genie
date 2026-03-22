---
title: "Billing settings"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/billing/billing-settings.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:10.770224"
---

# Billing settings

Billing settings

Warning

Billing settings can only be set for partner tenants.
Billing settings are not inherited by child tenants, and are set individually for each tenant.



Available billing settings
The platform provides a set of settings to enable partners to automate provisioning of the services.








Name
API setting name
Description
Permission



Tier level
tier_level_value
The level of minimum commitment i.e. volume discount. See available tier levels.
Read/Write

Licensing mode
licensing_mode
The mode defining how the partner will be charged for the services. See available licensing modes.
Read/Write

Contract type
contract_type
Type of the legal contract.
Read only

Acronis Account Number
acronis_account_number
The identifier of the customer.
Read only

Price list
pricing_info
Pricing information for the provided services.
Read only




Available licensing modes






Licensing mode
Description



per_gb
The partner is charged for storage usage only (Acronis Hosted, Azure Hosted, Google Hosted, Hybrid or local storage).

per_device
The partner is charged for each protected device and additionally for Acronis, Google or Azure Hosted storage. Hybrid Storage and Local Storage are included into the device fee.





Available tier levels






Tier level
Value



No commitment
-1

Tier 1
0

Tier 2
1

Tier 3
2

Tier 4
3

Tier 5
4



When the tier level and licensing mode are set, the administrator of the partner tenant will be able to see it under the Legal section in the management portal.