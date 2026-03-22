---
title: "Enabling upsell of service editions for a sub-tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/upsell/enabling-editions-upsell.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:54.852301"
---

# Enabling upsell of service editions for a sub-tenant

Enabling upsell of service editions for a sub-tenant
The platform allows a partner to promote functionality of higher-tier service editions in a customer tenant. When the
platform setting is enabled for a tenant, its users will see UI elements with additional functionality that, when
selected, will show a message with a proposal to contact user’s sales representative or to buy one of the suggested
editions.
The following table describes what the user will see with the different roles and the “Buyer” type:







Company Administrator
Buyer
Result



Yes
Yes
Buy now *

Yes
No
Contact your sales representative

No
Yes
Contact your sales representative

No
No
Contact your sales representative



* The buy link will be shown only if branding is enabled and the “Buy URL” option is configured.

To enable upsell of service editions for a sub-tenant

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



Define a variable named setting_name, and then assign a name of the setting to this variable:
>>> setting_name = 'PromoteHigherEditions'



Define a variable named setting_state, and then assign an object with the value key containing status of the feature to this variable:
>>> setting_state = {
...     'value': True
... }



Convert the setting_state object to a JSON text:
>>> setting_state = json.dumps(setting_state, indent=4)
>>> print(setting_state)
{
"value": true
}



Send a PUT request with the JSON text to the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint:
>>> response = requests.put(
...     f'{base_url}/applications/{application_id}/settings/tenants/{tenant_id}/{setting_name}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=setting_state,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has enabled upsell of additional features available in other editions for the tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the edition status object, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'effective': None,
'name': 'PromoteHigherEditions',
'own': {'exclusive': False, 'lock': False, 'value': True}}