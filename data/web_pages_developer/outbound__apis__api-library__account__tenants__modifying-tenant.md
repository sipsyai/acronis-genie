---
title: "Modifying tenant properties"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/modifying-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:59.913567"
---

# Modifying tenant properties

Modifying tenant properties

To modify tenant properties

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Assign either of the following values to the tenant_id variable – the UUID of a sub-tenant created via the API or a sub-tenant found by its name:
>>> tenant_id = created_tenant_id
>>> tenant_id
'0fcd4a69-8a40-4de8-b711-d9c83dc000f7'



Obtain the number of the latest tenant revision.
You will have to specify this number in a subsequent request to the tenant.
This is required to manage concurrent tenant modifications.

Fetch the tenant information as described in steps 3-5 of Fetching information about an individual tenant.
As the result, you should have a tenant variable with the tenant object.
Define a variable named tenant_version, and then assign the value of the version key from the tenant object to this variable:
>>> tenant_version = tenant['version']
>>> tenant_version
3





Define a variable named tenant_properties, and then assign an object containing new values for the tenant properties to this variable:
>>> tenant_properties = {
...     'name': 'JohnDoe, Inc',
...     'internal_tag': 'custom.tag.value',
...     'language': 'fr',
...     'contact': {
...         'address1': 'Kingston, New York 12401',
...         'email': 'john.doe@example.com',
...         'phone': '1-541-754-3010',
...     },
...     'version': tenant_version,  # this key is required
... }


The following tenant properties can be safely modified, without affecting the users within the tenant and any service-related data: name, kind, language, internal_tag, contact.

Important
A kind property can only be changed from partner to folder and vice versa.


Convert the tenant_properties object to a JSON text:
>>> tenant_properties = json.dumps(tenant_properties, indent=4)
>>> print(tenant_properties)
{
"name": "JohnDoe, Inc",
"internal_tag": "custom.tag.value",
"language": "fr",
"contact": {
"address1": "Kingston, New York 12401",
"email": "john.doe@example.com",
"phone": "1-541-754-3010"
},
"version": 3
}



Send a PUT request with the JSON text to the /tenants/{tenant_id} endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{tenant_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=tenant_properties,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has updated the properties of the specified tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the information about the updated tenant, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {'address1': 'Kingston, New York 12401',  # an update here
'address2': None,
'city': None,
'country': None,
'email': 'john.doe@example.com',  # an update here
'firstname': '',
'lastname': '',
'phone': '1-541-754-3010',  # an update here
'state': None,
'zipcode': None},
'customer_id': None,
'customer_type': 'default',
'default_idp_id': '11111111-1111-1111-1111-111111111111',
'enabled': True,
'has_children': False,
'id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'internal_tag': 'custom.tag.value',  # an update here
'kind': 'customer',
'language': 'fr',  # an update here
'name': 'JohnDoe, Inc',  # an update here
'owner_id': None,
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'update_lock': {'enabled': False, 'owner_id': None},
'version': 4}  # a new revision number