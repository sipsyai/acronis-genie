---
title: "Enabling/disabling an offering item"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/offering-items/enabling-disabling-ois.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:08.689562"
---

# Enabling/disabling an offering item

Enabling/disabling an offering item
In this procedure, you will enable the vms and storage offering items and disable the workstations offering item of the advanced edition as an example.

To enable/disable an offering item

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



Fetch the list of all offering items of the advanced edition for the tenant as described in Fetching available offering items.
As the result, you must have a variable assigned with the list of all offering items available for the tenant:
>>> offering_items = fetched_offering_items['items']
>>> pprint.pprint(offering_items)
[{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'locked': False,
'measurement_unit': 'quantity',
'name': 'adv_workstations',
'quota': {'overage': None, 'value': None, 'version': 0},
'status': 1,
'type': 'count',
'usage_name': 'workstations'},
...
{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'locked': False,
'measurement_unit': 'quantity',
'name': 'adv_vms',
'quota': {'overage': None, 'value': None, 'version': 0},
'status': 1,
'type': 'count',
'usage_name': 'vms'},
...]



Important
Offering items cannot be disabled or enabled for a personal tenant.


Iterate over the list of the offering items and set the status to
0 for adv_workstations and 1 for adv_vms.
>>> for offering_item in offering_items:
...     # Disable 'workstations' offering item
...     if offering_item['name'] == 'adv_workstations':
...         offering_item['status'] = 0
...     # Enable 'vms' offering item
...     if offering_item['name'] == 'adv_vms':
...         offering_item['status'] = 1



[Optional] To manage an offering item that is bound to an infrastructure:

Fetch the storages of the tenant as described in Fetching storages and store the
UUID of the storage:
>>> infra_id = fetched_infra_id
>>> infra_id
'019097a6-114f-4418-bd54-e01ef049f209'



Iterate over the list of the offering items and set the status to 0 for adv_storage.
>>> for offering_item in offering_items:
...     if offering_item['name'] == 'adv_storage' and offering_item['infra_id'] == infra_id:
...         offering_item['status'] = 1





Important
For a customer tenant, only one storage can be enabled.


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


Status code 200 means that the offering items have been disabled.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with the updated offering items, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'locked': False,
'measurement_unit': 'quantity',
'name': 'adv_workstations',
'status': 0,
'type': 'count',
'usage_name': 'workstations'},
...
{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'locked': False,
'measurement_unit': 'quantity',
'name': 'adv_vms',
'status': 0,
'type': 'count',
'usage_name': 'vms'},
...
{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'infra_id': '019097a6-114f-4418-bd54-e01ef049f209',
'locked': False,
'measurement_unit': 'bytes',
'name': 'adv_storage',
'status': 1,
'type': 'infra',
'usage_name': 'storage'},
...]}