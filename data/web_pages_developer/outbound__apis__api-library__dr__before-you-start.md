---
title: "Before you start"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/before-you-start.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:54.912519"
---

# Before you start

Before you start
Disaster Recovery API works in the scope of a specific customer tenant.
To ensure that correct resources are operated and proper permissions are granted,
the API client must have an access scope limited to the customer tenant.

Note
You can fetch a list of customer tenants using the Account Management API.
Refer to the corresponding documentation for more details.


Assuming that you have a customer tenant ID, store it in a variable:
>>> customer_tenant_id = '<customer tenant ID>'



Define a variable named scoped_data, and then assign the following values to this variable:
>>> scoped_data = {
...     "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
...     "assertion": token_info["access_token"],
...     "scope": f"urn:acronis.com:tenant-id:{customer_tenant_id}"
... }



Send a POST request to the /idp/token endpoint.
The request should contain authentication data in the request headers and contain the grant_type
field set to client_credentials in its body:
>>> response = requests.post(
...     f'{base_url}/idp/token',
...     headers={'Content-Type': 'application/x-www-form-urlencoded', **auth},
...     data=scoped_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has authenticated the API client and issued the scoped API client a token for accessing API endpoints (an access token).
When sending requests to API endpoints, the access token will have its access limited to the specified customer tenant ID.
The response body text contains an encoded JSON object with this token and some other information.

Convert the JSON text that the response body contains to an object, and then store this object in a variable named token_info:
>>> token_info = response.json()
>>> pprint.pprint(token_info)
{'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...',
'expires_on': 1562910964,
'id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjI5ZT...',
'token_type': 'bearer'}



In order to access Disaster Recovery APIs, update the base_url variable with the following path to the API:
>>> base_url = f'{datacenter_url}/api/dr/v2'
>>> base_url
'https://eu2.acronis.cloud/api/dr/v2'



Define a variable named scoped_auth, and then assign an object, that will be used for constructing an Authorization header in API requests, to this variable:
>>> scoped_auth = {'Authorization': 'Bearer ' + token_info['access_token']}
>>> scoped_auth
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}


You will need to specify this variable in every request to the API as follows:
requests.get(f'{base_url}/servers', headers=scoped_auth)


Now, your application is all set with access to the Disaster Recovery API.