# Licensing for Disaster Recovery to Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Licensing for Disaster Recovery to Microsoft Azure
Licensing for Disaster Recovery to Microsoft Azure

To enable Disaster Recovery to Microsoft Azure, the DR and direct backup to Azure offering item must be enabled for your tenant. This offering item enables:

Disaster Recovery (DR) to Azure that uses the customer’s own Azure subscription.

Direct backup to Azure.

One quota from the offering item is consumed when a recovery server is created or direct backup to Azure is enabled. Only one quota per workload is used, even if both DR and direct backup are active.

The quota for this offering item that is assigned to your tenant represents the maximum number of workloads that can be protected. A device that uses both Disaster Recovery to Azure and direct backup to Azure protection consumes one quota.

Hard quota overage

When the hard quota for the offering item is decreased, existing recovery servers might become unlicensed. The number of unlicensed recovery servers depends on the overage. Recovery servers that were in test or production failover remain functional but become unlicensed. Unlicensed recovery servers in the Standby state have limited DR operations. You cannot power on unlicensed servers until they are licensed again.

Increasing the offering item quota automatically assigns licenses to unlicensed devices and clears related alerts.

Generated alerts

The following alerts are generated when there are issues that are caused by missing licenses.

Recovery server is unlicensed - This alert is generated when a server becomes unlicensed.

Disaster Recovery protection was disabled for a workload - This alert is generated when there are no available licenses.

Automated test failover failed - This alert is generated when a failover is blocked due to a missing license.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.