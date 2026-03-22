---
title: "Deleting a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/deleting-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:26.123286"
---

# Deleting a tenant

Deleting a tenant

To delete a tenant

Warning
Deleting a tenant is not a reversible operation. It results in the following:

All services enabled within this tenant and all of its sub-tenants stop operating.
All service-related data (e.g., backups, synced files) of this tenant and all of its sub-tenants are deleted.
All user accounts within this tenant and all of its sub-tenants are deleted.
The tenant and all of its sub-tenants are deleted.



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



Disable the tenant, as described in steps 3-7 of Disabling a tenant.
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