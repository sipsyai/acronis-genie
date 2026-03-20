---
title: "Multi-site IPsec VPN and Point-to-site VPN access"
section: "Implementing disaster recovery"
subsection: "Connectivity and networks"
page_range: "950-969"
tags: [IPsec VPN, multi-site, point-to-site, VPN gateway, connectivity, OpenVPN, Active Directory, network management]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#multi-site-ipsec-vpn-concept.html"
---

# Multi-site IPsec VPN connection

You can use the Multi-site IPsec VPN connectivity to connect a single local site, or multiple local sites to the Disaster Recovery through a secure L3 IPsec VPN connection.

This connectivity type is useful for disaster recovery scenarios if you have one of the following use cases:

- You have one local site hosting critical workloads.
- You have multiple local sites hosting critical workloads (e.g., offices in different locations).
- You use third-party software sites or managed service providers sites, and are connected to them through an IPsec VPN tunnel.

To establish a Multi-site IPsec VPN communication between the local sites and the cloud site, a **VPN gateway** is used. When you start configuring the Multi-site IPsec VPN connection in the Cyber Protect console, the VPN gateway is automatically deployed in the cloud site. You should configure the cloud network segments and make sure that they do not overlap with the local network segments.

> **Note:** When using a Multi-site IPsec VPN connection, the VPN gateway is automatically assigned a public IP address.

## VPN gateway functions

- Connects the Ethernet segments of your local network and production network in the cloud in the L3 IPsec mode.
- Works as a default router and NAT for the machines in the test and production networks.
- Works as a DHCP server. All machines get network configuration via DHCP. You can set up a custom DNS configuration if needed.
- Works as a caching DNS.

## Configuring Multi-site IPsec VPN

You can configure a Multi-site IPsec VPN connection in the following two ways:

- From the **Disaster Recovery** > **Connectivity** tab.
- By applying a protection plan on devices, then manually switching from the automatically created Site-to-site Open VPN to Multi-site IPsec VPN.

### From the Connectivity tab

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. In the **Multi-site VPN connection** section, click **Configure**. A VPN gateway is deployed on the cloud site.
3. Configure the Multi-site IPsec VPN settings.

### From a protection plan

1. In the Cyber Protect console, go to **Devices**.
2. Apply a protection plan to one or multiple devices from the list.
3. Go to **Disaster Recovery** > **Connectivity**.
4. Click **Show properties**.
5. Click **Switch to Multi-site IPsec VPN**.
6. Configure the Multi-site IPsec VPN settings.
7. Reassign the IP addresses of the cloud network and cloud servers.

## Configuring the Multi-site IPsec VPN settings

**Prerequisites:**
- Multi-site IPsec VPN connectivity is configured.
- Each local IPsec VPN gateway has a public IP address.
- Your cloud network has enough IP addresses for the cloud servers and recovery servers.
- [If a firewall is used] The following IP protocols and UDP ports are allowed on the local sites: IP Protocol ID 50 (ESP), UDP Port 500 (IKE), and UDP Port 4500.
- The NAT-T configuration on the local sites is disabled.

### To configure a Multi-site IPsec VPN connection

1. **Add one or more networks to the cloud site.**
   a. Click **Add Network**.

   > **Note:** When you add a cloud network, a corresponding test network is added automatically with the same network address and mask for performing test failovers.

   b. In the **Network address** field, type the IP address of the network.

   > **Note:** Ensure that the cloud networks do not overlap with any local network in your environment.

   c. In the **Network mask** field, type the mask of the network.
   d. Click **Add**.

2. **Configure the settings for each local site.**
   a. Click **Add Connection**.
   b. Enter a name for the local VPN gateway.
   c. Enter the public IP address of the local VPN gateway.
   d. [Optional] Enter a description.
   e. Click **Next**.
   f. In the **Pre-shared key** field, type the pre-shared key, or click **Generate a new pre-shared key** to use an automatically generated value.

   > **Note:** You must use the same pre-shared key for the local and the cloud VPN gateways.

   g. Click **IPsec/IKE security settings** to configure the settings.

   > **Note:** Only IKEv2 protocol connections are supported. The default **Startup action** is **Add** (your local VPN gateway initiates the connection), but you can change it to **Start** (the cloud VPN gateway initiates) or **Route** (suitable for firewalls that support the route options).

   h. Configure the **Network policies**. The network policies specify the networks to which the IPsec VPN connects. Type the IP address and mask using the CIDR format. Local and cloud network segments should not overlap.
   i. Click **Save**.

