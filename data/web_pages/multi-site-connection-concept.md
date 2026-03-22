# Multi-site IPsec VPN connection

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Multi-site IPsec VPN connection
Multi-site IPsec VPN connection
The availability of this feature depends on the service quotas that are enabled for your account.

You can use the Multi-site IPsec VPN connectivity to connect a single local site, or multiple local sites to the Disaster Recovery through a secure L3 IPsec VPN connection.

This connectivity type is useful for disaster recovery scenarios if you have one of the following use cases:

you have one local site hosting critical workloads.
you have multiple local sites hosting critical workloads. For example, offices in different locations.
you use third-party software sites or managed service providers sites, and are connected to them through an IPsec VPN tunnel.

To establish a Multi-site IPsec VPN communication between the local sites and the cloud site, a VPN gateway is used. When you start configuring the Multi-site IPsec VPN connection in the Cyber Protect console, the VPN gateway is automatically deployed in the cloud site. You should configure the cloud network segments and make sure that they do not overlap with the local network segments. A secure VPN tunnel is established between local sites and the cloud site. The local and cloud servers can communicate through this VPN tunnel as if they are all in the same Ethernet segment.

When using a Multi-site IPsec VPN connection, the VPN gateway is automatically assigned a public IP address.

For each source machine to be protected, you must create a recovery server on the cloud site. It stays in the Standby state until a failover event happens. If a disaster happens and you start a failover process (in the production mode), the recovery server representing the exact copy of your protected machine is launched in the cloud. Your clients can continue working with the server, without noticing any background changes.

You can also launch a failover process in the test mode. This means that the source machine is still working and at the same time the respective recovery server is launched in the cloud in a special virtual network that is created in the cloud – test network. The test network is isolated to prevent duplication of IP addresses in the other cloud network segments.

VPN gateway

The major component that allows communication between the local sites and the cloud site is the VPN gateway. It is a virtual machine in the cloud on which the special software is installed, and the network is specifically configured. The VPN gateway serves the following functions:

Connects the Ethernet segments of your local network and production network in the cloud in the L3 IPsec mode.
Works as a default router and NAT for the machines in the test and production networks.

Works as a DHCP server. All machines in the production and test networks get the network configuration (IP addresses, DNS settings) via DHCP. Every time a cloud server will get the same IP address from the DHCP server.

If you prefer, you can set up a custom DNS configuration. For more information, see Configuring custom DNS servers.

Works as a caching DNS.
How routing works

Routing between the cloud networks is performed with the router on the cloud site so that servers from different cloud networks can communicate with each other.

Configuring Multi-site IPsec VPN

Switching from Multi-site IPsec VPN to Site-to-site Open VPN

Troubleshooting the IPsec VPN configuration

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.