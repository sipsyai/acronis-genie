---
title: "Updating a workload"
source: "https://developer.acronis.com/doc/connector/managing-workloads/updating-workloads/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:48.751572"
---

# Updating a workload

Updating a workload
You can update information about the workload by sending a PATCH request to the /api/workload_management/v5/workloads/{workload_id} endpoint.

Request structure







Parameter
Type
Description



name
string
A name of the workload.

attributes
object
A key-value map of workload attributes. Allowed values are defined by the attributes schema specified in the Vendor Portal.

client_id
string
An identifier of the API client that created the workload. Must be the client ID of your application.

allowed_actions
array of string
A list of workload action identifiers that are allowed for this workload.

enabled
boolean
Status of the workload. True if enabled, false otherwise.



Example of the workload update payload:
{
"name": "New virtual machine name",
"attributes": {
"hostname": "CORP-123456",
"mac_address": "0a:df:7e:25:36:7e"
}
}




Response structure
If the workload was updated successfully, the response returns status 204, without payload.

In this section

Step-by-step procedure