---
title: "Fetching storages"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/fetching-infras.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:26.547821"
---

# Fetching storages

Fetching storages

To fetch storages

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



Send a GET request to the /location/{location_id}/infra endpoint:
>>> response = requests.get(f'{base_url}/location/{location_id}/infra', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with the storage UUIDs, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': ['404e4325-ff66-4014-a54a-685717a56a18']}



Store the items array in a variable:
>>> storage_ids = response.json()['items']



Define a variable named params, and then assign the uuids query string parameter with comma-separated storage UUIDs to this variable:
>>> params = {
...     'uuids': ','.join(storage_ids)
... }



Send a GET request to the /infra endpoint:
>>> response = requests.get(f'{base_url}/infra', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with the storage objects, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'backend_type': None,
'capabilities': ['files_cloud'],
'id': 'f79546d7-d051-4e19-96f3-4cc68c2c5575',
'location_id': '2432af91-f3f5-4492-9566-e9aa4d25a2a5',
'name': 'Amazon S3 Files Cloud',
'owner_tenant_id': 'e5afb5e8-84b6-415b-969d-bc10d19f3301',
'platform_owned': False,
'readonly': False,
'url': 'amazon+s3://s3.amazonaws.com/my-bucket-name',
'version': 1}]}