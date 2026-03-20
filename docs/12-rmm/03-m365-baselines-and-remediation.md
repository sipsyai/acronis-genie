---
title: "Microsoft 365 Baselines, Templates, and Remediation"
section: "RMM"
subsection: "Microsoft 365 Baselines"
page_range: "1243-1255"
tags: [rmm, microsoft-365, baselines, security-posture, remediation, auto-remediation, tenant-baselines, templates, conditional-access, email-security, intune]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#m365-baseline-remediation.html"
---

# Working with Baselines

Microsoft 365 management enables you to monitor the status of all applied tenant baselines. Access the baselines functionality at **Microsoft 365 management > Baselines**.

## Monitoring Tenant Baselines

1. In the Cyber Protect console, go to **Microsoft 365 management > Baselines**.
2. (Optional) Select a tenant from the **Tenant** dropdown. You can also filter the list by category name.
3. In the list of baselines, you can:
   - Browse the status (**Passed** or **Deviated**) of all baselines applied to the selected tenant
   - Verify if the auto remediation option is enabled
   - View more details about a baseline by clicking on the relevant baseline row:
     - View the baseline description
     - View the current and required values of the baseline configuration
     - Define auto-remediation: Click **Enable auto-remediation** or **Disable auto-remediation**
     - Remediate the baseline deviation manually

## Tenant Baselines

The following table lists the currently supported Microsoft 365 tenant baselines by category:

### Audit
| Baseline | Description |
|----------|-------------|
| Mailbox Audit Log | Enable mailbox audit logs for the entire organization |
| Unified Audit Log | Enable or disable the audit log for the entire organization |

### Authentication and Authorization
| Baseline | Description |
|----------|-------------|
| Admin Consent Workflow | Allow users to request approval for apps requiring admin-level permissions |
| Authentication Method Policy - Email OTP | Email OTP for authentication, usable for Self-Service Password Recovery and guest sign-in |
| Authentication Method Policy - Microsoft Authenticator | Microsoft Authenticator app for passwordless or push notification authentication |
| Conditional Access Policy - Application of Enforced Restrictions for Unmanaged Devices | Block or limit access to SharePoint, OneDrive, and Exchange from unmanaged devices |
| Conditional Access Policy - Block Legacy Authentication | Block access via insecure legacy authentication methods |
| Conditional Access Policy - Block Unknown or Unsupported Device Access | Block users from accessing resources when device type is unknown or unsupported |
| Conditional Access Policy - Enforce MFA | Enforce multi-factor authentication |
| Conditional Access Policy - No Persistent Browser Sessions | Prevent persistent browser sessions |
| Conditional Access Policy - Require Approved Client Apps | Require an approved client app or app protection policy on mobile devices |
| Conditional Access Policy - Require Compliant or Hybrid Azure AD joined device | Require administrators to use compliant or hybrid Azure AD joined devices |
| Conditional Access Policy - Restrict Access To Azure Portal | Require multifactor authentication for Azure management |
| Conditional Access Policy - Restrict Access To Microsoft Admin Portal | Require multifactor authentication for administrators accessing Microsoft admin portals |
| Conditional Access Policy - Securing Security Info Registration | Ensure secure registration for MFA and self-service password reset via compliant devices |
| Conditional Access Policy - Sign-In Risk-Based Multi-Factor Authentication | Protect users from sign-in via MFA in risky sessions |
| Customer Lockbox | Require Microsoft support engineers to get customer approval before accessing data |
| Password Policy | Define password validity period and advance notification for expiration |
| SharePoint Modern Authentication Enforced | Enforce modern authentication protocols for global SharePoint access |
| User Consent Settings | Control when end users and group owners can grant consent to applications |
| Security Defaults Policy | Set of basic identity security mechanisms recommended by Microsoft (may override Conditional Access Policies) |

