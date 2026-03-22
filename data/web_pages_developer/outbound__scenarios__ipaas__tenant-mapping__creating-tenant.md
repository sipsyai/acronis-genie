---
title: "Creating or updating a customer tenant"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tenant-mapping/creating-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:28.711654"
---

# Creating or updating a customer tenant

Creating or updating a customer tenant
The MSP wants to be able to create a new customer tenant or update an existing customer tenant from within workflow in order to automate customer provisioning.

Standard input fields


Field
Value
Mandatory



Customer name
Text string


Mode

One of:
Trial
Production






2FA

One of:
Enabled
Disabled






Enhanced Security Mode

One of:
Enabled
Disabled






Administrator first name
Text string


Administrator last name
Text string


Email address
Text string


Language
Pulldown menu with all languages supported by Acronis. Default to English.






Input fields if Acronis PSA is enabled for the partner tenant


Field
Value
Mandatory



Business name
Text string. Same as customer name if left empty.


Type

One of:
Customer
Prospect






Debtor code
Number


Email
Text string. Use admin email if left empty.


Website
Text string


Main office
One, from a list of Customers.


VAT / Sales tax number
Text string


Country
Text string. Use partner tenant country if left empty.


Send invoices by

One of:
Mail (default)
Email






Tax

One of:
Tax-exempt (default)
or one from a list of taxes in Acronis PSA






Street
Text string


Number



Building



State



City



ZIP Code



Phone



Fax







Suggested default values to be used by the integration


Field
Value



Management mode
Managed by Service Provider.

Services
By default, all services are enabled.

Quotas
By default, all quotas are set to unlimited.





Post conditions

The customer tenant is created.
It is advised to enable all services and set all quotas to unlimited.