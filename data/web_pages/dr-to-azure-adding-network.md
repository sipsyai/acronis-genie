# Adding a production recovery network from Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Connectivity and networks in Microsoft Azure > Adding a production recovery network from Microsoft Azure
Adding a production recovery network from Microsoft Azure

After the DR site is configured, you can add additional production recovery networks from the ones that exist in Microsoft Azure.

To add a production recovery network from Microsoft Azure

In the Cyber Protect console, go to Disaster Recovery > Connectivity.

In the Production networks pane, click Add network.

In the Add production network window, in the Virtual network field, select a virtual network.

In the Subnet field, select the subnet.

To make this subnet default, select Set this subnet as 'Default' for mapping.

When applying the disaster recovery protection plan to the original devices, recovery servers are configured in the default subnet.

In the Mapping to local network field, click Add.

You can define mapping rules by entering one or more source local networks in the CIDR format. The service will then compare the IP address of the original device with the mapping rules. If the IP address matches any of the specified source local networks, the recovery server will be created in the corresponding Azure recovery network and subnet.

Enter one or more source local networks in the CIDR format.

To add the network, click Done.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.