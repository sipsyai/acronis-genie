---
title: "Access model"
source: "https://developer.acronis.com/doc/introduction/access-model.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:11:02.343159"
---

# Access model

Access model

General rules
To access the Acronis Cyber Platform and the tenant, Acronis partners and end customers
create user accounts for their users. For service integrations, Acronis partners
create a service account for the integration called an API client.
To identify the access of user accounts and API clients, Acronis Cyber Platform uses access policies.


Access policies
An access policy is a record that specifies:

who is allowed to access (a user account or API client)
what they can access (tenant settings, workloads, alerts, etc.)
where they can access (a tenant)
what actions to perform (a role)


For example, a partner - being on the highest level of the tenant model hierarchy - can access all sub-tenants.
This means that a partner user account can access each sub-tenant setting, services configuration, user accounts, etc.
At the same time, the user account will not be able to access any neighboring tenants or any tenants up the hierarchy or their data.





While the user account can access tenants and their data, the role applied to access policy defines what actions can be performed.
For example, the company administrator role allows any actions to be performed.
However, the read-only administrator role is only allowed to view tenants and their data.





Note

Access policies also apply to API clients.
An API client inherits the access policies from the user account that created it.




Management modes
In addition to general rules, Acronis Cyber Platform also provides two management modes that may alter the access to sub-tenants
for their administrators in parent tenants:


Managed by MSP mode
Allows access for parent tenant administrators.



Self-service management mode
Restricts access to the tenant for parent tenant administrators.



If sub-tenant administrators want to provide or restrict access to upper-level administrators, they can enable or disable support access in their tenant security settings.