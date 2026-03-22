---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/managing-workloads/fetching-workloads/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:21.678405"
---

# Step-by-step procedure

Step-by-step procedure

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL
'https://eu8.acronis.cloud'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Assuming that you have a customer tenant ID, store it in a variable:
>>> customer_tenant_id = '<customer tenant ID>'



Define a variable named params, and then assign an object with the include_all_attributes parameter to include all workload attributes to this variable:
>>> params = and ``search`` parameter to include all customer workload
...
{
# Include workload attributes in the response
"include_all_attributes": True,
"search": f"customerUuid = '{customer_tenant_id}'"
}



Send a GET request to the /api/workload_management/v5/workloads endpoint:
>>> response = requests.get(
...     f'{base_url}/api/workload_management/v5/workloads',
...     headers=auth,
...     params=params,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the list of workloads including all their attributes in the attributes field, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{
"items": [
{
"type_alias": "resource.machine",
"aggregates_detection_query": {},
"parent_child_relationship_query": [
{
"parent_type": "cti.a.p.wm.workload.v1.0~a.p.wm.group.v1.0~a.p.computers.v1.0"
}
],
"id": "2faf3f5c-0d7a-455f-bcf1-6fb7b8ec1bf2",
"created_at": "2023-11-07T14:40:01.976227998Z",
"updated_at": "2023-11-07T14:40:01.976227998Z",
"type": "cti.a.p.wm.workload.v1.0~a.p.wm.aspect.v1.0~vendor.application.mongodb.v1.0",
"is_auto_created": false,
"external_id": "2faf3f5c-0d7a-455f-bcf1-6fb7b8ec1bf2@286",
"tenant_id": "286",
"name": "MongoDB Server",
"user_defined_name": "MongoDB Server",
"attributes": {
"host_name": "DESKTOP-ABC321SDF",
"mac_address": "00:00:00:00:00",
"status": "OK",
"db_version": "v3.4.9"
},
"client_id": "696fcfe0-1272-454c-99cc-24ec2e037613",
"aggregation_status": "NOT_AGGREGATED"
},
...
],
"paging": {
"cursors": {
"total": 3
}
},
"dynamic_group_creation_forbidden": false,
"_links": [
{
"rel": "self",
"href": "/api/workload_management/v5/workloads"
}
]
}