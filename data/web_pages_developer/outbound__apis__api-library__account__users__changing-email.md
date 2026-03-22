---
title: "Changing a user account email"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/changing-email.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:32.828266"
---

# Changing a user account email

Changing a user account email

Note
You can only change the user account email if a user has opened the email confirmation link.


With this operation, the email will change if the user account was not activated.
If the user account was activated, an email confirmation link will be sent to the old user acount email address.


To change a user account email

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



Fetch the revision number of the user account, as described in Fetching user account information. The following variable should be available now:
>>> version
1



Define a variable named user_data, and then assign the user account email to update to this variable:
>>> user_data = {
...      "contact": {
...          "email": "johndoe@newmail.net"
...      },
...      "version": version
... }










Name
Value type
Required
Description



contact
contact object
No
The contact information of an account.

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


Status code 200 means that the email has been successfully changed (if the user account was not activated), or that an email confirmation link has been sent to the old email address of the user account if the user account was activated.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.




Important

The revision number will be incremented only if the email has been changed for a non-activated user account.