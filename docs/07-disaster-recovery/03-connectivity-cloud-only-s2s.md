---
title: "Connectivity and networks: Cloud-only mode and Site-to-site Open VPN"
section: "Implementing disaster recovery"
subsection: "Connectivity and networks"
page_range: "939-949"
tags: [connectivity, cloud-only, site-to-site, OpenVPN, VPN appliance, VPN gateway, networking]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#setting-up-connectivity.html"
---

# Connectivity and networks

With Disaster Recovery, you can define the following connectivity types to the cloud site:

- **Cloud-only mode** -- Does not require a VPN appliance deployment on the local site. The local and cloud networks are independent networks. This type of connection implies either the failover of all the local site's protected servers or partial failover of independent servers that do not need to communicate with the local site. Cloud servers on the cloud site are accessible through the point-to-site VPN, and public IP addresses (if assigned).

- **Site-to-site Open VPN connection** -- Requires a VPN appliance deployment on the local site. Allows you to extend your networks to the cloud and retain the IP addresses. Your local site is connected to the cloud site by means of a secure VPN tunnel. This type of connection is suitable in case you have tightly dependent servers on the local site. Cloud servers on the cloud site are accessible through the local network, point-to-site VPN, and public IP addresses (if assigned).

- **Multi-site IPsec VPN connection** -- Requires a local VPN device that supports IPsec IKE v2. When you start configuring the connection, Disaster Recovery automatically creates a cloud VPN gateway with a public IP address. Suitable for DR scenarios when you have one or several local sites hosting critical workloads or tightly dependent services. Cloud servers are accessible through the local network, point-to-site VPN, and public IP addresses (if assigned).

- **Point-to-site remote VPN access** -- A secure Point-to-site remote VPN access to your cloud and local site workloads from outside by using your endpoint device. For a local site access, this type of connection requires a VPN appliance deployment on the local site.

# Cloud-only mode

The cloud-only mode does not require a VPN appliance deployment on the local site. It implies that you have two independent networks: one on the local site, another on the cloud site. Routing is performed with the router on the cloud site.

## How routing works

In case the cloud-only mode is established, routing is performed with the router on the cloud site so that servers from different cloud networks can communicate with each other.

## Configuring Cloud-only mode

Cloud-only mode is the default connectivity type that is created automatically when you apply a disaster recovery plan to a workload.

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Select **Cloud-only** and click **Configure**.
   As a result, the VPN gateway and cloud network with the defined address and mask are deployed on the cloud site.

## Managing networks in Cloud-only mode

You can add and manage up to 23 networks in the cloud.

### Add a cloud network

1. Go to **Disaster Recovery** > **Connectivity**.
2. On **Cloud site**, click **Add cloud network**.
3. Define the cloud network parameters: the network address and mask, and then click **Done**.

### Delete a cloud network

**Prerequisites:** All cloud servers are deleted from the network that you want to delete.

1. Go to **Disaster Recovery** > **Connectivity**.
2. On **Cloud site**, click the network address that you want to delete.
3. Click **Delete** and confirm the operation.

### Change cloud network parameters

1. Go to **Disaster Recovery** > **Connectivity**.
2. On **Cloud site**, click the network address that you want to edit.
3. Click **Edit**.
4. Define the network address and mask, and click **Done**.

# Site-to-site Open VPN connection

The Site-to-site Open VPN connection allows you to extend your local networks to the cloud through a secure VPN tunnel. You can add and manage up to 23 networks in the cloud.

To establish a Site-to-site Open VPN connectivity between the local and cloud sites, a **VPN appliance** and a **VPN gateway** are used.

When you start configuring the Site-to-site Open VPN connectivity in the Cyber Protect console, the VPN gateway is automatically deployed in the cloud site. After the VPN gateway is deployed, you must do the following:

1. Deploy the VPN appliance on your local site.
2. Add the networks that you want to be protected.
3. Register the VPN appliance in the cloud.

Disaster Recovery will create a replica of your local network in the cloud. A secure VPN tunnel will be established between the VPN appliance and the VPN gateway. The production networks in the cloud will be bridged with your local networks. The local and cloud servers will communicate through this VPN tunnel as if they are all in the same Ethernet segment. Routing will be performed by your local router.

For each source machine that you want to protect, you must create a recovery server on the cloud site. It will stay in the **Standby** state until a failover event happens. If a disaster happens and you start a failover process (in the **production mode**), the recovery server will be started in the cloud with the same IP address as the source machine, in the same Ethernet segment. Your clients will continue working with the server, not noticing any background changes.

You can also start a failover process in the **test mode**. The source machine will be working and the respective recovery server with the same IP address will be started in the cloud. To prevent IP address conflicts, a special virtual network will be created in the cloud -- **test network**. The test network will be isolated to prevent duplication of the source machine IP address in one Ethernet segment. To access the recovery server in the test failover mode, you must assign a **Test IP address** to it.

## How routing works

When a Site-to-site connection is established, routing between cloud networks is performed by your local router. The VPN server does not perform routing between cloud servers located in different cloud networks. If a cloud server from one network wants to communicate with a server from another cloud network, the traffic goes through the VPN tunnel to the local router on the local site, then the local router routes it to another network, and it goes back through the tunnel to the destination server on the cloud site.

## VPN gateway

The VPN gateway is the major component that enables communication between the local and cloud sites. It is a virtual machine in the cloud on which the special software is installed, and the network is specifically configured. The VPN gateway has the following functions:

