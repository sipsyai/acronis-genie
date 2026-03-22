# Working with Disaster Recovery to Cyber Protect Cloud

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Working with Disaster Recovery to Cyber Protect Cloud
Working with Disaster Recovery to Cyber Protect Cloud
Some features might require additional licensing, depending on the applied licensing model.

The basic workflow for using disaster recovery is the following:

Create a recovery server of the workload that you want to protect in one of the following ways:

Create a protection plan that includes the Disaster recovery module and the Backup module with the What to backup setting set to Entire machine or System and boot volumes.

Apply the plan to your devices. This will automatically set up the default disaster recovery infrastructure. For more information, see Create a disaster recovery protection plan.

Unit administrators cannot create, modify, or apply disaster recovery protection plans.
Set up the disaster recovery cloud infrastructure manually and control each step. See Creating a recovery server.

Configure the connectivity to the cloud site.

Cloud-only mode
Site-to-site OpenVPN connection
Multi-site IPsec VPN connection
Point-to-site connection

Configure automated test failover.

Perform a test failover.

[When a disaster occurs] Perform a production failover.

[After the disaster] Perform a failback to the local site.

Configure runbooks.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.