# Network management in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Connectivity and networks in Microsoft Azure > Network management in Microsoft Azure
Network management in Microsoft Azure

Recovery networks are Azure Virtual Networks (VNets) and subnets where your backup systems (recovery servers) will run if your main systems fail.

There are two kinds of recovery networks: production recovery networks and test recovery networks.

Production recovery network

Production recovery networks are used during a real disaster when you need to move your services to Azure. Failovered workloads (VMs) are connected to these recovery networks so that business operations are resumed.

This is an example of a production network:

VNet: dr-prod-vnet-91a4e5bf

Subnet: subnet-one (10.0.10.0/24)

Test recovery network

Test recovery networks are used during manual or automated test failovers to verify that disaster recovery works without impacting your production systems.

To prevent IP conflicts or data leakage, test recovery networks must be isolated from the production environment. To avoid overlapping with production networks, it is best practice to use a dedicated VNet.

For more information about VNets planning and design, see the Microsoft Azure documentation.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.