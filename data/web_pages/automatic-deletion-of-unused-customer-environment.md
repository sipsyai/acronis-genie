# Automatic deletion of unused customer environments on the cloud site

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Automatic deletion of unused customer environments on the cloud site
Automatic deletion of unused customer environments on the cloud site

The Disaster Recovery service tracks the usage of the customer environments created for disaster recovery purposes and automatically deletes them if they are unused.

The following criteria are used to define if the customer tenant is active:

Currently, there is at least one cloud server or there were cloud server(s) in the last seven days.

OR

The VPN access to local site option is enabled and either the Site-to-site Open VPN tunnel is established or there are data reported from the VPN appliance for the last 7 days.

All the rest of the tenants are considered as inactive tenants. For such tenants the system performs the following:

Deletes the VPN gateway and all cloud resources related to the tenant.
Unregisters the VPN appliance.

The inactive tenants are rolled back to their state before the connectivity was configured.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.