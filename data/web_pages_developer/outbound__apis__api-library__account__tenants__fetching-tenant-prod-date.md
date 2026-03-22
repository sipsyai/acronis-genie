---
title: "Fetching the production start date of a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/fetching-tenant-prod-date.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:38.866997"
---

# Fetching the production start date of a tenant

Fetching the production start date of a tenant

To fetch the production start date of a tenant

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


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the object containing pricing information of the tenant, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'currency': None,
'mode': 'production',
'production_start_date': '2020-08-04T12:47:03',
'version': 1596545222672}



Fetch the production start date of the tenant:
>>> production_start_date = response.json()['production_start_date']
>>> production_start_date
'2020-08-04T12:47:03'


The following table describes the meaning of the production_start_date value for the three tenant modes:






Tenant mode
Production start date value



trial
ISO 8601 timestamp when tenant will be switched to production.

production
ISO 8601 timestamp when tenant was switched to production.

suspended
ISO 8601 timestamp when tenant was switched to production.