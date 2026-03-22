# Managing the disaster recovery site in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Managing the disaster recovery site in Microsoft Azure
Managing the disaster recovery site in Microsoft Azure

You can create and configure your disaster recovery (DR) site in Microsoft Azure either as part of the disaster recovery protection plan creation or as a separate procedure, from the Disaster Recovery screen.

When a disaster recovery protection plan is applied, the recovery server cloud network infrastructure is created only if it does not already exist. Existing cloud servers and networks are not changed or recreated.

A disaster recovery protection plan cannot be enabled if the IP address of a device cannot be detected. For example, when virtual machines are backed up agentless and are not assigned an IP address. In this case, we recommend that you create a recovery server manually.

When you apply a protection plan, recovery servers are configured in the subnet that is configured in the mapping rules during the configuration of the DR site location, and are based on the IP address of the original device. If the IP address matches any of the specified source local networks, the recovery server will be created in the corresponding Azure recovery network and subnet. The last octet of the private IP will be taken from the original machine's IP address.

Creating a disaster recovery site in Microsoft Azure

Removing the DR site from Microsoft Azure




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.