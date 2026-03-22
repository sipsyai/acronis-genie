---
title: "Remote desktop"
source: "https://developer.acronis.com/doc/cyberapps/intro/types/remote-desktop.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:58:49.029575"
---

# Remote desktop

Remote desktop
This type of CyberApp provides Remote Desktop access using an endpoint agent managed by the ISV cloud service. The purpose is to provide MSP technicians with remote desktop access to managed workloads directly from Acronis Cyber Platform.
There are two types:

Integration with a locally installed Remote Desktop application
Integration with direct communication to the ISV’s cloud



Integration with a locally installed Remote Desktop application
This integration model does not require direct communication between Acronis Cyber Platform and the ISV’s cloud. Instead, the Cyber Protection console makes a request to the locally installed Remote Desktop application that is normally used by the ISV’s service for remote access. To make such a request, existing workloads that have the Acronis agent and the vendor’s remote desktop agent installed are extended with a new action - open a remote session to the selected workload. The advantage of this integration method is its simplicity. But the following conditions must be met in order to open the Remote Desktop session successfully:

The Remote Desktop application must be installed on the same device that attempts to initiate a connection from the Cyber Protection Console.
The Remote Desktop application must be configured to launch with the MSP administrator account credentials.
The Remote Desktop agent must be installed on the target workload to initiate the remote session.
The Acronis agent must be installed on the target workload to discover and display the workload in the Cyber Protection console.
The MSP administrator account must have sufficient privileges provided by the vendor’s service to access the target workload.



Recommended extension points
Integration with a locally installed Remote Desktop application requires only three extension points.

CyberApp enablement form
CyberApp enablement form is needed to enable the CyberApp. No additional configuration is required. The CyberApp is enabled for all MSP customers simultaneously.


Workloads and actions
Acronis workloads must be extended with a new action that makes a request to the locally installed Remote Desktop application to establish a remote session. This request must include the target workload ID to allow the Remote Desktop application to establish the connection to the correct target.





Integration with direct communication to the ISV’s cloud
This integration model requires mapping customer tenants in Acronis Cyber Platform to corresponding organizations on the ISV’s vendor side. Then, for each mapped customer, ISV’s cloud reports the list of workloads with installed remote desktop agents to Acronis Cyber Platform. These workloads are reported as a new workload type with the new custom action named “Remote connect”. Workloads reported by the integration are merged with Acronis workloads in the management portal and displayed as a single entity, effectively adding the new “Remote connect” action to existing Acronis workloads.


Standard recommended extension points
The minimal integration scenario that allows the CyberApp to enrich Acronis Cyber Platform with Remote Desktop capabilities requires the following extension points:


CyberApp enablement form
To enable the CyberApp and perform customer mapping.



Workloads and actions
To display workloads with ISV agents in Acronis Cyber Platform Devices list and extend existing actions with new “Remote connect” action.




CyberApp enablement form
To ensure the correct synchronization of workloads from the ISV Cloud to Acronis, CyberApp settings must include:


Partner credentials and connection settings
Required to authenticate in the ISV cloud and fetch the list of end customers. These settings enable the CyberApp for the Partner.



Customers mapping
A list of customers, fetched from the ISV cloud, that allows the specification of an existing customer mapping or the creation of a new corresponding customer mapping in Acronis Cyber Platform. Mapping an ISV customer to Acronis customer results in enabling the CyberApp for the specific customer.



CyberApp configuration and mapping can be done only by the Partner. It cannot be done by end customers.


Workloads and actions
To report workloads with remote desktop agents installed from the ISV cloud to Acronis:

Workloads must be extended with a new workload type.
Workloads reported by the ISV’s connector must be merged with Acronis workloads (or displayed alongside, if there is no matching workload on the Acronis side).
A new workload type must bring new attributes and new actions. One of these actions must be a command to establish a remote session with the workload. If several types of remote connections are possible (For example, for attended and unattended access) the CyberApp may bring several custom actions.
To successfully merge ISV’s and Acronis workloads, the ISV’s workload attributes must include network parameters (host name and MAC address).
Additional attributes are optional:

Endpoint agent status.
Endpoint agent version.






Extended recommended extension points
Extended scenarios may include additional extension points:


Alerts
To display alerts generated by the Remote Desktop service.



Main menu
To configure tenant-level settings for Remote Desktop tools.



Widgets and reports
To display ISV endpoint agent status and other statistics.




Alerts
Alerts can be optionally used to report issues that occurred during remote sessions. Alerts must be submitted as a new alert type and contain the following parameters:


Workload status.
Status description.
Workload name.
Error name.
Error description.




Main menu
To be able to configure the parameters for remote connection, it is recommended to create a dedicated page for the CyberApp in the Settings section of the Cyber Protection console (a new menu Item). This page should contain CyberApp settings that are applied to the customer tenant. Such settings may be:

Preferred server parameters.
Wake-on-LAN.
Default settings for remote connection:

Audio (on/off).
Chat (on/off).
Recording (on/off).



Settings specified on this dedicated page are saved in the Acronis Cyber Platform and synchronized with the ISV’s cloud by the Connector. Alternatively, they can be used as parameters during the remote session request.


Widgets and Reports
A Remote Desktop CyberApp may create widgets to report endpoint agent state and remote session issues:

Pie-chart diagram with Remote Desktop agents’ statuses.
List of 10 latest alerts generated by Remote Desktop CyberApp.

These widgets should be declared by the CyberApp. The widget data must be based only on alerts or workload attributes submitted by the CyberApp.
It is recommended to add CyberApp-specific widgets to the Overview dashboard in the Cyber Protection console.