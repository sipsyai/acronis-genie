---
title: "CyberApp components"
source: "https://developer.acronis.com/doc/cyberapps/intro/overview/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:57:59.846704"
---

# CyberApp components

CyberApp components

General overview
The following diagram is a general overview of the major components of a deployed CyberApp.



Deployed CyberApp Description defines the marketing materials for a CyberApp. These materials are used to create an entry (card) on integration catalogs.
For more information, see DESCRIPTIONS (CyberApp marketing).



Integration catalogs are data center-specific inbound web portals that list deployed CyberApps which are available for use by Acronis partners.
In the integration catalog, Acronis partners and customers can find CyberApps, learn more about them, enable them, and configure them from the integration catalog.
For more information, see Integration catalogs.


Acronis public website integration catalog is a publicly available catalog of all deployed CyberApps. This catalog is for information only.

The deployed CyberApp Version defines the CyberApp functionality. Versions include extension points, which extend the funtionality of the Acronis Cyber Protect Console, and custom callbacks, which exchange data with the ISV cloud service through two critical CyberApp components:
For more information, see VERSIONS (CyberApp functionality).



Custom callbacks are created by the CyberApp developers. They define the structure of the callback request and response payloads.
For more information, see Custom callbacks.



Extension points allow a CyberApp developer to extend the Acronis Cyber Platform with a new resource type, UI form, and/or feature of the integrated cloud service. Extension points can be divided into:





Base domain model type extensions
For example, a new alert type provided by the CyberApp.
When the CyberApp extends a platform alert type with the new alert type, it inherits the following original behavior as well:



Standard Alerts API methods (create, read, update, dismiss, delete).
Alerts management UI.
Alerts aggregation rules.
User notification pipeline (emails, push notifications, daily recaps, etc.).
Appropriate events generation on alert state change (alert created, alert dismissed, etc.).




UI extensions
For example, a new menu item in the Acronis Cyber Platform, provided by the CyberApp.
The CyberApp developer describes the appearance of the new menu item UI (label, form contents, child forms, etc.) using the UI builder.





For more information, see Extension points.




Acronis standard callbacks define the structure of the standard Acronis callback request and response payloads, which exchange data between Acronis and the ISV service when the CyberApp is enabled by a partner and/or customer. These are created and managed by Acronis. The CyberApp callback handler must include functionaity to handle these standard callbacks.
For more information, see Enabling the CyberApp.


CyberApp callback gateway handles callback requests and responses between the Acronis platform and the CyberApp callback handler. Acronis hosts and manages this component.

CyberApp callback handler accepts HTTP requests from the Acronis CyberApp callback gateway, processes them according to the specified format, sends the corresponding action to be executed by the ISV service and returns the operation result. The CyberApp callback handler is hosted on the ISV cloud service.
For more information, see The callback handler.



Acronis APIs provide public endpoints for ISVs to interact directly with Acronis data through the CyberApp Connector.
For more information, see Acronis platform APIs.



CyberApp Connector is a software component, responsible for data flow between the ISV service and Acronis Cyber Platform. It receives and sends data via the Acronis APIs. While extension points define the functionality of the CyberApp, the connector requests and delivers data, such as alerts, workloads, events, etc. The connector may be developed and hosted on the ISV side, or Acronis can host it on the Acronis Cyber Platform.
For more information, see The connector.




In this section

CyberApp enablement
Acronis menu items
Alerts, workloads, and workload actions
Widgets and reports