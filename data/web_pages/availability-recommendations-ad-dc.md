# Availability Recommendations Ad Dc

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Recommendations for the Active Directory Domain Services availability
Recommendations for the Active Directory Domain Services availability

If your protected workloads need to authenticate in a domain controller, we recommend that you have an Active Directory Domain Controller (AD DC) instance at the Disaster Recovery site.

Active Directory Domain Controller for L2 Open VPN connectivity

With the L2 Open VPN connectivity, the IP addresses of the protected workloads are retained in the cloud site during a test failover or a production failover. Therefore, the AD DC during a test failover or a production failover has the same IP address as in the local site.

With custom DNS you can set your own custom DNS server for all cloud servers. For more information, see Configuring custom DNS servers.

Active Directory Domain Controller for L3 IPsec VPN connectivity

With L3 IPsec VPN connectivity, the IP addresses of the protected workloads are not retained in the cloud site. Therefore, we recommend that you have an additional dedicated AD DC instance as a primary server in the cloud site before you perform a production failover.

The recommendations for a dedicated AD DC instance that is configured as a primary server in the cloud site are the following:

Turn off Windows firewall.
Join the primary server to the Active Directory service.
Ensure that the primary server has Internet access.
Add the Active Directory feature.

With custom DNS you can set your own custom DNS server for all cloud servers. For more information, see Configuring custom DNS servers.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.