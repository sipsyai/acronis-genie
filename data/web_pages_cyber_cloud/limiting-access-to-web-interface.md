# Limiting access to the web interface

Limiting access to the web interface
Limiting access to the web interface

Administrators can limit access to the web interface by specifying a list of IP addresses from which members of a tenant are allowed to log in.

Enabling login control prevents recovery from cloud storage by using unregistered bootable media. See this KB article.
This restriction also applies to accessing Management Portal via API.
This restriction applies only at the level where it is set. It is not applied to members of the child tenants.

To limit access to the web interface

Log in to Management Portal.

Navigate to the tenant in which you want to limit the access.

Click Settings > Security.
Enable the Login control switch.

In Allowed IP addresses, specify the allowed IP addresses.

You can enter any of the following parameters, separated by a semicolon:

IP addresses, for example: 192.0.2.0
IP ranges, for example: 192.0.2.0-192.0.2.255
Subnets, for example: 192.0.2.0/24
Click Save.
When the MDR service is enabled for a tenant, the IP range of the MDR vendor is added automatically to the list of allowed IP addresses to enable the operation of the service.

For service providers who use Cyber Infrastructure (hybrid model):

If the Login control switch is enabled under Settings > Security in Management Portal, add the external public IP address (or addresses) of the Cyber Infrastructure nodes to the Allowed IP addresses list.

Back to Top



Last build date: Tuesday, March 10, 2026

Partner Administrator Help for Management Portal26.02.