# Configuring Site-to-site Open VPN

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Configuring Site-to-site Open VPN
Configuring Site-to-site Open VPN
The availability of this feature depends on the service quotas that are enabled for your account.
Requirements for the VPN appliance
System requirements
1 CPU
1 GB RAM
8 GB disk space
Ports
TCP 443 (outbound) – for VPN connection
TCP 80 (outbound) – for automatic update of the appliance

Ensure that your firewalls and other components of your network security system allow connections through these ports to any IP address.

Configuring a Site-to-site Open VPN connection

The VPN appliance extends your local network to the cloud through a secure VPN tunnel. This kind of connection is often referred to as a "Site-to-site" (S2S) connection. You can follow the procedure below or watch the video tutorial.

To configure a connection through the VPN appliance

In the Cyber Protect console, go to Disaster Recovery > Connectivity.

Select Site-to-site Open VPN connection, and click Configure.

The system starts deploying the VPN gateway in the cloud. This will take some time. Meanwhile, you can proceed to the next step.

The VPN gateway is provided without additional charge. It will be deleted if the Disaster Recovery functionality is not used, i.e. no primary or recovery server is present in the cloud for seven days.

In the VPN appliance block, click Download and deploy, and then, depending on the virtualization platform you are using, download the VPN appliance.

Option	Description
VMware	VPN appliance image for vSphere.


Hyper-V

VPN appliance image for Hyper-V.
KVM/QEMU	VPN appliance image for KVM/QEMU-based hypervisors, including Proxmox, Virtuozzo Infrastructure, and Scale Computing.

Deploy the appliance and connect it to the production networks.

[For VMware] In vSphere, ensure that Promiscuous mode and Forged transmits are enabled and set to Accept for all virtual switches that connect the VPN appliance to the production networks. To access these settings, in vSphere Client, select the host > Summary > Network, and then select the switch > Edit settings... > Security.

[For Hyper-V] In Hyper-V, create a Generation 1 virtual machine with 1024 MB of memory. Also, we recommend that you enable Dynamic Memory for the machine. Once the machine is created, go to Settings > Hardware > Network Adapter > Advanced Features and select the Enable MAC address spoofing check box.

Power on the appliance.
Open the appliance console and log in with the "admin"/"admin" user name and password.
[Optional] Change the password.
[Optional] Change the network settings if needed. Define which interface will be used as the WAN for Internet connection.

Register the appliance in the Cyber Protection service by using the credentials of the company administrator.

These credentials are only used once to retrieve the certificate. The data center URL is predefined.

If two-factor authentication is configured for your account, you will also be prompted to enter the TOTP code. If two-factor authentication is enabled but not configured for your account, you cannot register the VPN appliance. First, you must go to the Cyber Protect console login page and complete the two-factor authentication configuration for your account. For more details on two-factor authentication, go to the Management Portal Administrator guide.

Once the configuration is complete, the appliance will have the Online status. The appliance connects to the VPN gateway and starts to report information about networks from all active interfaces to the Disaster Recovery service. The Cyber Protect console shows the interfaces, based on the information from the VPN appliance.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.