---
title: "Disabling a service for a sub-tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/services/disabling-service.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:42.425865"
---

# Disabling a service for a sub-tenant

Disabling a service for a sub-tenant

Warning
Disabling a service is not a reversible operation and results in the following:

The service becomes unavailable and stops operating within this tenant and all of its sub-tenants.
All offering items of the service are disabled for this tenant and all of its sub-tenants.
All service-related data (e.g., backups, synced files) that belongs to users of this tenant and all of its sub-tenants are deleted.



To disable a service for a sub-tenant

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



Obtain the list of services enabled for the tenant as described in steps 3-6 of Fetching information about services enabled for a tenant.
As the result, you should have a tenant_applications variable with the list of service objects.
In this list, find the service that you want to disable by its internal name (the value of a service object’s type key) and store its UUID (the value of a service object’s id key) in a variable named application_id:
>>> application_id = None
>>> for application in tenant_applications:
...     if application['type'] == 'backup':
...         application_id = application['id']
...         break
... else:
...     print('The backup service is not enabled for this tenant.')
...
>>> application_id
'6e6d758d-8e74-3ae3-ac84-50eb0dff12eb'



Important
Disabling the platform service, which is the management portal, is not possible.


Send a DELETE request to the /applications/{application_id}/bindings/tenants/{tenant_id} endpoint:
>>> response = requests.delete(
...     f'{base_url}/applications/{application_id}/bindings/tenants/{tenant_id}',
...     headers=auth,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the platform has disabled the service for the tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.