# Best practices for Disaster Recovery network configuration

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Connectivity and networks in Microsoft Azure > Best practices for Disaster Recovery network configuration
Best practices for Disaster Recovery network configuration

When you configure the recovery networks in Disaster Recovery to Microsoft Azure, we recommend that you follow the following best practices:

Separate production and test VNets and subnets

Keep test and production environments isolated.

Use Azure tags and naming conventions

Clearly label networks (for example, dr-prod and dr-test) for easy identification and automation.

Plan IP ranges carefully

Ensure that the VNets and subnets do not conflict with on-premises networks if there is a connectivity between the DR site and on-premises, for example via IPsec VPN or ExpressRoute.

Maintain consistent address schemes for easier routing and identity integration.

Preconfigure required network resources

NSGs, route tables, custom DNS, and public IPs should be configured in advance for both test and production recovery networks.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.