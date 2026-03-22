---
title: "Searching for a user account by its login"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/searching/searching-for-user.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:38.203110"
---

# Searching for a user account by its login

Searching for a user account by its login

To search for a user account by its login

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /search endpoint.
The endpoint URL must contain a tenant query parameter set to the UUID of the tenant where the search will start and a text query parameter set to the login of a user account to be searched for:
>>> account_login = 'foobar'
>>> params = {'tenant': tenant_id, 'text': account_login}
>>> response = requests.get(f'{base_url}/search', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body text contains an encoded JSON object consisting of the items member. The items member is an array of result objects. If no resources containing the specified text are found, this array is empty.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


Convert the JSON text to an object, and then store the value of the object items key in a variable named results:
>>> results = response.json()['items']
>>> pprint.pprint(results)
[{'first_name': '',
'id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'kind': 'customer',
'last_name': '',
'name': 'Foobar',  # a match here
'obj_type': 'tenant',
'parent_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'path': ['JohnSmith, Inc', 'Foobar']},
{'first_name': 'John',
'id': '2ae8a1e9-4dba-4a07-b711-d9c83dc000f7',
'last_name': 'Doe',
'login': 'JohnDoe',
'obj_type': 'user',
'parent_id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'path': ['JohnSmith, Inc', 'Foobar']},  # a match in the email address
{'first_name': '',
'id': '2ae8a1e9-4dba-4a07-b56a-c51cec1485fc',
'last_name': '',
'login': 'foobar',  # a match here
'obj_type': 'user',
'parent_id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'path': ['JohnSmith, Inc', 'Foobar']}]



Find the object where the value of the obj_type key is user and the value of the login key equals to the login of a user account being searched for (account_login):
>>> found_account = None
>>> for res in results:
...     if res['obj_type'] == 'user' and res['login'] == account_login:
...         found_account = res
...         break
... else:
...     print('A user account with this login is not found.')
...
>>> pprint.pprint(found_account)
{'first_name': '',
'id': '2ae8a1e9-4dba-4a07-b56a-c51cec1485fc',
'last_name': '',
'login': 'foobar',
'obj_type': 'user',
'parent_id': '0fcd4a69-8a40-4de8-b711-d9c83dc000f7',
'path': ['JohnSmith, Inc', 'Foobar']}









Name
Value type
Description



obj_type
string
The type of a resource that this object represents.

id
string
The account UUID.

login
string
The account login.

parent_id
string
The UUID of a tenant where this account is registered.

first_name
string
The firstname value from the contact object of the account.

last_name
string
The lastname value from the contact object of the account.

path
array of strings
The path to the tenant, which UUID is specified in the parent_id member, relative to the tenant where the search started.