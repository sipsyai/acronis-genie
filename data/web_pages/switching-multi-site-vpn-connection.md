# Switching from Multi-site IPsec VPN to Site-to-site Open VPN

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Switching from Multi-site IPsec VPN to Site-to-site Open VPN
Switching from Multi-site IPsec VPN to Site-to-site Open VPN

You can easily switch form a Multi-site IPsec VPN connection to a Site-to-site Open VPN connection.

When you switch the connectivity type, the active VPN connections are deleted, but the cloud servers and network configurations are preserved. However, you will still need to reassign the IP addresses of the cloud networks and servers.

The following table compares the basic characteristics of the Site-to-site Open VPN connection and the Multi-site IPsec VPN connection.

Site-to-site Open VPN	Multi-site IPsec VPN
Local site support	Single	Single, Multiple
VPN Gateway mode	L2 Open VPN	L3 IPsec VPN
Network segments	Extends the local network to the cloud network	Local networks and cloud network segments should not overlap
Supports Point-to-Site access to local site	Yes	No
Supports Point-to-Site access to cloud site	Yes	Yes
Requires a public IP offering item	No	Yes

To switch from a Multi-site IPsec VPN connection to a Site-to-site Open VPN connection

In the Cyber Protect console, go to Disaster Recovery > Connectivity.

Click Show properties.

Click Switch to site-to-site Open VPN.

Click Reconfigure.

Reassign the IP addresses of the cloud network and cloud servers.

Configure the Site-to-site connection settings.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.