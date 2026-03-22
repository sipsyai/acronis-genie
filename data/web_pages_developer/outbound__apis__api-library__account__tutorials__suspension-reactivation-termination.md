---
title: "Suspending / Reactivating / Terminating"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tutorials/suspension-reactivation-termination.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:42.082820"
---

# Suspending / Reactivating / Terminating

Suspending / Reactivating / Terminating

Suspending a partner or customer
If you want to temporarily suspend a service for a partner or customer, you can disable their tenant in the platform.
This will restrict access to the platform services for all user accounts located in the tenant and its sub-tenants.

Note

When you disable a tenant, the service-related data will be preserved in the platform.
Therefore, Acronis will continue to bill for disabled customer usage.



To suspend a partner or customer

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






Reactivating a suspended partner or customer
If you want a suspended customer or partner to begin using the services again, you can re-enable their tenant.
This allows access to the platform services for all user accounts located in the tenant and its sub-tenants.

To reactivate a suspended partner or customer

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
...     'enabled': True,
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


Status code 200 means that the platform has re-enabled the tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.






Terminating a partner or customer relationship
If a partner or customer no longer wants to use the services, you can delete their tenant.

Warning
Deleting a tenant is an irreversible operation. It results in:

All services enabled within this tenant and all sub-tenants cease to operate.
Deletion of all service-related data (e.g., backups, synced files) of this tenant and all sub-tenants.
Deletion of all user accounts within this tenant and all sub-tenants.
Deletion of all sub-tenants.



To terminate a partner or customer relationship

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


Obtain the number of the latest tenant revision.
You will have to specify this number in a subsequent request to the tenant.
This is required to manage concurrent tenant modifications.

Fetch the tenant information as described in steps 3-5 of Fetching information about an individual tenant.
As the result, you should have a tenant variable with the tenant object.
Define a variable named tenant_version, and then assign the value of the version key from the tenant object to this variable:
>>> tenant_version = tenant['version']
>>> tenant_version
3





Send a DELETE request to the /tenants/{tenant_id} endpoint.
The endpoint URL must contain a version query parameter set to the number of the latest tenant revision:
>>> params = {'version': tenant_version}
>>> response = requests.delete(f'{base_url}/tenants/{tenant_id}', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the platform has deleted the tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.