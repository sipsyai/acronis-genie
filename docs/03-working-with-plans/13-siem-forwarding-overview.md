---
title: "SIEM forwarding plans overview"
section: "Working with plans"
subsection: "SIEM forwarding plans"
page_range: "262-266"
tags: [SIEM, security, log forwarding, compliance, SOC, installation]
acronis_version: "26.02"
---

# SIEM forwarding plans

> **Important:** This option is only available for partner administrators with access to Cyber Protection.

SIEM (Security Information and Event Management) platforms are cybersecurity solutions that provide centralized log management, offer real-time threat detection, facilitate incident investigations, and help organizations meet compliance requirements. They work by consolidating and analyzing security data, such as logs from firewalls, intrusion detection systems, servers, and applications. This is done in real-time, to generate prioritized alerts for any suspicious activities and potential threats. Security teams then use the consolidated data and alerts to investigate flagged cybersecurity incidents, understand their scope, and take timely action to contain and mitigate threats.

SIEM platforms provide a comprehensive view of an organization's security posture, enabling early detection of advanced threats and anomalies. They help organizations meet regulatory and industry-specific security compliance standards, by providing centralized data and reporting. They offer a centralized console for managing security events, providing better visibility into the security operations center (SOC).

## How Acronis SIEM forwarding works

With Acronis SIEM forwarding plans, you nominate a protected device for each participating customer. The Acronis agent on that device acts as the SIEM data writer. It writes alert, event, task, activity, and audit log information to a folder on the device. This data can then be forwarded to the SIEM platform for processing.

> **Important:** Regulatory compliance demands customer have individual SIEM 'data lakes'. By using the Acronis agent to write the SIEM data on a customer's protected device, compliance is achieved. This means that each SIEM customer must have an individual SIEM forwarding plan. You can create individual SIEM forwarding plans for specific single customer, and you can also create a generic SIEM plan for multiple customers, and choose an Acronis protected device for each customer to act as the writing device and data store.

## SIEM feature installation

In order for a device to be used as the SIEM writer device, it must have the SIEM feature installed on the Acronis agent. This can be done either manually, through the standard Acronis agent installation GUI, or unattended, when a SIEM forwarding plan is applied to the device.

### Installing the SIEM feature using GUI

You can install the SIEM feature on your SIEM writer device using the Acronis agent installation GUI.

> **Important:** You must explicitly request the SIEM Log Forwarder feature during the installation.

**Prerequisite:** Read the instructions found in "Installing protection agents by using the graphical user interface" (p. 61).

**To install the SIEM feature using GUI:**

1. Run the installation file. The initial installation screen appears.
2. Click **Customize installation settings**. The **Installation settings** screen appears.
3. Click **Change** to specify **What to install**. The **What to install** screen appears.
4. Ensure that you select the **SIEM Log Forwarder** check-box.
5. Click **Done**.
6. [Optional] Make other required changes to the installation settings.
7. Click **Install** to install the Acronis agent with the SIEM log forwarding feature enabled.

### Installing the SIEM feature unattended

With unattended SIEM feature installation, the feature installation is triggered when a SIEM forwarding plan is applied to the device. The installation progress can be monitored via the Activities section in the Cyber Protect console.

## SIEM forwarding plan lists

There are SIEM forwarding plan lists on your partner level and on your customer levels.

### Partner-level plan list

At the partner level, the SIEM forwarding plan list provides a summary of any and all SIEM forwarding plans you have implemented for customers. The partner-level SIEM forwarding plan list displays the following details:

- **Name** -- The SIEM forwarding plan name.
- **Method** -- Whether the SIEM forwarding plan uses the files or the syslog server method.
- **Customers** -- The customer or customers using the plan.
- **Data** -- The Acronis data forwarded as part of the SIEM forwarding plan.

### Customer-level plan list

Each customer can have only one SIEM forwarding plan. Therefore, at the customer level, the SIEM forwarding plan list is either empty (because you have not created a plan for them) or has a single entry, displaying the following details:

- **Name** -- The SIEM forwarding plan name.
- **Method** -- Whether the SIEM forwarding plan uses the files or the syslog server method.
- **Writer device** -- The device used to write and store the Acronis SIEM data.
- **Data** -- The Acronis data forwarded as part of the SIEM forwarding plan.

### Opening a SIEM forwarding plan list

1. Open the Protection console at either the partner level or at a customer level.
2. Select **Management** from the main menu.
3. Select **SIEM forwarding plans** from the submenu.
