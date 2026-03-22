# Tenant baselines

RMM > Managing and monitoring the Microsoft 365 environment > Working with baselines > Tenant baselines
Tenant baselines

The following table lists the currently supported Microsoft 365 tenant baselines.

Category	Baseline	Description
Audit	Mailbox Audit Log	Enable mailbox audit logs for the entire organization. For more information, see M365 Security Posture Management.
Audit	Unified Audit Log	Enable or disable the audit log for the entire organization. For more information, see M365 Security Posture Management.
Authentication and authorization	Admin Consent Workflow	The admin consent workflow in Microsoft Entra ID allows users to request approval for apps that require admin-level permissions. When enabled, users can submit requests, and designated reviewers (like IT admins) are notified to approve or deny them. This helps control access to sensitive data and ensures secure, auditable permission management. For more information, see M365 Security Posture Management.
Authentication and authorization	Authentication Method Policy - Email OTP	Email OTP sends a code to a user's email account which is then used to authenticate. For members of a tenant, email OTP is usable only for Self-Service Password Recovery. It may also be configured to be used for sign-in by guest users. For more information, see M365 Security Posture Management.
Authentication and authorization	Authentication Method Policy - Microsoft Authenticator	The Microsoft Authenticator app is a flagship authentication method, usable in passwordless or simple push notification approval modes. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access policy - Application of Enforced Restrictions for Unmanaged Devices	Block or limit access to SharePoint, OneDrive, and Exchange content from unmanaged devices. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Block Legacy Authentication	Block access via insecure legacy authentication methods. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Block Unknown or Unsupported Device Access	Users will be blocked from accessing company resources when the device type is unknown or unsupported. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Enforce MFA	Enforce multi-factor authentication. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - No Persistent Browser Sessions	Prevent persistent browser sessions. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Require Approved Client Apps	Require an approved client app or an app protection policy when using mobile devices. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Require Compliant or Hybrid Azure AD joined device	Require administrator users to perform actions from a compliant or hybrid Azure AD joined device. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Restrict Access To Azure Portal	Require multifactor authentication for Azure management. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Restrict Access To Microsoft Admin Portal	Require multifactor authentication for administrators accessing Microsoft admin portals. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Securing Security Info Registration	Ensure all users securely register for multi-factor authentication (MFA) and self-service password reset (SSPR) via compliant devices or specific conditions during registration. For more information, see M365 Security Posture Management.
Authentication and authorization	Conditional Access Policy - Sign-In Risk-Based Multi-Factor authentication	Protect users from sign-in via multi-factor authentication in risky sessions. For more information, see M365 Security Posture Management.
Authentication and authorization	Customer Lockbox	Require Microsoft support engineers to get customer approval before accessing their data during support cases. For more information, see M365 Security Posture Management.
Authentication and authorization	Password Policy	This policy defines how long a password remains valid before the user must change it, and how many days in advance the user is notified of upcoming expiration. Use it to ensure that user credentials are rotated regularly (or set to never expire, if appropriate) in line with your security and operational requirements. For more information, see M365 Security Posture Management.
Authentication and authorization	SharePoint Modern Authentication Enforced	Enforce the use of only modern authentication protocols for global SharePoint access by disabling legacy authentication protocols. For more information, see M365 Security Posture Management.
Authentication and authorization	User Consent Settings	Control when end users and group owners are allowed to grant consent to applications, and when they will be required to request administrator review and approval. Allowing users to grant apps access to data helps them acquire useful applications and be productive, but can represent a risk in some situations if it is not monitored and controlled carefully. For more information, see M365 Security Posture Management.
Email security	Automatic Forwarding - Block	Transport rule to block automatic forwarding. For more information, see M365 Security Posture Management.
Email security	Default Hosted Outbound Spam Filter Policy	A default Exchange Online Protection (EOP) outbound spam filter policy that monitors and blocks suspicious outbound mail, helping MSPs detect and prevent compromised accounts from sending spam or malicious content. For more information, see M365 Security Posture Management.
Email security	DKIM Signing For Default Domain	Ensure that DomainKeys Identified Mail (DKIM) signing is enabled for the default domain. For more information, see M365 Security Posture Management.
Email security	Mail Auto Forwarding	Disable automatic forwarding to external domains by default for the entire organization (attackers or malicious actors can automatically forward all mail to another mailbox, and breach compliance if the auto-forwarding is to an external domain). For more information, see M365 Security Posture Management.
Email security	Malware File Types Filter Policy	A policy that blocks known or custom malicious file types from being attached to emails, helping prevent malware infections. Administrators can add or remove specific file extensions to tailor protection for each tenant. For more information, see M365 Security Posture Management.
Email security	Malware Internal Sender Filter Notification Policy	A configuration within Exchange Online Protection (EOP) that alerts administrators when an internal sender is blocked for attempting to send malware, helping MSPs quickly detect and respond to potential account compromise. For more information, see M365 Security Posture Management.
Email security	Preset EOP Policy (Standard)	A Microsoft-managed Exchange Online Protection (EOP) policy that applies a standard baseline of email security across your tenant. Created from a template in the Defender Admin Console, this policy is fully managed and maintained by Microsoft once deployed. For more information, see M365 Security Posture Management.
Email security	Preset EOP Policy (Strict)	A Strict Pre-set Exchange Online Protection Policy is a pre-set policy created from a template in Office 365 Defender Admin Console. They are controlled by Microsoft once created. For more information, see M365 Security Posture Management.
Email security	Standard Default Anti Phishing Policy	Default Anti Phishing Policy for Exchange Mailboxes that covers anti-spoof intelligence. For more information, see M365 Security Posture Management.
General	Security Defaults Policy

