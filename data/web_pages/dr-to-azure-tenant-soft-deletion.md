# Soft deletion of tenants that have a disaster recovery site in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Soft deletion of tenants that have a disaster recovery site in Microsoft Azure
Soft deletion of tenants that have a disaster recovery site in Microsoft Azure

The soft deletion of a tenant feature (Recycle bin) is supported for the Microsoft Azure DR site configuration.

To ensure business continuity during the soft and hard deletion, Azure VMs in failover will not be stopped or deleted.

Corner case

If you disable the DR and direct backup to Azure offering item (either intentionally or accidentally), a soft delete of the Azure DR configuration is triggered. This means that the configuration is removed but remains in the Recycle bin for 30 days. If during this period you configure a new DR site in a different location (not Microsoft Azure), to recover the initial DR configuration to Microsoft Azure, you must enable the DR and direct backup to Azure offering item, remove the new configuration, and then recover the initial one.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.