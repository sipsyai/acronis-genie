# Configuring custom DNS servers

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Configuring custom DNS servers
Configuring custom DNS servers
The availability of this feature depends on the service quotas that are enabled for your account.

When you configure a connectivity, Disaster Recovery creates your cloud network infrastructure. The cloud DHCP server automatically assigns default DNS servers to the recovery servers and primary servers, but you can change the default settings and configure custom DNS servers. The new DNS settings will be applied at the time of the next request to the DHCP server.

Prerequisites

One of the connectivity types to the cloud site must be set.

To configure a custom DNS server

In the Cyber Protect console, go to Disaster Recovery > Connectivity.

Click Show properties.

Click Default (Provided by Cloud Site).

Select Custom servers.

Type the IP address of the DNS server.

[Optional] If you want to add another DNS server, click Add, and type the DNS server IP address.

After you add the custom DNS servers, you can also add the default DNS servers. In that way, if the custom DNS servers are unavailable, Disaster Recovery will use the default DNS servers.

Click Done.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.