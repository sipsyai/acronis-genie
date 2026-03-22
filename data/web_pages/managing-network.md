# Managing networks for Site-to-site Open VPN

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Managing networks for Site-to-site Open VPN
Managing networks for Site-to-site Open VPN
Some features might require additional licensing, depending on the applied licensing model.

You can add and manage up to 23 networks in the cloud.

Adding networks
Delete network
Change parameters

Prerequisites

Site-to-site Open VPN connectivity is configured, as described in Configuring Site-to-site Open VPN.

To add networks on the local site and extend them to the cloud

On the VPN appliance, set up the new network interface with the local network that you want to extend in the cloud.

If you want to add one or more networks, for each additional network, add one virtual network interface (network adapter) to the virtual machine on which the virtual appliance is running.

The following example demonstrates the step for a virtual machine that is running on a Hyper-V hypervisor.

The new virtual network adapters must be configured with the local virtual network that you want to extend to the cloud.

Log in to the console of the VPN appliance, and then in the Networking section, configure the network settings for one of the interfaces (adapters).

The IP address configuration is mandatory for only one of the virtual network interfaces, to enable Internet access. You can skip the IP configuration for the other network interfaces.

Promiscuous mode and Forged transmits or MAC address spoofing must be enabled for each adapter. For more information, see this knowledge base article.

The VPN appliance starts automatically to report information about the networks from all active interfaces to Disaster Recovery.

Log in to the Cyber Protect console, and then go to Disaster recovery > Connectivity.

All local networks are automatically extended to the cloud site.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.