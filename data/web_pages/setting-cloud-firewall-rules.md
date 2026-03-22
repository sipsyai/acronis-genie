# Setting firewall rules for cloud servers

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Cloud servers > Setting firewall rules for cloud servers
Setting firewall rules for cloud servers

You can edit the default firewall rules for the primary and recovery servers in the cloud.

To edit the firewall rules of a server on your cloud site

In the Cyber Protect console, go to Disaster Recovery> Servers.

If you want to edit the firewall rules of a recovery server, click the Recovery servers tab. Alternatively, if you want to edit the firewall rules of a primary server, click the Primary servers tab.

Click the server, and then click Edit.

Click the Cloud firewall rules tab.

If you want to change the default action for the inbound connections:

In the Inbound drop-down field, select the default action.

Action	Description
Deny all

Denies any inbound traffic.

You can add exceptions and allow traffic from specific IP addresses, protocols, and ports.


Allow all

Allows all inbound TCP and UDP traffic.

You can add exceptions and deny traffic from specific IP addresses, protocols, and ports.

Changing the default action invalidates and removes the configuration of existing inbound rules.

If you want to save the existing exceptions, in the confirmation window, select Save filled-in exceptions.

Click Confirm.

If you want to add an exception:

Click Add exception.

Specify the firewall parameters.

Firewall parameter	Description
Protocol

Select the protocol for the connection. The following options are supported:

TCP

UDP

TCP+UDP


Server port

Select the ports to which the rule applies. You can specify the following:

a specific port number (for example, 2298)

a range of port numbers (for example, 6000-6700)

any port number. Use * if you want the rule to apply to any port number.


Client IP address

Select the IP addresses to which the rule applies. You can specify the following:

a specific IP address (for example, 192.168.0.0)

a range of IP addresses using the CIDR notation (for example, 192.168.0.0/24)

any IP address. Use * if you want the rule to apply to any IP address.

If you want to remove an existing inbound exception, click the bin icon next to it.

If you want to change the default action for the outbound connections:

In the Outbound drop-down field, select the default action.

Action	Description
Deny all

Denies any outbound traffic.

You can add exceptions and allow traffic to specific IP addresses, protocols, and ports.


Allow all

Allows all outbound traffic.

You can add exceptions and deny traffic from specific IP addresses, protocols, and ports.

Changing the default action invalidates and removes the configuration of existing outbound rules.

If you want to save the existing exceptions, in the confirmation window, select Save filled-in exceptions.

Click Confirm.

If you want to add an exception:

Click Add exception.

Specify the firewall parameters.

Firewall parameter	Description
Protocol

Select the protocol for the connection. The following options are supported:

TCP

UDP

TCP+UDP


Server port

Select the ports to which the rule applies. You can specify the following:

a specific port number (for example, 2298)

a range of port numbers (for example, 6000-6700)

any port number. Use * if you want the rule to apply to any port number.


Client IP address

Select the IP addresses to which the rule applies. You can specify the following:

a specific IP address (for example, 192.168.0.0)

a range of IP addresses using the CIDR notation (for example, 192.168.0.0/24)

any IP address. Use * if you want the rule to apply to any IP address.

If you want to remove an existing outbound exception, click the bin icon next to it.

Click Save.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.