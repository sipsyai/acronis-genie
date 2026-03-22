---
title: "Updating a location"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/updating-location.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:00.274088"
---

# Updating a location

Updating a location

To update a location

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Assign the location_id variable the UUID of a location created via the API or a location found in tenant’s locations:
>>> location_id = created_location_id
>>> location_id
'8fcd353b-0a40-40f2-9a55-ef8137d48800'



Fetch the revision number of the location as described in the chapters above. The following variable should be available now:
>>> version
0



Define a variable named location_data, and then assign the location information to update to this variable:
>>> location_data = {
...     "name": "Moscow Data Center",
...     "version": version
... }










Name
Value type
Required
Description



name
string
Yes
The new name of the location.

version
number
Yes
Revision number.




Convert the location_data object to a JSON text:
>>> location_data = json.dumps(location_data, indent=4)



Send a PUT request with the JSON text to the /locations/{location_id} endpoint:
>>> response = requests.put(
...     f'{base_url}/locations/{location_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=location_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the location has been successfully updated.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the updated location information, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'id': '8fcd353b-0a40-40f2-9a55-ef8137d48800',
'name': 'Moscow Data Center',
'owner_tenant_id': '0bb386ae-e66d-4e7b-84fb-cddcf60002de',
'platform_owned': True,
'readonly': False,
'version': 1}