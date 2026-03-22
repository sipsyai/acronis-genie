---
title: "Changing quotas"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/offering-items/changing-quotas.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:04.484702"
---

# Changing quotas

Changing quotas
Quotas enable you to limit the ability to use the service.
Quotas are managed through the offering items, which represent the set of services and service features.
The user account quotas are controlled via user account personal tenants.
There are two types of quotas:


Soft
The quota is considered “soft” when you do not set a quota overage.
This means that restrictions on using the backup service are not applied.



Hard
The quota is considered “hard” when you set a quota overage.
An overage allows to exceed the quota by the specified value.
When the overage is exceeded, restrictions on using the service are applied.



In this procedure, the vms, storage and workstations offering items of the advanced edition will be used as an example.

To change quotas

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch the UUID of the tenant which offering items and/or offering item quotas you want to modify:

To modify the quotas of a user account, use a personal tenant of the user account created via the API or find the user account and use its UUID to fetch the user account information and store its personal tenant UUID:
>>> tenant_id = created_user_personal_tenant_id
>>> tenant_id
'e18a5b6f-5ba4-44b0-8b41-033148877aee'



To enable/disable or modify quotas of a sub-tenant, use the sub-tenant created via the API or find the sub-tenant and store its UUID:
>>> tenant_id = created_tenant_id
>>> tenant_id
'95303d96-628c-4265-9afa-07bee3fccf39'





Fetch the list of all offering items of the advanced for the tenant as described in Fetching available offering items.
As a result, you will have a variable assigned with a list of all offering items available for the tenant:
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

Disabled offering items do not have the quota field.
The quota limits are removed by setting the value (soft quota)
and overage (hard quota) fields to None.
Setting value (soft quota) to 0 will set it to zero.
This means that the offering item will not be available to
the tenant since the quota will be already exceeded.
Setting value (soft quota) limit to None will reset
version to 0 and overage to None.
version must have the same value as in previously fetched
offering item object.



Iterate over the list of offering items and set the soft quota for the adv_vms to 15 virtual machines
and for the adv_workstations to 10 workstations.
>>> for offering_item in offering_items:
...     # Check if the offering item is enabled
...     if offering_item['status']:
...         if offering_item['name'] == 'adv_workstations':
...             offering_item['quota']['value'] = 10  #  measurement_unit - quantity
...         elif offering_item['name'] == 'adv_vms':
...             offering_item['quota']['value'] = 15  #  measurement_unit - quantity



[Optional] To change the quota of an offering item that is bound to an infrastructure:

Fetch the storages of the tenant as described in
Fetching storages and store the UUID of the storage:
>>> infra_id = fetched_infra_id
>>> infra_id
'019097a6-114f-4418-bd54-e01ef049f209'



Iterate over the list of the offering items and set the soft quota for the storage to 214748364800
bytes (200 gibibytes) with specified infra_id.
>>> for offering_item in offering_items:
...     # Check if the offering item is enabled and if it contains specified 'infra_id'
...     if offering_item['name'] == 'adv_storage' \
...             and offering_item['status'] \
...             and offering_item['infra_id'] == infra_id:
...         offering_item['quota']['value'] = 214748364800  #  measurement_unit - bytes





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

Also, the response body contains the items array with the updated offering item, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'locked': False,
'measurement_unit': 'quantity',
'name': 'adv_workstations',
'quota': {'overage': None,
'value': 10,
'version': 1565794018233},
'status': 1,
'type': 'count',
'usage_name': 'workstations'},
...
{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'advanced',
'locked': False,
'measurement_unit': 'quantity',
'name': 'adv_vms',
'quota': {'overage': None, 'value': 15, 'version': 1565794018233},
'status': 1,
'type': 'count',
'usage_name': 'vms'},
...
{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
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