# Preparing machines for remote installation manually

Installing and deploying Cyber Protection agents > Device discovery > Remote installation of agents > Preparing machines for remote installation manually
Preparing machines for remote installation manually
For successful installation on a remote machine running Windows 7 or later, the option Control panel > Folder options > View > Use Sharing Wizard must be disabled on that machine.
For successful installation on a remote machine that is not a member of an Active Directory domain, User Account Control (UAC) must be disabled on that machine. For more information on how to disable it, see "Requirements on User Account Control (UAC)" > To disable UAC.
By default, the credentials of the built-in administrator account are required for remote installation on any Windows machine. To perform remote installation by using the credentials of another administrator account, User Account Control (UAC) remote restrictions must be disabled. For more information on how to disable them, see "Requirements on User Account Control (UAC)" > To disable UAC remote restrictions.

File and Printer Sharing must be enabled on the remote machine. To access this option:

On a machine running Windows 2003 Server: go to Control panel > Windows Firewall > Exceptions > File and Printer Sharing.
On a machine running Windows Server 2008, Windows 7, or later: go to Control panel > Windows Firewall > Network and Sharing Center > Change advanced sharing settings.

Cyber Protection uses TCP ports 445, 25001, and 43234 for remote installation.

Port 445 is automatically opened when you enable File and Printer Sharing. Ports 43234 and 25001 are automatically opened through Windows Firewall. If you use a different firewall, make sure that these three ports are open (added to exceptions) for both incoming and outgoing requests.

After the remote installation is complete, port 25001 is automatically closed through Windows Firewall. Ports 445 and 43234 need to remain open if you want to update the agent remotely in the future. Port 25001 is automatically opened and closed through Windows Firewall during each update. If you use a different firewall, keep all the three ports open.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.