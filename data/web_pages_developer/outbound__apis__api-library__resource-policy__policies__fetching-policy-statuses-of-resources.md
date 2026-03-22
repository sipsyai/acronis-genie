---
title: "Fetching policy execution statuses of resources"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/fetching-policy-statuses-of-resources.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:47.416740"
---

# Fetching policy execution statuses of resources

Fetching policy execution statuses of resources

To fetch policy execution statuses of resources

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



[Optional] Define a variable named filters, and then assign an object containing the ID of the tenant which policy statuses need to be fetched to this variable:
>>> filters = {
...     'tenant_id': '5b15f6e1-88ec-4dce-b523-0e8394c0bc19'
... }



Note
To fetch policy statuses of multiple tenants, provide the tenant IDs in the following format:

Multiple tenants - or(5b15f6e1-88ec-4dce-b523-0e8394c0bc19,c70134c4-a244-4b22-99ad-e081301f7530)
All except specific tenants - not(5b15f6e1-88ec-4dce-b523-0e8394c0bc19,c70134c4-a244-4b22-99ad-e081301f7530)



Send a GET request to the /policy_management/v4/policy_statuses endpoint:
>>> response = requests.get(
...     f'{base_url}/policy_management/v4/policy_statuses',
...     headers=auth,
...     params=filters,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with the items key, containing an array of objects with resource data and status of its policies execution as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'context': {'agent_id': '23effcf6-2798-4631-9a52-5785bf3af657',
'agent_name': 'DESKTOP-JRPTA4A',
'id': '5c350066-2ba6-4eeb-aa91-1213dd35f033',
'name': 'DESKTOP-JRPTA4A',
'tenant_id': '17',
'tenant_name': '',
'type': 'resource.machine',
'user_defined_name': 'DESKTOP-JRPTA4A'},
'policies': [{'names': [],
'next_run_time': '2020-10-12T12:10:00Z',
'running': {'state': 'idle'},
'status': 'ok',
'type': 'policy.security.patch_management'},
...]}],
'paging': {'cursors': {'total': 1}}}