# Configuring critical endpoints

Acronis Managed Detection and Response (MDR) > Enabling the Acronis MDR Service > Configuring critical endpoints
Configuring critical endpoints

MDR partners can configure a list of critical endpoints that require approval before any response actions (including isolation) are executed on them.

Before performing any response action on these endpoints, the MDR team will contact the primary contact for escalations to request approval (including a phone call if the incident is critical). If the primary contact is not reachable, the team will contact the secondary contact, and so on until a contact responds.

No response actions will be executed on any critical endpoint until an escalation contact approves it.

To configure the list of critical endpoints

In the Cyber Protect Cloud console, verify that you are at the All customers level.
Navigate to Devices > Machines with agents.

Locate the Critical Endpoints group.

The group is created automatically when the MDR service is enabled.

Add devices to the group.

To add devices that already exist, click Add devices and select from the list of devices under each customer.
To add a new device, click Add in the upper right corner and follow the on-screen prompts.

Escalation contacts will receive incident notifications and approve remediation actions when required.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.