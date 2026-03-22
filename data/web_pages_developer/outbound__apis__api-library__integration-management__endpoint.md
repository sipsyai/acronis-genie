---
title: "API endpoint"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/integration-management/endpoint.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:27.589859"
---

# API endpoint

API endpoint
To report the integration activation status, the API client must use the /api/integration_management/v2/status endpoint.

Query string parameters

The endpoint accepts the tenantID query string parameter.
This parameter specifies the universally unique identifier (UUID) of the Acronis tenant for which the integration status is reported.


Note
Usually, this is an Acronis partner tenant, where the integration is configured.

If not specified, the tenant universally unique identifier (UUID) of the Acronis tenant where the API client is registered will be used.


Request body structure

Note
This describes the fields using the following JSON Path syntax:

. is a path to the object’s field.
[*] is an array that specifies all elements.

For example, the events[*].category notation means that events is an array
where all items are objects containing the category field.









Field
Type

Description



application_code

String.Up to 1000 chars.



Required if application_id is not specified.

CyberApp code in the vendor.application format.Mutually exclusive with application_id.




application_id
UUID string
Required if application_code is not specified.

ID of the integration.Mutually exclusive with application_code.




module
Object
Required
Information about integration.

module.name

String.Between 1 and 255 chars.



Required
Integration name.

module.version

String.Up to 255 chars.




Integration version.

vendor_system
Object

Information about the product integrated with Acronis.

vendor_system.name

String.Between 1 and 255 chars.



Required
Integrated product name.

vendor_system.version

String.Up to 255 chars.




Integrated product version.

events
Array of objects


List of events.Event represents an action that integration performed on a tenant.




events[*].category

String.Between 1 and 150 chars.



Required

Event category is an arbitrary string identifying a group of events.For example, “activation”.




events[*].action

String.Between 1 and 500 chars.



Required

Event action is an arbitrary string identifying an event.For example, “activated integration”.




events[*].activation_event

Boolean.Default false





Set to true if the event indicates that integration has been activated on a tenant.This flag will set activated_at to the time when the request was received if integration was inactive before.




events[*].deactivation_event

Boolean.Default false





Set to true if the event indicates that integration has been deactivated on a tenant.This flag will set deactivated_at to the time when the request was received if integration was active before.




activated_at

Date and time.RFC 3339 format.




The timestamp when integration was activated on a tenant.

deactivated_at

Date and time.RFC 3339 format.




The timestamp when integration was deactivated on a tenant.



Example
{
"application_code": "<vendor.application>",
"module": {
"name": "Integration backend",
"version": "1.0.0"
},
"vendor_system": {
"name": "Product integrated with Acronis",
"version": "22.04.1"
},
"events": [
{
"category": "activation",
"action": "activated integration",
"activation_event": true
}
]
}