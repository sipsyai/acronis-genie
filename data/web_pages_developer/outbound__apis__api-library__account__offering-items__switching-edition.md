---
title: "Switching the edition of a service"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/offering-items/switching-edition.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:25.506876"
---

# Switching the edition of a service

Switching the edition of a service
In this procedure, we assume that you have a customer sub-tenant with the Cyber Protection service enabled with the Per workload billing mode, and that you want to switch it to the Per gigabyte billing mode.

Important

Currently, editions are supported only by Cyber Protection and File Sync & Share services.
Switching to an unavailable edition will switch all offering items off. To re-enable them, see Enabling/disabling an offering item.



To switch the edition of a service

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Use the sub-tenant created via the API or find the sub-tenant and store its UUID:
>>> tenant_id = created_tenant_id
>>> tenant_id
'95303d96-628c-4265-9afa-07bee3fccf39'



Obtain the list of services enabled for the tenant, which UUID is specified in the tenant_id variable, as described in steps 3-6 of Fetching information about services enabled for a tenant.
As the result, you should have a tenant_applications variable with the list of service objects.
In this list, find the backup service (the value of a service object’s type key) and store its UUID (the value of a service object’s id key) in a variable named application_id:
>>> application_id = None
>>> for application in tenant_applications:
...     if application['type'] == 'backup':
...         application_id = application['id']
...         break
...
>>> application_id
'6e6d758d-8e74-3ae3-ac84-50eb0dff12eb'



Define a variable named switch_data, and then assign an object with the target_edition key containing a target edition and the application_id key containing the ID of the service to this variable:
>>> switch_data = {
...     'target_edition': 'pck_per_gigabyte',
...     'application_id': application_id
... }



Convert the updated_offering_items object to a JSON text:
>>> updated_offering_items = json.dumps(updated_offering_items, indent=4)



Send a PUT request with the JSON text to the /tenants/{tenant_id}/edition endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{tenant_id}/edition',
...     headers={'Content-Type': 'application/json', **auth},
...     data=updated_offering_items,
... )



Note
You can do a switching check before you actually apply the edition by
sending a GET request to the /tenants/{tenant_id}/edition endpoint.


Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the edition of the offering items has been updated.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the warning array, containing a list of warnings which occurred during the edition switching, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{"warnings": [""]}