---
title: "Fetching resources with the protection plan"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/resources/fetching-resources-with-plan.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:37.984160"
---

# Fetching resources with the protection plan

Fetching resources with the protection plan

To fetch resources with the protection plan

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the protection plans, as described in Fetching a list of policies and protection plans.
As an example, the ID of the first protection plan will be taken. The following variable
should be available as the result:
>>> policy_id = fetched_protection_plans[0]['id']
>>> policy_id
114e46fb-9760-4e05-a50f-e15153def9ca



Define a variable named filters, and then assign an object containing the ID of the protection plan in the policy_id key and include_applied_context key set to true to this variable:
>>> filters = {
...     'policy_id': policy_id,
...     'include_applied_context': True
... }



Send a GET request to the /policy_management/v4/policies endpoint:
>>> response = requests.get(f'{base_url}/policy_management/v4/policies', headers=auth, params=filters)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes  and API error codes.

Also, the response body contains an object with the items key, containing an array of protection policy objects formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'context': {'items': ['5c350066-2ba6-4eeb-aa91-1213dd35f033']},
'policy': [{'created_at': '2020-12-10T17:41:52.914678091Z',
'days_without_backup_alert': None,
'default_name_template_id': '',
'deleted_at': None,
'enabled': True,
'id': '114e46fb-9760-4e05-a50f-e15153def9ca',
'ls_features': '',
'name': 'My Protection Plan',
'origin': 'upstream',
'plan_hash': '',
'root_template_id': '',
'source_type': '',
'template_source_id': '',
'tenant_id': '22',
'type': 'policy.protection.total',
'updated_at': '2020-12-10T17:41:52.912088286Z'},
...]}]}



Convert the JSON text that the response body contains to an object, and then fetch the first object
containing the information about the protection plan and the IDs of resources, to which the plan
is applied:
>>> plan_context_pair = response.json()['items'][0]



Fetch the list of resource IDs that have the applied plan:
>>> resource_ids = plan_context_pair['context']['items']
>>> resource_ids
['5c350066-2ba6-4eeb-aa91-1213dd35f033']