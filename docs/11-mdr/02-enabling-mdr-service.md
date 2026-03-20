---
title: "Enabling the Acronis MDR Service"
section: "Acronis Managed Detection and Response (MDR)"
subsection: "Enabling MDR"
page_range: "1225-1229"
tags: [mdr, enabling, configuration, escalation-contacts, licensing, critical-endpoints, partner-administrator]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#a-mdr-enabling.html"
---

# Enabling the Acronis MDR Service

The enabling of MDR service in the Cyber Protect Cloud console can be performed only by Partner administrator users and only on the partner level.

If login control for the web interface is enabled, the IP range of the MDR vendor will be added automatically to the list of allowed IP addresses to allow the monitoring of the environment.

## Before You Begin

Before enabling Acronis MDR, ensure that all of the following prerequisites are met:

- The Managed Detection and Response service is enabled for your Partner account depending on your licensing model:
  - For solution-based licensing: Security and RMM solution or Ultimate Protection solution and the Managed Detection and Response add-on.
  - For service-based licensing: Protection service and the Detection and Response offering item.
- The Acronis Cyber Protection agent is installed on all endpoints.
- All protected endpoints are actively reporting telemetry.

## Steps to Enable MDR

**Required privileges**: Partner administrator

### Step 1: Enable MDR at the Partner Level

1. Sign in to Acronis Cyber Protect Cloud console.
2. Navigate to **Protection > MDR**.
3. Click **Enable Acronis TRU**.

### Step 2: Configure Escalation Contacts

Escalation contacts will receive incident notifications and approve remediation actions when required. The escalation contacts that you configure are common for all child tenants.

1. Configure a primary and a secondary contact. For each contact, provide:
   - Name
   - Email
   - Contact number
   - Time zone
2. Add more contacts if needed. You can configure up to 4 escalation contacts in total.

In the event of an escalation, Acronis TRU follows the escalation path and calls each contact up to six times before moving to the next contact. After a call or if no contact is made, Acronis TRU sends an email to all contacts with an overview of the escalation and the incident.

### Step 3: Select the Service Level

- **Standard MDR**: Acronis TRU team provides only recommendations on resolving security incidents.
- **Advanced MDR**: Acronis TRU team executes response actions when needed.

### Step 4: Enable MDR in Multiple DCs (Optional)

If you manage customers across multiple Acronis data centers, switch on the **Enable MDR in multiple DCs** toggle.

If the configuration was successful, the MDR dashboard will display the list of your customers, showing Customers, Vendor, Status, and Service level columns.

### Step 5: Enable MDR for Your Customers

1. In the list of customers, select the ones for which you want to enable the Acronis MDR service.
2. Click **Enable Acronis TRU MDR**.
3. Assign the appropriate service level.
4. Switch the **I accept and understand how to exclude Critical Endpoints** toggle.
5. Click **Enable**.

For the first two weeks after the activation, MDR operates in learning mode to establish a baseline of normal behavior on protected workloads and reduce false positives. You may be asked to confirm alerts, approve exclusions, or provide context for specific activities.

## Configuring Critical Endpoints

MDR partners can configure a list of critical endpoints that require approval before any response actions (including isolation) are executed on them.

Before performing any response action on these endpoints, the MDR team will contact the primary contact for escalations to request approval (including a phone call if the incident is critical). If the primary contact is not reachable, the team will contact the secondary contact, and so on until a contact responds.

No response actions will be executed on any critical endpoint until an escalation contact approves it.

### Steps to Configure the List of Critical Endpoints

1. In the Cyber Protect Cloud console, verify that you are at the **All customers** level.
2. Navigate to **Devices > Machines with agents**.
3. Locate the **Critical Endpoints** group. The group is created automatically when the MDR service is enabled.
4. Add devices to the group:
   - To add devices that already exist, click **Add devices** and select from the list of devices under each customer.
   - To add a new device, click **Add** in the upper right corner and follow the on-screen prompts.

Escalation contacts will receive incident notifications and approve remediation actions when required.
