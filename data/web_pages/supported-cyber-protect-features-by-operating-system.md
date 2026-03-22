# Supported protection features by operating system

Getting started with Cyber Protection > Supported protection features by operating system
Supported protection features by operating system

This topic contains information about the protection features of Cyber Protect Cloud. For the list of operating systems and environments supported by backup and recovery, see Supported operating systems and environments for backup and recovery.

The protection features are only supported on machines on which a protection agent is installed. They are not available for virtual machines that are backed up in the agentless mode, for example, by Agent for Hyper-V, Agent for VMware, Agent for Virtuozzo Hybrid Infrastructure, Agent for Scale Computing, or Agent for oVirt.

Some features might require additional licensing, depending on the applied licensing model.

Supported operating systems and versions
Windows
Linux
macOS

Unless stated otherwise for a specific feature set, the following Windows versions are supported:

Windows 7 Service Pack 1 and later
Windows Server 2008 R2 Service Pack 1 and later

For Windows 7, you must install the following updates from Microsoft before installing the protection agent:

Windows 7 Extended Security Updates (ESU)
KB4474419
KB4490628

For more information on the required updates, see this knowledge base article.

Feature	Windows	Linux	macOS
Default protection plans
Remote Workers	Yes	No	No
Office Workers (third-party antivirus)	Yes	No	No
Office Workers (Cyber Protect antivirus)	Yes	No	No
Cyber Protect Essentials (only for Cyber Protect Essentials edition)	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Forensic backup
Collecting memory dump	Yes	No	No
Snapshot of running processes	Yes	No	No
Notarization of local image forensic backup	Yes	No	No
Notarization of cloud image forensic backup	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Continuous data protection (CDP)
CDP for files and folders	Yes	No	No
CDP for changed files via application tracking	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Autodiscovery and remote installation
Network-based discovery	Yes	No	No
Active Directory-based discovery*	Yes	No	No
Template-based discovery (importing machines from a file)	Yes	No	No
Manual adding of devices	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

*Active Directory-based discovery does not operate as expected with the default configuration of Windows Server 2025 because it enforces LDAP encryption by default. See this knowledge base article.

Active Protection
Feature	Windows	Linux	macOS
Process Injects detection	Yes	No	No
Automatic recovery of affected files from the local cache	Yes	Yes	Yes
Self-defense for Acronis backup files	Yes	No	No
Self-defense for Acronis software	Yes	No

Yes

(Only Active Protection and antimalware components)


Trusted/blocked process management	Yes	No	Yes
Processes/folders exclusions	Yes	Yes	Yes
Ransomware detection based on a process behavior (AI-based)	Yes	Yes	Yes
Cryptomining process detection based on process behavior	Yes	No	No
External drives protection (HDD, flash drives, SD cards)	Yes	No	Yes
Network folder protection	Yes	No*	Yes
Server-side protection	Yes	No	No
Zoom, Cisco Webex, Citrix Workspace, and Microsoft Teams protection	Yes	No	No


*Network folders in Linux are treated as local folders, hence Active Protection will automatically protect network folders in Linux OS, as if they are local folders.

For more information about the supported operating systems and their versions, see Supported operating systems for antivirus and antimalware protection.

Antivirus and Antimalware protection
Feature	Windows	Linux	macOS
Fully-integrated Active Protection functionality	Yes	No	No
Real-time antimalware protection	Yes

Yes



Yes


Advanced real-time antimalware protection with local signature-based detection	Yes

Yes



Yes


Static analysis for portable executable files	Yes	No

Yes1


On-demand antimalware scanning	Yes

Yes2



Yes


Network folder protection	Yes

No3

No
Server-side protection	Yes	No	No
Scan of archive files	Yes	No

Yes


Scan of removable drives	Yes	No

Yes


Scan of new and changed files only	Yes	No

Yes


File/folder exclusions	Yes

Yes



Yes4


Processes exclusions	Yes	No	Yes
Behavioral analysis engine	Yes	Yes5

Yes


Exploit prevention	Yes	No	No
Quarantine	Yes	Yes	Yes
Quarantine auto clean-up	Yes	Yes	Yes
URL filtering (http/https)	Yes	No	No
Corporate-wide whitelist	Yes	No

Yes


Firewall management6	Yes	No	No
Microsoft Defender Antivirus management7	Yes	No	No
Microsoft Security Essentials management	Yes	No	No
Registering and managing Antivirus and Antimalware protection via Windows Security Center	Yes	No	No


1 Static analysis for portable executable files is supported only for scheduled scans on macOS.

2 Start conditions are not supported for on-demand scanning on Linux.

3 Network folders in Linux are treated as local folders, hence Active Protection will automatically protect network folders in Linux OS, as if they are local folders.

4 File/folder exclusions are only supported for the case when you specify files and folders that will not be scanned by real-time protection or scheduled scans on macOS.

5 The Behavioral analysis engine supports the following Linux versions:

