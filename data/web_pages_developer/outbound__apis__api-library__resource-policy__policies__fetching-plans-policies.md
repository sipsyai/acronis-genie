---
title: "Fetching a list of policies and protection plans"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/fetching-plans-policies.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:43.214797"
---

# Fetching a list of policies and protection plans

Fetching a list of policies and protection plans

To fetch a list of policies and protection plans

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Send a GET request to the /policy_management/v4/policies endpoint:
>>> response = requests.get(f'{base_url}/policy_management/v4/policies', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with the items key, containing an array of protection policy objects as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'policy': [{'created_at': '2020-10-07T08:41:38.875763304Z',
'days_without_backup_alert': None,
'deleted_at': None,
'enabled': True,
'id': 'dac6c7c4-6b3f-4b46-9aa8-b78a189a0f10',
'ls_features': '',
'name': 'New protection plan',
'origin': 'upstream',
'plan_hash': '',
'source_type': '',
'template_source_id': '',
'tenant_id': '16',
'type': 'policy.protection.total',
'updated_at': '2020-10-07T08:41:38.87333237Z'},
...
{'created_at': '2020-10-07T08:41:38.949457464Z',
'days_without_backup_alert': None,
'deleted_at': None,
'enabled': True,
'id': '4d7d580c-32ac-468e-9688-e74906f5d765',
'ls_features': 'DataProtectionMap',
'origin': 'upstream',
'parent_ids': ['dac6c7c4-6b3f-4b46-9aa8-b78a189a0f10'],
'plan_hash': '',
'source_type': '',
'template_source_id': '',
'tenant_id': '16',
'type': 'policy.security.data_protection_map',
'updated_at': '2020-10-07T08:41:38.946928605Z'}]}],
'paging': {'cursors': {'total': 1}}}



Convert the JSON text, that the response body contains, to an object, and then fetch the list of policies from the response:
>>> policies = response.json()['items']



[Optional] Fetch the protection plans that will be used in related procedures:
>>> protection_plans = []
>>> for policy in policies:
...     if policy['type'] == 'policy.protection.total':
...         protection_plans.append(policy)