---
title: "Creating a user account"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/creating-user.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:41.248411"
---

# Creating a user account

Creating a user account

Important
The platform enforces the following rules for user account logins:


User account login must be at least 3 characters long. Otherwise, it will not be possible to find it via /search.
User account login can contain ASCII letters, numbers, and the following special characters: .@_-+:!#$%^*={}’`/?.
User account login must be sanitized and trimmed of any whitespace.
The user account email can be used as the user account login.




To create a user account

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable with the username query string parameter:
>>> login = "JohnDoe"  # username as login
>>> params = {"username": login}










Name
Value type
Required
Description



username
string
Yes
A username to check for availability.




Check if the login is available by sending a GET request to the /users/check_login endpoint:
>>> response = requests.get(f'{base_url}/users/check_login', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the specified login is not taken by any other account in the platform.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Define a variable named user_data, and then assign the user account contact information to this variable:
>>> user_data = {
...     "tenant_id": tenant_id,
...     "login": login,
...     "contact": {
...         "email": "johndoe@mysite.com",
...         "firstname": "John",
...         "lastname": "Doe",
...         "types": ["billing"]
...     }
... }










Name
Value type
Required
Description



tenant_id
UUID string
Yes
A tenant UUID where the user account will be created.

login
string
Yes
A login of the user account.

contact
contact object
Yes
The contact information of an account. Requires the email parameter.




Convert the user_data object to a JSON text:
>>> user_data = json.dumps(user_data, indent=4)



Send a POST request with the JSON text to the /users endpoint:
>>> response = requests.post(
...     f'{base_url}/users',
...     headers={'Content-Type': 'application/json', **auth},
...     data=user_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has created an unactivated user account with the JohnDoe login. If the user was created in the customer tenant, a personal tenant for this user also will be created.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the user account information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'activated': False,
'business_types': [],
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
'enabled': True,
'id': '1c234e69-5469-424a-a6d1-ff5658b387a6',
'idp_id': '11111111-1111-1111-1111-111111111111',
'language': 'en',
'login': 'JohnDoe',
'mfa_status': 'disabled',
'notifications': ['quota', 'reports', 'backup_daily_report'],
'personal_tenant_id': None,
'tenant_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'terms_accepted': False,
'version': 1}



Store the revision number and the UUID of the user account which will be required for user account management:
>>> user_id = response.json()['id']
>>> user_id
'1c234e69-5469-424a-a6d1-ff5658b387a6'
>>> version = response.json()['version']
>>> version
1


If this user account is created in the customer tenant, then also store the UUID of its personal tenant in a variable:
>>> personal_tenant_id = response.json()['personal_tenant_id']
>>> personal_tenant_id
'e18a5b6f-5ba4-44b0-8b41-033148877aee'




The next step is activation of the new user account.