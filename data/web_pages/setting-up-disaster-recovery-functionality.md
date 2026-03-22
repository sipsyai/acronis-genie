# Setting Up Disaster Recovery Functionality

Setting up the disaster recovery infrastructure / environment
Some features might require additional licensing, depending on the applied licensing model.

To set up the disaster recovery environment

Configure the connectivity type to the cloud site:

Point-to-site connection
Site-to-site OpenVPN connection
Multi-site IPsec VPN connection
Cloud-only mode
Create a protection plan with the backup module enabled and select the entire machine or system plus boot volumes for backing up. At least one protection plan is required for creating a recovery server.
Apply the protection plan to the workloads (physical servers or virtual machines) that you want to protect.

Change the default configuration of the recovery servers that were created for each workload on which you applied the protection plan.

Perform a test failover to check how it works.
[Optional] Create the primary servers for application replication.

As a result, you have set up the disaster recovery functionality to protect your local servers from a disaster.

If a disaster occurs, you can fail over the workload to the recovery servers in the cloud. At least one recovery point must be created before failing over to recovery servers. When your local site is recovered from a disaster, you can switch the workload back to your local site by performing failback. For more information about the failback process, see Performing agentless failback via a hypervisor agent and Performing agent-based failback via bootable media.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.