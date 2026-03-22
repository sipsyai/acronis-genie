---
title: "Fetching available offering items"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/offering-items/fetching-available-ois.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:12.905675"
---

# Fetching available offering items

Fetching available offering items

To fetch available offering items

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





Define a variable named params, and then assign a dictionary containing query string parameters to this variable:
>>> params = {}



[Optional] Apply the filtering by enabled or disabled offering items with the status query string parameter:
>>> params['status'] = 1 # Return only enabled offering items



[Optional] Apply the filtering by offering type with the type query string parameter:
>>> params['type'] = 'infra' # Return only offering items with type 'infra'. Possible values are 'infra', 'count' and 'feature'.



Send a GET request to the /tenants/{tenant_id}/offering_items endpoint:
>>> response = requests.get(
...     f'{base_url}/tenants/{tenant_id}/offering_items',
...     headers=auth,
...     params=params,
... )



Note
By default, this endpoint returns offering items of the (Legacy) Cyber Backup - Standard Edition. You can fetch
all offering items available for the tenant or user account by providing * or edition name in the edition
query string parameter. For more details, see Account Management API reference.


Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with the available offering items, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'standard',
'infra_id': '019097a6-114f-4418-bd54-e01ef049f209',
'locked': False,
'measurement_unit': 'bytes',
'name': 'storage',
'quota': {'overage': None, 'value': None, 'version': 0},
'status': 1,
'type': 'infra',
'usage_name': 'storage'},
{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'edition': 'standard',
'infra_id': 'debe7865-fa8d-4c16-8e26-adcf8d7fd23d',
'locked': False,
'measurement_unit': 'bytes',
'name': 'dr_storage',
'quota': {'overage': None, 'value': None, 'version': 0},
'status': 1,
'type': 'infra',
'usage_name': 'dr_storage'},
...]}