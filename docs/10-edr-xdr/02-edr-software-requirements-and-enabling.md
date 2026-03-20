---
title: "EDR Software Requirements and Enabling"
section: "Endpoint Detection and Response (EDR)"
subsection: "Setup and Configuration"
page_range: "1135-1138"
tags: [edr, software-requirements, enabling, protection-plan, configuration, supported-os]
acronis_version: "26.02"
---

# Software Requirements for Endpoint Detection and Response

Endpoint Detection and Response (EDR) supports the following operating systems:

## Supported Operating Systems

- **Microsoft Windows 7** Service Pack 1 and later
- **Microsoft Windows Server 2008 R2** and later
- **macOS** versions 13, 14, 15, 26
- **Linux OS versions**:
  - CentOS 7.x
  - Debian 10.x, 11.x
  - CloudLinux 7.x, 8.x
  - Ubuntu 16.04, 18.04, 20.04, and 22.04

## CPU Requirements

For endpoints running on Intel or AMD CPUs, EDR is supported only on processors that include the SSE4.2 instruction set:

- Intel CPUs released after 2011
- AMD CPUs released after 2012

# Enabling Endpoint Detection and Response (EDR) Functionality

You can enable EDR in any protection plan.

## Steps to Enable EDR

1. In the Cyber Protect console, go to **Management > Protection plans**.
2. Select the relevant protection plan from the displayed list, and in the right sidebar, click **Edit**. Alternatively, create a new protection plan and continue to the next step.
3. In the protection plan sidebar, enable the **Endpoint Detection and Response (EDR)** module by clicking the switch next to the module name.
4. In the displayed dialog, click **Enable**. Note that you can enable EDR and still disable any of the Antivirus & Antimalware, Active Protection and URL filtering functionality in the protection plan.
5. (Optional) To collect data for EDR events continuously, even when there are no particular detections, enable **Extended monitoring**. The collected data about security events is preserved for 180 days on the data center.

## Recommended Modules

When enabling EDR, it is recommended to also enable the following modules for best possible detection coverage:

- Antivirus & Antimalware protection
  - Real-time protection
  - Behavior engine
  - Exploit prevention
  - Potentially unwanted application
  - Active Protection
  - Network folder protection
  - Cryptomining process detection
- URL Filtering
- Microsoft Defender Antivirus (optional)

## Important Notes on Microsoft Defender Antivirus

If you enable **Microsoft Defender Antivirus** for real-time protection, the **Real-time protection** module is automatically disabled to prevent conflicts. Virus/malware detections and quarantine are handled by Microsoft Defender Antivirus, and any EDR incidents related to virus/malware detections are created from information provided by Microsoft Defender Antivirus. EDR includes other detection engines that can create other types of incidents without involvement from Microsoft Defender Antivirus.

Similarly, if you enable **Real-time protection**, the **Microsoft Defender Antivirus** module is automatically disabled.

Tamper protection settings in Windows must also be disabled to ensure Microsoft Defender Antivirus works correctly in Cyber Protect Cloud.

If **Behavior engine** or **Antivirus & Antimalware protection** are disabled in the protection plan when EDR is enabled, **Endpoint Detection and Response (EDR)** is also disabled.

## Licensing

If you do not have the required license, the licensing warning icon appears next to the toggle. The **Detection and Response** icon is added to the list of protection packs required for the implementation of the protection plan. If the licensing issue is not resolved, the EDR functionality will be disabled when the plan is applied to workloads.

# How to Use Endpoint Detection and Response (EDR)

The general workflow when working with EDR consists of three main steps:

| Step | Description |
|------|-------------|
| **Step 1: Review incidents** | In the EDR incident list: understand the security posture of an organization (how many incidents need to be investigated), understand which are the most critical incidents and prioritize their investigation according to severity, and understand which incidents are new or ongoing. |
| **Step 2: Investigate incidents** | In the EDR cyber kill chain: understand the objectives of the attacker and view the attack techniques used, verify how likely any incident is a true malicious attack, verify whether or not a threat feed is impacting a workload, and see what response actions have already been applied to an incident. |
| **Step 3: Remediate incidents** | In the relevant EDR remediation sections: quickly and easily remediate an entire incident by applying global response actions, remediate individual attack points within an incident, and apply actions to prevent the attack (or future attacks) from spreading or affecting workloads that have not yet been targeted by the attacker. |
