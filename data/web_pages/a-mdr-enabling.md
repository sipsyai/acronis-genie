# Enabling the Acronis MDR Service

Acronis Managed Detection and Response (MDR) > Enabling the Acronis MDR Service
Enabling the Acronis MDR Service

The enabling of Acronis MDR service in the Cyber Protect Cloud console can be performed only by Partner administrator users and only on the partner level.

If login control for the web interface is enabled, the IP range of the MDR vendor will be added automatically to the list of allowed IP addresses to allow the monitoring of the environment.
Before You Begin

Before enabling Acronis MDR, ensure that all of the following prerequisites are met.

The Managed Detection and Response service is enabled for your Partner account depending on your licensing model:
For solution-based licensing: Security and RMM solution or Ultimate Protection solution and the Managed Detection and Response add-on.
For service-based licensing: Protection service and the Detection and Response offering item.
The Acronis Cyber Protection agent is installed on all endpoints.
All protected endpoints are actively reporting telemetry.

To enable MDR

Partner administrator
Enable MDR at the Partner level
Sign in to Acronis Cyber Protect Cloud console.
Navigate to Protection > MDR.

Click Enable Acronis TRU.

Configure escalation contacts.

Escalation contacts will receive incident notifications and approve remediation actions when required.

The escalation contacts that you configure are common for all child tenants.

Configure a primary and a secondary contact.

]

Add more contacts if needed.

You can configure up to 4 escalation contacts in total.

Select the service level.

Standard MDR - Acronis TRU team provides only recommendations on resolving security incidents.
Advanced MDR - Acronis TRU team executes response actions when needed.

If you manage customers across multiple Acronis data centers, switch on the Enable MDR in multiple DCs toggle.

If the configuration was successful, the MDR dashboard will display the list of your customers.

Enable MDR for your customers.

In the list of customer, select the ones for which you want to enable the Acronis MDR service.
Click Enable Acornis TRU MDR.
Assign the appropriate service level.
Switch the I accept and understand how to exclude Critical Endpoints toggle.
Click Enable.

For the first two weeks after the activation, MDR operates in learning mode to establish a baseline of normal behavior on protected workloads and reduce false positives.

You may be asked to confirm alerts, approve exclusions, or provide context for specific activities.

Configuring critical endpoints

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.