---
title: "The connector"
source: "https://developer.acronis.com/doc/connector/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:35.267804"
---

# The connector

The connector

To enable data exchange between your service and Acronis Cyber Platform, you must create a connector to push or pull the necessary data to/from Acronis Cyber Platform.
This chapter describes the connector component and provides brief, step-by-step instructions in the interactive Python shell.



Note
If you do not have Python installed, you can get it from https://www.python.org/downloads/.



The following diagram shows the connector as an independent component, and its relation between your service and Acronis Cyber Platform:



The purpose of the connector depends on the type of integration.
For example:



A outbound integration might pull Acronis Cyber Platform workloads, alerts, etc., to replicate them in your service for further processing.
An inbound integration (CyberApp) might pull Acronis Cyber platform users and their access rights to provision them on your service, enable
the service, and push your service events, alerts, etc., to Acronis Cyber Platform.



Note
On request, Acronis can create and host the connector on behalf of the Vendor.


In this section

Data mapping
CyberApp data access scopes
API Authentication
Managing workloads
Managing alerts
Sample code in GitHub