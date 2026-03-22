---
title: "Deleting a user account"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/deleting-user.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:45.447937"
---

# Deleting a user account

Deleting a user account

Warning

Deleting a user account results in all data associated with the user account being deleted.
This operation is not reversible.



To delete a user account

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



Disable the user account.
Fetch the revision number of the user account as described in Fetching user account information. The following variable should be available now:
>>> version
1



Define a variable named params, and then assign the version query string parameter to this variable:
>>> params = {
...     'version': version
... }










Name
Value type
Required
Description



version
number
Yes
Revision number.




Send a DELETE request to the /users/{user_id} endpoint:
>>> response = requests.delete(f'{base_url}/users/{user_id}', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the user account has been successfully deleted.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.