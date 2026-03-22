# Editing the default settings of a recovery server

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Creating a disaster recovery protection plan > Editing the default settings of a recovery server
Editing the default settings of a recovery server

When you create and apply a disaster recovery protection plan, a recovery server is created with default settings. You can edit these default settings when necessary.

The following procedure applies to recovery servers that are located in Cyber Protect Cloud. If you want to configure the settings of a recovery server that is located in Microsoft Azure, follow the steps that are described in Creating recovery servers in Microsoft Azure.

A recovery server is created only if it does not exist. Existing recovery servers are not changed or recreated.

To edit the default settings of the recovery server

Go to Devices > All devices.

Select a device, and click Disaster recovery.

Edit the default settings of the recovery server.

The recovery server settings are described in the following table.

Setting



Default value

Description
CPU and RAM	auto	The number of virtual CPUs and the amount of RAM for the recovery server. The default settings will be automatically determined based on the original device CPU and RAM configuration.
Cloud network	auto	Cloud network to which the server will be connected. For details on how cloud networks are configured, see Cloud network infrastructure.
IP address in production network	auto	The IP address that the server will have in the production network. By default, the IP address of the original machine is set.
Test IP address	disabled	Test IP address gives you the capability to test a failover in the isolated test network and to connect to the recovery server via RDP or SSH during a test failover. In the test failover mode, the VPN gateway will replace the test IP address with the production IP address by using the NAT protocol. If a test IP address is not specified, the console will be the only way to access the server during a test failover.
Internet Access	enabled	Enable the recovery server to access the Internet during a real or test failover. By default, TCP port 25 is denied for outbound connections.
Use Public address	disabled	Having a public IP address makes the recovery server available from the Internet during a failover or test failover. If you do not use a public IP address, the server will be available only in your production network. The public IP address will be shown after you complete the configuration. By default, TCP port 443 is open for inbound connections.
Set RPO threshold	disabled	RPO threshold defines the maximum allowable time interval between the last recovery point and the current time. The value can be set within 15 – 60 minutes, 1 – 24 hours, 1 – 14 days.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.