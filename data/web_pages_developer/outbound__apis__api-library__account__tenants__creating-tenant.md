---
title: "Creating a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/creating-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:21.913923"
---

# Creating a tenant

Creating a tenant

To create a tenant

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named tenant, and then assign an object containing the properties of a new tenant to this variable:
>>> tenant = {
...     'name': 'Foobar',
...     'kind': 'customer',
...     'parent_id': tenant_id,
...     'internal_tag': 'some.unique.tag.value',
...     'language': 'en',
...     'contact': {
...         'address1': '366 5th Ave',
...         'email': 'foo.bar@example.com',
...         'phone': '1 123 4567890',
...     },
... }


The object must contain the name, kind, and parent_id keys.
When specifying a value for the kind key, keep in mind the platform’s hierarchy described in "User accounts and tenants".
For example, it is not possible to create a unit tenant in a partner tenant.

If you do not specify a language key, the default language of the tenant will be English (en).
For the list of supported values, see Supported language codes.


Convert the tenant object to a JSON text:
>>> tenant = json.dumps(tenant, indent=4)



Send a POST request with the JSON text to the /tenants endpoint:
>>> response = requests.post(
...     f'{base_url}/tenants',
...     headers={'Content-Type': 'application/json', **auth},
...     data=tenant,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the platform has created a tenant with the specified properties.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the tenant information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {'address1': '366 5th Ave',
'address2': None,
'city': None,
'country': None,
'email': 'foo.bar@example.com',
'firstname': '',
'lastname': '',
'phone': '1 123 4567890',
'state': None,
'zipcode': None},
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
'update_lock': {'enabled': False, 'owner_id': None},
'version': 1}


Customer tenants are created in trial mode.
This mode means that usage data for the created tenant will not be included in monthly service usage reports.

Convert the JSON text that the response body contains to an object and store the value of the object’s id key in a variable named created_tenant_id, for example.
This UUID will be required for performing operations with the tenant:
>>> created_tenant_id = response.json()['id']
>>> created_tenant_id
'0fcd4a69-8a40-4de8-b711-d9c83dc000f7'