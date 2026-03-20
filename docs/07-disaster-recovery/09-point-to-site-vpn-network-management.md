---
title: "Point-to-site VPN and network management"
section: "Implementing disaster recovery"
subsection: "Point-to-site VPN remote access"
page_range: "962-970"
tags: [point-to-site, VPN, OpenVPN, remote access, network management, public IP, test IP, IP reconfiguration, Active Directory]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#dr-to-azure-network-management.html"
---

# Point-to-site remote VPN access

The Point-to-site connection is a secure connection from the outside by using your endpoint devices (such as computer or laptop) to the cloud and local sites through a VPN. It is available after you establish a Site-to-site Open VPN connection to the disaster recovery site. This type of connection is useful in the following cases:

- In many companies, the corporate services and web resources are available only from the corporate network. You can use the Point-to-site connection to securely connect to the local site.
- In case of a disaster, when a workload is switched to the cloud site and your local network is down, you may need direct access to your cloud servers. This is possible through the Point-to-site connection to the cloud site.

For the Point-to-site connection to the local site, you need to install the VPN appliance on the local site, configure the Site-to-site connection, and then the Point-to-site connection to the local site. Your remote employees will have access to the corporate network through L2 VPN.

The Point-to-site configuration uses certificates to authenticate to the VPN client. Additionally user credentials are used for authentication.

- Users should use their Cyber Protect Cloud credentials to authenticate in the VPN client. They must have either a "Company Administrator" or a "Cyber Protection" user role.
- If you re-generated the OpenVPN configuration, you need to provide the updated configuration to all of the users using the Point-to-site connection to the cloud site.

## Configuring Point-to-site remote VPN access

If you need to connect to your local site remotely, you can configure the Point-to-site connection to the local site.

### Prerequisites

- Site-to-site Open VPN connectivity is configured.
- The VPN appliance is installed on the local site.

### To configure the Point-to-site connection to the local site

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**.
3. Enable the **VPN access to local site** option.
4. Ensure that your user who needs to establish the Point-to-site connection to the local site has:
   - A user account in Cyber Protect Cloud. These credentials are used for authentication in the VPN client.
   - A "Company Administrator" or "Cyber Protection" user role.
5. Configure the OpenVPN client:
   a. Download the OpenVPN client version 2.4.0 or later from https://openvpn.net/community-downloads/.
   b. Install the OpenVPN client on the machine from which you want to connect to the local site.
   c. Click **Download configuration for OpenVPN**. The configuration file is valid for users in your organization with the "Company Administrator" or "Cyber Protection" user role.
   d. Import the downloaded configuration to the OpenVPN client.
   e. Log in to the OpenVPN client with your Cyber Protect Cloud user credentials.
   f. [Optional] If two-factor authentication is enabled for your organization, then you should provide the one-time generated TOTP code.

> **Important**
> If you enabled two-factor authentication for your account, you need to re-generate the configuration file and renew it for your existing OpenVPN clients. Users must re-log in to Cyber Protect Cloud to set up two-factor authentication for their accounts.

> **Note**
> OpenVPN Connect client is not supported.

## Managing point-to-site connection settings

In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity** and then click **Show properties** in the upper right corner.

### VPN access to local site

This option is used for managing VPN access to the local site. By default it is enabled. If it is disabled, then the Point-to-site access to the local site will be not allowed.

### Download configuration for OpenVPN

This will download the configuration file for the OpenVPN client. The file is required to establish a Point-to-site connection to the cloud site.

### Re-generate configuration

You can re-generate the configuration file for the OpenVPN client. This is required in the following cases:

- If you suspect that the configuration file is compromised.
- If two-factor authentication was enabled for your account.

As soon as the configuration file is updated, connecting by means of the old configuration file becomes not possible. Make sure to distribute the new file among the users who are allowed to use the Point-to-site connection.

### Active point-to-site connections

You can view all active point-to-site connections in **Disaster recovery** > **Connectivity**. Click the machine icon on the blue **Point-to-site** line and you will see the detailed information about active point-to-site connections grouped by the user name.

## Recommendations for Active Directory Domain Services availability

If your protected workloads need to authenticate in a domain controller, we recommend that you have an Active Directory Domain Controller (AD DC) instance at the Disaster Recovery site.

### Active Directory Domain Controller for L2 Open VPN connectivity

With the L2 Open VPN connectivity, the IP addresses of the protected workloads are retained in the cloud site during a test failover or a production failover. Therefore, the AD DC during a test failover or a production failover has the same IP address as in the local site. With custom DNS you can set your own custom DNS server for all cloud servers.

### Active Directory Domain Controller for L3 IPsec VPN connectivity

With L3 IPsec VPN connectivity, the IP addresses of the protected workloads are not retained in the cloud site. Therefore, we recommend that you have an additional dedicated AD DC instance as a primary server in the cloud site before you perform a production failover.

The recommendations for a dedicated AD DC instance that is configured as a primary server in the cloud site are the following:

- Turn off Windows firewall.
- Join the primary server to the Active Directory service.
- Ensure that the primary server has Internet access.
- Add the Active Directory feature.

---

# Network management

## Public and test IP addresses

If you assign the public IP address when creating a recovery server, the recovery server becomes available from the Internet through this IP address. When a packet comes from the Internet with the destination public IP address, the VPN gateway remaps it to the respective production IP address by using NAT, and then sends it to the corresponding recovery server.

If you assign the test IP address when creating a recovery server, the recovery server becomes available in the test network through this IP address. When you perform the test failover, the original machine is still running while the recovery server with the same IP address is launched in the test network in the cloud. There is no IP address conflict, as the test network is isolated. The recovery servers in the test network are reachable by their test IP addresses, which are remapped to the production IP addresses through NAT.

## IP address reconfiguration

For proper disaster recovery performance, the IP addresses assigned to the local and cloud servers must be consistent. If there is any inconsistency or mismatch in IP addresses, you will see the exclamation mark next to the corresponding network in **Disaster Recovery** > **Connectivity**.

Common reasons for IP address inconsistency:

1. A recovery server was migrated from one network to another, or the network mask of the cloud network was changed.
2. The connectivity type was switched from one without Site-to-site connection to a Site-to-site connection, placing a local server in a different network than the recovery server on the cloud site.
3. The connectivity type was switched from Site-to-site Open VPN to Multi-site IPsec VPN, or the reverse.
4. Editing network parameters on the VPN appliance site (adding interfaces, editing masks via DHCP, etc.).

### To resolve the issue with network settings

1. Click the network that requires IP address reconfiguration. You will see a list of servers, their status, and IP addresses. Servers with inconsistent network settings are marked with an exclamation mark.
2. To change network settings for a server, click **Go to server**. To change network settings for all servers at once, click **Change** in the notification block.
3. Change the IP addresses as needed by defining them in the **New IP** and **New test IP** fields.
4. When ready, click **Confirm**.

### Move servers to a suitable network

When you create a disaster recovery protection plan and apply it on selected devices, the system checks device IP addresses and automatically creates cloud networks if there are not existing cloud networks where IP address fits. By default, the cloud networks are configured with maximum ranges recommended by IANA for private use (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). You can narrow your network by editing the network mask.

To reconfigure cloud networks when the network on the cloud site might become a superset of the local networks:

1. Click the cloud network that requires network size reconfiguration and then click **Edit**.
2. Reconfigure the network size with the correct settings.
3. Create other required networks.
4. Click the notification icon next to the number of devices connected to the network.
5. Click **Move to a suitable network**.
6. Select the servers that you want to move to suitable networks and then click **Move**.
