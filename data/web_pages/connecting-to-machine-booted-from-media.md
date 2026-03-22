# Connecting to a machine booted from bootable media

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Connecting to a machine booted from bootable media
Connecting to a machine booted from bootable media
Local connection

To operate directly on the machine booted from bootable media, click Manage this machine locally in the startup window.

After a machine boots from bootable media, the machine terminal displays a startup window with the IP addresses obtained from DHCP or set according to the preconfigured values.

Configuring network settings

To change the network settings for a current session, in the startup window, click Configure network. The Network Settings window that appears allows you to configure the network settings for each network interface card (NIC) of the machine.

The changes that are made during a session will be lost after the machine reboots.

Adding VLANs

In the Network Settings window, you can add virtual local area networks (VLANs). Use this functionality if you need access to a backup location that is included in a specific VLAN.

VLANs are mainly used to divide a local area network into segments. A NIC that is connected to an access port of the switch always has access to the VLAN specified in the port configuration. A NIC connected to a trunk port of the switch can access the VLANs allowed in the port configuration only if you specify the VLANs in the network settings.

To enable access to a VLAN via a trunk port

Click Add VLAN.
Select the NIC that provides access to the local area network that includes the required VLAN.
Specify the VLAN identifier.

After you click OK, a new entry appears in the list of network adapters.

If you need to remove a VLAN, click the required VLAN entry, and then click Remove VLAN.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.