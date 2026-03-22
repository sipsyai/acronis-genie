# Azure resources that are created during the DR site configuration and failover

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Azure resources that are created during the DR site configuration and failover
Azure resources that are created during the DR site configuration and failover

When you add a connection to your Azure subscription, the system creates a resource group with the prefix cyber-protect-rg* in the Azure region that you selected during the configuration of the Azure connection. This resource group has the following tag: Application:CyberProtect. For more information, see Microsoft Azure connection security and audit (72684).

When the (DR) site configuration is completed, a resource group with the prefix dr-rg* is created to aggregate the resources for failover. This resource group has the following tag: Application:DisasterRecovery.

During disaster recovery operations, temporary workers (agents) are deployed to orchestrate failover, failback, and post-failover backup operations. These are temporary Azure VMs that are running in the cyber-protect-rg* resource group. All Azure resources that are required for a disaster recovery failover, such as storage accounts, and failed-over VMs are created in the dr-rg* resource group. You can manage the Azure region for the Azure connection resource group, the DR resource group, and their associated resources during the DR site configuration.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.