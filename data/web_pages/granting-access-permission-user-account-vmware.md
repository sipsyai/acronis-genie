# Granting access permission to the user account

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Granting access permission to the user account
Granting access permission to the user account

The user account that is used by Agent for VMware must have access to all levels of the vSphere infrastructure, such as vCenter, datacenters, clusters, ESXi hosts, resource pools, and virtual machines.

To grant access permission to the user account

In vSphere Client, go to Inventory.
Right-click the vCenter object for which you want to grant permission, and then click Add Permission.

In the Add Permission dialog, select a user account and a role.

The role must include the privileges that are listed in Required privileges for Agent for VMware.

Select the Propagate to children check box.
Click OK.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.