---
title: "CyberFit Score for machines"
section: "Managing workloads in the Cyber Protect console"
subsection: "CyberFit Score for machines"
page_range: "456-462"
tags: [CyberFit Score, security assessment, scoring, antimalware, backup, firewall, VPN, encryption, NTLM]
acronis_version: "26.02"
---

# CyberFit Score for machines

CyberFit Score provides you with a security assessment and scoring mechanism that evaluates the security posture of your machine. It identifies security gaps in the IT environment and open attack vectors to endpoints and provides recommended actions for improvements in the form of a report. This feature is available in all Cyber Protect editions.

The CyberFit Score functionality is supported on:

- Windows 7 (first version) and later versions
- Windows Server 2008 R2 and later versions

## How it works

The protection agent that is installed on a machine performs a security assessment and calculates the CyberFit Score for the machine. The CyberFit Score of a machine is automatically periodically recalculated.

## CyberFit scoring mechanism

The CyberFit Score for a machine is calculated, based on the following metrics:

- Antimalware protection: 0-275
- Backup protection: 0-175
- Firewall: 0-175
- Virtual private network (VPN): 0-75
- Full disk encryption: 0-125
- Network security: 0-25

The maximum CyberFit Score for a machine is **850**.

## Scoring details by metric

| Metric | What is assessed? | Recommendations | Scoring |
|--------|------------------|-----------------|---------|
| **Antimalware** | The agent checks whether antimalware software is installed on a machine. | Findings: You have antimalware protection enabled (+275 points); You don't have antimalware protection, your system may be at risk (0 points). Recommendation: Have an antimalware solution installed and enabled. Refer to websites such as AV-Test or AV-Comparatives for recommended solutions. | 275 - antimalware software is installed; 0 - no antimalware software is installed |
| **Backup** | The agent checks if a backup solution is installed on a machine. | Findings: You have a backup solution protecting your data (+175 points); No backup solution was found, your data may be at risk (0 points). Recommendation: Back up your data regularly. Consider using Acronis Cyber Protect / Cyber Backup / True Image, or Windows Server Backup. | 175 - backup solution is installed; 0 - no backup solution is installed |
| **Firewall** | The agent checks whether a firewall is available and enabled. It checks Windows Firewall and Network Protection for public and private firewalls, and checks for 3rd party firewall solutions. | Findings: Public and private firewall enabled (+175 points); Public firewall only (+100 points); Private firewall only (+75 points); No firewall enabled (0 points). Recommendation: Enable firewall for public and private networks. | 175 - public and private firewall enabled OR a third-party firewall is enabled; 100 - Windows public firewall is enabled; 75 - Windows private firewall is enabled; 0 - neither a Windows firewall, nor a third-party firewall solution are enabled |
| **Virtual Private Network (VPN)** | The agent checks whether a VPN solution is installed on a machine and whether the VPN is enabled and running. | Findings: VPN solution found and safely receiving/sending data (+75 points); No VPN solution found (0 points). Recommendation: Use VPN to access your corporate network and confidential data, especially from public places. Consider: Acronis Business VPN, OpenVPN, Cisco AnyConnect, NordVPN, TunnelBear, ExpressVPN, PureVPN, CyberGhost VPN, Perimeter 81, VyprVPN, IPVanish VPN, Hotspot Shield VPN, Fortigate VPN, ZYXEL VPN, SonicWall GVPN, LANCOM VPN. | 75 - VPN is enabled and running; 0 - VPN is not enabled |
| **Disk encryption** | The agent checks whether a machine has disk encryption enabled (checks Windows BitLocker). | Findings: Full disk encryption enabled (+125 points); Only some hard drives are encrypted (+75 points); No disk encryption was found (0 points). Recommendation: Turn on Windows BitLocker to improve protection of your data and files. | 125 - all disks are encrypted; 75 - at least one disk is encrypted but there are also unencrypted disks; 0 - no disks are encrypted |
| **Network security (outgoing NTLM traffic)** | The agent checks whether a machine has restricted outgoing NTLM traffic to remote servers. | Findings: Outgoing NTLM traffic is denied, credentials are protected (+25 points); Outgoing NTLM traffic is not denied, credentials may be vulnerable (0 points). Recommendation: Deny all outgoing NTLM traffic to remote servers. Guide: Restrict outgoing NTLM traffic to remote servers. | 25 - outgoing NTLM traffic is set to DenyAll; 0 - outgoing NTLM traffic is set to another value |

## Score ratings

Based on the summed points awarded to each metric, the total CyberFit Score of a machine can fit one of the following ratings that reflect the endpoint's level of protection:

| Score range | Rating |
|-------------|--------|
| 0 - 579 | Poor |
| 580 - 669 | Fair |
| 670 - 739 | Good |
| 740 - 799 | Very good |
| 800 - 850 | Excellent |

You can see the CyberFit Score for your machines in the Cyber Protect console: go to **Devices** > **All devices**. In the list of devices, you can see the **#CyberFit Score** column. You can also run the CyberFit Score scan for a machine to check its security posture.

You can also get information about the CyberFit Score in the corresponding widget and report pages.

## Running a CyberFit Score scan

1. In the Cyber Protect console, go to **Devices**.
2. Select the machine and click **#CyberFit Score**.
3. If the machine has never been scanned before, then click **Run a first scan**.
4. After the scan is completed, you will see the total CyberFit Score for the machine along with the scores of each of the six assessed metrics -- Antimalware, Backup, Firewall, Virtual Private Network (VPN), Disk encryption, and NT LAN Manager (NTLM) traffic.
5. To check how to increase the score of each metric for which the security configurations could be improved, expand the corresponding section and read the recommendations.
6. After addressing the recommendations, you can always recalculate the CyberFit Score of the machine by clicking on the arrow button right under the total CyberFit Score.
