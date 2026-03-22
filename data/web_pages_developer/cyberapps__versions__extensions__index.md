---
title: "Extension points"
source: "https://developer.acronis.com/doc/cyberapps/versions/extensions/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:02:21.682731"
---

# Extension points

Extension points

Extensions points are ways for the CyberApp to introduce new resource types or processing flows in the Acronis Cyber Cloud platform.
For example, the CyberApp might describe a new alert type that Acronis Cyber Platform receives from your platform.

There are four extension points:



Alerts
(1 on the screenshot, below)
An alert’s purpose is to notify Customer and Partner administrators about some incident that requires their attention.
The CyberApp can post alerts with types already available in the Acronis Cyber Cloud platform, or register alerts with a new type, which you specify in the CyberApp.
New alert types must be mapped to Acronis alert severity levels.
CyberApp alerts are posted by the connector and appear in the Acronis Cyber Platform interface in the same way as native Platform alerts.



Main menu
(3 on the screenshot, below. In this example, the main menu item created by the CyberApp is called EMAIL SECURITY)
CyberApp main menu items create dedicated menu items in the Acronis Cyber Protection Console  with a custom page.
They can also appear as subitems of existing Acronis menu items and can also include child menu items.
The purpose of this extension point is to provide the interface for CyberApp configuration (For example, a list of exclusions for antimalware protection, a list of trusted web resources, etc.).
The submitted configuration is stored on Acronis Cyber Platform and synchronized with ISV service by the connector.



Workloads and actions
(2 on the screenshot, below)
CyberApp device types and a list of displayed device properties and actions.
The purpose of this extension point is to allow Acronis Cyber Platform to display and manage devices reported by ISV service.
ISV devices must be registered as a new device type and may include existing and new attributes.
The list of ISV devices and their attributes is posted by the connector.



Widgets and Reports
(4 on the screenshot, below)
CyberApp widgets and reports that visualize data provided by the ISV service.
The CyberApp can register new widgets in the form of:



Pie chart diagram.
Bar chart diagram.
Table.



Data presented in the widget can be collected from alerts, events and devices’ attributes reported by the CyberApp.
Widgets registered by the CyberApp can be included in the reports and delivered to selected recipients by schedule.








In this section

Alerts
Main menu
Workloads and actions
Widgets and reports