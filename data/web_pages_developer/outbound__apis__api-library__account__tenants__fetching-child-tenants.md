---
title: "Fetching information about child tenants"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/fetching-child-tenants.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:34.649267"
---

# Fetching information about child tenants

Fetching information about child tenants

To fetch information about child tenants

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



[Optional] If you want to inspect child tenants of a sub-tenant created via the API or a sub-tenant found by its name, assign its UUID to the tenant_id variable:
>>> tenant_id = created_tenant_id
>>> tenant_id
'0fcd4a69-8a40-4de8-b711-d9c83dc000f7'



Send a GET request to the /tenants/{tenant_id}/children endpoint.
A successful response will contain the UUIDs of child tenants of the specified tenant.
If you want to include the information about child tenants in the response, add an include_details query parameter with the true value to the endpoint URL:
>>> params = {'include_details': 'true'}
>>> response = requests.get(f'{base_url}/tenants/{tenant_id}/children', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body text contains an encoded JSON object consisting of the items member. The items member is an array of objects of the tenant’s child tenants. If the tenant has no child tenants, this array is empty.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text to an object, and then store the value of the object’s items key in a variable named child_tenants:
>>> child_tenants = response.json()['items']
>>> pprint.pprint(response.json())
[{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {...},
'customer_id': None,
'customer_type': 'default',
'default_idp_id': '11111111-1111-1111-1111-111111111111',
'enabled': True,
'has_children': True,
'id': '95303d96-628c-4265-9afa-07bee3fccf39',
'internal_tag': None,
'kind': 'customer',
'language': 'en',
'name': 'Customer, Inc',
'owner_id': None,
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'update_lock': {...},
'version': 2},
{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {...,
'customer_id': None,
'customer_type': 'default',
'default_idp_id': '11111111-1111-1111-1111-111111111111',
'enabled': True,
'has_children': True,
'id': '5138b44f-2d05-422f-8c5e-340332a76597',
'internal_tag': None,
'kind': 'customer',
'language': 'en',
'name': 'JohnDoe',
'owner_id': None,
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'update_lock': {...},
'version': 1}]