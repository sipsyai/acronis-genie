---
title: "Fetch a list of the recovery server’s recovery points"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/fetch-recovery-points.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:24.403588"
---

# Fetch a list of the recovery server’s recovery points

Fetch a list of the recovery server’s recovery points

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/dr/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Obtain scoped access token for the customer tenant.
As a result, the following variables should be available:
>>> scoped_auth # the 'Authorization' header value with the scoped access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the information about the recovery server by its ID and store the information in the recovery_server variable.
>>> recovery_server = response.json()



In the recovery_server, check that _issues is empty and that the _link to the stop failover action is present.
>>> recovery_points_link = None
...
# Check if the server has issues
>>> if len(recovery_server['_issues']) > 0:
...     for issue in recovery_server['_issues']:
...         print(f"Error: {issue['message']}")
... else:
...     # If there are no issues, check if the server has a link to stop failover
...     for i in recovery_server['_links']:
...         if i['rel'] == 'DR_CLOUD_SERVER_RECOVERY_POINTS':
...             recovery_points_link = i['href']
...             break
...
>>> if recovery_points_link is None:
...     print('Cannot check recovery points.')


If there are no issues and the link is present, the recovery_points_link variable will contain the URL to the Vault Manager API
endpoint that you may use to fetch the list of recovery points.

Send a GET request to the Vault Manager API using the recovery_points_link URL and the scoped authentication token:
>>> response = requests.get(recovery_points_link, headers=scoped_auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of backups that can be used as recovery points in the Disaster Recovery API formatted as a JSON text. When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'items': [{'actions': ['restoreDisks',
'restoreFiles',
'downloadFiles',
'deleteByAgent',
'validate',
'replicate'],
'archive_id': '1f8867c2-179f-ef34-159f-84279a18174d',
'attributes': {'Kind': 'full',
'MarkedForDeletion': '0',
'SliceMediaIDs': ''},
'backup_id': 'c2aa0462-dd30-4e08-afce-1bad7cfbf8be',
'catalog_status': {'MsTeamsChannel': False,
'MsTeamsMails': True,
'MsTeamsSite': False},
'created': '2018-02-02T01:40:05Z',
'deleted': False,
'notarized': False,
'resource_ids': ['EDD63875-4641-44AA-B1A6-BACB4610AA11'],
'size': 70844416,
'source_key': '',
'source_usn': 0,
'tapes': ['7E1DBD9A-7A7A-4D98-AB13-50084215FCDD',
'3DBFADA4-D2E9-442E-9942-39685E956EC1',
'C2067C48-0819-41E2-9749-4B448793A782'],
'tapes_for_restore': ['3DBFADA4-D2E9-442E-9942-39685E956EC1',
'C2067C48-0819-41E2-9749-4B448793A782'],
'tenant_id': '00000000-0000-0000-0000-000000000000',
'tenant_locator': '/00000000-0000-0000-0000-000000000000/',
'type': 'full',
'vault_id': '885b7fe4-95ce-71fd-fff5-8de5b3cce9bb'}],
'paging': {'cursors': {'before': 'eyJfdXJsUGF0aCI6WyIvYXBpL3ZhdWx0X21hbmFnZXIvdjEvYXJjaGl2ZXMiXSwib2Zmc2V0IjpbIjAiXX0'}}}