# Workers in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Workers in Microsoft Azure
Workers in Microsoft Azure

Workers are temporary, on-demand agents that run in your Azure subscription in the system resource group (with the prefix: "cyber-protect-rg*") during disaster recovery operations, such as failover, back up after failover, and failback. One worker is deployed for each operation and is deleted after operation completes. This on-demand model helps reduce costs by automatically deploying workers only during active DR operations and removing them afterward.

The initial deployment of the worker for a test or production failover might take several minutes. Starting workers for the subsequent failovers should be faster.

To monitor the status of active workers, go to Public clouds, click the connection to your Microsoft Azure subscription, and then click the Workers tab.

If a disaster recovery operation fails because of an error with the worker, you can generate a report and view more information about the error. To do this, go to the Workers tab, turn on the Troubleshooting switch, click the Instructions link, and then follow the instructions.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.