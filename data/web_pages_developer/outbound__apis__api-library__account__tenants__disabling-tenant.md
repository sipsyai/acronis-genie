---
title: "Disabling a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/disabling-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:30.357768"
---

# Disabling a tenant

Disabling a tenant

To disable a tenant

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





Define a variable named tenant_update, and then assign the following object to this variable:
>>> tenant_update = {
...     'enabled': False,
...     'version': tenant_version,  # this key is required
... }



Convert the tenant_update object to a JSON text:
>>> tenant_update = json.dumps(tenant_update, indent=4)
>>> print(tenant_update)
{
"enabled": false,
"version": 3
}



Send a PUT request with the JSON text to the /tenants/{tenant_id} endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{tenant_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=tenant_update,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has disabled the tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.