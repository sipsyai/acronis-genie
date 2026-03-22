---
title: "Provisioning a partner tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tutorials/provisioning-partner-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:37.865171"
---

# Provisioning a partner tenant

Provisioning a partner tenant
For this tutorial, you must have a partner tenant with:

Cyber Protect service enabled.
An API client created by the tenant administrator.

We will do the following:

Create a new partner tenant, using the POST /tenants endpoint.

Note
The partner tenant will be created in the production billing mode, Self-service management mode and Enhanced security enabled.


Enable all offering items for the new partner tenant, using the GET /tenants/{partner_id}/offering_items/available_for_child and PUT /tenants/{new_partner_id}/offering_items endpoints.

Note
This will automatically enable all the services that are available for your tenant.


Enable two-factor authentication for the new partner tenant, using the PUT /tenants/{new_partner_id}/mfa/status endpoint.
Create a user account in the new partner tenant, using the GET /users/check_login and POST /users endpoint.
Assign the Company administrator role to the new user account, using the PUT /users/{user_id}/access_policies endpoint.

Note
This will allow the user to manage its partner tenant.


Send an activation e-mail to the new user, using the POST /users/{user_id}/send-activation-email endpoint.


To provision a partner tenant

Authenticate and set up partner tenant variable

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named partner_id, and then assign the universally unique identifier (UUID) of your partner tenant to this variable:
>>> partner_id = tenant_id
>>> partner_id
'ede9f834-70b3-476c-83d9-736f9f8c7dae'






Create a partner tenant

Define a variable named partner, and then assign an object containing the minimum information about the partner tenant to this variable:
>>> partner = {
...     'name': 'Partner, Inc',
...     'kind': 'partner',
...     'parent_id': partner_id,
...     'customer_id': 'partner-service-provider',
...     'ancestral_access': False,
...     'enhanced_security': True
... }










Name
Value type
Required
Description



name
string
Yes
A tenant name. The name must be unique in your tenant hierarchy.

kind
string
Yes
A tenant type.

parent_id
UUID string
Yes
The UUID of a tenant where this tenant will be created.

customer_id
string
No
An arbitrary ID of the customer that can be used for reporting purposes.

ancestral_access
boolean
No (true by default)
If true, sets the Managed by service provider mode that allows access for parent tenant administrators. Otherwise, sets the Self-service management mode that restricts access to this tenant for parent tenant administrators.

enhanced_security
boolean
No (false by default)
If true, enables backups encryption. Cannot be turned off once enabled.




Convert the partner object to a JSON text:
>>> partner = json.dumps(partner, indent=4)
>>> print(partner)
{
"name": "Partner, Inc",
"kind": "partner",
"parent_id": "ede9f834-70b3-476c-83d9-736f9f8c7dae",
"customer_id": "partner-service-provider",
"ancestral_access": false,
"enhanced_security": true
}



Send a POST request with the JSON text to the /tenants endpoint:
>>> response = requests.post(
...     f'{base_url}/tenants',
...     headers={'Content-Type': 'application/json', **auth},
...     data=partner,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the platform has created the partner tenant in the production mode.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the tenant information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {...},
'customer_id': 'partner-service-provider',
'customer_type': 'default',
'default_idp_id': '11111111-1111-1111-1111-111111111111',
'enabled': True,
'has_children': False,
'id': '95303d96-628c-4265-9afa-07bee3fccf39',
'internal_tag': None,
'kind': 'partner',
'language': 'en',
'name': 'Partner, Inc',
'owner_id': None,
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'update_lock': {'enabled': False, 'owner_id': None},
'version': 1}



Define a variable named new_partner_id, and then assign the UUID of the created tenant to this variable:
>>> new_partner_id = response.json()['id']
>>> new_partner_id
'95303d96-628c-4265-9afa-07bee3fccf39'





Note
For more information about how the API represents tenants and what operations are available with them, see Managing tenants.



Enable two-factor authentication

Important

