---
title: "Fetching a list of plans applicable for a resource"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/fetching-applicable-plans-for-resource.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:39.011221"
---

# Fetching a list of plans applicable for a resource

Fetching a list of plans applicable for a resource

To fetch a list of plans applicable for a resource

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the resources as described in Fetching a list of all resources, then define the
resource_id variable and assign it with the ID of a resource. As an example, the ID of the
first resource will be taken:
>>> resource_id = resources[0]['id']
>>> resource_id
'5c350066-2ba6-4eeb-aa91-1213dd35f033'



Define a variable named filters, and then assign an object containing the resource ID in the applicable_to_context_id key to this variable:
>>> filters = {
...     'applicable_to_context_id': resource_id
... }



Note
To fetch plans that are applicable to multiple resources, provide the resource IDs in the following format:
or(5b15f6e1-88ec-4dce-b523-0e8394c0bc19,c70134c4-a244-4b22-99ad-e081301f7530)


Send a GET request to the /policy_management/v4/policies endpoint:
>>> response = requests.get(f'{base_url}/policy_management/v4/policies', headers=auth, params=filters)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with the items key, containing an array of protection policy objects as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'policy': [{'created_at': '2020-03-19T21:01:17.548049845Z',
'days_without_backup_alert': None,
'default_name_template_id': '',
'deleted_at': None,
'enabled': True,
'id': 'd7836ee7-203a-4037-be0b-cabff37fa267',
'ls_features': '',
'name': 'My Protection Plan',
'origin': 'upstream',
'plan_hash': '',
'root_template_id': '',
'source_type': '',
'template': True,
'template_source_id': '',
'tenant_id': '23',
'type': 'policy.protection.total',
'updated_at': '2020-03-19T21:02:29.031812085Z'},
...]}],
'paging': {'cursors': {'total': 1}}}