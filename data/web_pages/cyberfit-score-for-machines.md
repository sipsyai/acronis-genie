# #CyberFit Score for machines

Managing workloads in the Cyber Protect console > #CyberFit Score for machines
#CyberFit Score for machines

#CyberFit Score provides you with a security assessment and scoring mechanism that evaluates the security posture of your machine. It identifies security gaps in the IT environment and open attack vectors to endpoints and provides recommended actions for improvements in the form of a report. This feature is available in all Cyber Protect editions.

The #CyberFit Score functionality is supported on:

Windows 7 (first version) and later versions
Windows Server 2008 R2 and later versions
How it works

The protection agent that is installed on a machine performs a security assessment and calculates the #CyberFit Score for the machine. The #CyberFit Score of a machine is automatically periodically recalculated.

#CyberFit scoring mechanism

The #CyberFit Score for a machine is calculated, based on the following metrics:

Antimalware protection 0-275
Backup protection 0-175
Firewall 0-175
Virtual private network (VPN) 0-75
Full disk encryption 0-125
Network security 0-25

The maximum #CyberFit Score for a machine is 850.

Metric	What is assessed?	Recommendations to users	Scoring
Antimalware	The agent checks whether antimalware software is installed on a machine.

Findings:

You have antimalware protection enabled (+275 points)
You don’t have antimalware protection, your system may be at risk (0 points)

Recommendations provided by #CyberFit Score:

You should have an antimalware solution installed and enabled on your machine to stay protected from security risks.

You should refer to websites such as AV-Test or AV-Comparatives for a list of recommended antimalware solutions.



275 - antimalware software is installed on a machine

0 - no antimalware software is installed on a machine


Backup

The agent checks if a backup solution is installed on a machine.





Findings:

You have a backup solution protecting your data (+175 points)
No backup solution was found, your data may be at risk (0 points)

Recommendations provided by #CyberFit Score:

We recommend that you back up your data regularly to prevent data loss or ransomware attacks. Below are some backup solutions that you should consider using:

Acronis Cyber Protect / Cyber Backup / True Image
Windows Server Backup (Windows Server 2008 R2 and later)


175 - a backup solution is installed on a machine

0 - no backup solution is installed on a machine


Firewall

The agent checks whether a firewall is available and enabled in your environment.

The agent does the following:

1. Checks Windows Firewall and Network Protection whether a public firewall is turned on.

2. Checks Windows Firewall and Network Protection whether a private firewall is turned on.

3. Checks for a 3-rd party firewall solution/agent if Windows public and private firewalls are disabled.



Findings:

You have a firewall enabled for public and private networks, or a 3-rd party firewall solution is found (+175 points)
You have a firewall enabled only for public networks (+100 points)
You have a firewall enabled only for private networks (+75 points)
You have no firewall enabled, your network connection is not secure (0 points)

Recommendations provided by #CyberFit Score:

We recommend that you enable firewall for your public and private networks to improve your security protection against malicious attacks on your system. Below, detailed guides are provided on setting-up your Windows firewall, depending on your security needs and network architecture:

Guides for end-users/employees:

How to set up Windows Defender Firewall on your PC

How to set up Windows Firewall on your PC

Guides for system administrators and engineers:

How to deploy Window Defender Firewall with Advanced Security

How to create Advanced Rules in Windows Firewall



100 - Windows public firewall is enabled

75 - Windows private firewall is enabled

175 - Windows public and private firewall are enabled
OR
a third-party firewall solution is enabled

0 - neither a Windows firewall, nor a third-party firewall solution are enabled


Virtual Private Network (VPN)	The agent checks whether a VPN solution is installed on a machine and whether the VPN is enabled and running.

Findings:

You have a VPN solution and can safely receive and send data across public and shared networks (+75 points)
No VPN solution was found, your connection to public and shared networks is not secure (0 points)

Recommendations provided by #CyberFit Score:

We recommend that you use VPN to access your corporate network and confidential data. It is critical to use a VPN to keep your communications safe and private, especially if you use complimentary Internet access from a cafe, library, airport, or elsewhere. Below are some VPN solutions that you should consider using:

Acronis Business VPN
OpenVPN
Cisco AnyConnect
NordVPN
TunnelBear
ExpressVPN
PureVPN
CyberGhost VPN
Perimeter 81
VyprVPN
IPVanish VPN
Hotspot Shield VPN
Fortigate VPN
ZYXEL VPN
SonicWall GVPN
LANCOM VPN


75 - VPN is enabled and running

0 - VPN is not enabled


Disk encryption

The agent checks whether a machine has disk encryption enabled.

The agent checks whether Windows BitLocker is turned on.



Findings:

You have full disk encryption enabled, your machine is protected against physical tampering (+125 points)
Only some hard drives are encrypted, your machine may be at risk from physical tampering (+75 points)
No disk encryption was found, your machine is at risk from physical tampering (0 points)

Recommendations provided by #CyberFit Score:

We recommend that you turn on Windows BitLocker to improve protection of your data and files.

Guide: How to turn on device encryption on Windows



125 - all disks are encrypted

75 - at least one of your disks is encrypted but there are also unencrypted disks

0 - no disks are encrypted


Network security (outgoing NTLM traffic to remote servers)	The agent checks whether a machine has restricted outgoing NTLM traffic to remote servers.

Findings:

Outgoing NTLM traffic to remote servers is denied, your credentials are protected (+25 points)
Outgoing NTLM traffic to remote servers is not denied, your credentials may be vulnerable to exposure (0 points)

Recommendations provided by #CyberFit Score:

For better security protection, we recommend that you deny all outgoing NTLM traffic to remote servers. You can find information on how to change the NTLM settings and add exceptions by following the link below.

Guide: Restrict outgoing NTLM traffic to remote servers



25 - outgoing NTLM traffic is set to DenyAll

0 - outgoing NTLM traffic is set to another value

Based on the summed points awarded to each metric, the total #CyberFit Score of a machine can fit one of the following ratings that reflect the endpoint's level of protection:

0 - 579 - Poor
580 - 669 - Fair
670 - 739 - Good
740 - 799 - Very good
800 - 850 - Excellent

You can see the #CyberFit Score for your machines in the Cyber Protect console: go to Devices > All devices. In the list of devices, you can see the #CyberFit Score column. You can also run the #CyberFit Score scan for a machine to check its security posture.

You can also get information about the #CyberFit Score in the corresponding widget and report pages.

Running a #CyberFit Score scan

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.