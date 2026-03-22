---
title: "Fetching information about services enabled for a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/services/fetching-services.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:09.303282"
---

# Fetching information about services enabled for a tenant

Fetching information about services enabled for a tenant

To fetch information about services enabled for a tenant

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



[To inspect services enabled for a sub-tenant] Assign either of the following values to the tenant_id variable – the UUID of a sub-tenant created via the API or a sub-tenant found by its name:
>>> tenant_id = created_tenant_id
>>> tenant_id
'0fcd4a69-8a40-4de8-b711-d9c83dc000f7'



Send a GET request to the /tenants/{tenant_id}/applications endpoint:
>>> response = requests.get(f'{base_url}/tenants/{tenant_id}/applications', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body text contains an encoded JSON object consisting of the items member. The items member is an array of UUIDs of services that are enabled for this tenant and can be enabled for its sub-tenants. If no services are enabled, this array is empty.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

>>> application_ids = response.json()['items']
>>> pprint.pprint(application_ids)
['6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'b71b2c18-590a-303c-9d5a-8444fbe713ac',
'7459244f-68f3-3bf4-9f53-5f63ecc1d91f']



[Optional] Translate these UUIDs to service objects:

Fetch the services information as described in steps 2-4 of Fetching information about all platform services.
As the result, you should have an applications variable with the list of service objects.
Iterate over these objects and collect the ones, which value of the id key is present in the application_ids list, and then store them, for example, as a separate list in a variable named tenant_applications:
>>> ids = set(application_ids)
>>> tenant_applications = [app for app in applications if app['id'] in ids]
>>> pprint.pprint(tenant_applications)
[{'api_base_url': '/bc/',
'id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'name': 'Backup',
'type': 'backup',
'usages': ['workstations',
'servers',
'vms',
'mobiles',
'virtualhosts',
'win_server_essentials',
'mailboxes',
'storage',
'workstation_storage',
'server_storage',
'vm_storage',
'mobile_storage',
'virtualhost_storage',
'win_server_essentials_storage',
'mailbox_storage', ...]},
{'api_base_url': '/pds/',
'id': 'b71b2c18-590a-303c-9d5a-8444fbe713ac',
'name': 'Physical Data Shipping',
'type': 'physical_data_shipping',
'usages': ['drives_shipped_to_cloud', 'drives_shipped_from_cloud']},
{'api_base_url': '/mc/',
'id': '7459244f-68f3-3bf4-9f53-5f63ecc1d91f',
'name': 'Management Portal',
'type': 'platform',
'usages': []}]