CentOS 7.x
Debian 10.x, 11.x
CloudLinux 7.x, 8.x
Ubuntu 16.04, 18.04, 20.04, and 22.04

6 Firewall management is supported on Windows 8 and later. Windows Server is not supported.

7 Microsoft Defender Antivirus management is supported on Windows 8.1 and later.

For more information about the supported operating systems and their versions, see Supported operating systems for antivirus and antimalware protection.

Feature	Windows	Linux	macOS
Endpoint detection and response
Endpoint detection and response1	Yes	Yes	Yes
Extended monitoring	Yes	Yes	No


1See EDR features.

For more information about the supported operating systems and their versions, see Software requirements for Endpoint Detection and Response.

Feature	Windows	Linux	macOS
Vulnerability assessment
Vulnerability assessment of operating system and its native applications	Yes	Yes*	Yes
Vulnerability assessment for 3rd-party applications	Yes	No	Yes


For more information about the supported operating systems and their versions, see Supported Microsoft and third-party products for vulnerability assessment, Supported Linux products for vulnerability assessment, and Supported Apple and third-party products for vulnerability assessment.

* The vulnerability assessment depends on the availability of official security advisories for specific distribution, for example https://lists.centos.org/pipermail/centos-announce, https://lists.centos.org/pipermail/centos-cr-announce, and others.

Feature	Windows	Linux	macOS
Patch management
Patch auto-approval	Yes	No	No
Patch auto-installation	Yes	No	No
Patch testing	Yes	No	No
Manual patch installation	Yes	No	No
Patch scheduling	Yes	No	No
Fail-safe patching: backup of machine before installing patches as part of protection plan	Yes	No	No
Cancelation of a machine reboot if a backup is running	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Data protection map
Adjustable definition of important files	Yes	No	No
Scanning machines to find unprotected files	Yes	No	No
Unprotected locations overview	Yes	No	No
Ability to start the protection action from the Data protection map widget (Protect all files action)	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Disk health
AI-based HDD and SSD health control	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Smart protection plans based on Acronis Cyber Protection Operations Center (CPOC) alerts
Threat feed	Yes	No	No
Remediation wizard	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Backup scanning
Antimalware scan of image backups as part of backup plan	Yes	No	No
Scanning of image backups for malware in cloud	Yes	No	No
Malware scan of encrypted backups	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Safe recovery
Antimalware scanning with Antivirus and Antimalware protection during the recovery process	Yes	No	No
Safe recovery for encrypted backups	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Remote desktop connection
Connection via NEAR	Yes	Yes	Yes
Connection via RDP	Yes	No	No
Connection via Apple Screen Sharing	No	No	Yes
Connection via web client	Yes	No	No
Connection via Quick Assist	Yes	Yes	Yes
Remote assistance	Yes	Yes	Yes
File transfer	Yes	Yes	Yes
Screenshot transmission	Yes	Yes	Yes


For more information about the supported operating systems and their versions, see Supported operating systems for remote desktop and assistance.

Feature	Windows	Linux	macOS
#CyberFit Score
#CyberFit Score status	Yes	No	No
#CyberFit Score standalone tool	Yes	No	No
#CyberFit Score recommendations	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

Feature	Windows	Linux	macOS
Data loss prevention
Device control	Yes	No

Supported on Macs with Intel processors running macOS 10.15 and later or macOS 11.2.3 or later.

Not supported on ARM-based Apple silicon processors, such as Apple M1 / M2.


Data Loss Prevention	Yes	No	No
See the supported Windows versions in the beginning of this section (Supported operating systems and versions).
Feature	Windows	Linux	macOS
Management options
Upsell scenarios to promote Cyber Protect editions	Yes	Yes	Yes
Web-based centralized and remote management console	Yes	Yes	Yes
Supported operating systems and versions: Platform independent.
Feature	Windows	Linux	macOS
Protection options
Remote wipe

Yes

No	No
Supported for Windows 10 and later.
Feature	Windows	Linux	macOS
Cyber Protect Monitor
Cyber Protect app	Yes	No	Yes
Protection status for Zoom	Yes	No	No
Protection status for Cisco Webex	Yes	No	No
Protection status for Citrix Workspace	Yes	No	No
Protection status for Microsoft Teams	Yes	No	No


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

On macOS, Cyber Protect Monitor is supported for all versions on which you can install Agent for Mac, except macOS 10.x. For more information, see Agent for Mac.

Feature	Windows	Linux	macOS
Software inventory
Software inventory scanning	Yes	No	Yes
Software inventory monitoring	Yes	No	Yes


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

On macOS, Software inventory is supported for versions 10.13.x − 13.x.

Feature	Windows	Linux	macOS
Hardware inventory
Hardware inventory scanning	Yes	No	Yes
Hardware inventory monitoring	Yes	No	Yes


See the supported Windows versions in the beginning of this section (Supported operating systems and versions).

On macOS, Hardware inventory is supported for versions 10.13.x − 13.x.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.