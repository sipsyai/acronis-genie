---
title: "Enabling a service for a sub-tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/services/enabling-service.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:46.663828"
---

# Enabling a service for a sub-tenant

Enabling a service for a sub-tenant

To enable a service for a sub-tenant

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



Obtain the UUID of the parent tenant of this sub-tenant.
You will need this UUID to list services that can be enabled for child tenants.

Fetch the tenant information as described in steps 3-5 of Fetching information about an individual tenant.
As the result, you should have a tenant variable with the tenant object.
Define a variable named parent_tenant_id, and then assign the value of the parent_id key from the tenant object to this variable:
>>> parent_tenant_id = tenant['parent_id']
>>> parent_tenant_id
'ede9f834-70b3-476c-83d9-736f9f8c7dae'





Obtain the list of services enabled for the tenant, which UUID is specified in the parent_tenant_id variable, as described in steps 3-6 of Fetching information about services enabled for a tenant.
As the result, you should have a tenant_applications variable with the list of service objects.
In this list, find the service that you want to enable by its internal name (the value of a service object’s type key) and store its UUID (the value of a service object’s id key) in a variable named application_id:
>>> application_id = None
>>> for application in tenant_applications:
...     if application['type'] == 'backup':
...         application_id = application['id']
...         break
... else:
...     print('Cannot enable the backup service for this tenant.')
...
>>> application_id
'6e6d758d-8e74-3ae3-ac84-50eb0dff12eb'



Send a POST request to the /applications/{application_id}/bindings/tenants/{tenant_id} endpoint:
>>> response = requests.post(
...     f'{base_url}/applications/{application_id}/bindings/tenants/{tenant_id}',
...     headers=auth,
... )



Check the status code of the response:
>>> response.status_code
204



Status code 204 means that the platform has enabled the service for the tenant.
Enabling a service does not enable its offering item(s), if any. The offering item(s) must be enabled separately.


Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.