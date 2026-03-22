---
title: "Deleting a storage"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/deleting-infra.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:18.143692"
---

# Deleting a storage

Deleting a storage

Important
If the storage is in use by any tenant, you will not be able to remove the storage.
The force parameter allows you to ignore existing usage of the storage when set to True.
Be aware that this operation is not reversible and all data related to the storage will be deleted.


To delete a storage

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



Fetch the revision number of the storage as described in the chapters above. The following variable should be available now:
>>> version
1



Define a variable named params, and then assign the version and force query string parameters to this variable:
>>> params = {
...     'version': version,
...     'force': False
... }










Name
Value type
Required
Description



version
number
Yes
Revision number.

force
boolean
No
Flag that allows you to force delete the storage. False by default.




Send a DELETE request to the /infra/{infra_id} endpoint:
>>> response = requests.delete(f'{base_url}/infra/{infra_id}', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the storage has been successfully deleted.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.