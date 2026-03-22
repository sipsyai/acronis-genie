---
title: "Fetch a workload ID linked to the recovery server"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/fetch-cloud-server-linked-workload.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:11.759254"
---

# Fetch a workload ID linked to the recovery server

Fetch a workload ID linked to the recovery server

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/dr/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Obtain scoped access token for the customer tenant.
As a result, the following variables should be available:
>>> scoped_auth # the 'Authorization' header value with the scoped access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the information about the recovery server by its ID and store the information in the recovery_server variable.
>>> recovery_server = response.json()



Read the contents of the recovery.resource_id field:
>>> recovery_server['recovery']['resource_id'] # identifier of the protected workload
'04f06cab-a2dc-412d-8284-efc30286d0d8'