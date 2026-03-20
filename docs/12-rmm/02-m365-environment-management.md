---
title: "Managing and Monitoring the Microsoft 365 Environment"
section: "RMM"
subsection: "Microsoft 365 Management"
page_range: "1237-1242"
tags: [rmm, microsoft-365, m365, security-posture, connections, customer-mapping, risk-dashboard, baselines]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#m365-overview.html"
---

# Managing and Monitoring the Microsoft 365 Environment

Under service-based licensing, this functionality is part of the paid offering RMM - Microsoft 365 seats. The functionality includes continuous auditing of the Microsoft 365 security posture with best practice baselines, remediation of baseline deviations and user risks, and user onboarding and offboarding. Under solution-based licensing, the complete functionality is included in the Security and RMM and the Ultimate Protection license, under the Microsoft 365 seats offering. A charge is applied for each user allocated with an Exchange Online mailbox license.

The Microsoft 365 security monitoring and management service enables you to:

- Easily onboard Microsoft 365 customer tenants to Cyber Protect Cloud
- Provide a continuous audit of customers' Microsoft 365 security posture
- Monitor breaches and risks with best practice Microsoft 365 baseline templates
- Remediate baseline deviations (in one-click) and security control misconfigurations
- Monitor and manage Microsoft 365 user risks
- Onboard and offboard Microsoft 365 users

## Configuring Microsoft 365 Connections

This feature is only available for Partner administrator users. When Microsoft 365 security monitoring and management is enabled in Cyber Protect, you can connect to the relevant Microsoft 365 clients associated with your (or your customer's) Microsoft account. You can then map the Microsoft 365 tenants to the relevant customers in Cyber Protect.

### Connecting to a Microsoft CSP Account

1. In the Cyber Protect console, go to **M365 management > Configuration**.
2. Click **Connect Microsoft account**. You are redirected to the Microsoft login page.
3. Sign in to the Microsoft account with your CSP credentials, and accept the permissions requested by Acronis. The permissions are for the **Octiga Multi-Tenant Security** enterprise application registered in Entra ID, connected with the service provider's Microsoft 365 tenant.
4. In the displayed **Customer mapping** tab, map the Microsoft 365 clients with the relevant customers in Cyber Protect Cloud.

When you log in to your Microsoft CSP account, the system automatically retrieves all customer tenants associated with the CSP account.

### Connecting to a Regular Microsoft Account

1. In the Cyber Protect console, go to **M365 management > Configuration**.
2. Click **Connect Microsoft account**. You are redirected to the Microsoft login page.
3. Sign in to the Microsoft account, and accept the permissions requested by Acronis. The permissions are for the **Octiga Multi-Tenant Security** enterprise application registered in the Entra ID account of the partner tenant.
4. Click **Add customer's Microsoft account**. You are prompted to sign in with the relevant customer account credentials. The permissions are for the **Octiga Cloud Security** enterprise application registered in the Entra ID account of the customer tenant.
5. In the displayed **Customer mapping** tab, map the Microsoft 365 clients with the relevant customers.
6. (Optional) Repeat the above steps for additional customer Microsoft accounts.

When onboarding tenants with a large number of users (over 1000), the system might take some time to retrieve all details, as each user needs to be verified and some Microsoft APIs can only be triggered once every two seconds.

## Customer Mapping

After onboarding of Microsoft 365 tenants in Cyber Protect Cloud is completed, you can map the Microsoft 365 tenants associated with that account to customers in Cyber Protect Cloud.

1. In the Cyber Protect console, go to **Microsoft 365 management > Configuration**.
2. In the **Customer mapping** tab, select the relevant Microsoft 365 tenant(s), and then click **Map to existing customer**.
3. Select the relevant customer from the dropdown, and click **Map**.

When successfully mapped:
- **Mapped** status is shown in the **Mapping status** column
- The system applies the predefined tenant baselines to the customer tenant
- Security posture monitoring starts and runs for the customer tenant

To remove the mapping, select the tenant(s) and click **Remove mapping**. When mapping is removed, the Microsoft 365 security monitoring and management service is automatically disabled for the selected customer(s).

## Disabling the Microsoft 365 Management Service

1. In the Cyber Protect console, go to **Microsoft 365 management > Configuration**.
2. Click the **Settings** tab, and then click **Disable service**.
3. In the confirmation dialog, click **Disable**. Disabling removes the connected Acronis application from the App registrations directory and all customer-related data stored on Cyber Protect Cloud.

## Reviewing Security Posture

Partner administrators can review the security posture of multiple Microsoft 365 tenants in one dashboard. Access this at **Microsoft 365 management > Security posture**.

The **Security posture** screen displays for each Microsoft 365 tenant:
- Tenant name
- Tenant baselines (with number of deviations if relevant)
- Users (the number of users)
- Mailboxes (the number of mailboxes)

At the top of the screen, icons indicate the total number of tenants with deviations and the total number of deviations across all tenants.

## Reviewing the Risk Dashboard

The Risk dashboard highlights any risks (or deviations) to a Microsoft 365 tenant's baselines, baseline categories, and user accounts. Access it by clicking the tenant row in the Security posture screen.

The Risk dashboard includes:

### Baselines
- Tenant baselines (passed and deviated counts)

### Baseline Categories
Each category shows passed and deviated counts:
- Audit
- Email Security
- Authentication & Authorization
- Sharing
- Remote Access

### User Account Risks
- **MFA**: User accounts where MFA is disabled or not enrolled
- **Admin mailboxes**: Global administrator accounts with a mailbox
- **Anonymous admins**: Possible shared administrator accounts
- **Shared mailboxes**: User accounts with shared mailboxes
- **Dormant accounts**: Users not logged in for three months
- **Dormant admins**: Administrator accounts not logged in for six months
- **Guests**: Guest user accounts
