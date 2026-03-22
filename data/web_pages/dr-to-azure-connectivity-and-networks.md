# Connectivity and networks in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Connectivity and networks in Microsoft Azure
Connectivity and networks in Microsoft Azure

Disaster Recovery to Microsoft Azure enables the orchestration of testing, failover, and failback, and the selection of recovery networks (Azure VNets and subnets) for both production and test failover scenarios. You can configure these networks during the initial DR site configuration or later: from the Connectivity screen, or individually for each recovery server.

You retain full control over Azure networking and connectivity, and have the flexibility to leverage native Azure platform capabilities or bring custom solutions, such as third-party firewalls or SD-WAN appliances into the DR site, by connecting them to the selected recovery networks.

Below is an overview of key Azure networking services, their relevance for disaster recovery use cases, and links for more information.

Azure Firewall

Azure Firewall provides centralized, stateful network traffic filtering across multiple VNets and subnets. It helps enforce security rules between workloads after a failover and supports scenarios where DR environments must meet corporate compliance or segmentation policies.

You can use Azure Firewall to control outbound and inbound traffic to and from failovered VMs (for example, to limit Internet access and allow only allowlisted sources). For managed exposure, position Azure Firewall between the on-premises network (via VPN) and the Azure DR VNets.

For more information, see the Microsoft Azure documentation.

Network security groups (NSGs)

NSGs allow defining granular rules to allow or deny network traffic to VMs or subnets. NSGs operate at the VM NIC and subnet level.

You can apply NSGs to control access to recovery VMs, ensure isolation of test failovers, or expose only necessary ports (for example, RDP and HTTP). NSGs are essential for securely enabling connectivity based on whether the recovery VM is in a test or production mode.

For more information, see the Microsoft Azure documentation.

DNS servers

Azure VNets support custom DNS server configurations or integration with Azure DNS. This controls how name resolution works in the DR environment.

Ensure that DR VMs resolve names correctly, either to other recovered services in Azure or to external systems. Custom DNS is essential when restoring AD-integrated environments or for DNS forwarding to on-prem systems.

For more information, see the Microsoft Azure documentation.

Subnet routing (User-defined routes)

Azure allows the creation of custom routes (UDRs) to control traffic flow between subnets and to on-premises networks, overriding default system routing.

Create routes to direct traffic from recovery VMs through firewalls, to VPN gateways, or inspection points. This helps to enforce routing policies and ensure connectivity back to on-premises via VPN or ExpressRoute.

For more information, see the Microsoft Azure documentation.

Public IP addresses

Azure VMs can be assigned public IP addresses (static or dynamic) to allow direct Internet access when needed. This is useful for exposing services or remote access.

Assign public IPs to failover workloads that require external access (for example, web servers and remote management). Avoid for sensitive workloads. Use Bastion or VPN instead where possible.

For more information, see the Microsoft Azure documentation.

Azure Bastion

Azure Bastion enables secure, browser-based RDP/SSH access to VMs without exposing public IPs. Operates via the Azure portal and uses TLS encryption.

Access recovered VMs securely for diagnostics or manual reconfiguration after failover. This is especially useful in test failover where exposing to the internet is not desired.

For more information, see the Microsoft Azure documentation.

Azure Site-to-Site VPN

Site-to-Site VPN provides an encrypted IPsec connection between your on-premises network and Azure VNets, enabling hybrid connectivity.

Ensure seamless access to recovered workloads from on-premises networks. Critical for accessing internal apps or restoring cross-dependencies with systems still running on-premises.

For more information, see the Microsoft Azure documentation.

Azure ExpressRoute

ExpressRoute offers dedicated private connectivity between your data center and Azure, bypassing the Internet for improved speed, reliability, and security.

Recommended for enterprise-grade DR with large datasets or low-latency requirements. Use to connect on-premises systems with DR VMs in Azure without relying on VPN.

For more information, see Microsoft Azure documentation.

Network management in Microsoft Azure

Best practices for Disaster Recovery network configuration

Recommendations for the Active Directory Domain Services availability

Configuring the test recovery network

Adding a production recovery network from Microsoft Azure

Adding a test recovery network from Microsoft Azure

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.