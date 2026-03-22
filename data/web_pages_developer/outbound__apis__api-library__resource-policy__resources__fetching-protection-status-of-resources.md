---
title: "Fetching the protection status of resources"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/resources/fetching-protection-status-of-resources.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:21.095076"
---

# Fetching the protection status of resources

Fetching the protection status of resources

To fetch the protection status of resources

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Send a GET request to the /resource_management/v4/resource_statuses endpoint:
>>> response = requests.get(f'{base_url}/resource_management/v4/resource_statuses', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with the items key, containing an array of objects with aggregate status of protection plan execution, resource, and policy information formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'aggregate': {'names': 'New protection plan', 'status': 'idle'},
'context': {'created_at': '2021-02-03T14:57:07.311022688Z',
'external_id': '5c350066-2ba6-4eeb-aa91-1213dd35f033@17',
'id': '5c350066-2ba6-4eeb-aa91-1213dd35f033',
'name': 'DESKTOP-JRPTA4A',
'tenant_id': '17',
'type': 'resource.machine',
'updated_at': '2021-02-04T07:19:51.764276308Z',
'user_defined_name': 'DESKTOP-JRPTA4A'},
'policies': [{'last_run': '2021-02-03T15:00:48Z',
'last_success_run': '2021-02-03T15:00:48Z',
'type': 'policy.backup.machine'}]},
{'aggregate': {'status': 'not_protected'},
'context': {'created_at': '2021-02-03T15:16:14.104982477Z',
'external_id': '60458941-d9be-4121-8c9f-95aaa09e4a4b@17',
'id': '60458941-d9be-4121-8c9f-95aaa09e4a4b',
'name': 'DESKTOP-AQXOA6B',
'tenant_id': '17',
'type': 'resource.virtual_machine.mshyperv',
'updated_at': '2021-02-04T07:19:51.764276308Z',
'user_defined_name': 'DESKTOP-AQXOA6B'}}
...],
'paging': {'cursors': {'total': 37}}}