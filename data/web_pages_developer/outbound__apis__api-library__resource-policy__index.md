---
title: "Resource and Policy Management"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:17.931851"
---

# Resource and Policy Management

Resource and Policy Management

Introduction
The Resource and Policy Management API consists of two interrelated APIs:


Resource Management API
You can use the Acronis Resource Management API to view information about available resources.



Policy Management API
You can use the Acronis Policy Management API to:



View information about protection plans and policies.
Create/update/delete a protection plan.
Apply/revoke a protection plan to/from resources.
Enable and disable specific policies.





Note
Some operations might not be covered in this API guide. For a list of all public endpoints and full technical details, see the Resource and Policy Management API reference.



Definitions


Policy
A policy is a data protection module that can be applied to resources and executed by the Cyber Protection agent.
For a full list of protection policies and their settings, see Protection policy settings.



Application
An application is an entity that represents a bound between a protection plan and a resource and provides information about their statuses.



Resource
A resource (also known as a workload) is a data source, such as physical and virtual hosts, databases, mailboxes, websites, etc., that can be the subject of a protection plan.
From the perspective of policies and applications, resources serve as contexts to which policy rules or settings are applied and executed.





Data format
The API uses the secure HTTP/1.1 over TLS 1.2 protocol, and operates mostly with JSON-formatted messages.


Location
The Acronis Resource and Policy Management API consists of two APIs that are available at the following URLs (the API base URLs)

Resource Management API is available at: <datacenter_url>/api/resource_management/v<version>, where:
Policy Management API is available at: <datacenter_url>/api/policy_management/v<version>, where:


<datacenter_url> is the URL of the Acronis data center where the client using the API is registered.

<version> is the API version number.
The Resource Management API and the Policy Management API are currently version 4.







In this section

API error codes
Managing resources
Managing protection plans and policies