# Cross-subscription configuration issues in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Cross-subscription configuration issues in Microsoft Azure
Cross-subscription configuration issues in Microsoft Azure

If you are using two different subscriptions for Microsoft Azure - for example, one for direct backup to Microsoft Azure ("Subscription 1"), and another one for the configuration of the DR site in Microsoft Azure ("Subscription 2") - but you remove the access to "Subscription 1", the following issues will occur:

Failover will fail

You cannot start a failover, as the backup data is stored in "Subscription 1".

Failback will fail

If the access to "Subscription 1" is removed after a failover was performed, it will not be possible to access all backup data that is stored in the subscription. Therefore, it will not be possible to perform backup operations of VM in failover and failback. While backup data remains in "Subscription 1", failover or recovery operations rely on valid access and permissions to the original storage location. Removing access breaks this dependency, even if DR operations are started in a different subscription.

Do not remove or revoke access to the original Azure subscription if backups that are stored there are still used or needed.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.