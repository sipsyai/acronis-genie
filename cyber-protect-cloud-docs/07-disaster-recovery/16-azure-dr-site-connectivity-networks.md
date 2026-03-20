---
title: "Azure DR site management, connectivity, and networks"
section: "Implementing disaster recovery"
subsection: "Disaster Recovery to Microsoft Azure"
page_range: "1021-1029"
tags: [Azure DR site, protection plan, connectivity, Azure VNet, Azure Firewall, NSG, Azure Bastion, ExpressRoute, VPN, network management, recovery network, test network]
acronis_version: "26.02"
---

# Creating a disaster recovery protection plan with Microsoft Azure

The disaster recovery protection plan is a protection plan in which the **Disaster recovery** module is enabled. For Microsoft Azure, the DR site location must be configured. It is not possible to apply a protection plan with an Azure DR location if it was not configured.

> **Note**
> - Applying a disaster recovery protection plan creates cloud recovery servers. Existing cloud networks are not changed or recreated.
> - After you configure disaster recovery, you will be able to perform a test or production failover from any of the recovery points (backups) that were generated after the recovery server for the device was created.
> - A disaster recovery protection plan cannot be enabled if the IP address of a device cannot be detected (e.g., when virtual machines are backed up agentless and are not assigned an IP address). In this case, create a recovery server manually.
> - When you apply a protection plan, recovery servers are configured in the subnet that was configured in the mapping rules during the configuration of the DR site location, based on the IP address of the original device.

### To create a disaster recovery protection plan

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Select the machines that you want to protect.
3. Click **Protect**, and then click **Create plan**.
4. Configure the backup options. The plan must back up the entire machine, or only the disks required for booting up and providing the necessary services, to the Cloud storage or Microsoft Azure storage.
5. Enable the **Disaster recovery** module by turning on the switch next to the module name.
6. In the **Location** field, select **Microsoft Azure**.
7. Click **Create**.

The plan is created and applied to the selected machines. The recovery servers with default parameters are created.

---

# Managing the disaster recovery site in Microsoft Azure

You can create and configure your disaster recovery (DR) site in Microsoft Azure either as part of the disaster recovery protection plan creation or as a separate procedure, from the **Disaster Recovery** screen.

## Creating a disaster recovery site in Microsoft Azure

### Prerequisites

- You have a subscription to Microsoft Azure.
- Your Microsoft account has one of the following Entra ID roles: Cloud Application Administrator, Application Administrator, or Global Administrator.
- Your Microsoft account has the Owner role for the Azure subscription.
- The DR and direct backup to Azure offering item is enabled for your tenant.

### From All Devices

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Select the workloads that you want to protect.
3. In the **Actions** menu, click **Protect**.
4. Create a protection plan and configure the following settings:
   a. In the **Backup** module, in the **Where to back up** field, select the storage location.
   b. Enable the **Disaster recovery** module, and then click the **Location** field.
   c. In the **Disaster recovery site configuration** wizard, on the **Site location** tab, select **Microsoft Azure Cloud**, and then click **Next**.
   d. On the **Azure subscription** tab, select or add your Microsoft Azure subscription, and then click **Next**.
   e. On the **Target region** tab, in the **Azure region** field, select the Azure region for the DR site.
   f. On the **Recovery network** tab, configure the recovery networks for production and test failover, and then click **Next**.

   | Option | Description |
   |--------|-------------|
   | **Default configuration** | Use this option if you want the production and test networks in Azure to be created automatically, with one network for each environment. |
   | **Advanced configuration** | Use this option if you want to select your existing Azure networks as the production and test networks and configure network mapping. |

   g. On the **Summary** tab, review the parameters of your DR site, and then click **Configure**.

### From Connectivity

1. In the Cyber Protect console, go to **Disaster Recovery**.
2. Click **Configure**.
3. In the **Disaster recovery site configuration** wizard, on the **Site location** tab, select **Microsoft Azure Cloud**, and then click **Next**.
4. On the **Azure subscription** tab, select or add your subscription, and then click **Next**.
5. On the **Target region** tab, select the Azure region for the DR site.
6. On the **Recovery network** tab, configure the recovery networks and then click **Next**.
7. On the **Summary** tab, review the parameters and then click **Configure**.

The DR site is created in Azure, located in the selected Azure region. On the **Disaster Recovery** > **Connectivity** screen, you can view the production and test networks.

## Removing the DR site from Microsoft Azure

### Prerequisites

There are no recovery servers on the DR site.

### To remove the DR site from Microsoft Azure

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Remove disaster recovery site**.
3. In the **Remove disaster recovery site** window, enter your login, and then click **Remove**.

---

# Connectivity and networks in Microsoft Azure

Disaster Recovery to Microsoft Azure enables the orchestration of testing, failover, and failback, and the selection of recovery networks (Azure VNets and subnets) for both production and test failover scenarios. You can configure these networks during the initial DR site configuration or later: from the **Connectivity** screen, or individually for each recovery server.

