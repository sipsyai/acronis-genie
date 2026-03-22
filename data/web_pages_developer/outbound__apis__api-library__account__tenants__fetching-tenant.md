---
title: "Fetching information about an individual tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/fetching-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:43.081533"
---

# Fetching information about an individual tenant

Fetching information about an individual tenant

To fetch information about an individual tenant

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



[Optional] If you want to inspect a sub-tenant created via the API or a sub-tenant found by its name, assign its UUID to the tenant_id variable:
>>> tenant_id = created_tenant_id
>>> tenant_id
'0fcd4a69-8a40-4de8-b711-d9c83dc000f7'



Send a GET request to the /tenants/{tenant_id} endpoint:
>>> response = requests.get(f'{base_url}/tenants/{tenant_id}', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means the response body contains the tenant information formatted as a JSON text.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text that the response body contains to an object, and then store this object in a variable named tenant:
>>> tenant = response.json()
>>> pprint.pprint(tenant)
{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {...},
'customer_id': None,
'customer_type': 'default',
'default_idp_id': '11111111-1111-1111-1111-111111111111',
'enabled': True,
'has_children': False,
'id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'internal_tag': 'some.unique.tag.value',
'kind': 'customer',
'language': 'en',
'name': 'Foobar',
'owner_id': None,
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'update_lock': {...},
'version': 1}