# Troubleshooting IPsec VPN configuration issues

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Troubleshooting IPsec VPN configuration issues
Troubleshooting IPsec VPN configuration issues
The availability of this feature depends on the service quotas that are enabled for your account.

The following table describes the IPsec VPN configuration problems that occur most often, and explains how to troubleshoot them.

Problem	Possible solution
I see the following error message: IKE phase 1 negotiation error. Check the IPsec IKE settings on the Cloud and the Local sites.

Click Retry and check if a more specific error message appears. For example, a more specific error message may be an error message about an algorithm mismatch or an incorrect Pre-shared key.

For security reasons, the following restrictions apply to the IPsec VPN connectivity:

IKEv1 is called for deprecation in RFC8247 and is not supported due to security risks. Only IKEv2 protocol connections are supported.

The following Encryption algorithms are not considered secure and are not supported: DES, and 3DES.

The following Hash algorithms are not considered secure and are not supported: SHA1, and MD5.

Diffie-Hellman group number 2 is not considered secure and is not supported.


The connection between my local site and the cloud site stays in status Connecting.

Check:

If the UDP port 500 is open (when you use a firewall).

The connectivity between the local site and the cloud site.

If the IP address of the local site is correct.




The connection between my local site and the cloud site stays in status Waiting for a connection.



You see this status when the Startup action for cloud site is set to Add, which means that the cloud site is waiting for the local site to initiate the connection.

Initiate connection from the local site.


The connection between my local site and the cloud site stays in status Waiting for traffic.

You see this status when the Startup action for cloud site is set to Route.

If you are expecting a connection from the local site, do the following:

From the local site, try to ping the virtual machine in the cloud site. This is a standard behavior necessary for establishing a tunnel for some devices, for example Cisco ASA. (Route mode)

Ensure that the local site established a tunnel by setting the Startup action of the local site to Start.




The connection between my local site and the cloud site is established, but I can see that one or more of the network policies are down.



This issue may be due to the following reasons:

Network mapping in the cloud IPsec site is different from the network mapping in the local site.

Ensure that the network mappings and the sequence of the network policies in the local and cloud sites match exactly.

This state is correct when the Startup action of the local site and/or of the cloud site is set to Route (for example, on Cisco ASA devices), and currently there is no traffic. You can try to ping to make sure that the tunnel is established. If the ping is not working, check the network mapping on the local and the cloud site.


I want restart a specific IPsec connection.

To restart a specific IPsec connection:

In the Disaster recovery > Connectivity screen, click the IPsec connection.

Click Disable connection.

Click the IPsec connection again.

Click Enable connection.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.