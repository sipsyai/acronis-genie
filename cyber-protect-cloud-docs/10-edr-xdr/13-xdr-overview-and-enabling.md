---
title: "Extended Detection and Response (XDR) Overview and Enabling"
section: "Extended Detection and Response (XDR)"
subsection: "Overview and Setup"
page_range: "1215-1216"
tags: [xdr, overview, enabling, integrations, microsoft-365, fortimail, advanced-security]
acronis_version: "26.02"
---

# Extended Detection and Response (XDR)

XDR is part of the Security and RMM protection pack, which in turn is part of the Cyber Protection service. You must enable Endpoint Detection and Response (EDR) functionality in a protection plan for XDR to work.

XDR uses EDR for event correlation and identifying advanced attacks on endpoints, and then extends that functionality by identifying advanced threats across endpoints, email, identity, and beyond.

By using the XDR graph across multiple XDR integrations (including FortiMail Workspace Security and Microsoft 365), you can also respond to incidents with specific actions available for each type of integration, such as blocking email senders or suspending users.

XDR is compatible with workstations, servers, virtual machines, and web hosting servers.

## Why You Need Extended Detection and Response (XDR)

MSPs offering security services previously had to choose between insufficient, incomplete protection, or costly and complex solutions. XDR overcomes these limitations by extending and enriching the functionality provided by EDR, identifying advanced threats across endpoints, email, identity, and beyond.

With an ever-growing attack surface (multiple customers in remote locations, a mix of on-premises and cloud-based workloads, and private and public clouds), security infrastructure gaps (due to a multitude of security tools deployed for different customers), and constantly evolving cyber threats (such as AI-based tools for attackers), the need for a unified solution is clear.

### Key Benefits

- **Extend protection**: Protect against sophisticated threats on client environments across vulnerable attack surfaces with extensive visibility covering endpoints, email, Microsoft Entra ID, and Microsoft 365 applications (such as SharePoint, OneDrive, and Teams). Enhanced visibility means faster detections than EDR alone can provide.
- **Natively integrate**: Easily integrate across cybersecurity, data protection, and endpoint management platforms. XDR is designed to protect vulnerable attack surfaces for unmatched business continuity.
- **Highly efficient with enhanced remediation**: Easily launch, manage, scale, and deliver security services. XDR includes AI-based incident analysis and single-click response for easy investigation and remediation, with AI-assisted and automatic remediation actions protecting against multi-stage and advanced cyber threats. Proactive security also enables technicians to identify and remediate potential issues before an attacker exploits them.

## Enabling Extended Detection and Response (XDR)

In order for XDR to work, the Endpoint Detection and Response (EDR) option must first be enabled in the relevant protection plans. This ensures that the **XDR: On/Off** option switch is displayed for customer tenants. If this option switch is not displayed, contact your partner administrator.

### Steps to Enable XDR

1. Ensure that EDR is enabled in your protection plans.
2. Go to **Protection > Incidents**.
3. In the top right of the screen, click **XDR: OFF**.
4. You are prompted to configure XDR integrations, which are required for XDR to protect your workloads. Click **Configure XDR integrations**.
   - If you have existing XDR integrations configured and want to add additional integrations, click **Add XDR integrations**.
   - You are automatically redirected to Management Portal, where you can select and configure the relevant XDR integrations.
5. When at least one XDR configuration is configured, the XDR option switch is enabled (**XDR: ON**), and you can start working with XDR.

### Supported Integrations

- **Microsoft 365**: Integrates with SharePoint, OneDrive, Teams, and Outlook for collaboration application monitoring.
- **FortiMail Workspace Security** (formerly Perception Point): Integrates for email security monitoring.
- **Microsoft Entra ID**: Integrates for identity management monitoring.
