---
title: "Fetching the pricing information for a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/billing/fetching-pricing-info.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:14.992021"
---

# Fetching the pricing information for a tenant

Fetching the pricing information for a tenant

To fetch the pricing information for a tenant

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Assign either of the following values to the tenant_id variable – the UUID of a tenant created via the API or a tenant found by its name:
>>> tenant_id = created_tenant_id
>>> tenant_id
'0fcd4a69-8a40-4de8-b711-d9c83dc000f7'



Obtain the list of services enabled for the tenant, which UUID is specified in the tenant_id variable, as described in steps 3-6 of Fetching information about services enabled for a tenant.
As the result, you should have a tenant_applications variable with the list of service objects.
In this list, find the platform service (the value of a service object’s type key) and store its UUID (the value of a service object’s id key) in a variable named application_id:
>>> application_id = None
>>> for application in tenant_applications:
...     if application['type'] == 'platform':
...         application_id = application['id']
...         break
...
>>> application_id
'6e6d758d-8e74-3ae3-ac84-50eb0dff12eb'



Define a variable named setting_name, and then assign a name of the price list setting to this variable:
>>> setting_name = 'pricing_info'



Send a GET request to the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint:
>>> response = requests.get(
...     f'{base_url}/applications/{application_id}/settings/tenants/{tenant_id}/{setting_name}',
...     headers=auth,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the price list setting object, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'effective': None,
'name': 'pricing_info',
'own': {'exclusive': False,
'lock': False,
'value': {'currency': 'USD',
'licensing_mode': 'per_gb',
'pricing': [{'description': 'Cloud Storage',
'price': 0.09,
'sku': 'ACRCLST'},
{'description': 'Google Hosted Storage',
'price': 0.12,
'sku': 'ACRGLST'},
{'description': 'Local Storage',
'price': 0.05,
'sku': 'PRTLCST'}],
'tier_level': 'Minimal monthly payment 100 USD'}}}