---
title: "Automatic provisioning"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/provisioning/auto-provisioning.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:31:09.871906"
---

# Automatic provisioning

Automatic provisioning
The MSP wants to automatically provision a new Acronis customer tenant every time a new customer account is detected in PSA with active contract and assigned mapped features.

Preconditions

MSP has enabled the CyberApp.
Customer provisioning options are configured.



Basic flow

The following option needs to be available: Automatically create customers (default: off).
The MSP changes the option.
The MSP saves the changes.



Post conditions
If Automatically create customers is:


OFF
Customer tenants will not be created automatically.



ON
Customer tenants will be created automatically, according to the following flow:


The CyberApp detects which PSA customers are not mapped.
For every such customer, the CyberApp pulls available active contracts and checks if they have a service that is already mapped to Acronis feature.

If all the above is true, customer tenants are created.
For every new customer tenant, an account is also created using the options configured in the Customer provisioning options.







API endpoints
Create tenant


Create tenant.
The value of kind attribute defines the tenant type:


customer
partner
folder
unit




Note

Enhanced security mode is enabled/disabled with true/false value in:
"settings": {"enhanced_security": false}


Tenant billing mode (trial or production)

Update tenant pricing settings.

2FA / MFA

Fetch tenant MFA status.
Manage tenant MFA status.

Create a user for a tenant

Create user.

Set user roles

Update user access policies.

Activate a user by one of activation types

Activate with set user password.
Activate by send activation email.