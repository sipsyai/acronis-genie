# Default cloud network infrastructure

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Creating a disaster recovery protection plan > Default cloud network infrastructure
Default cloud network infrastructure

The cloud network infrastructure that is created automatically when you apply a disaster recovery protection plan to your workloads consists of the following components:

A recovery server for each protected device.

The recovery server is a virtual machine in the cloud that is a copy of the selected device.

For each of the selected devices, a recovery server with default settings is created in the Standby state (virtual machine not running). The recovery server is sized automatically depending on the CPU and RAM of the protected device.

VPN gateway on the cloud site.
Cloud networks to which the recovery servers are connected.

The system checks devices IP addresses and if there are no existing cloud networks where an IP address fits, it automatically creates suitable cloud networks. If you already have existing cloud networks where the recovery servers IP addresses fit, the existing cloud networks will not be changed or recreated.

If you do not have existing cloud networks or you setup disaster recovery configuration for the first time, the cloud networks will be created with maximum ranges recommended by IANA for private use (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) based on your devices IP address range. You can narrow your network by editing the network mask.
If you have devices on multiple local networks, the network on the cloud site may become a superset of the local networks. You may reconfigure networks in the Connectivity section. See Managing networks for Site-to-site Open VPN.
If you need to set up Site-to-site Open VPN connectivity, download the VPN appliance and configure it. See Configuring Site-to-site Open VPN. Make sure your cloud network ranges match your local network ranges connected to the VPN appliance.
To change the default network configuration, navigate to Disaster Recovery > Connectivity, or on the Disaster recovery module of the protection plan, click Go to connectivity.

If you revoke, delete, or turn off the Disaster recovery module of a protection plan, the recovery servers and cloud networks will not be deleted automatically. You can remove the disaster recovery infrastructure manually, if necessary.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.