# Configuring primary servers

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Cloud servers > Configuring primary servers
Configuring primary servers

A primary server is a virtual machine that does not have a linked machine on the local site if compared to a recovery server. Primary servers are used for protecting an application by replication, or running various auxiliary services (such as a web server).

Typically, a primary server is used for real-time data replication across servers running crucial applications. You set up the replication by yourself, using the application's native tools. For example, Active Directory replication, or SQL replication, can be configured among the local servers and the primary server.

Alternatively, a primary server can be included in an AlwaysOn Availability Group (AAG) or Database Availability Group (DAG).

Both methods require a deep knowledge of the application and the administrator rights. A primary server constantly consumes computing resources and space on the fast disaster recovery storage. It needs maintenance on your side: monitoring the replication, installing software updates, and backing up. The benefits are the minimal RPO and RTO with a minimal load on the production environment (as compared to backing up entire servers to the cloud).

Primary servers are always launched only in the production network and have the following network parameters:

Parameter	Description
Cloud network	(required) The cloud network to which a primary server will be connected.
IP address in production network	(required) The IP address that the primary server will have in the production network. By default, the first free IP address from your production network is set.
Public IP address	(optional) The IP address for accessing a primary server from the Internet. If a server has no public IP address, it can be reached only from the local network, not through the Internet.
Internet access	(optional) Enables a primary server to access the Internet.

Creating a primary server

Operations with primary servers

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.