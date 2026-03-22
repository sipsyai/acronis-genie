---
title: "Provisioning"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/provisioning/customer-options.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:31:14.076486"
---

# Provisioning

Provisioning
The MSP wants to configure the way customer tenants are created in Acronis.

Preconditions

The MSP has enabled the CyberApp.



Basic flow

The MSP can configure the following:

New customer tenants mode dropdown with 2 values:

Trial
Production (default)


Create accounts based on dropdown with 2 values:

Company’s primary contact (default)
Company name


Two-factor authentication checkbox (default: unselected)


The MSP changes the options (if necessary) and saves the changes.



Post conditions
Depending on the combination of the options above, the associated Acronis tenant and user accounts are created by the CyberApp using Acronis public API as follows:

The customer tenant will be created with the POST /tenants endpoint.
Depending on New customer tenants mode, the pricing mode of the tenant will be set using the PUT /tenants/{tenant_id}/pricing endpoint.
Depending on Two-factor authentication, the two-factor authentication setting will be set using the PUT /tenants/{tenant_id}/mfa/status endpoint.
Account is created based on the Company’s primary contact. The login user info for the new customer tenant will be set to match the first user of the mapped customer in PSA system:

User login is set to the PSA user’s first name.
User email is set to PSA user’s email.
First name is set to PSA user’s first name.
Last name is set to PSA user’s last name.


After the tenant is created, the account is created with the POST /users endpoint.
The CyberApp can activate the created account by setting the user’s password
or by sending an activation email to the user’s email.

If enhanced security mode is:


ON
Only encrypted backups will be allowed.



OFF
All backups will be allowed.







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