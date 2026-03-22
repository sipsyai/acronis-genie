---
title: "Deleting all protection plans for a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/deleting-plans-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:34.795346"
---

# Deleting all protection plans for a tenant

Deleting all protection plans for a tenant

To delete all protection plans for a tenant

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named filters, and then assign an object containing the ID of the tenant where plans need to be deleted to this variable:
>>> filters = {
...     'tenant_id': '16'
... }



Note
For the list of available query string parameters, see the Resource and Policy Management API reference.


Send a DELETE request to the /policy_management/v4/policies endpoint:
>>> response = requests.delete(
...     f'{base_url}/policy_management/v4/policies',
...     headers=auth,
...     params=filters,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that all protection plans for the specified tenant have been successfully deleted.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.