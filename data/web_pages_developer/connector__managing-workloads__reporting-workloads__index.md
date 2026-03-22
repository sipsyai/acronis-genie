---
title: "Reporting workloads"
source: "https://developer.acronis.com/doc/connector/managing-workloads/reporting-workloads/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:40.357899"
---

# Reporting workloads

Reporting workloads

You can report workloads to Acronis Cyber Protect Cloud by sending a POST request to the /api/workload_management/v5/workloads endpoint.
Reported workloads appear in the Cyber Protection console.
Example:



Interaction diagram





Request structure







Parameter
Type
Description



items
array of object
A list of workloads to be reported.

items[*].type
string
The identifier of the workload type.

items[*].name
string
A name of the workload.

items[*].attributes
object
A key-value map of workload attributes. Allowed values are defined by the attributes schema specified in the Vendor Portal.

items[*].client_id
string
An identifier of the API client that created the workload. Must be the client ID of your application.

items[*].allowed_actions
array of string
A list of workload action identifiers that are allowed for this workload.

items[*].tenant_id
string
The identifier of the tenant where the workload was created.

items[*].enabled
boolean
Status of the workload. True if enabled, false otherwise.



Example of the workload:
{
"items": [
{
"type": "cti.a.p.wm.workload.v1.0~a.p.wm.aspect.v1.0~vendor.application.virtual_machine.v1.0",
"name": "MongoDB Server",
"attributes": {
"hostname": "DESKTOP-12ABC3D",
"mac_address": "0a:df:7e:25:36:7e"
},
"client_id": "696fcfe0-1272-454c-99cc-24ec2e037613",
"allowed_actions": [
"cti.a.ui.item.v1.0~a.ui.ext_p.workload_actions.action.v1.0~vendor.application.open_console.v1.0"
],
"tenant_id": "f234baa2-e404-4d78-93de-4f3a77448d02",
"enabled": true
}
]
}




Response structure
If the workloads were created successfully, the response returns status 204, without payload.

In this section

Step-by-step procedure