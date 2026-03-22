# Recommendations for the Active Directory Domain Services availability

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Connectivity and networks in Microsoft Azure > Recommendations for the Active Directory Domain Services availability
Recommendations for the Active Directory Domain Services availability

If your protected workloads need to authenticate in a domain controller, we recommend that you have an Active Directory Domain Controller (AD DC) instance at the DR site in Microsoft Azure.

Recommendations for AD DS availability in DR site in Azure

The recommendations for a dedicated AD DC instance on the DR site are the following:

Turn off Windows Firewall.

Join the AD DC to the Active Directory service.

Ensure that the Azure VM has Internet access.

Add the Active Directory feature.

Deploy at least one domain controller in the DR site in Azure

Recovered workloads need to authenticate, apply Group Policies, and resolve names. Deploy an additional domain controller VM in Azure in advance, before the failover.

Use a replicated domain controller (Not read-only)

Read-only domain controllers (RODCs) may not support all authentication scenarios after a failover. Deploy a writeable domain controller and replicate it with your on-premises AD forest.

Ensure proper DNS configuration

Recovered VMs must resolve domain names and locate domain controllers. Configure the recovery VNet to use the IP address of the Azure-based domain controller(s) as the custom DNS server.

Replicate SYSVOL and ensure time syncronization

Group Policies and domain operations rely on SYSVOL replication and correct time. Ensure that SYSVOL is synchronized and configure NTP or time synchronization settings for consistency between Azure and on-premises environments.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.