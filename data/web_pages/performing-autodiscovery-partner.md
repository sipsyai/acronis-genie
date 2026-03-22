# Performing autodiscovery of machines at the partner level

Managing workloads in the Cyber Protect console > The Cyber Protect console > Administration levels in the Cyber Protect console > Performing autodiscovery of machines at the partner level
Performing autodiscovery of machines at the partner level

You can perform autodiscovery of machines at the partner level (All customers).

Prerequisites

There is at least one machine with an installed protection agent in your customer's local network or Active directory domain.

Only agents that are installed on Windows machines can be discovery agents. If there are no discovery agents in your customer's environments, you will not be able to use the Multiple devices option in the Add devices panel.

Autodiscovery is not supported for adding Domain Controllers, due to additional permissions required for the agent service to run.

Remote installation of agents is supported only for machines running Windows (Windows XP is not supported). For remote installation on a machine running Windows Server 2012 R2, Windows update KB2999226 must be installed.

To perform autodiscovery of machines at the partner tenant level

Search Active Directory
Scan local network
Manually or by importing a file

To add multiple devices from the Active Directory

In the Cyber Protect console, go to Devices > All devices.
Click Add.

In Multiple devices, click Discover devices.

The discovery wizard opens.

Select a customer tenant, and then select the discovery agent that will perform the scan to detect machines.

A discovery agent is a workload on which a protection agent is installed.

The discovery agent must be a member of the Active Directory domain.

You can select an agent that is associated with the selected tenant.

Select Search Active Directory, and then click Next.

In the Search Active Directory window, select how to search for the machines, and then click OK.

Option	Description


In organizational unit list

Select the group of machines to be added.
By LDAP dialect query.	Use the LDAP dialect query to select the machines. Search base defines where to search, while Filter allows you to specify the criteria for machine selection.

In the list of discovered machines, select the machines that you want to add, and then click Next.

The Select onboarding option tab opens. The following onboarding options are available.

Option	Description
Complete automatic onboarding via Active Directory

This option uses a domain controller on which a discovery agent is installed to onboard discovered devices from Active Directory. No manual preconfiguration of the devices is required.


Manual preconfiguration and automatic onboarding

This option requires manual preconfiguration of the devices and uses a discovery agent to onboard discovered devices.


Add as unmanaged machines

This option adds the discovered devices to the console as unmanaged devices, without installing a protection agent on them.

Depending on the onboarding option that you will select, do the following:

If you selected Complete automatic onboarding via Active Directory, complete steps 4-13 from the corresponding procedure.
If you selected Manual preconfiguration and automatic onboarding, complete steps 4-11 from the corresponding procedure.
If you selected Add as unmanaged machines, select the user account under which to register the devices, and then click Add.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.