---
title: "Registering a storage"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/registering-infra.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:47.616214"
---

# Registering a storage

Registering a storage

Important
This procedure is applicable only for registering “Files & Sync” storage. For more information, see “Acronis Files Cloud: how to register storage”
For the information on how to register a “Backup” storage, see “Acronis Cyber Infrastructure Quick Start Guide”


To register a storage

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



Define a variable named infra_data, and then assign the new storage to this variable:
>>> infra_data = {
...     "owner_tenant_id": tenant_id,
...     "location_id": location_id,
...     "name": "Amazon S3 Files Cloud",
...     "url": "amazon+s3://AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMIzK7MDENGMbPxRfiCYEXAMPLEKEY@s3.amazonaws.com/my-bucket-name",
...     "capabilities": [
...         "files_cloud"
...     ]
... }










Name
Value type
Required
Description



owner_tenant_id
UUID string
Yes
The UUID of the tenant where the new location will be created.

location_id
UUID string
Yes
An UUID of the location where the storage should be moved.

name
string
Yes
The name of the storage.

url
string
Yes
The storage URL. See storage url formatting rules

capabilities
array of strings
Yes
The list of services this storage can be used in. See the list of available storage capabilities.




Convert the infra_data object to a JSON text:
>>> infra_data = json.dumps(infra_data, indent=4)



Send a POST request with the JSON text to the /infra endpoint:
>>> response = requests.post(
...     f'{base_url}/infra',
...     headers={'Content-Type': 'application/json', **auth},
...     data=infra_data,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the platform has created a new storage named Amazon Files Cloud in the NYC Data Center location.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the storage object, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'backend_type': None,
'capabilities': ['files_cloud'],
'id': 'f79546d7-d051-4e19-96f3-4cc68c2c5575',
'location_id': 'afac0e4d-9deb-4201-9df3-e124dd7d9955',
'name': 'Amazon S3 Files Cloud',
'owner_tenant_id': 'e5afb5e8-84b6-415b-969d-bc10d19f3301',
'platform_owned': False,
'readonly': False,
'url': 'amazon+s3://s3.amazonaws.com/my-bucket-name',
'version': 1}



Note
The provided storage URL is cleaned from storage access credentials for security reasons.


[Optional] Store the UUID of the location and version, in case if you need to modify or delete it:
>>> infra_id = response.json()['id']
>>> infra_id
'f79546d7-d051-4e19-96f3-4cc68c2c5575'
>>> infra_version = response.json()['version']
>>> infra_version
1