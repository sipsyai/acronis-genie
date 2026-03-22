---
title: "Updating the brand logo"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/branding/updating-logo.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:57.101577"
---

# Updating the brand logo

Updating the brand logo

To update the brand logo

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





Define a variable named image_path, and then assign a path to the image to this variable:
>>> image_path = '<path_to_image>'



Important
If the path contains backslashes, remember to escape them with an additional backslash.


Define a variable named uploaded_file, and then assign an object with branding options to this variable:
>>> uploaded_file = {
...     'file': open(image_path, 'rb')
... }



Send a POST request to the /tenants/{tenant_id}/brand/logo endpoint:
>>> response = requests.post(
...     f'{base_url}/tenants/{tenant_id}/brand/logo',
...     headers=auth,
...     files=uploaded_file,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the logo has been uploaded and changed. Version number of the tenant will be also increased by 1.

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



[Optional] Increase the value of the tenant_version variable by 1:
>>> tenant_version = tenant_version + 1