---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/authentication/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:22.506083"
---

# Step-by-step procedure

Step-by-step procedure

Store the API client credentials that you have obtained when you created the CyberApp in the client_id and client_secret variables.
>>> client_id = '<your client ID>'
>>> client_secret = '<your client secret>'



Store the data center URL where the CyberApp will be deployed. This URL will be used for authentication and requests:
>>> datacenter_url = 'https://eu8.acronis.cloud'



Encode the client ID and client secret string using Base64 encoding and store the result in a variable:
>>> from base64 import b64encode  # Used for encoding to Base64
>>> encoded_client_creds = b64encode(f'{client_id}:{client_secret}'.encode('ascii'))



Define a variable named basic_auth, and then assign an object with the Authorization key containing authentication data to this variable:
>>> basic_auth = {
...     'Authorization': 'Basic ' + encoded_client_creds.decode('ascii')
... }



Send a POST request to the /bc/idp/token endpoint. The request should contain authentication data in the request headers and contain the grant_type field set to client_credentials in its body:
>>> response = requests.post(
...     f'{datacenter_url}/bc/idp/token',
...     headers={'Content-Type': 'application/x-www-form-urlencoded', **basic_auth},
...     data={'grant_type': 'client_credentials'},
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the platform has authenticated the API client and issued the API client a token for accessing API endpoints (an access token).
The response body text contains an encoded JSON object with this token and some other information.

Convert the JSON text that the response body contains to an object, and then store this object in a variable named token_info:
>>> token_info = response.json()
>>> pprint.pprint(token_info)
{'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...',
'expires_on': 1562910964,
'id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjI5ZT...',
'token_type': 'bearer'}



Define a variable named auth, and then assign an object, that will be used for constructing an Authorization header in API requests, to this variable:
>>> auth = {'Authorization': 'Bearer ' + token_info['access_token']}
>>> auth
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}


You will need to specify this variable in every request to the API as follows:
requests.get(f'{datacenter_url}/clients/{client_id}', headers=auth)