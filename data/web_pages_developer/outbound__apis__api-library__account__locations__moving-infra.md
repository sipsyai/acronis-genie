---
title: "Moving a storage"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/moving-infra.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:43.405275"
---

# Moving a storage

Moving a storage

Important
If the storage is assigned to any other tenants, you must turn off related service(s)
for these tenants in order to move the storage. Be aware that disabling the service(s)
will delete all the data in the storage.


To move a storage

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Assign the infra_id variable the UUID of an infrastructure component created via the API or an infrastructure component found in location’s infrastructure components:
>>> infra_id = created_infra_id
>>> infra_id
'f79546d7-d051-4e19-96f3-4cc68c2c5575'



Assign the location_id variable the UUID of a location created via the API or a location found in tenant’s locations:
>>> location_id = created_location_id
>>> location_id
'8fcd353b-0a40-40f2-9a55-ef8137d48800'



Fetch the revision number of the storage as described in the chapters above. The following variable should be available now:
>>> version
1



Define a variable named infra_data, and then assign the storage to move to this variable:
>>> infra_data = {
...     "location_id": location_id,
...     "version": version
... }










Name
Value type
Required
Description



location_id
UUID string
Yes
An UUID of the location where the storage should be moved.

version
number
Yes
Revision number.




Convert the infra_data object to a JSON text:
>>> infra_data = json.dumps(infra_data, indent=4)



Send a PUT request with the JSON text to the /infra/{infra_id} endpoint:
>>> response = requests.put(
...     f'{base_url}/infra/{infra_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=infra_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the storage has been successfully moved.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the updated storage, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'backend_type': None,
'capabilities': ['files_cloud'],
'id': 'f79546d7-d051-4e19-96f3-4cc68c2c5575',
'location_id': '2432af91-f3f5-4492-9566-e9aa4d25a2a5',
'name': 'Amazon S3 Files Cloud',
'owner_tenant_id': 'e5afb5e8-84b6-415b-969d-bc10d19f3301',
'platform_owned': False,
'readonly': False,
'url': 'amazon+s3://s3.amazonaws.com/my-bucket-name',
'version': 2}