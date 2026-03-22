---
title: "Endpoint security"
source: "https://developer.acronis.com/doc/cyberapps/intro/types/endpoint-security.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:58:31.709102"
---

# Endpoint security

Endpoint security

This type of CyberApp provides endpoint protection and security using an endpoint agent managed by the ISV cloud service.
The purpose of such CyberApps is to allow the management and monitoring of ISV endpoint agents from Acronis Cyber Platform.



CyberApp scenarios

Typical
Typical endpoint security CyberApps include the following:


Establishing connection to the ISV cloud.
Connection parameters and credentials to allow endpoint protection data to be transferred to Acronis Cyber Platform using the CyberApp enablement form extension point.



Mapping customers.
Pairing ISV customers to Acronis tenants to be able to report the list of protected workloads to the correct tenant using the Custom integration setting extension point.


Reporting protected workloads and their statuses to the Devices list in Acronis Cyber Protection Console, using the Workloads and actions extension point.
Reporting alerts on detected threats and security issues to the Alerts list in Acronis Cyber Protection Console using the Alerts extension point.



Extended
To increase the value of the CyberApp for MSPs, it is recommended to enhance it with additional monitoring and management functionalities:

Create CyberApp-specific widgets to monitor endpoint protection status using the Widgets and reports extension point.
Provide the ability to configure tenant-level settings in Acronis Cyber Protection Console using the Main menu extension point.




Recommended extension points
To be able to extend Acronis Cyber Platform with endpoint security capabilities, the following extension points should be used.

CyberApp enablement form

Endpoint security management is performed at the customer-level. This means that the Partner needs to configure the CyberApp for each end customer individually.
Typically, an endpoint security CyberApp contains the following settings:




Client ID and client secret
Required to authenticate in the ISV cloud and fetch the list of end customers.
These settings enable the CyberApp for the Partner.



Customers mapping
A list of customers fetched from the ISV cloud that allows the specification of an existing customer mapping or the creation of a new corresponding customer mapping in Acronis Cyber Platform.
Mapping an ISV customer to an Acronis customer results in enabling the CyberApp for the specific customer.




CyberApp configuration and mapping can be done only by the Acronis Partner. It cannot be done by end customers.


Workloads and actions

An endpoint security CyberApp should submit the list of workloads with endpoint protection agents installed and registered for the customer to the list of the customer’s workloads in Acronis Cyber Platform.
To do so, the CyberApp must register a new workload type and define what attributes this type will bring.
Examples of possible additional attributes:



Workload name in ISV cloud.
Endpoint protection status.
Endpoint protection agent version and status.
Timestamp of last Malware definitions update.
Timestamp of last system scan.
Workload network parameters (IP address and MAC address).




Alerts

To be able to notify about malware activity or other security issues on a managed workload, an endpoint security CyberApp must submit alerts to Acronis Cyber Platform.
Each alert has a type. Alerts about detected malware must be submitted as an existing alert type and contain the following parameters:



Threat name.
Action executed upon the threat detection.
MD5, SHA1, SHA256 checksums of the detected object.
File path.
File name.
Workload name.



The CyberApp can also create new alert types to report other types of security issues or incidents, depending on the functionality an endpoint protection agent can provide.
For example, if the endpoint protection agent has a function to monitor external devices connected to the protected workload and the agent generates an event “Unauthorized device is connected”, this event should also be submitted to Acronis Cyber Platform as an alert. To be able to report such alerts, the CyberApp must register a new alert type and also define the attributes and their format for the alert content.



Main menu
To configure tenant-level protection settings for endpoint protection, it is recommended to create a dedicated page for the CyberApp in the Management section of Acronis Cyber Protection Console (a new menu item). This page should contain CyberApp settings that are applied to the customer tenant. Such settings can include an exclusions list, lists of allowed and forbidden applications, global network protection settings, etc.
Page content must be described in Vendor Portal. Settings specified on this dedicated page are communicated from Acronis Cyber Platform to the ISV cloud via API Callback Gateway.


Widgets and reports
An endpoint security CyberApp should create several widgets to report the endpoint protection state:

Pie-chart diagram with endpoint agents protection status.
Pie-chart diagram with malware definitions status.
List of 10 latest alerts generated by endpoint protection.

These widgets should be declared by the CyberApp. The widget data must be based only on alerts or workload attributes submitted by the CyberApp.
It is recommended to add CyberApp-specific widgets to the Overview dashboard in Acronis Cyber Protection Console and in the Detected Threats report.  Additionally, the CyberApp can register a new custom report on endpoint protection with all the widgets created by the CyberApp.