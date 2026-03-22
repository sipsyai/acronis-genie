# General recommendations for local sites

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > General recommendations for local sites
General recommendations for local sites
The availability of this feature depends on the service quotas that are enabled for your account.

When you configure the local sites for your Multi-site IPsec VPN connectivity, consider the following recommendations:

For each IKE Phase, set at least one of the values that are configured in the cloud site for the following parameters: Encryption algorithm, Hash algorithm, and Diffie-Hellman group numbers.

Enable Perfect forward secrecy with at least one of the values for Diffie-Hellman group numbers that is configured in the cloud site for IKE Phase 2.

Configure the same Lifetime value for IKE Phase 1 and IKE Phase 2 as in the cloud site.

Configurations with NAT traversal (NAT-T) are not supported. Disable the NAT-T configuration on the local site. Otherwise, the additional UDP encapsulation cannot be negotiated.

The Startup action configuration defines which side initiates the connection. The default value Add means that the local site initiates the connection, and cloud site is waiting for the connection initiation. Change the value to Start if you want the cloud site to initiate the connection, or to Route if you want both sides to be able to initiate the connection (suitable for firewalls that support the route option).

For more information and configuration examples for different solutions, see:

This series of knowledge base articles
This video example
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.