### Email Security
| Baseline | Description |
|----------|-------------|
| Automatic Forwarding - Block | Transport rule to block automatic forwarding |
| Default Hosted Outbound Spam Filter Policy | Exchange Online Protection outbound spam filter that monitors and blocks suspicious outbound mail |
| DKIM Signing For Default Domain | Ensure DomainKeys Identified Mail signing is enabled for the default domain |
| Mail Auto Forwarding | Disable automatic forwarding to external domains by default |
| Malware File Types Filter Policy | Block known or custom malicious file types from being attached to emails |
| Malware Internal Sender Filter Notification Policy | Alert administrators when an internal sender is blocked for attempting to send malware |
| Preset EOP Policy (Standard) | Microsoft-managed Exchange Online Protection policy applying a standard baseline |
| Preset EOP Policy (Strict) | Strict Pre-set Exchange Online Protection Policy controlled by Microsoft |
| Standard Default Anti Phishing Policy | Default Anti Phishing Policy for Exchange Mailboxes covering anti-spoof intelligence |

### General
| Baseline | Description |
|----------|-------------|
| Security Defaults Policy | Basic identity security mechanisms recommended by Microsoft |

### Intune
| Baseline | Description |
|----------|-------------|
| Android Enterprise - Compliance Policy | Compliance policy for managed Android devices |
| iOS/iPadOS - Compliance Policy | Compliance policy for managed iOS/iPadOS devices |
| MAC OS - Compliance Policy | Compliance policy for managed macOS devices |
| Windows 10 or Later - Compliance Policy | Enforces security standards for Windows 10+ devices (encryption, secure boot, Defender status, OS version) |
| Windows 10 or Later Configuration Policy - Block Password Saving In Google Chrome | Block password saving in Google Chrome |
| Windows 10 or Later Configuration Policy - Block Password Saving In Microsoft Edge | Block password saving in Microsoft Edge |

### Mobile Access
| Baseline | Description |
|----------|-------------|
| Default Mobile Device Mailbox Policy | Manage security settings of mailboxes on mobile devices |

### Remote Access
| Baseline | Description |
|----------|-------------|
| Modern Authentication | Enable modern authentication for the entire organization |
| SMTP Access | Disable SMTP access for the entire organization (SMTP is unsafe legacy email protocol) |

### Sharing
| Baseline | Description |
|----------|-------------|
| Anonymous Links Expiry | Ensure anonymous links expire after a certain number of days |
| External (Guest) Users Resharing | Prevent guest users from resharing items shared with them |
| Global Default Sharing Policy | Control sharing at the organization level in SharePoint and OneDrive |
| SharePoint Block Infected Files Download | Block infected SharePoint files from being downloaded |
| SharePoint Storage Warning | Set a warning threshold for SharePoint sites nearing the storage limit |

## Editing Tenant Baselines

You can edit baselines that are not managed by a template to change the baseline configuration on the tenant where the baseline is applied.

Required role: Partner administrator.

1. In the Cyber Protect console, go to **Microsoft 365 management > Baselines**.
2. Click the pencil icon at the end of the relevant baseline row. The edit baseline dialog opens.
3. Apply changes as needed and click **Save**.

Saving the baseline does not change the value in Microsoft 365. It simply saves a configuration target for the baseline. A deviation check starts to assess whether the baseline state is different from the desired state.

## Remediating Tenant Baselines Manually

You can remediate deviations in tenant baselines by enforcing the required baseline configuration on the tenant.

In service-based licensing, this functionality requires the **RMM > Microsoft 365 seats** service quota. In solution-based licensing, it is enabled with either **Security and RMM** or **Ultimate Protection** license.

The automatic remediation option must be enabled to automatically remediate deviations. However, manual remediation does not require it.

### Steps to Remediate Tenant Baseline Deviations

1. In the Cyber Protect console, go to **Microsoft 365 management > Baselines**.
2. Select the relevant tenant row. The baseline details pane is displayed.
3. Click **Remediate**.
