---
title: "Changing storage quotas of partner sub-tenants"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tutorials/changing-storage-quotas.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:20.980982"
---

# Changing storage quotas of partner sub-tenants

Changing storage quotas of partner sub-tenants
In this procedure, the storage offering item of the advanced edition will be used as an example.

To change storage quotas of partner sub-tenants

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Use the sub-tenant created via the API or find the sub-tenant and store its UUID:
>>> tenant_id = created_tenant_id
>>> tenant_id
'95303d96-628c-4265-9afa-07bee3fccf39'



Fetch the list of all offering items of the advanced for the tenant as described in Fetching available offering items.
As the result, you must have a variable assigned with the list of all offering items available for the tenant:
>>> offering_items = fetched_offering_items['items']
>>> pprint.pprint(offering_items)
[{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'infra_id': '51ac5df1-f53b-4b09-b1e5-687fe5dedc23',
'locked': False,
'measurement_unit': 'bytes',
'name': 'adv_storage',
'quota': {'overage': None, 'value': None, 'version': 0},
'status': 1,
'type': 'infra',
'usage_name': 'storage'},
...]



Important

The quota limits are removed by setting the value (soft quota)
and/or overage (hard quota) attributes to None.
Setting the value (soft quota) to 0 will set it to zero.
This means that the offering item will not be available to
the tenant since the quota will be already exceeded.
Setting the value (soft quota) limit to None will reset
the version to 0 and the overage to None.
Disabled offering items do not have the quota object.



Fetch the storages of the tenant, as described in Fetching storages and store the UUID of the storage:
>>> infra_id = fetched_infra_id
>>> infra_id
'019097a6-114f-4418-bd54-e01ef049f209'


>>> infra_id = fetched_infra_id
>>> infra_id
'019097a6-114f-4418-bd54-e01ef049f209'



Iterate over the list of the offering items and set the soft quota for the storage to 214748364800
bytes (200 gibibytes) with specified infra_id.
>>> for offering_item in offering_items:
...     # Check if the offering item is enabled, if it is infra and contains specified "infra_id"
...     if offering_item['status'] \
...             and offering_item['type'] == 'infra' \
...             and offering_item['infra_id'] == infra_id :
...         if offering_item['usage_name'] == 'storage':
...             offering_item['quota']['value'] = 214748364800  #  measurement_unit - bytes



Define a variable named updated_offering_items, and then assign an object with the offering_items key with the list of offering items to this variable:
>>> updated_offering_items = {
...     'offering_items': offering_items
... }



Convert the updated_offering_items object to a JSON text:
>>> updated_offering_items = json.dumps(updated_offering_items, indent=4)



Send a PUT request with the JSON text to the /tenants/{tenant_id}/offering_items endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{tenant_id}/offering_items',
...     headers={'Content-Type': 'application/json', **auth},
...     data=updated_offering_items,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the quotas of the offering items have been changed.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with the updated offering item quotas, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'infra_id': '51ac5df1-f53b-4b09-b1e5-687fe5dedc23',
'locked': False,
'measurement_unit': 'bytes',
'name': 'adv_storage',
'quota': {'overage': None,
'value': 214748364800,
'version': 1565794018233},
'status': 1,
'type': 'infra',
'usage_name': 'storage'},
...]}