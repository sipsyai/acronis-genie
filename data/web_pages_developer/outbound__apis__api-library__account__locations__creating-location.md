---
title: "Creating a location"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/creating-location.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:13.937248"
---

# Creating a location

Creating a location

To create a location

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named location_data, and then assign the new location data to this variable:
>>> location_data = {
...     "owner_tenant_id": tenant_id,
...     "name": "NYC Data Center"
... }










Name
Value type
Required
Description



owner_tenant_id
UUID string
Yes
The UUID of the tenant where the new location will be created.

name
string
Yes
The name of the new location.




Convert the location_data object to a JSON text:
>>> location_data = json.dumps(location_data, indent=4)



Send a POST request with the JSON text to the /locations endpoint:
>>> response = requests.post(
...     f'{base_url}/locations',
...     headers={'Content-Type': 'application/json', **auth},
...     data=location_data,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the platform has created a new location named NYC Data Center.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the location information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'id': '8fcd353b-0a40-40f2-9a55-ef8137d48800',
'name': 'NYC Data Center',
'owner_tenant_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae',
'platform_owned': False,
'readonly': False,
'version': 0}



[Optional] Store the UUID of the location and version, in case if you need to modify or delete it:
>>> location_id = response.json()['id']
>>> location_id
'8fcd353b-0a40-40f2-9a55-ef8137d48800'
>>> version = response.json()['version']
>>> version
0