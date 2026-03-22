# Site-to-site Open VPN - Additional information

Site-to-site Open VPN - Additional information
Site-to-site Open VPN - Additional information

When you create a recovery server, you configure its IP address in production network and its Test IP address.

After you perform failover (run the virtual machine in the cloud), and log in to the virtual machine to check the IP address of the server, you see the IP address in production network.

When you perform test failover, you can reach the test server only by using the Test IP address, which is visible only in the configuration of the recovery server.

To reach a test server from your local site, you must use the Test IP address.

The network configuration of the server always shows the IP address in production network (as the test server mirrors how the production server would look). This happens because the test IP address does not belong to the test server, but to the VPN gateway, and is translated to the production IP address using NAT.

The diagram below shows an example of the Site-to-site Open VPN configuration. Some of the servers in the local environment are recovered to the cloud using failover (while the network infrastructure is ok).

The customer enabled Disaster Recovery by:

configuring the VPN appliance (14), and connected it to the dedicated cloud VPN server (15)

protecting some of the local servers with Disaster Recovery (1, 2, 3, x8, and x10)

Some servers on the local site (like 4) are connected to networks which are not connected to the VPN appliance. Such servers are not protected with Disaster Recovery.

Part of the servers (connected to different networks) work in the local site: (1, 2, 3, and 4)

The protected servers (1, 2, and 3) are being tested with test failover (11, 12, and 13)

Some servers in the local site are unavailable (x8, x10). After performing failover, they become available in the cloud (8, and 10)

Some primary servers (7, and 9), connected to different networks, are available in the cloud environment

(5) is a server in the Internet with a public IP address

(6) is a workstation connected to the cloud using a Point-to-site VPN connection (p2s)

In this example, the following connection setup is available (for example, "ping") from a server in the From: row to a server in the To: column.

To:	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15
From:	 	local	local	local	local	internet	p2s	primary	failover	primary	failover	test failover	test failover	test failover	VPN appliance	VPN server
1	local	 	direct	via local router 1	via local router 2	via local router 1 and Internet	no

via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: NAT (VPN server)

via local router 1 and Internet: pub



via tunnel: NAT (VPN server)

via local router 1 and Internet: pub



via local router 1 and tunnel: NAT (VPN server)

via local router 1 and Internet: pub

direct	no
2	local	direct	 	via local router 1	via local router 2	via local router 1 and Internet	no

via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: NAT (VPN server)

via local router 1 and Internet: pub



via tunnel: NAT (VPN server)

via local router 1 and Internet: pub



via local router 1 and tunnel: NAT (VPN server)

via local router 1 and Internet: pub

direct	no
3	local	via local router 1	via local router 1	 	via local router 2	via local router 1 and Internet	no

via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: local

via local router 1 and Internet: pub



via tunnel: NAT (VPN server)

via local router 1 and Internet: pub



via tunnel: NAT (VPN server)

via local router 1 and Internet: pub



via local router 1 and tunnel: NAT (VPN server)

via local router 1 and Internet: pub

via local router	no
4	local	via local router 2 and router 1	via local router 2 and router 1	via local router 2	 	via local router 2, and router 1, and Internet	no

via local router 2 and tunnel: local

via local router 2, and local router 1, and Internet: pub



via local router 2 and tunnel: local

via local router 2, and local router 1, and Internet: pub



via local router 2 and tunnel: local

via local router 2, and local router 1, and Internet: pub



via local router 2 and tunnel: local

via local router 2, and local router 1, and Internet: pub



via tunnel: NAT (VPN server)

via local router 2, and router 1, and Internet: pub



via tunnel: NAT (VPN server)

via local router 2, and router 1, and Internet: pub



via tunnel: NAT (VPN server)

via local router 2, and router 1, and Internet: pub

via local router 2	no
5	internet	no	no	no	no	 	n/a	via Internet: pub	via Internet: pub	via Internet: pub	via Internet: pub	via Internet: pub	via Internet: pub	via Internet: pub	no	no
6	p2s	no	no	no	no	via Internet

via p2s VPN (VPN server): local

via Internet: pub



via p2s VPN (VPN server): local

via Internet: pub



via p2s VPN (VPN server): local

via Internet: pub



via p2s VPN (VPN server): local

via Internet: pub



via p2s VPN - NAT (VPN server)

via Internet: pub



via p2s VPN - NAT (VPN server)

via Internet: pub



via p2s VPN - NAT (VPN server)

via Internet: pub

no	no
7	primary	via tunnel	via tunnel	via tunnel and local router 1	via tunnel and local router 1 and 2	via Internet (via VPN server)	no	 	direct in cloud: local	via tunnel and local router 1: local	via tunnel and local router 1: local	via VPN server: NAT	via VPN server: NAT	via tunnel and local router 1: NAT	no	DHCP and DNS protocols only
8	failover	via tunnel	via tunnel	via tunnel and local router 1	via tunnel and local router 1 and 2	via Internet (via VPN server)	no	direct in cloud: local	 	via tunnel and local router 1: local	via tunnel and local router 1: local	via VPN server: NAT	via VPN server: NAT	via tunnel and local router 1: NAT	no	DHCP and DNS protocols only
9	primary	via tunnel and local router 1	via tunnel and local router 1	via tunnel	via tunnel	via Internet (via VPN server)	no	via tunnel and local router 1: local	via tunnel and local router 1: local	 	direct in cloud: local	via tunnel and local router 1: NAT	via tunnel and local router 1: NAT	via VPN server: NAT	no	DHCP and DNS protocols only
10	failover	via tunnel and local router 1	via tunnel and local router 1	via tunnel	via tunnel	via Internet (via VPN server)	no	via tunnel and local router 1: local	via tunnel and local router 1: local	direct in cloud: local	 	via tunnel and local router 1: NAT	via tunnel and local router 1: NAT	via VPN server: NAT	no	DHCP and DNS protocols only
11	test failover	no	no	no	no	via Internet (via VPN server)	no	no	no	no	no	 	direct in cloud: local	via VPN server: local (routing)	no	DHCP and DNS protocols only
12	test failover	no	no	no	no	via Internet (via VPN server)	no	no	no	no	no	direct in cloud: local	 	via VPN server: local (routing)	no	DHCP and DNS protocols only
13	test failover	no	no	no	no	via Internet (via VPN server)	no	no	no	no	no	via VPN server: local (routing)	via VPN server: local (routing)	 	no	DHCP and DNS protocols only
14	VPN appliance	direct	direct	via local router 1	via local router 2	via Internet (local router 1)	no	no	no	no	no	no	no	no	 	no
15	VPN server	no	no	no	no	no	no	no	no	no	no	no	no	no	no
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.