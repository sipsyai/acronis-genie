# Configuring the Multi-site IPsec VPN settings

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Configuring the Multi-site IPsec VPN settings
Configuring the Multi-site IPsec VPN settings
The availability of this feature depends on the service quotas that are enabled for your account.

After you configure a Multi-site IPsec VPN, you must configure the cloud site and the local sites settings on the Disaster Recovery > Connectivity tab.

Prerequisites

Multi-site IPsec VPN connectivity is configured. For more information about configuring the Multi-site IPsec VPN connectivity, see Configuring Multi-site IPsec VPN.

Each local IPsec VPN gateway has a public IP address.

Your cloud network has enough IP addresses for the cloud servers that are copies of your protected machines (in the production network), and for the recovery servers (with one or two IP addresses, depending on your needs).

[If you use a firewall between the local sites and the cloud site] The following IP protocols and UDP ports are allowed on the local sites: IP Protocol ID 50 (ESP), UDP Port 500 (IKE), and UDP Port 4500.

The NAT-T configuration on the local sites is disabled.

To configure a Multi-site IPsec VPN connection

Add one or more networks to the cloud site.

Click Add Network.

When you add a cloud network, a corresponding test network is added automatically with the same network address and mask for performing test failovers. The cloud servers in the test network have the same IP addresses as the ones in the cloud production network. If you need to access a cloud server from the production network during a test failover, when you create a recovery server, assign it a second test IP address.

In the Network address field, type the IP address of the network.

Ensure that the cloud networks do not overlap with any local network in your environment. Otherwise, a tunnel cannot be established.

In the Network mask field, type the mask of the network.

Click Add.

Configure the settings for each local site that you want to connect to the cloud site, following the recommendations for the local sites. For more information about these recommendations, see General recommendations for local sites.

Click Add Connection.

Enter a name for the of the local VPN gateway.

Enter the public IP address of the local VPN gateway.

Enter a description of the local VPN gateway.

Click Next.

In the Pre-shared key field, type the pre-shared key, or click Generate a new pre-shared key to use an automatically generated value.

You must use the same pre-shared key for the local and the cloud VPN gateways.

Click IPsec/IKE security settings to configure the settings. For more information about the settings that you can configure, see IPsec/IKE security settings.

You can use the default settings, which are populated automatically, or use custom values. Only IKEv2 protocol connections are supported. The default Startup action when establishing the VPN is Add (your local VPN gateway initiates the connection), but you can change it to Start (the cloud VPN gateway initiates the connection) or Route (suitable for firewalls that support the route options).

Configure the Network policies.

The network policies specify the networks to which the IPsec VPN connects. Type the IP address and mask of the network using the CIDR format. The local and cloud network segments should not overlap.

Click Save.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.