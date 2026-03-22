---
title: "Automatic de-provisioning"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/provisioning/auto-deprovisioning.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:31:05.650549"
---

# Automatic de-provisioning

Automatic de-provisioning
The MSP wants to configure the way customer tenants are automatically de-provisioned in Acronis.

Preconditions

The MSP has enabled the CyberApp.



Basic flow

The following options for de-provisioning are available:

Disable the customers

On/Off  - Checkbox (default: Clear).
Days - Numeric field (default value: 10 days. Disabled when the checkbox is Clear).


Delete the customers

On/Off  - Checkbox (default: Clear).
Days - Numeric field (default value: 30 days. Disabled when the checkbox is Clear).




The MSP changes the options (if necessary) and saves the changes.



Post conditions

If Disable the customers is Selected, customer tenants will be disabled after
the specified number of Days after the CyberApp detects that the
mapped PSA customer account does not have an active contract with a mapped service.
The tenant will be disabled using the PUT /tenants/{tenant_id}
endpoint.
To verify that the tenant has been disabled, the CyberApp can use the GET /tenants/{tenant_id} endpoint.

If Delete the customers is Selected, customer tenants will be deleted after
the specified number of Days after the CyberApp detects that the
mapped PSA customer account does not have an active contract with a mapped service.
The tenant will be disabled using the PUT /tenants/{tenant_id}
endpoint and then deleted using the DELETE /tenants/{tenant_id}
endpoint.
To verify that the tenant has been deleted, the CyberApp can use the GET /tenants/{tenant_id} endpoint.




API endpoints
Disable tenant

Update tenant by setting "enabled": false in body.

Delete tenant

Delete tenant.

Check status

Fetch tenant.