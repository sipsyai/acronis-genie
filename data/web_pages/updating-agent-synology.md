# Updating Agent for Synology

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Synology > Updating Agent for Synology
Updating Agent for Synology

You can update Agent for Synology 6.x to a newer version of Agent for Synology 6.x. Similarly, you can update Agent for Synology 7.x to a newer version of Agent for Synology 7.x.

To update the agent, run the newer version of the setup program in Synology DiskStation Manager. The original registration of the agent, its settings, and the plans that are applied to the protected workloads will be preserved.

You cannot update the agent from the Cyber Protect console.

Upgrading Agent for Synology 6.x to Agent for Synology 7.x is supported only by uninstalling the older agent and installing the newer agent. In this case, all protection plans are revoked and you must re-apply them manually.

Agent for Synology 7.x
Agent for Synology 6.x
Prerequisites
You are a member of the administrators group on the NAS device.
There are at least 200 MB of free space on the NAS volume on which you want to install the agent.
An SSH client is available on your machine. This document uses Putty as an example.

To update Agent for Synology

In DiskStation Manager, open Package Center.
Click Manual Install, and then click Browse.

Select the newer SPK file for Agent for Synology 7.x that you downloaded from the Cyber Protect console, and then click Next.

A warning that you will install a third-party software package is shown. This message is part of the standard installation procedure.

To confirm that you want to install the package, click Agree.
Check the settings, and then click Done.

In Synology DiskStation Manager Package Center, open Cyber Protect Agent for Synology, and then verify that you see the following screen.

In Synology DiskStation Manager Control Panel, go to Terminal & SNMP, and then enable the SSH access to the NAS device.

Run the install script on the NAS device by using an SSH client (in this example, Putty).

The script enables the root access to DSM 7.0 or later, which is required to configure the agent.

Start Putty, and then specify the IP address or host name of your Synology NAS device.

Click Open, and then log in as a Synology DSM administrator.

Run the following command.

sudo /var/packages/CyberProtectAgent/target/install/install

In Synology DiskStation Manager Control Panel, go to Terminal & SNMP, and then disable the SSH access to the NAS device. The SSH access is no longer required.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.