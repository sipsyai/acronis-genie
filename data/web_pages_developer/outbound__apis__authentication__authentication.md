---
title: "Authenticating to the Acronis platform"
source: "https://developer.acronis.com/doc/outbound/apis/authentication/authentication.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:27:28.436682"
---

# Authenticating to the Acronis platform

Authenticating to the Acronis platform

Important
To authenticate to the Acronis platform, you must have an activated administrator account.

By authenticating to the Acronis platform with an access token, the integration will have the right to perform operations in the tenant and its sub-tenants on behalf of the administrator.

Note

Before you begin, you must have started the Python shell and configured its session.
The requests, json, and pprint modules should be loaded in the interactive shell.



To authenticate to the Acronis platform

Register an API client in the tenant

Follow the procedures described in the Acronis Cyber Protect Cloud Partner Guide.
Define variables client_id, client_secret and datacenter_url and assign the saved client ID, client secret, and data center URL data from the previous step to them:

>>> client_id = '<your client ID>'
>>> client_secret = '<your client secret>'
>>> datacenter_url = '<the Acronis data center URL>'



Note
The Account Management API base URL is <your data center URL>/api/2.



Define a variable base_url and assign the Account Management API base URL to it.

>>> base_url = f'{datacenter_url}/api/2'







Issue an access token to the API client

Encode the client ID and client secret string using Base64 encoding, and store the result in a variable:

>>> from base64 import b64encode  # Used for encoding to Base64
>>> encoded_client_creds = b64encode(f'{client_id}:{client_secret}'.encode('ascii'))




Define a variable named basic_auth, and then assign an object with the Authorization key containing authentication data to this variable:
>>> basic_auth = {
...     'Authorization': 'Basic ' + encoded_client_creds.decode('ascii')
... }



Send a POST request to the /idp/token endpoint.
The request should contain authentication data in the request headers and contain the grant_type
field set to client_credentials in its body:
>>> response = requests.post(
...     f'{base_url}/idp/token',
...     headers={'Content-Type': 'application/x-www-form-urlencoded', **basic_auth},
...     data={'grant_type': 'client_credentials'},
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has authenticated the API client and issued the API client a token for accessing API endpoints (an access token).
The response body text contains an encoded JSON object with this token and some other information.

Convert the JSON text that the response body contains to an object, and then store {‘access_token’: ‘eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD…’, in a variable named token_info:
>>> token_info = response.json()
>>> pprint.pprint(token_info)
'expires_on': 1562910964,
'id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjI5ZT...',
'token_type': 'bearer'}



Define a variable named auth, and then assign an object, that will be used for constructing an Authorization header in API requests, to this variable:
>>> auth = {'Authorization': 'Bearer ' + token_info['access_token']}
>>> auth
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}


You will need to specify this variable in every request to the API as follows:
requests.get(f'{base_url}/clients/{client_id}', headers=auth)

In order to access an Acronis product API, update the base_url variable with the Acronis product API location:

>>> base_url = f'{datacenter_url}/<product API location>'



To find the appropriate Acronis API location, see the first page of the appropriate API chapter.




[For Account Management API only] Fetch the ID of the client’s tenant

Send a GET request to the /clients/{client_id} endpoint:
>>> response = requests.get(f'{base_url}/clients/{client_id}', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains an object with information about your API client formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{...
'data': {'client_name': 'My API client'},
'tenant_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'type': 'api_client'}



Define a variable named tenant_id, and then assign the ID of the tenant, fetched from the response body, to this variable:
>>> tenant_id = response.json()['tenant_id']
>>> tenant_id
'ede9f834-70b3-476c-83d9-736f9f8c7dae'




Your integration now has access to the appropriate Acronis API.