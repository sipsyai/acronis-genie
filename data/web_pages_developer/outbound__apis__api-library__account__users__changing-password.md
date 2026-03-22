---
title: "Changing a user account password"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/changing-password.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:37.031380"
---

# Changing a user account password

Changing a user account password

Important
The platform enforces the following rule for user account passwords:

Password may contain any unicode and special characters.

Also, the platform enforces the following rules for the /users/{user_id}/password endpoint:

Only API clients can access this endpoint.
Password can be changed only for user accounts located in sub-tenants.



To change a user account password

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



Define a variable named password, and then assign the new user password to this variable:
>>> password = {
...      "password": "newUserPassword312"
... }










Name
Value type
Required
Description



password
string
Yes
A new password.




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


Status code 204 means that the password has been successfully changed.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.