You retain full control over Azure networking and connectivity, and have the flexibility to leverage native Azure platform capabilities or bring custom solutions, such as third-party firewalls or SD-WAN appliances into the DR site, by connecting them to the selected recovery networks.

## Key Azure networking services

### Azure Firewall

Azure Firewall provides centralized, stateful network traffic filtering across multiple VNets and subnets. It helps enforce security rules between workloads after a failover and supports scenarios where DR environments must meet corporate compliance or segmentation policies. Position Azure Firewall between the on-premises network (via VPN) and the Azure DR VNets.

### Network security groups (NSGs)

NSGs allow defining granular rules to allow or deny network traffic to VMs or subnets. NSGs operate at the VM NIC and subnet level. NSGs are essential for securely enabling connectivity based on whether the recovery VM is in a test or production mode.

### DNS servers

Azure VNets support custom DNS server configurations or integration with Azure DNS. This controls how name resolution works in the DR environment. Custom DNS is essential when restoring AD-integrated environments or for DNS forwarding to on-prem systems.

### Subnet routing (User-defined routes)

Azure allows the creation of custom routes (UDRs) to control traffic flow between subnets and to on-premises networks, overriding default system routing. This helps to enforce routing policies and ensure connectivity back to on-premises via VPN or ExpressRoute.

### Public IP addresses

Azure VMs can be assigned public IP addresses (static or dynamic) to allow direct Internet access when needed. Assign public IPs to failover workloads that require external access. Avoid for sensitive workloads -- use Bastion or VPN instead where possible.

### Azure Bastion

Azure Bastion enables secure, browser-based RDP/SSH access to VMs without exposing public IPs. Operates via the Azure portal and uses TLS encryption. Especially useful in test failover where exposing to the internet is not desired.

### Azure Site-to-Site VPN

Site-to-Site VPN provides an encrypted IPsec connection between your on-premises network and Azure VNets, enabling hybrid connectivity. Critical for accessing internal apps or restoring cross-dependencies with systems still running on-premises.

### Azure ExpressRoute

ExpressRoute offers dedicated private connectivity between your data center and Azure, bypassing the Internet for improved speed, reliability, and security. Recommended for enterprise-grade DR with large datasets or low-latency requirements.

---

# Network management in Microsoft Azure

Recovery networks are Azure Virtual Networks (VNets) and subnets where your backup systems (recovery servers) will run if your main systems fail. There are two kinds of recovery networks: production recovery networks and test recovery networks.

## Production recovery network

Production recovery networks are used during a real disaster when you need to move your services to Azure. Failovered workloads (VMs) are connected to these recovery networks so that business operations are resumed.

Example: VNet: `dr-prod-vnet-91a4e5bf`, Subnet: `subnet-one (10.0.10.0/24)`

## Test recovery network

Test recovery networks are used during manual or automated test failovers to verify that disaster recovery works without impacting your production systems. To prevent IP conflicts or data leakage, test recovery networks must be isolated from the production environment. It is best practice to use a dedicated VNet.

## Best practices for Disaster Recovery network configuration

- **Separate production and test VNets and subnets** -- Keep test and production environments isolated.
- **Use Azure tags and naming conventions** -- Clearly label networks (e.g., `dr-prod` and `dr-test`).
- **Plan IP ranges carefully** -- Ensure VNets and subnets do not conflict with on-premises networks if using VPN or ExpressRoute.
- **Preconfigure required network resources** -- NSGs, route tables, custom DNS, and public IPs should be configured in advance.

## Adding a production recovery network from Microsoft Azure

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. In the **Production networks** pane, click **Add network**.
3. In the **Add production network** window, select a virtual network and subnet.
4. [Optional] To make this subnet default, select **Set this subnet as 'Default' for mapping**.
5. In the **Mapping to local network** field, click **Add** and enter source local networks in CIDR format.
6-8. Enter the source local networks and click **Done**.

## Adding a test recovery network from Microsoft Azure

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. In the **Test networks** pane, click **Add network**.
3-8. Follow similar steps as adding a production network.

## Recommendations for Active Directory Domain Services availability

If your protected workloads need to authenticate in a domain controller, we recommend that you have an AD DC instance at the DR site in Microsoft Azure.

Recommendations for a dedicated AD DC instance on the DR site:

- Turn off Windows Firewall.
- Join the AD DC to the Active Directory service.
- Ensure that the Azure VM has Internet access.
- Add the Active Directory feature.
- Deploy at least one domain controller in the DR site in Azure. Recovered workloads need to authenticate, apply Group Policies, and resolve names.
- Use a replicated domain controller (not read-only). RODCs may not support all authentication scenarios after a failover.
- Ensure proper DNS configuration. Configure the recovery VNet to use the Azure-based domain controller(s) as the custom DNS server.
- Replicate SYSVOL and ensure time synchronization between Azure and on-premises environments.
