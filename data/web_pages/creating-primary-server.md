# Creating a primary server

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Cloud servers > Creating a primary server
Creating a primary server

Prerequisites

One of the connectivity types to the cloud site must be set.

To create a primary server

Go to Disaster Recovery > Servers > Primary servers tab.
Click Create.

In the Create primary server wizard, on the Server configuration tab, do the following:

Select a template for the new virtual machine.

Select the flavor of the configuration (number of virtual cores and the size of RAM).

The following table shows the maximum total amount of disk space (GB) for each flavor.

Type	vCPU	RAM (GB)	Maximum total amount of disk space (GB)
F1	1	2	500
F2	1	4	1,000
F3	2	8	2,000
F4	4	16	4,000
F5	8	32	8,000
F6	16	64	16,000
F7	16	128	32,000
F8	16	256	64,000
[Optional] Change the virtual disk size. If you need more than one hard disk, click Add disk, and then specify the new disk size. You can add up to 10 disks for a primary server.
Change the default name of the recovery server.
Add a description.

On the Network tab, do the following:

Specify the cloud network in which the primary server will be included.

Select the DHCP option.

DHCP option	Description
Provided by cloud site	This is the default setting. The IP address of the server will be provided by an automatically configured DHCP server in the cloud.
Custom	The IP address of the server will be provided by your own DHCP server in the cloud.

Specify the MAC address.

The MAC address is a unique identifier that is assigned to the network adapter of the server. If you use custom DHCP, you can configure it to always assign a specific IP adresses to a specific MAC address. This ensures that the primary server always gets the same IP address. You can run applications that have licenses that are registered with the MAC address.

Specify the IP address that the server will have in the production network.

By default, the first free IP address from your production network is set.

If you use a DHCP server, add this IP address to the server exclusion list in order to avoid IP address conflicts.

If you use a custom DHCP server, you must specify the same IP address in IP address in production network as the one configured in the DHCP server. Otherwise, test failover will not work properly, and the server will not be reachable via a public IP address.

[Optional] Select the Internet access check box.

If you select this option, the primary server will have access to the Internet. By default, TCP port 25 is open for outbound connections to public IP addresses.

[Optional] Select the Use public IP address check box.

With a public IP address, the primary server becomes accessible from the Internet. If you do not select this setting, the server will be available only in your production network.

The public IP address will be shown after you complete the configuration. By default, TCP port 443 is open for inbound connections to public IP addresses.

If you clear the Use Public IP address check box or delete the recovery server, its public IP address will not be reserved.

[Optional] On the Settings tab, select Set RPO threshold, and then set the value.

RPO threshold defines the maximum time interval between the last recovery point and the current time. The value can be set within 15 – 60 minutes, 1 – 24 hours, 1 – 14 days.

[Optional] On the Cloud firewall rules tab, edit the default firewall rules. For more information, see Setting firewall rules for cloud servers.
Click Create.

The primary server becomes available in the production network. You can manage the server by using its console, RDP, SSH, or TeamViewer.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.