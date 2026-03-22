---
title: "Enabling the backup service for a user in a customer tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tutorials/tutorial.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:50.652183"
---

# Enabling the backup service for a user in a customer tenant

Enabling the backup service for a user in a customer tenant
For this tutorial, you must have a partner tenant with:

The backup service enabled.
The Workstations and Backup storage offering items enabled.
An activated administrator account.
This account will be used to perform the operations in the tenant via the API.

In this tutorial, we will:

Create a customer tenant in the partner tenant using the POST /tenants endpoint.
Enable the Workstations and Backup storage offering items for the new customer tenant using the
GET /tenants/{partner_id}/offering_items/available_for_child and PUT /tenants/{customer_id}/offering_items endpoints.

Note
This will automatically enable the backup service for the tenant.


Create a user account in the new customer tenant using the GET /users/check_login and POST /users endpoints.
Assign the Backup User role to the new user account using the PUT /users/{user_id}/access_policies endpoint.

Note
This will automatically enable the backup service with the Workstations and Backup storage offering items for the account, and will also set the same quotas for the account as the ones set for the tenant.


Activate the new account by setting its password using the POST /users/{user_id}/password endpoint.


To enable the backup service for a user in a customer tenant

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






Create a customer tenant in the partner tenant

Define a variable named customer, and then assign an object containing the minimum information about the customer tenant to this variable:
>>> customer = {
...     'name': 'Customer, Inc',
...     'kind': 'customer',
...     'parent_id': partner_id,
... }










Name
Value type
Required
Description



name
string
Yes
A tenant name.

kind
string
Yes
A tenant type.

parent_id
UUID string
Yes
The UUID of a tenant where this tenant will be created.




Convert the customer object to a JSON text:
>>> customer = json.dumps(customer, indent=4)
>>> print(customer)
{
"name": "Customer, Inc",
"kind": "customer",
"parent_id": "ede9f834-70b3-476c-83d9-736f9f8c7dae"
}



Send a POST request with the JSON text to the /tenants endpoint:
>>> response = requests.post(
...     f'{base_url}/tenants',
...     headers={'Content-Type': 'application/json', **auth},
...     data=customer,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the platform has created the customer tenant in the trial mode.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the tenant information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'ancestral_access': True,
'brand_id': 3579,
'brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0',
'contact': {...},
'customer_id': None,
'customer_type': 'default',
'default_idp_id': '11111111-1111-1111-1111-111111111111',
'enabled': True,
'has_children': False,
'id': '95303d96-628c-4265-9afa-07bee3fccf39',
'internal_tag': None,
'kind': 'customer',
'language': 'en',
'name': 'Customer, Inc',
'owner_id': None,
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'update_lock': {'enabled': False, 'owner_id': None},
'version': 1}



Define a variable named customer_id, and then assign the UUID of the created tenant to this variable:
>>> customer_id = response.json()['id']
>>> customer_id
'95303d96-628c-4265-9afa-07bee3fccf39'





Note
For more information about how the API represents tenants and what operations are available for them, see Managing tenants.



Enable offering items for the customer tenant

Fetch the list of offering items available for customer tenants of the partner tenant by sending a GET request to the /tenants/{partner_id}/offering_items/available_for_child endpoint.
The endpoint URL should contain a kind query parameter set to customer:
>>> response = requests.get(
...     f'{base_url}/tenants/{partner_id}/offering_items/available_for_child',
...     headers=auth,
...     params={'kind': 'customer'},
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body text contains an encoded JSON object consisting of the items member. The items member is an array of objects of offering items that can be enabled for customer tenants. If no items can be enabled, this array is empty.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the tenant information, formatted as a JSON text. When converted to an object, it will look like this:

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



In this list, find the objects where the value of the name key is either workstations (the Workstations offering item) or storage (the Backup storage offering item) and store them in the following items object:
>>> item_names = {'workstations', 'storage'}
>>> items_to_enable = [item for item in offering_items if item['name'] in item_names]
>>> items = {'offering_items': items_to_enable}



Convert the items object to a JSON text:
>>> items = json.dumps(items, indent=4)



Send a PUT request with the JSON text to the /tenants/{customer_id}/offering_items endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{customer_id}/offering_items',
...     headers={'Content-Type': 'application/json', **auth},
...     data=items,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has enabled the backup service with the specified offering items for the tenant.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.




Note

For more information about how the API represents services and what operations are available with them, see Managing services.
For more information about offering items, see Managing offering items and quotas.




Create a user account in the customer tenant

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
...     'tenant_id': customer_id,
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


Status code 200 means that the platform has created, in the customer tenant, an unactivated user account with the RichardDoe login and a personal tenant.
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



Assign the backup user role to the user account

Define a variable named roles, and then assign the following object containing the role information to this variable:
>>> roles = {
...     'items': [
...         {
...             'tenant_id': customer_id,
...             'trustee_id': user_id,
...             'role_id': 'backup_user',
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
"role_id": "backup_user",
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


Status code 200 means that the platform has assigned the specified role to the user account and enabled the backup service with the Workstations and Backup storage offering items for the account.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.




Note
For more information about user account roles, see Managing user account roles.



Activate the user account by setting its password

Define a variable named password, and then assign an object containing the password key with a password string to this variable:
>>> password = {'password': 'newUserPassword312'}


A password may be of any length and contain any unicode characters.

Convert the password object to a JSON text:
>>> password = json.dumps(password, indent=4)
>>> print(password)
{
"password": "newUserPassword312"
}



Send a POST request with the JSON text to the /users/{user_id}/password endpoint:
>>> response = requests.post(
...     f'{base_url}/users/{user_id}/password',
...     headers={'Content-Type': 'application/json', **auth},
...     data=password,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the platform has set the specified password for the user account and activated this account.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.




Note
For more information about activation of user accounts, see Activating a user account.