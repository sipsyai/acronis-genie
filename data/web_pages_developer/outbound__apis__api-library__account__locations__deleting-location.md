---
title: "Deleting a location"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/deleting-location.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:22.344176"
---

# Deleting a location

Deleting a location

Important
If the location has registered storages, you must delete or move them first.
Otherwise, you will not be able to delete the location.


To delete a location

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




Send a DELETE request to the /locations/{location_id} endpoint:
>>> response = requests.delete(f'{base_url}/locations/{location_id}', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the location has been successfully deleted.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.