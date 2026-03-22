---
title: "Fetching locations"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/fetching-locations.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:30.775702"
---

# Fetching locations

Fetching locations

To fetch locations

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /tenants/{tenant_id}/locations endpoint:
>>> response = requests.get(f'{base_url}/tenants/{tenant_id}/locations', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the locations array with location UUIDs, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
...        {'locations': ['edbbebe2-f8b0-4176-89b0-b6eb19dd239a',
...               'afac0e4d-9deb-4201-9df3-e124dd7d9955',
...               '2432af91-f3f5-4492-9566-e9aa4d25a2a5']}



Store the locations array in a variable:
>>> location_ids = response.json()['locations']



Define a variable named params, and then assign the uuids query string parameter with comma-separated location UUIDs to this variable:
>>> params = {
...     'uuids': ','.join(location_ids)
... }



Send a GET request to the /locations endpoint:
>>> response = requests.get(f'{base_url}/locations', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with the location objects, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'id': 'edbbebe2-f8b0-4176-89b0-b6eb19dd239a',
'name': 'Acronis Cloud',
'owner_tenant_id': '8beef6be-c136-4ef6-a900-0e74c703ddcc',
'platform_owned': True,
'readonly': True,
'version': 2},
{'id': 'afac0e4d-9deb-4201-9df3-e124dd7d9955',
'name': 'NYC, USA',
'owner_tenant_id': 'e5afb5e8-84b6-415b-969d-bc10d19f3301',
'platform_owned': False,
'readonly': False,
'version': 0},
{'id': '2432af91-f3f5-4492-9566-e9aa4d25a2a5',
'name': 'Moscow, Russia',
'owner_tenant_id': 'e5afb5e8-84b6-415b-969d-bc10d19f3301',
'platform_owned': False,
'readonly': False,
'version': 0}]}