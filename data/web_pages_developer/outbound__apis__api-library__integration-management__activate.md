---
title: "Activating an integration"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/integration-management/activate.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:19.175679"
---

# Activating an integration

Activating an integration

To activate an integration

Authenticate to the cloud platform via the Python shell.
These variables should be available:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/integration_management/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define these common variables, which describe the integration and will be used in status reporting requests:
# Replace '<vendor.application>' with your application code
>>> application_code = '<vendor.application>'
>>> module = {'name': 'Integration backend', 'version': '1.0.0'}
>>> vendor_system = {'name': 'Product integrated with Acronis', 'version': '22.04.1'}



Define a variable named status, and then assign a dictionary with information about the integration status to this variable:
>>> status = {
...     'application_code': application_code,
...     'module': module,
...     'vendor_system': vendor_system,
...     'events': [{'category': 'activation', 'action': 'activated integration', 'activation_event': True}],
... }



[Optional] Define the target_tenant_id variable and specify the tenant UUID where you want to report the integration activation:
>>> target_tenant_id = tenant_id



Convert the status object to a JSON text:
>>> status = json.dumps(status, indent=4)



Send a POST request with the JSON text to the /status?tenantID={target_tenant_id} endpoint:
>>> response = requests.post(
...     f'{base_url}/status?tenantID={target_tenant_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=status,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the integration has been successfully activated.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes.