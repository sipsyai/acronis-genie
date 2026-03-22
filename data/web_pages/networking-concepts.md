# Networking Concepts

Networking concepts
Some features might require additional licensing, depending on the applied licensing model.

With Disaster Recovery to Cyber Protect Cloud, you can define the following connectivity types to the cloud site:

Cloud-only mode

This type of connection does not require a VPN appliance deployment on the local site.

The local and cloud networks are independent networks. This type of connection implies either the failover of all the local site's protected servers or partial failover of independent servers that do not need to communicate with the local site.

Cloud servers on the cloud site are accessible through the point-to-site VPN, and public IP addresses (if assigned).

Site-to-site Open VPN connection

This type of connection requires a VPN appliance deployment on the local site.

The Site-to-site Open VPN connection allows to extend your networks to the cloud and retain the IP addresses.

Your local site is connected to the cloud site by means of a secure VPN tunnel. This type of connection is suitable in case you have tightly dependent servers on the local site, such as a web server and a database server. In case of partial failover, when one of these servers is recreated on the cloud site while the other stays on the local site, they will still be able to communicate with each other via a VPN tunnel.

Cloud servers on the cloud site are accessible through the local network, point-to-site VPN, and public IP addresses (if assigned).

Multi-site IPsec VPN connection

This type of connection requires a local VPN device that supports IPsec IKE v2.

When you start configuring the Multi-site IPsec VPN connection, Disaster Recovery automatically creates a cloud VPN gateway with a public IP address.

With Multi-site IPsec VPN your local sites are connected to the cloud site by means of a secure IPsec VPN tunnel.

This type of connection is suitable for Disaster Recovery scenarios when you have one or several local sites hosting critical workloads or tightly dependent services.

In case of partial failover of one of the servers, the server is recreated on the cloud site while the others remain on the local site, and they are still able to communicate with each other through an IPsec VPN tunnel.

In case of partial failover of one of the local sites, the rest of the local sites remain operational, and will still be able to communicate with each other through an IPsec VPN tunnel.


Point-to-site remote VPN access

A secure Point-to-site remote VPN access to your cloud and local site workloads from outside by using your endpoint device.

For a local site access, this type of connection requires a VPN appliance deployment on the local site.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.