When enabling two-factor authentication, all users accounts in the configured tenant will be
required to set up two-factor authentication. They will be unable to log in until they
set it up.
For Unit tenants, two-factor authentication setting is inherited from the parent tenant.



Define a variable named mfa_status, and then assign an object with the enabled key containing desired status of two-factor authentication to this variable:
>>> mfa_status = {
...     'enabled': True
... }



Convert the mfa_status object to a JSON text:
>>> mfa_status = json.dumps(mfa_status, indent=4)
>>> print(mfa_status)
{
"enabled": true
}



Send a PUT request with the JSON text to the /tenants/{new_partner_id}/mfa/status endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{new_partner_id}/mfa/status',
...     headers={'Content-Type': 'application/json', **auth},
...     data=mfa_status,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has changed the status of two-factor authentication for the tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the information about the status of the two-factor authentication, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{
"mfa_status": "enabled",
"users_with_totp_enabled_count": 0,
"users_count": 0,
"update_allowed": true
}






Enable offering items for the partner tenant

Fetch the list of offering items available for partner tenants in your tenant by sending a GET request to the /tenants/{partner_id}/offering_items/available_for_child endpoint.
The endpoint URL should contain a kind query parameter set to partner:
>>> response = requests.get(
...     f'{base_url}/tenants/{partner_id}/offering_items/available_for_child',
...     headers=auth,
...     params={'kind': 'partner'},
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body text contains an encoded JSON object consisting of the items member. The items member is an array of objects of offering items that can be enabled for partner tenants. If no items can be enabled, this array is empty.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text to an object, and then store the value of the object items key in a variable named offering_items:
>>> offering_items = response.json()['items']
>>> pprint.pprint(offering_items)
[{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'infra_id': '019097a6-114f-4418-bd54-e01ef049f209',
'locked': False,
'measurement_unit': 'bytes',
'name': 'storage',
'quota': {'overage': None, 'value': None, 'version': 0},
'status': 1,
'type': 'infra'},
{'application_id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'locked': False,
'measurement_unit': 'quantity',
'name': 'workstations',
'quota': {'overage': None, 'value': None, 'version': 0},
'status': 1,
'type': 'count'}, ...]



Define a variable named items, and then assign a dict containing the list of all available offering items to this variable:
>>> items = {'offering_items': offering_items}



Convert the items object to a JSON text:
>>> items = json.dumps(items, indent=4)



Send a PUT request with the JSON text to the /tenants/{new_partner_id}/offering_items endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{new_partner_id}/offering_items',
...     headers={'Content-Type': 'application/json', **auth},
...     data=items,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has enabled all available offering items for the new partner tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.




Note

For more information about how the API represents services and what operations are available with them, see Managing services.
Information about offering items is available in Managing offering items and quotas.




Create a user account in the partner tenant

Define a variable named user_login, and then assign the login for a new user account to this variable:
>>> user_login = 'RichardDoe'



Check if this login is available in the platform. To do this, send a GET request to the /users/check_login endpoint.
The endpoint URL should contain a username query parameter set to the login:
>>> response = requests.get(
...     f'{base_url}/users/check_login',
...     headers=auth,
...     params={'username': user_login},
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the login is not taken by any other account registered in the platform.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Define a variable named account, and then assign an object containing the minimum information about the user account to this variable:
>>> account = {
...     'tenant_id': new_partner_id,
...     'login': user_login,
...     'contact': {
...         'email': 'richard.doe@example.com',
...         'firstname': 'Richard',
...         'lastname': 'Doe',
...     },
... }










Name
Value type
Required
Description



tenant_id
string
Yes
The UUID of a tenant where an account will be created.

login
string
Yes
An account login.

contact
object
Yes
The contact information of an account.

email
string
Yes
An email address that will be used for account activation and service notifications.

firstname
string
No
The first name of a user.

lastname
string
No
The last name of a user.




Convert the account object to a JSON text:
>>> account = json.dumps(account, indent=4)
>>> print(account)
{
"tenant_id": "95303d96-628c-4265-9afa-07bee3fccf39",
"login": "RichardDoe",
"contact": {
"email": "richard.doe@example.com",
"firstname": "Richard",
"lastname": "Doe"
}
}



Send a POST request with the JSON text to the /users endpoint:
>>> response = requests.post(
...     f'{base_url}/users',
...     headers={'Content-Type': 'application/json', **auth},
...     data=account,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that, in the partner tenant, the platform has created a non-activated user account with the RichardDoe login and a personal tenant.
The personal tenant is for managing the account’s offering item quotas.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the account information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'activated': False,
'business_types': [],
'contact': {'email': 'richard.doe@example.com',
'firstname': 'Richard',
'lastname': 'Doe', ...},
'created_at': '2019-07-09T06:03:00.502053+00:00',
'enabled': True,
'id': 'fb00afe1-c8c5-43c6-9ca5-76ea33091715',
'idp_id': '11111111-1111-1111-1111-111111111111',
'language': 'en',
'login': 'RichardDoe',
'notifications': ['quota', 'reports', 'backup_daily_report'],
'personal_tenant_id': 'b1ab6d40-f88e-46a3-9092-2aadeae0b888',
'tenant_id': '95303d96-628c-4265-9afa-07bee3fccf39',
'terms_accepted': False,
'version': 1}



Define a variable named user_id, and then assign the UUID of the created user account to this variable:
>>> user_id = response.json()['id']
>>> user_id
'fb00afe1-c8c5-43c6-9ca5-76ea33091715'





Note
For more information about how the API represents user accounts and what operations are available with them, see Managing user accounts.



Assign the company administrator role to the user account

Define a variable named roles, and then assign the following object containing the role information to this variable:
>>> roles = {
...     'items': [
...         {
...             'tenant_id': new_partner_id,
...             'trustee_id': user_id,
...             'role_id': 'partner_admin',
...             'id': '00000000-0000-0000-0000-000000000000',
...             'issuer_id': '00000000-0000-0000-0000-000000000000',
...             'trustee_type': 'user',
...             'version': 0,
...         },
...     ],
... }










Name
Value type
Required
Description



items
array of objects
Yes
The list of roles to be assigned to an account.

tenant_id
string
Yes
The UUID of a tenant where the account is registered.

trustee_id
string
Yes
The account UUID.

role_id
string
Yes
The internal name of a role.

id, issuer_id
string
Yes
The value must be 00000000-0000-0000-0000-000000000000.

trustee_type
string
Yes
The value must be user.

version
number
Yes
The value must be 0.




Convert the roles object to a JSON text:
>>> roles = json.dumps(roles, indent=4)
>>> print(roles)
{
"items": [
{
"tenant_id": "95303d96-628c-4265-9afa-07bee3fccf39",
"trustee_id": "fb00afe1-c8c5-43c6-9ca5-76ea33091715",
"role_id": "partner_admin",
"id": "00000000-0000-0000-0000-000000000000",
"issuer_id": "00000000-0000-0000-0000-000000000000",
"trustee_type": "user",
"version": 0
}
]
}



Send a PUT request with the JSON text to the /users/{user_id}/access_policies endpoint:
>>> response = requests.put(
...     f'{base_url}/users/{user_id}/access_policies',
...     headers={'Content-Type': 'application/json', **auth},
...     data=roles,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has assigned the specified role to the user account.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.




Note
For more information about user account roles, see Managing user account roles.



Send activation e-mail to the user

Send a POST request to the /users/{user_id}/send-activation-email endpoint:
>>> response = requests.post(
...     f'{base_url}/users/{user_id}/send-activation-email',
...     headers={'Content-Type': 'application/json', **auth}
... )


The /users/{user_id}/send-activation-email requires an empty JSON body.

Check the status code of the response:
>>> response.status_code
204


Status code 204 means that an email message with the activation link has been sent.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.




Note
For more information about activation of user accounts, see Activating a user account.