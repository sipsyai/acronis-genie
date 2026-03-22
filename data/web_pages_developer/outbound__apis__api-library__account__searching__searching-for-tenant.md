---
title: "Searching for a tenant by its name"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/searching/searching-for-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:33.970542"
---

# Searching for a tenant by its name

Searching for a tenant by its name

To search for a tenant by its name

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /search endpoint.
The endpoint URL must contain a tenant query parameter set to the UUID of the tenant where the search will start and a text query parameter set to the name of a tenant to be searched for:
>>> tenant_name = 'Foobar'
>>> params = {'tenant': tenant_id, 'text': tenant_name}
>>> response = requests.get(f'{base_url}/search', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means the response body text contains an encoded JSON object consisting of the items member. The items member is an array of result objects. If no resources containing the specified text are found, this array is empty.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text to an object, and then store the value of the object items key in a variable named results:
>>> results = response.json()['items']
>>> pprint.pprint(results)
[{'first_name': '',
'id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'kind': 'customer',
'last_name': '',
'name': 'Foobar',  # a match here
'obj_type': 'tenant',
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'path': ['JohnSmith, Inc', 'Foobar']},
{'first_name': 'John',
'id': '2ae8a1e9-4dba-4a07-b711-d9c83dc000f7',
'last_name': 'Doe',
'login': 'JohnDoe',
'obj_type': 'user',
'parent_id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'path': ['JohnSmith, Inc', 'Foobar']},  # a match in the email address
{'first_name': '',
'id': '2ae8a1e9-4dba-4a07-b56a-c51cec1485fc',
'last_name': '',
'login': 'foobar',  # a match here
'obj_type': 'user',
'parent_id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'path': ['JohnSmith, Inc', 'Foobar']}]



Find the object where the value of the obj_type key is tenant and the value of the name key equals to the name of a tenant being searched for (tenant_name):
>>> found_tenant = None
>>> for res in results:
...     if res['obj_type'] == 'tenant' and res['name'] == tenant_name:
...         found_tenant = res
...         break
... else:
...     print('A tenant with this name is not found.')
...
>>> pprint.pprint(found_tenant)
{'first_name': '',
'id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'kind': 'customer',
'last_name': '',
'name': 'Foobar',
'obj_type': 'tenant',
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'path': ['JohnSmith, Inc', 'Foobar']}









Name
Value type
Description



obj_type
string
The type of a resource that this object represents.

id
string
The tenant UUID.

name
string
The tenant name.

kind
string
The tenant type.

parent_id
string
The UUID of a tenant where this tenant is located.

first_name
string
The firstname value from the contact object of the tenant.

last_name
string
The lastname value from the contact object of the tenant.

path
array of strings
The path to this tenant relative to the tenant where the search started.