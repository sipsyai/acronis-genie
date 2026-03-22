---
title: "Setting the partner tenant tier level and the licensing mode"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/billing/setting-tier-licensing.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:23.395426"
---

# Setting the partner tenant tier level and the licensing mode

Setting the partner tenant tier level and the licensing mode

Warning

This can only be set for partner tenants.
The settings are not inherited by child tenants, and are set individually for each tenant.



To set the tier level and the licensing mode

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Assign either of the following values to the tenant_id variable – the UUID of a partner tenant created via the API or a partner tenant found by its name:
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



Define a variable named setting_name, and then assign a name of the licensing mode setting to this variable:
>>> setting_name = 'licensing_mode'



Define a variable named setting_value, and then assign an object with the value key containing the licensing mode to this variable:
>>> setting_value = {
...     'value': 'per_gb'
... }



Convert the setting_value object to a JSON text:
>>> setting_value = json.dumps(setting_value, indent=4)
>>> print(setting_value)
{
"value": 3
}



Send a PUT request with the JSON text to the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint:
>>> response = requests.put(
...     f'{base_url}/applications/{application_id}/settings/tenants/{tenant_id}/{setting_name}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=setting_value,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has successfully assigned the tenant with the licensing mode.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the tier level setting object, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'effective': None,
'name': 'licensing_mode',
'own': {'exclusive': False, 'lock': False, 'value': 'per_gb'}}



Define a variable named setting_name, and then assign a name of the tier level setting to this variable:
>>> setting_name = 'tier_level_value'



Define a variable named setting_value, and then assign an object with the value key containing the tier level to this variable:
>>> setting_value = {
...     'value': 3
... }



Convert the setting_value object to a JSON text:
>>> setting_value = json.dumps(setting_value, indent=4)
>>> print(setting_value)
{
"value": 3
}



Send a PUT request with the JSON text to the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint:
>>> response = requests.put(
...     f'{base_url}/applications/{application_id}/settings/tenants/{tenant_id}/{setting_name}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=setting_value,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has assigned the tenant with the new tenant tier level.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the tier level setting object, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'effective': None,
'name': 'tier_level_value',
'own': {'exclusive': False, 'lock': False, 'value': 3}}