Security defaults is a set of basic identity security mechanisms recommended by Microsoft. When enabled, these recommendations will be automatically enforced in your organization. Administrators and users will be better protected from common identity-related attacks. For more information, see M365 Security Posture Management.

This will override some settings, such as Conditional Access Policies.

Intune	Android Enterprise - Compliance Policy	Compliance policy for managed Android devices. For more information, see M365 Security Posture Management.
Intune	iOS/iPadOS - Compliance Policy	Compliance policy for managed iOS/iPadOS devices. For more information, see M365 Security Posture Management.
Intune	MAC OS - Compliance Policy	Compliance policy for managed macOS devices. For more information, see M365 Security Posture Management.
Intune	Windows 10 or Later - Compliance Policy	A compliance policy that enforces security standards for Windows 10 and later devices managed through Intune. It validates encryption, secure boot, Defender status, OS version, and device health to ensure endpoints meet organizational and regulatory security requirements across all client environments. For more information, see M365 Security Posture Management.
Intune	Windows 10 or Later Configuration Policy - Block Password Saving In Google Chrome	Configuration policy for blocking password saving in Google Chrome. For more information, see M365 Security Posture Management.
Intune	Windows 10 or Later Configuration Policy - Block Password Saving In Microsoft Edge	Configuration policy for blocking password saving in Microsoft Edge. For more information, see M365 Security Posture Management.
Mobile Access	Default Mobile Device Mailbox Policy	Set the default mobile device mailbox policy to manage many different security settings of mailboxes on mobile devices. For more information, see M365 Security Posture Management.
Remote access	Modern Authentication	Enable modern authentication for the entire organization. For more information, see M365 Security Posture Management.
Remote access	SMTP Access	Disable SMTP access for the entire organization. SMTP is regarded as an unsafe legacy email protocol. For more information, see M365 Security Posture Management.
Sharing	Anonymous Links Expiry	Ensure anonymous links expire after a certain number of days. For more information, see M365 Security Posture Management.
Sharing	External (Guest) Users Resharing

Prevent guest users who have shared access to an item (where the item was shared using guest sharing, and not via an anonymous link) from resharing the item with others. The Prevent External Users From Resharing setting ensures limited access to shared items. For more information, see M365 Security Posture Management.


Sharing	Global Default Sharing Policy	Control sharing at the organization level in SharePoint and OneDrive. For more information, see M365 Security Posture Management.
Sharing	SharePoint Block Infected Files Download	Block SharePoint files that are infected from being downloaded. For more information, see M365 Security Posture Management.
Sharing	SharePoint Storage Warning	Use this baseline to set a warning threshold for SharePoint sites nearing the storage limit. If any of the sites go over the storage threshold(s) set by the baseline then the baseline will deviate thereby raising an alert. For more information, see M365 Security Posture Management.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.