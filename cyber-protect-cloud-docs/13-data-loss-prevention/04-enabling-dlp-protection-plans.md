---
title: "Enabling DLP in Protection Plans and Advanced Settings"
section: "Data Loss Prevention"
subsection: "Enabling DLP in Protection Plans"
page_range: "1462-1465"
tags: [dlp, protection-plan, device-control, observation-mode, enforcement-mode, advanced-settings, ocr, allowlist, security-level]
acronis_version: "26.02"
---

# Enabling Data Loss Prevention in Protection Plans

Data Loss Prevention features can be included in any protection plan for a customer tenant if the Protection service and the Data Loss Prevention pack are enabled for this customer.

## DLP and Device Control Coordination

DLP features and Device control can be used independently or together (in a single protection plan, or in two plans protecting the same workload). If used together, their functional capabilities are coordinated as follows:

- **Device control stops controlling user access** to those local channels in which DLP inspects the content of transferred data. However, Device control retains the control over the following device types if they are configured to Read-only or Denied access:
  - Removable
  - Encrypted removable
  - Mapped drive

  For example, if you have both Device control and DLP enabled and you have Read-only access configured for USB devices in Device control, the Read-only access will be applied to all USB devices, except for the ones in the allowlist, regardless of the access settings in the DLP module. If the default Enable access is configured in Device control, the access setting in DLP will be applied.

- **User access to the following local channels and peripherals in the allowlist** is enforced by Device Control:
  - Optical drives
  - Floppy drives
  - MTP-connected mobile devices
  - Bluetooth adapters
  - Windows clipboard
  - Screenshot captures
  - USB devices and device types (except for Removable storage and Encrypted)

## Creating a Protection Plan with DLP

1. Navigate to **Management** > **Protection plans**.
2. Click **Create plan**.
3. Expand the **Data Loss Prevention** section and click the **Mode** row. The **Mode** dialog opens.
   - To start the creation or renewal of the data flow policy, select **Observation mode** and then select how to process data transfers (Allow all, Justify all, or Mixed).

     > **Warning:** Select **Observation mode** only if you do not have a data flow policy created before or if you are renewing the policy. Data leakage is not prevented in the Observation mode.

   - To enforce the existing data flow policy, select **Enforcement mode**, and then select how strictly to enforce the data flow policy rules:

     | Option | Description |
     |--------|-------------|
     | **Strict enforcement** | The data flow policy is enforced as is and will not be extended with new permissive policy rules when previously unobserved sensitive data flows are detected. |
     | **Adaptive enforcement (Enforcement with learning)** | The enforced policy continues its automatic adaptation to those business operations that were not performed during the observation period or to changes in business processes. This mode allows the enforced data flow policy to expand based on newly learned data flows detected on the workloads. |

     > **Important:** Before switching a company or unit policy from Observation to Enforcement mode, it is crucial to adjust the default rules for each sensitive data category from the permissive to a prohibitive state. Default rules are marked with an asterisk (*) in the **Data flow policy** view.

4. Click **Done** to close the Mode dialog.
5. (Optional) To configure optical character recognition, allowlists, and more protection options, click **Advanced Settings**.
6. Save the protection plan and apply it to the workloads that you want to protect.

## Advanced Settings

You can use the advanced settings in protection plans with Data Loss Prevention to increase the quality of data content inspection in channels controlled by DLP, as well as exclude from any preventive controls data transfers to peripheral device types in the allowlist, categories of network communications, destination hosts, as well as data transfers initiated by applications in the allowlist.

### Available Advanced Settings

- **Optical character recognition** -- Turns on or off optical character recognition (OCR) in order to extract pieces of text in 31 language for further content inspection from graphical files and images in documents, messages, scans, screenshots, and other objects.

- **Transfer of password-protected data** -- The content of password-protected archives and documents cannot be inspected. With this setting, DLP allows the administrator to select whether outgoing transfers of password-protected data are to be allowed or blocked.

- **Prevent data transfer on errors** -- Sometimes, the analysis of content that is being sent might fail or another control error might occur in DLP agent operations. If this option is enabled, the transfer will be blocked. If the option is disabled, the transfer will be allowed despite the error.

- **Allowlist for device types and network communications** -- Data transfers to the types of peripheral devices and in network communications checked in this list are allowed regardless of their data sensitivity and the enforced data flow policy.

  > **Warning:** This option is used if issues with a specific Device type or Protocol occur. Do not enable it unless advised by a Support representative.

- **Allowlist for remote hosts** -- Data transfers to destination hosts specified in this list are allowed regardless of their data sensitivity and the enforced data flow policy.

- **Allowlist for applications** -- Data transfers performed by applications specified in this list are allowed regardless of their data sensitivity and the enforced data flow policy.

### Security Level Indicator

The **Security level** indicator of Advanced settings displayed in the **Create protection plan** view and in the "Details" view of a protection plan has the following logic of level indication:

- **Basic** indicates that none of the advanced settings is turned on.
- **Moderate** indicates that one or more settings are turned on, but the combination of **OCR**, **Transfer of password-protected data**, and **Prevent data transfer on errors** is not activated.
- **Strict** indicates that at least the combination of **OCR**, **Transfer of password-protected data**, and **Prevent data transfer on errors** settings is activated.

## Automated Detection of Destination

In Mixed Observation mode, Data Loss Prevention applies different rules depending on the destination of the detected data transfer -- internal or external. The logic for determining a destination as internal is described below. All other destinations are considered external.

For each intercepted data transfer, Data Loss Prevention detects automatically if the destination HTTP, FTP, or SMB server is internal by performing a DNS request and comparing the FQDN names of the machine where the DLP agent runs and the remote server. If the DNS request fails, it also checks if the protected workload and the remote server are in the same network. Servers that have the same domain name (or are in the same subnetwork) as the machine where the DLP agent runs are considered internal.

For email communication, DLP treats as internal transfers all emails sent from a corporate email address by using the corporate mail server if the recipient email is on the same domain as the sender email, and the recipient mail server name is the same.

Non-corporate emails are treated as external communication unless the recipient account is known. Communications via messengers are treated as external communications unless the recipient account is known. Known accounts are updated as DLP monitors the user activity on the network.
