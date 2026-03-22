# User accounts and tenants

User accounts and tenants
User accounts and tenants

User accounts

There are two user account types:

Administrator accounts

These have access to Management Portal. They have the administrator role in all services.

User accounts

These do not have access to Management Portal. Their access to the services, and their roles in the services, are defined by an administrator.

Tenants

Each account belongs to a tenant. A tenant is a part of Management Portal resources (such as user accounts and child tenants) and service offerings (enabled services and offering items within them) dedicated to partner or a customer. The tenant hierarchy is supposed to match the client/vendor relationships between the service users and providers.

There are four tenant types:

Partner

Typically corresponds to service providers that resell the services.

Folder

Is a supplementary tenant, that is typically used by partner administrators to group partners and customers to configure separate offerings and/or different branding.

Customer

Typically corresponds to organizations that use the services.

Unit

Typically corresponds to units or departments within the organization.

An administrator can create and manage tenants, administrator accounts, and user accounts on or below their level in the hierarchy.

An administrator of parent tenant of type 'partner' can act as a lower-level administrator in tenants of type 'customer' or 'partner', whose management mode is Managed by service provider. Thus, the partner-level administrator can, for example, manage user accounts and services, or access backups and other resources in the child tenant. However, the administrators at the lower level can limit the access to their tenant for higher-level administrators.

The following diagram illustrates an example hierarchy of the partner, folder, customer, and unit tenants.

The following table summarizes operations that can be performed by administrators and users.

Operation	Users	Customer and unit administrators	Partner and folder administrators
Create tenants

No



Yes



Yes


Create accounts

No



Yes



Yes


Download and install the software

Yes



Yes



No*


Manage services

Yes



Yes



Yes


Create reports about the service usage

No



Yes



Yes


Configure branding

No



No



Yes

A user can be created from any type of tenant, and to have a shared email address as long as it is created from the most privileged to the least privileged. For example, a partner tenant can create a folder, customer, and unit tenant, while a customer tenant cannot create a folder tenant.
Unit administrators cannot create, modify, or apply Disaster Recovery protection plans.

Tenants

Users

Back to Top



Last build date: Tuesday, March 10, 2026

Partner Administrator Help for Management Portal26.02.