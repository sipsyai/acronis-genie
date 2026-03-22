---
title: "Fetching information about an individual service"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/services/fetching-service.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:05.099114"
---

# Fetching information about an individual service

Fetching information about an individual service

To fetch information about an individual service

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Obtain the list of services enabled for the tenant, which UUID is specified in the tenant_id variable, or its sub-tenant as described in steps 2-5 of Fetching information about services enabled for a tenant.
As the result, you should have an application_ids variable with the list of service UUIDs.
Define a variable named application_id, and then assign the UUID of a service that you want to inspect to this variable:
>>> application_id = application_ids[0]
>>> application_id
'6e6d758d-8e74-3ae3-ac84-50eb0dff12eb'



Send a GET request to the /applications/{application_id} endpoint:
>>> response = requests.get(f'{base_url}/applications/{application_id}', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body contains the service information formatted as a JSON text.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text that the response body contains to an object, and then store this object in a variable named application:
>>> application = response.json()
>>> pprint.pprint(application)
{'api_base_url': '/bc/',
'id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'name': 'Protection',
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
'mailbox_storage', ...]}