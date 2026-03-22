# Adding multiple devices

Installing and deploying Cyber Protection agents > Device discovery > Discovering multiple devices > Adding multiple devices
Adding multiple devices

Before adding multiple devices, ensure that the requirements are met. For more information, see Device discovery requirements.

The functionality is not supported for adding domain controllers due to additional permissions required for the agent service to run.
Search Active Directory
Scan local network
Manually or by importing a file

To add multiple devices from the Active Directory

In the Cyber Protect console, go to Devices > All devices.
Click Add.

In Multiple devices, click Discover devices.

The discovery wizard opens.

Select the discovery agent that will perform the scan to detect machines.

A discovery agent is a workload on which a protection agent is installed.

The discovery agent must be a member of the Active Directory domain.

You can select an agent that is associated with the selected unit or its child units.

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

Requirements on User Account Control (UAC)

Agent components




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.