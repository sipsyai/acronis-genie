# IP address reconfiguration

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > IP address reconfiguration
IP address reconfiguration

For proper disaster recovery performance, the IP addresses assigned to the local and cloud servers must be consistent. If there is any inconsistency or mismatch in IP addresses, you will see the exclamation mark next to the corresponding network in Disaster Recovery > Connectivity.

Some of the commonly known reasons for IP address inconsistency are listed below:

A recovery server was migrated from one network to another, or the network mask of the cloud network was changed. As a result, cloud servers have the IP addresses from networks to which they are not connected.
The connectivity type was switched from one without Site-to-site connection to a Site-to-site connection. As a result, a local server is placed in the network different from the one that was created for the recovery server on the cloud site.
The connectivity type was switched from Site-to-site Open VPN to Multi-site IPsec VPN, or from Multi-site IPsec VPN to Site-to-site Open VPN. For more information about this scenarios, see Switching connections, Switching from Multi-site IPsec VPN to Site-to-site Open VPN, and Reassigning IP addresses.

Editing the following network parameters on the VPN appliance site:

Adding an interface via the network settings
Editing the network mask manually via the interface settings
Editing the network mask via DHCP
Editing the network address and mask manually via the interface settings
Editing the network mask and address via DHCP

As a result of the actions listed above, the network on the cloud site may become a subset or superset of the local network, or the VPN appliance interface may report the same network settings for different interfaces.

To resolve the issue with network settings

Click the network that requires IP address reconfiguration.

You will see a list of servers in the selected network, their status, and IP addresses. The servers whose network settings are inconsistent are marked with an exclamation mark.

To change network settings for a server, click Go to server. To change network settings for all servers at once, click Change in the notification block.
Change the IP addresses as needed by defining them in the New IP and New test IP fields.
When ready, click Confirm.

Move servers to a suitable network

When you create a disaster recovery protection plan and apply it on selected devices, the system checks device IP addresses and automatically creates cloud networks if there are not existing cloud networks where IP address fits. By default, the cloud networks are configured with maximum ranges recommended by IANA for private use (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). You can narrow your network by editing the network mask.

In the case that the selected devices were on multiple local networks, the network on the cloud site might become a superset of the local networks. In this case, to reconfigure cloud networks:

Click the cloud network that requires network size reconfiguration and then click Edit.
Reconfigure the network size with the correct settings.
Create other required networks.
Click the notification icon next to the number of devices connected to the network.
Click Move to a suitable network.
Select the servers that you want to move to suitable networks and then click Move.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.