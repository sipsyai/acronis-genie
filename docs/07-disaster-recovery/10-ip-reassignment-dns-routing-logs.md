---
title: "IP reassignment, custom DNS, local routing, and logs"
section: "Implementing disaster recovery"
subsection: "Network management"
page_range: "970-975"
tags: [IP reassignment, DNS, custom DNS, local routing, MAC addresses, VPN gateway, logs, network packets, troubleshooting]
acronis_version: "26.02"
---

# Reassigning IP addresses

You must reassign the IP addresses of the cloud networks and the cloud servers in order to complete the configuration in the following cases:

- After you switch from Site-to-site Open VPN to Multi-site IPsec VPN, or the opposite.
- After you apply a protection plan (if the Multi-site IPsec VPN connectivity is configured).

## Cloud network

### To reassign the IP address of a cloud network

1. In the **Connectivity** tab, click the IP address of the cloud network.
2. In the **Network** pop-up, click **Edit**.
3. Type the new the network address and network mask.
4. Click **Done**.

After you reassign the IP address of a cloud network, you must reassign the cloud servers that belong to the reassigned cloud network.

## Cloud server

### To reassign the IP address of a server

1. In the **Connectivity** tab, click the IP address of the server in the cloud network.
2. In the **Servers** pop-up, click **Change IP address**.
3. In the **Change IP address** pop-up, type the new IP address of the server, or use the automatically generated IP address which is part of the reassigned cloud network.
4. Click **Confirm**.

> **Note**
> Disaster Recovery automatically assigns IP addresses from the cloud network to all cloud servers that were part of the cloud network before the reassignment of the network IP address. You can use the suggested IP addresses to reassign the IP addresses of all the cloud servers at once.

---

# Reinstalling the VPN gateway

If there is an issue with the VPN gateway which you cannot resolve, you might want to reinstall the VPN gateway. Possible issues include the following:

- The VPN gateway is in **Error** status.
- The VPN gateway is in **Pending** status for a long time.
- The VPN gateway status is undetermined for a long time.

Reinstalling the VPN gateway process includes the following automatic actions: deleting the existing VPN gateway virtual machine completely, installing a new virtual machine from the template, and applying the settings of the previous VPN gateway on the new virtual machine.

### Prerequisites

One of the connectivity types to the cloud site must be set.

### To reinstall the VPN gateway

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click the gear icon of the VPN gateway, and select **Reinstall VPN gateway**.
3. In the **Reinstall VPN gateway** dialog, enter your login.
4. Click **Reinstall**.

---

# Configuring custom DNS servers

When you configure a connectivity, Disaster Recovery creates your cloud network infrastructure. The cloud DHCP server automatically assigns default DNS servers to the recovery servers and primary servers, but you can change the default settings and configure custom DNS servers. The new DNS settings will be applied at the time of the next request to the DHCP server.

### Prerequisites

One of the connectivity types to the cloud site must be set.

### To configure a custom DNS server

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**.
3. Click **Default (Provided by Cloud Site)**.
4. Select **Custom servers**.
5. Type the IP address of the DNS server.
6. [Optional] If you want to add another DNS server, click **Add**, and type the DNS server IP address.
7. Click **Done**.

> **Note**
> After you add the custom DNS servers, you can also add the default DNS servers. In that way, if the custom DNS servers are unavailable, Disaster Recovery will use the default DNS servers.

## Deleting custom DNS servers

### Prerequisites

Custom DNS servers are configured.

### To delete a custom DNS server

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**.
3. Click **Custom servers**.
4. Click the delete icon next to the DNS server.
5. Click **Done**.

> **Note**
> The delete operation is disabled when only one custom DNS server is available. If you want to delete all custom DNS servers, select **Default (provided by Cloud Site)**.

---

# Configuring local routing

In addition to your local networks that are extended to the cloud through the VPN appliance, you may have other local networks that are not registered in the VPN appliance but have servers which need to communicate with cloud servers. To establish the connectivity between such local servers and cloud servers, you need to configure the local routing settings.

### To configure local routing

1. Go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**, and then click **Local routing**.
3. Specify the local networks in the CIDR notation.
4. Click **Save**.

As a result, the servers from the specified local networks can communicate with the cloud servers.

---

# Downloading MAC addresses

You can download a list of MAC addresses, and then extract them and import them in the configuration of your custom DHCP server.

### Prerequisites

- One of the connectivity types to the cloud site must be set.
- At least one primary or recovery server with a MAC address must be configured.

### To download the list of MAC addresses

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**.
3. Click **Download the list of MAC addresses**, and then save the CSV file.

---

# Working with logs

Disaster Recovery collects logs for the VPN appliance and the VPN gateway. The logs are saved as .txt files, which are compressed in a .zip archive. You can download and extract the archive, and use the information for troubleshooting or monitoring purposes.

## Log files in the archive

The following list describes the log files that are part of the .zip archive:

| Log file | Description |
|----------|-------------|
| `dnsmasq.config.txt` | Configuration of the service that provides DNS and DHCP addresses |
| `dnsmasq.leases.txt` | Current DHCP address leases |
| `dnsmasq_log.txt` | Logs of the dnsmasq service |
| `ebtables.txt` | Information about the firewall tables |
| `free.txt` | Information about the free memory |
| `ip.txt` | Logs from the configuration of the network interfaces, including names for **Capturing network packets** settings |
| `NetworkManager_log.txt` | Logs from the NetworkManager service |
| `NetworkManager_status.txt` | Information about the status of the NetworkManager service |
| `openvpn@p2s_log.txt` | Logs from the OpenVPN service |
| `openvpn@p2s_status.txt` | Information about the status of the VPN tunnels |
| `ps.txt` | Currently running processes on the VPN gateway or VPN appliance |
| `resolv.conf.txt` | Configuration of the DNS servers |
| `routes.txt` | Information about the networking routes |
| `uname.txt` | Current version of the kernel of the operating system |
| `uptime.txt` | Length of period for which the operating system has not been restarted |
| `vpnserver_log.txt` | Logs from the VPN service |
| `vpnserver_status.txt` | Status of the VPN server |

## Downloading the logs of the VPN appliance

1. On the **Connectivity** page, click the gear icon next to the VPN appliance.
2. Click **Download log**.
3. [Optional] Select **Capture network packets**, and configure the settings.
4. Click **Done**.
5. When the .zip archive is ready for download, click **Download log**, and save it locally.

## Downloading the logs of the VPN gateway

1. On the **Connectivity** page, click the gear icon next to the VPN gateway.
2. Click **Download log**.
3. [Optional] Select **Capture network packets**, and configure the settings.
4. Click **Done**.
5. When the .zip archive is ready for download, click **Download log**, and save it locally.

## Capturing network packets

To troubleshoot and analyze the communication between the local production site and a primary or recovery server, you can choose to collect network packets on the VPN gateway or VPN appliance.

After collecting 32,000 network packets, or reaching time limit, capturing network packets stops, and the results are written in a .libpcap file that is added to the logs .zip archive.

| Setting | Description |
|---------|-------------|
| **Network interface name** | The network interface on which to capture network packets. If you want to capture network packets on all network interfaces, select **Any**. |
| **Time limit (seconds)** | The time limit for capturing network packets. The maximum value you can set is 1800. |
| **Filtering** | An extra filter to apply on the captured network packets. You can enter a string containing protocols, ports, directions, and their combinations, separated by space, such as: "and", "or", "not", "(", ")", "src", "dst", "net", "host", "port", "ip", "tcp", "udp", "icmp", "arp", "esp". |
