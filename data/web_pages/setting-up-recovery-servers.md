# Configuring recovery servers

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Cloud servers > Configuring recovery servers
Configuring recovery servers

A recovery server – a replica of the original machine based on the protected server backups stored in the cloud. Recovery servers are used for switching workloads from the original servers in case of a disaster.

When creating a recovery server, you must specify the following network parameters:

Parameter	Description
Cloud network	(required) The cloud network to which a recovery server will be connected.
IP address in production network	(required) The IP address with which a virtual machine for a recovery server will be launched. This address is used in both the production and test networks. Before launching, the virtual machine is configured for getting the IP address via DHCP.
Test IP address	(optional) The IP address to access a recovery server from the client-production network during a test failover, to prevent the production IP address from being duplicated in the same network. This IP address is different from the IP address in the production network. Servers in the local site can reach the recovery server during the test failover via the test IP address, while access in the reverse direction is not available. Internet access from the recovery server in the test network will be available if the Internet access option is selected during the recovery server creation.
Public IP address	(optional) The IP address to access a recovery server from the Internet. If a server has no public IP address, it can be reached only from the local network.
Internet access	(optional) Enables the recovery server to access the Internet (in both the production and test failover cases).

Creating a recovery server

Operations with recovery servers

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.