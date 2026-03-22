---
title: "Fetching tenants usage batch"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/usage-reporting/tenants-usage.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:20.161425"
---

# Fetching tenants usage batch

Fetching tenants usage batch

Tenants and personal tenants provide metrics of service usage on level of offering items.
A Personal tenant represents a tenant bound to a specific user account, and is used only to control user account quotas and to collect user account real usage of a service.


To fetch tenants usage batch

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Collect the tenant UUIDs using search and define an array to store them. The following variable will be used as an example:
>>> tenant_ids
['d8515984-648a-4a38-9aeb-c91ec704ccda', '6838f6a2-42b4-44a3-8c7f-2a796185951c']



Define a variable named params, and then assign the tenants query string parameter to this variable:
>>> params = {
...     'tenants': ','.join(tenant_id)
... }










Name
Value type
Required
Description



tenants
string
Yes
Comma-separated tenant UUIDs.

usage_names
string
No
A filter of usages by comma-separated list of usage names. For example: storage,local_storage

editions
string
No
A filter of usages by comma-separated list of editions. For example: standard,advanced,disaster_recovery




Send a GET request to the /tenants/usages endpoint:
>>> response = requests.get(f'{base_url}/tenants/usages', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with usages of the specified tenants, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'tenant': 'd8515984-648a-4a38-9aeb-c91ec704ccda',
'usages': [{'absolute_value': 0,
'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'standard',
'infra_id': '019097a6-114f-4418-bd54-e01ef049f209',
'measurement_unit': 'bytes',
'name': 'storage',
'usage_name': 'storage',
'offering_item': {'quota': {'overage': None,
'value': None,
'version': 0},
'status': 1},
'range_start': '2019-08-01T00:00:00',
'tenant_id': 1326401,
'type': 'infra',
'value': 0}, ...]},
{'tenant': '6838f6a2-42b4-44a3-8c7f-2a796185951c',
'usages': [{'absolute_value': 0,
'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'standard',
'infra_id': '019097a6-114f-4418-bd54-e01ef049f209',
'measurement_unit': 'bytes',
'name': 'storage',
'usage_name': 'storage',
'offering_item': {'quota': {'overage': None,
'value': None,
'version': 0},
'status': 1},
'range_start': '2019-08-01T00:00:00',
'tenant_id': 1318423,
'type': 'infra',
'value': 0}, ...]}]}






To fetch cloud and immutable storage usages

Note
The immutable_storage usage may not appear in the service usage until its information is collected and updated by the service.


Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Collect the tenant UUIDs using search and define an array to store them. The following variable will be used as an example:
>>> tenant_ids
['d8515984-648a-4a38-9aeb-c91ec704ccda']



Define a variable named params, and then assign the tenants query string parameter to this variable:
>>> params = {
...     'tenants': ','.join(tenant_id),
...     'usage_names': 'storage,immutable_storage' # Total cloud storage used and Cloud storage used by immutable storage
... }



Send a GET request to the /tenants/usages endpoint:
>>> response = requests.get(f'{base_url}/tenants/usages', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with usages of the specified tenants, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'tenant': 'd8515984-648a-4a38-9aeb-c91ec704ccda',
'usages': [{'absolute_value': 344064,
'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'pck_per_workload',
'infra_id': '019097a6-114f-4418-bd54-e01ef049f209',
'measurement_unit': 'bytes',
'name': 'pw_base_storage',
'offering_item': {'quota': {'overage': None,
'value': None,
'version': 0},
'status': 1},
'range_start': '2025-06-01T00:00:00Z',
'tenant_id': 6492521,
'tenant_uuid': 'd8515984-648a-4a38-9aeb-c91ec704ccda',
'type': 'infra',
'usage_name': 'storage',
'value': 344064},
{'absolute_value': 200064,
'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'pck_per_workload',
'infra_id': '019097a6-114f-4418-bd54-e01ef049f209',
'measurement_unit': 'bytes',
'name': 'immutable_storage',
'range_start': '2025-06-01T00:00:00Z',
'tenant_id': 6492521,
'tenant_uuid': 'd8515984-648a-4a38-9aeb-c91ec704ccda',
'type': 'infra',
'usage_name': 'immutable_storage',
'value': 200064}]}]}