- Connects the Ethernet segments of your local network and production network in the cloud in the L2 mode.
- Provides iptables and ebtables rules.
- Works as a default router and NAT for the machines in the test and production networks.
- Works as a DHCP server. All machines in the production and test networks get the network configuration (IP addresses, DNS settings) via DHCP. Every time a cloud server will get the same IP address from the DHCP server. If you need to set up the custom DNS configuration, you should contact the support team.
- Works as a caching DNS.

### VPN gateway network configuration

The VPN gateway has several network interfaces:

- External interface, connected to the Internet
- Production interfaces, connected to the production networks
- Test interface, connected to the test network

In addition, two virtual interfaces are added for Point-to-site and Site-to-site connections. When the VPN gateway is deployed and initialized, the bridges are created -- one for the external interface, and one for the client and production interfaces. Though the client-production bridge and the test interface use the same IP addresses, the VPN gateway can route packages correctly by using a specific technique.

## VPN appliance

The **VPN appliance** is a virtual machine on the local site with Linux that has special software installed, and a special network configuration. It enables the communication between the local and cloud sites.

## Enabling the Site-to-site connectivity

You can enable the Site-to-site connectivity in the following cases:

- If you need the cloud servers on the cloud site to communicate with servers on the local site.
- After a failover to the cloud, the local infrastructure is recovered, and you want to fail back your servers to the local site.

### To enable the site-to-site connectivity

1. Go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**, and then enable the **Site-to-site connection** option.

As a result, the site-to-site VPN connection is enabled between the local and cloud sites. The Disaster Recovery service gets the network settings from the VPN appliance and extends the local networks to the cloud site.

## Configuring a Site-to-site Open VPN connection

The VPN appliance extends your local network to the cloud through a secure VPN tunnel ("Site-to-site" or S2S connection).

### To configure a connection through the VPN appliance

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Select **Site-to-site Open VPN connection**, and click **Configure**. The system starts deploying the VPN gateway in the cloud. Meanwhile, you can proceed to the next step.

   > **Note:** The VPN gateway is provided without additional charge. It will be deleted if the Disaster Recovery functionality is not used, i.e. no primary or recovery server is present in the cloud for seven days.

3. In the **VPN appliance** block, click **Download and deploy**, and then, depending on the virtualization platform you are using, download the VPN appliance.

   | Option | Description |
   |--------|-------------|
   | **VMware** | VPN appliance image for vSphere. |
   | **Hyper-V** | VPN appliance image for Hyper-V. |
   | **KVM/QEMU** | VPN appliance image for KVM/QEMU-based hypervisors, including Proxmox, Virtuozzo Infrastructure, and Scale Computing. |

4. Deploy the appliance and connect it to the production networks.
5. [For VMware] In vSphere, ensure that **Promiscuous mode** and **Forged transmits** are enabled and set to **Accept** for all virtual switches that connect the VPN appliance to the production networks.
6. [For Hyper-V] Create a **Generation 1** virtual machine with 1024 MB of memory. Enable **Dynamic Memory** for the machine. Go to **Settings** > **Hardware** > **Network Adapter** > **Advanced Features** and select the **Enable MAC address spoofing** check box.
7. Power on the appliance.
8. Open the appliance console and log in with the "admin"/"admin" user name and password.
9. [Optional] Change the password.
10. [Optional] Change the network settings if needed. Define which interface will be used as the WAN for Internet connection.
11. Register the appliance in the Cyber Protection service by using the credentials of the company administrator.

    > **Note:** If two-factor authentication is configured for your account, you will also be prompted to enter the TOTP code.

Once the configuration is complete, the appliance will have the **Online** status. The appliance connects to the VPN gateway and starts to report information about networks from all active interfaces to the Disaster Recovery service.

## Managing the VPN appliance settings

On the **Disaster Recovery** > **Connectivity** tab, you can:

- Download log files.
- Unregister the appliance (if you need to reset the VPN appliance settings or switch to the Cloud-only mode).

In the VPN appliance console, you can:

- Change the password for the appliance.
- View/change the network settings and define which interface to use as the WAN for the Internet connection.
- Register/change the registration account (by repeating the registration).
- Restart the VPN service.
- Reboot the VPN appliance.
- Run the Linux shell command (only for advanced troubleshooting cases).

## Managing networks for Site-to-site Open VPN

You can add and manage up to 23 networks in the cloud.

### Adding networks

**Prerequisites:** Site-to-site Open VPN connectivity is configured, as described in "System requirements."

1. On the VPN appliance, set up the new network interface with the local network that you want to extend in the cloud.
2. [Optional] If you want to add one or more networks, for each additional network, add one virtual network interface (network adapter) to the virtual machine on which the virtual appliance is running.
3. Log in to the console of the VPN appliance, and then in the **Networking** section, configure the network settings for one of the interfaces (adapters).

   > **Note:**
   > - The IP address configuration is mandatory for only one of the virtual network interfaces, to enable Internet access. You can skip the IP configuration for the other network interfaces.
   > - Promiscuous mode and Forged transmits or MAC address spoofing must be enabled for each adapter.

4. Log in to the Cyber Protect console, and then go to **Disaster recovery** > **Connectivity**. All local networks are automatically extended to the cloud site.

### Deleting and changing networks

To delete or change cloud network parameters in Site-to-site Open VPN mode, follow the same procedures as in Cloud-only mode: navigate to **Disaster Recovery** > **Connectivity**, select the network, and use the **Delete** or **Edit** options.

### VPN appliance system requirements

- 1 CPU
- 1 GB RAM
- 8 GB disk space

### Required ports

- TCP 443 (outbound) -- for VPN connection
- TCP 80 (outbound) -- for automatic update of the appliance

Ensure that your firewalls and other components of your network security system allow connections through these ports to any IP address.
