---
title: "Awareness Dashboard and Site-to-Site Open VPN"
section: "Additional Cyber Protection Tools"
subsection: "Awareness Dashboard and VPN"
page_range: "1496-1504"
tags: [awareness-dashboard, security-awareness-training, wizer, site-to-site-vpn, openvpn, disaster-recovery, failover, network-configuration]
acronis_version: "26.02"
---

# Awareness Dashboard

This dashboard is available if the Security Awareness Training service is enabled by the service provider.

The dashboard is accessible at the Customer level for users with the following roles: Partner Administrator, Customer Administrator, Protection Administrator, or Cyber Administrator.

The dashboard provides an overview of the progress of the security awareness training in the organization and serves as a gateway to navigate to the Security Awareness Training admin console in Wizer.

## Operating the Security Awareness Training Service

To manage users and training content available for your organization, click **Admin Console** in the upper left of the Awareness dashboard. The Wizer admin console will open. For detailed instructions, see the Wizer documentation.

---

# Site-to-Site Open VPN - Additional Information

When you create a recovery server, you configure its **IP address in production network** and its **Test IP address**.

After you perform failover (run the virtual machine in the cloud), and log in to the virtual machine to check the IP address of the server, you see the **IP address in production network**.

When you perform test failover, you can reach the test server only by using the **Test IP address**, which is visible only in the configuration of the recovery server.

> **Note:** The network configuration of the server always shows the **IP address in production network** (as the test server mirrors how the production server would look). This happens because the test IP address does not belong to the test server, but to the VPN gateway, and is translated to the production IP address using NAT.

## Network Architecture Example

The diagram below shows an example of the Site-to-site Open VPN configuration. Some of the servers in the local environment are recovered to the cloud using failover (while the network infrastructure is ok).

The example architecture involves:

1. **The customer enabled Disaster Recovery by:**
   a. Configuring the VPN appliance (14), and connecting it to the dedicated cloud VPN server (15)
   b. Protecting some of the local servers with Disaster Recovery (1, 2, 3, x8, and x10). Some servers on the local site (like 4) are connected to networks which are not connected to the VPN appliance -- such servers are not protected with Disaster Recovery.

2. **Part of the servers** (connected to different networks) work in the local site: (1, 2, 3, and 4)

3. **The protected servers** (1, 2, and 3) are being tested with test failover (11, 12, and 13)

4. **Some servers in the local site are unavailable** (x8, x10). After performing failover, they become available in the cloud (8, and 10)

5. **Some primary servers** (7, and 9), connected to different networks, are available in the cloud environment

6. **(5)** is a server in the Internet with a public IP address

7. **(6)** is a workstation connected to the cloud using a Point-to-site VPN connection (p2s)

## Connection Availability Matrix

The following connection setup is available (for example, "ping") from a server in the **From:** row to a server in the **To:** column:

### Key Server Types and Connectivity

| Server | Type | Key Connectivity |
|--------|------|-----------------|
| 1 | local | Direct to 2; via local routers to 3, 4; via tunnel to cloud servers (7-10); via tunnel NAT to test failover (11-13); via local router to VPN appliance (14) |
| 2 | local | Direct to 1; via local routers to 3, 4; via tunnel to cloud servers (7-10); via tunnel NAT to test failover (11-13); direct to VPN appliance (14) |
| 3 | local | Via local to 1, 2; via local router to 4; via tunnel to cloud servers (7-10); via tunnel NAT to test failover (11-13); via local router to VPN appliance (14) |
| 4 | local | Via local routers to 1, 2, 3; via local router and tunnel to cloud servers (7-10); via local router and tunnel NAT to test failover (11-13); via local router 2 to VPN appliance (14) |
| 5 | internet | No connection to local servers (1-4); via internet public to cloud servers (7-13) |
| 6 | p2s | Via p2s VPN to cloud servers (7-13); no connection to local or VPN infrastructure |
| 7 | primary (cloud) | Via tunnel to local servers (1-3); direct in cloud to 8; via tunnel and local router to 4; via VPN server NAT to test failovers (11-12); no connection to VPN appliance (14) |
| 8 | failover (cloud) | Via tunnel to local servers (1-3); direct in cloud to 7; via VPN server NAT to test failovers (11-12); no connection to VPN appliance (14); DHCP and DNS protocols only to VPN server (15) |
| 9 | primary (cloud) | Via tunnel to local servers (1-3); via tunnel to 7, 8; direct in cloud to 10; via VPN server NAT to test failovers; no connection to VPN appliance (14); DHCP and DNS protocols only to VPN server (15) |
| 10 | failover (cloud) | Via tunnel to local servers (1-3); direct in cloud to 9; via VPN server NAT to test failovers; no connection to VPN appliance (14); DHCP and DNS protocols only to VPN server (15) |
| 11-13 | test failover | No connection to local servers (1-4); via internet (VPN server) to 5; direct in cloud local between test failovers; via VPN server local routing to 11-13; no connection to VPN appliance (14); DHCP and DNS protocols only to VPN server (15) |
| 14 | VPN appliance | Direct to 1, 2; via local routers to 3, 4; via internet (local router 1) to 5; no connection to cloud servers (7-15) |
| 15 | VPN server | No connection to any server |

### Important Notes

- Test failover servers (11, 12, 13) exist on a single cloud test network and communicate with each other directly. They can reach the internet only via the VPN server.
- The VPN appliance (14) connects local servers to cloud via an L2 VPN tunnel but cannot directly reach cloud servers itself.
- The VPN server (15) handles DHCP/DNS for cloud servers but has no direct connectivity to any server.
- Point-to-site (p2s) workstation (6) accesses cloud servers through the VPN but cannot reach local servers or infrastructure.
