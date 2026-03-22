---
title: "Switching a customer tenant to production mode"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/switching-tenant-modes.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:12.554071"
---

# Switching a customer tenant to production mode

Switching a customer tenant to production mode
A customer tenant that is using services in trial mode can only be switched to production mode once.

Important

If you switch from trial to production in the middle of a month, the entire month will be included in the monthly service usage report.
For this reason, we recommend that you switch on the first day the month.


The mode is automatically switched to production when the tenant has been in trial mode for one full month.
The tenant mode is available in the tenant pricing settings.

To switch a customer tenant to production mode

Warning
Switching the customer tenant mode is not reversible.


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



Fetch the tenant pricing settings by sending a GET request to the /tenants/{tenant_id}/pricing endpoint:
>>> response = requests.get(f'{base_url}/tenants/{tenant_id}/pricing', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body contains the tenant pricing settings formatted as a JSON object.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text that the response body contains to an object, and then store this object in a variable named tenant_pricing:
>>> tenant_pricing = response.json()
>>> pprint.pprint(tenant_pricing)
{'currency': None,
'mode': 'trial',
'production_start_date': '2020-08-04T12:47:03',
'version': 1596545222672}



Change the value of the mode key to production in the tenant_pricing object:
>>> tenant_pricing['mode'] = 'production'



Convert the tenant_pricing object to a JSON text:
>>> tenant_pricing = json.dumps(tenant_pricing, indent=4)



Send a PUT request with the JSON text to the /tenants/{tenant_id}/pricing endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{tenant_id}/pricing',
...     headers={'Content-Type': 'application/json', **auth},
...     data=tenant_pricing,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has switched the tenant to production mode..

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.