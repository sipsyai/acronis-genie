---
title: "Enabling quota upsell for a user account"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/upsell/enabling-quota-upsell.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:59.062410"
---

# Enabling quota upsell for a user account

Enabling quota upsell for a user account
To enable quota upsell, a partner can assign the Buyer type to a user account in a customer tenant. When the type is
assigned to a user account, the user will receive email notifications and alert notifications with a proposal to
contact user’s sales representative or to buy more quota when the quota is exceeded or almost reached.
The following table describes what the user will see with the different roles and the Buyer type:







Company Administrator
Buyer
Result



Yes
Yes
Buy now *

No
Yes
Contact your sales representative



* The buy link will be shown only if branding is enabled and the ‘Buy URL’ option is configured.

To enable quota upsell for a user account

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Assign the user_id variable the UUID of a user account created via the API or a user account found via search:
>>> user_id = created_user_id
>>> user_id
'1c234e69-5469-424a-a6d1-ff5658b387a6'



Fetch the revision number of the user account as described in the chapters above. The following variable should be available now:
>>> version
1



Define a variable named user_data, and then assign the user account status to update to this variable:
>>> user_data = {
...     'business_types': ['buyer'],
...     'version': version
... }










Name
Value type
Required
Description



business_types
array of strings
No
List of business types. The only available type for user accounts is buyer.

version
number
Yes
Revision number.




Convert the user_data object to a JSON text:
>>> user_data = json.dumps(user_data, indent=4)



Send a PUT request with the JSON text to the /users/{user_id} endpoint:
>>> response = requests.put(
...     f'{base_url}/users/{user_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=user_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the user account status has been successfully updated.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the user account information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'activated': True,
'business_types': ['buyer'],
'contact': {'address1': '',
'address2': '',
'city': '',
'country': '',
'email': 'johndoe@mysite.com',
'firstname': 'John',
'lastname': 'Doe',
'phone': '',
'state': '',
'zipcode': ''},
'created_at': '2019-07-25T07:11:02.807354+00:00',
'enabled': False,
'id': '1c234e69-5469-424a-a6d1-ff5658b387a6',
'idp_id': '11111111-1111-1111-1111-111111111111',
'language': 'en',
'login': 'JohnDoe',
'mfa_status': 'disabled',
'notifications': ['quota', 'reports', 'backup_daily_report'],
'personal_tenant_id': None,
'tenant_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'terms_accepted': False,
'version': 2}


The revision number increments with each update, so update the version variable where necessary.