## IPsec/IKE security settings

| Parameter | Description |
|-----------|-------------|
| **Encryption algorithm** | The encryption algorithm for data in transit. By default, all algorithms are selected. You must configure at least one of the selected algorithms on your local gateway device for each IKE phase. |
| **Hash algorithm** | The hash algorithm for data integrity and authenticity. By default, all algorithms are selected. |
| **Diffie-Hellman group numbers** | Define the strength of the key used in the Internet Key Exchange (IKE) process. Higher group numbers are more secure but require additional time. By default, all groups are selected. |
| **Lifetime (seconds)** | Duration of a connection instance with encryption/authentication keys. Phase 1: 900-28800 seconds (default 28800). Phase 2: 900-3600 seconds (default 3600). Phase 2 must be less than Phase 1. |
| **Rekey margin time (seconds)** | Margin time before connection/keying-channel expiration during which the local side attempts to negotiate a replacement. Range: 900-3600 seconds. Default: 3600. |
| **Replay window size (packet)** | The IPsec replay window size. Default -1 uses the value configured with charon.replay_window in the strongswan.conf file. A value of 0 disables the IPsec replay protection. |
| **Rekey fuzz (%)** | Maximum percentage by which margin values are randomly increased to randomize rekeying intervals. 0% disables randomization. |
| **DPD timeout (seconds)** | Time after which a dead peer detection (DPD) timeout occurs. Default: 30. |
| **Dead peer detection (DPD) timeout action** | **Restart** - Restart the session. **Clear** - End the session. **None** - Take no action. |
| **Startup action** | **Add** - your local VPN gateway initiates the connection. **Start** - the cloud VPN gateway initiates the connection. **Route** - suitable for VPN gateways that support the route option; tunnel is up only when there is traffic. |

### Security restrictions for IPsec VPN connectivity

- IKEv1 is not supported (only IKEv2 protocol connections are supported).
- Unsupported Encryption algorithms: DES, 3DES.
- Unsupported Hash algorithms: SHA1, MD5.
- Diffie-Hellman group number 2 is not supported.

## General recommendations for local sites

- For each IKE Phase, set at least one of the values that are configured in the cloud site for Encryption algorithm, Hash algorithm, and Diffie-Hellman group numbers.
- Enable Perfect forward secrecy with at least one of the Diffie-Hellman group numbers configured for IKE Phase 2.
- Configure the same **Lifetime** value for IKE Phase 1 and IKE Phase 2 as in the cloud site.
- NAT traversal (NAT-T) configurations are not supported. Disable NAT-T on the local site.

## Switching between VPN types

You can easily switch between Site-to-site Open VPN and Multi-site IPsec VPN connections. When you switch the connectivity type, the active VPN connections are deleted, but the cloud servers and network configurations are preserved. You will still need to reassign the IP addresses of the cloud networks and servers.

| Feature | Site-to-site Open VPN | Multi-site IPsec VPN |
|---------|----------------------|---------------------|
| Local site support | Single | Single, Multiple |
| VPN Gateway mode | L2 Open VPN | L3 IPsec VPN |
| Network segments | Extends local network to cloud network | Local and cloud network segments should not overlap |
| Point-to-Site access to local site | Yes | No |
| Point-to-Site access to cloud site | Yes | Yes |
| Requires a public IP offering item | No | Yes |

## Troubleshooting IPsec VPN configuration issues

| Problem | Possible solution |
|---------|------------------|
| **IKE phase 1 negotiation error** | Click **Retry** and check for more specific errors (algorithm mismatch, incorrect pre-shared key). |
| Connection stays in **Connecting** status | Check: UDP port 500 is open, connectivity between sites, IP address of local site is correct. |
| Connection stays in **Waiting for a connection** | Startup action is set to **Add** on cloud site. Initiate connection from the local site. |
| Connection stays in **Waiting for traffic** | Startup action is set to **Route**. Try pinging from the local site to the cloud site VM. Ensure the local site established a tunnel. |
| Network policies are down | Ensure network mappings and sequence of policies match exactly on local and cloud sites. |
| Restart a specific IPsec connection | In **Disaster recovery** > **Connectivity**, click the connection, then **Disable connection**, click again, then **Enable connection**. |

## Downloading IPsec VPN log files

**Prerequisites:** Multi-site IPsec VPN connectivity is configured.

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click the gear icon next to the VPN gateway of the cloud site.
3. Click **Download log**.
4. Click **Done**.
5. When the .zip archive is ready for download, click **Download log**, and save it locally.

