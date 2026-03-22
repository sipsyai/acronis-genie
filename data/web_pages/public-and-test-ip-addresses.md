# Public and test IP addresses

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Public and test IP addresses
Public and test IP addresses

If you assign the public IP address when creating a recovery server, the recovery server becomes available from the Internet through this IP address. When a packet comes from the Internet with the destination public IP address, the VPN gateway remaps it to the respective production IP address by using NAT, and then sends it to the corresponding recovery server.

If you assign the test IP address when creating a recovery server, the recovery server becomes available in the test network through this IP address. When you perform the test failover, the original machine is still running while the recovery server with the same IP address is launched in the test network in the cloud. There is no IP address conflict, as the test network is isolated. The recovery servers in the test network are reachable by their test IP addresses, which are remapped to the production IP addresses through NAT.

For more information about Site-to-site Open VPN, see Site-to-site Open VPN - Additional information.

IP address reconfiguration

Reassigning IP addresses

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.