---
title: "Fetching information about tenants"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/fetching-tenants.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:47.296838"
---

# Fetching information about tenants

Fetching information about tenants

To fetch information about tenants

Note
With the GET /tenants endpoint, you can also include information about contacts and offering items for the requested tenants.
For more details, see the Account Management API reference.


Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named tenant_ids, and then assign the UUIDs of tenants that you want to inspect to this variable:
>>> tenant_ids = [
...     '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
...     'ede9f834-70b3-476c-83d9-736f9f8c7dae',
...     '5138b44f-2d05-422f-8c5e-340332a76597',
... ]



Send a GET request to the /tenants endpoint.
The endpoint URL must contain a uuids query parameter set to a comma-separated string of the tenant UUIDs:
>>> uuids = ','.join(tenant_ids)
>>> response = requests.get(f'{base_url}/tenants', headers=auth, params={'uuids': uuids})



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body text contains an encoded JSON object consisting of the items member. The items member is an array of objects of the tenants, which UUIDs, from the list specified in the request, have been found in the platform.
If no UUIDs have been found, this array is empty.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text to an object, and then store the value of the object’s items key in a variable named tenants:
>>> tenants = response.json()['items']
>>> pprint.pprint(response.json())
[{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {...},
'customer_id': None,
'customer_type': 'default',
'enabled': True,
'has_children': True,
'id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'kind': 'partner', ...},
{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {...},
'customer_id': None,
'customer_type': 'default',
'enabled': True,
'has_children': False,
'id': '5138b44f-2d05-422f-8c5e-340332a76597',
'kind': 'customer', ...}]