---
title: "Fetching user account information"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/fetching-user-info.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:53.884665"
---

# Fetching user account information

Fetching user account information

To fetch user account information

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



Send a GET request to the /users/{user_id} endpoint:
>>> response = requests.get(f'{base_url}/users/{user_id}', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the user account information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'activated': True,
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
'zipcode': ''
'types': ['billing']},
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



[Optional] Store the revision number of the user account, in case if you need to modify or delete it:
>>> version = response.json()['version']
>>> version
1