### Log files in the archive

- `ip.txt` - Contains logs from network interface configuration (two IP addresses: a public IP and a local IP).
- `swanctl-list-loaded-config.txt` - Contains information about all IPsec sites.
- `swanctl-list-active-sas.txt` - Contains connections and policies that are in status active or connecting.

# Point-to-site remote VPN access

The Point-to-site connection is a secure connection from the outside by using your endpoint devices (computer or laptop) to the cloud and local sites through a VPN. It is available after you establish a Site-to-site Open VPN connection to the disaster recovery site.

Use cases:

- Corporate services and web resources are available only from the corporate network. You can use the Point-to-site connection to securely connect to the local site.
- In case of a disaster, when a workload is switched to the cloud site and your local network is down, you may need direct access to your cloud servers through the Point-to-site connection.

For the Point-to-site connection to the local site, you need to install the VPN appliance on the local site, configure the Site-to-site connection, and then the Point-to-site connection. Your remote employees will have access to the corporate network through L2 VPN.

Users should use their Cyber Protect Cloud credentials to authenticate in the VPN client. They must have either a "Company Administrator" or a "Cyber Protection" user role.

## Configuring Point-to-site remote VPN access

**Prerequisites:**
- Site-to-site Open VPN connectivity is configured.
- The VPN appliance is installed on the local site.

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**.
3. Enable the **VPN access to local site** option.
4. Ensure that the user has a Cyber Protect Cloud account with "Company Administrator" or "Cyber Protection" role.
5. Configure the OpenVPN client:
   a. Download the OpenVPN client version 2.4.0 or later from https://openvpn.net/community-downloads/.

   > **Note:** OpenVPN Connect client is not supported.

   b. Install the OpenVPN client on the machine from which you want to connect.
   c. Click **Download configuration for OpenVPN**. The configuration file is valid for users in your organization with the required role.
   d. Import the downloaded configuration to the OpenVPN client.
   e. Log in to the OpenVPN client with your Cyber Protect Cloud user credentials.
   f. [Optional] If two-factor authentication is enabled, provide the one-time generated TOTP code.

> **Important:** If you enabled two-factor authentication for your account, you need to re-generate the configuration file and renew it for your existing OpenVPN clients.

## Managing point-to-site connection settings

In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity** and then click **Show properties**:

- **VPN access to local site** -- Enable or disable VPN access to the local site. By default it is enabled.
- **Download configuration for OpenVPN** -- Download the configuration file for the OpenVPN client.
- **Re-generate configuration** -- Re-generate the configuration file if it is compromised or if two-factor authentication was enabled.
- **Active point-to-site connections** -- View all active connections by clicking the machine icon on the blue **Point-to-site** line.

# Network management

## Public and test IP addresses

If you assign the public IP address when creating a recovery server, the recovery server becomes available from the Internet through this IP address. When a packet comes from the Internet with the destination public IP address, the VPN gateway remaps it to the respective production IP address by using NAT, and then sends it to the corresponding recovery server.

If you assign the test IP address when creating a recovery server, the recovery server becomes available in the test network through this IP address. When you perform the test failover, the original machine is still running while the recovery server with the same IP address is launched in the test network in the cloud. There is no IP address conflict, as the test network is isolated.

## Active Directory Domain Services availability

If your protected workloads need to authenticate in a domain controller, we recommend that you have an Active Directory Domain Controller (AD DC) instance at the Disaster Recovery site.

- **For L2 Open VPN connectivity:** The IP addresses are retained during failover, so the AD DC has the same IP address as in the local site. With custom DNS you can set your own DNS server for all cloud servers.
- **For L3 IPsec VPN connectivity:** IP addresses are not retained. We recommend having a dedicated AD DC instance as a primary server in the cloud site. Turn off Windows firewall, join it to the AD service, ensure Internet access, and add the AD feature.

## IP address reconfiguration

For proper disaster recovery performance, the IP addresses assigned to the local and cloud servers must be consistent. If there is any inconsistency or mismatch, you will see an exclamation mark next to the corresponding network in **Disaster Recovery** > **Connectivity**.

Common reasons for IP address inconsistency:

1. A recovery server was migrated from one network to another, or the network mask was changed.
2. The connectivity type was switched from one without Site-to-site to one with Site-to-site.
3. The connectivity type was switched between VPN types.
4. Editing network parameters on the VPN appliance site (IP address, mask, gateway IP address, or DNS).
