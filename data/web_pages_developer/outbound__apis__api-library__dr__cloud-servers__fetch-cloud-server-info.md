---
title: "Fetch information about the cloud server"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/fetch-cloud-server-info.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:07.538324"
---

# Fetch information about the cloud server

Fetch information about the cloud server

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



Fetch a UUID of the cloud server that you want to get information about and store it in the server_id variable:
>>> server_id = '2ab0d820-f3ca-4056-af8f-fe2e7ff5bb7f'  # the cloud server ID



Send a GET request to the /servers/{server_id} endpoint:
>>> response = requests.get(f'{base_url}/servers/{server_id}', headers=scoped_auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains an information about the cloud server formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'_issues': [],
'_links': [{'href': 'https://dev.acronis.cloud/bc/login?tenant_id=46&return_url=/api/2/idp/authorize?client_id=21098572-c62e-5220-8537-c7cf8050d97f&response_type=code&redirect_uri=/bc/api/gateway/cb&scope=offline_access+openid+profile+email&state=%252Fui%252F#/dr-servers?id=6782e594-781d-4ad2-b8ca-25a0c40f9938',
'rel': 'DR_CLOUD_SERVER_PAGE',
'type': 'text/html'},
{'href': 'https://dev.acronis.cloud/bc/api/vault_manager/v1/backups?backupType=differential&backupType=full&backupType=incremental&embed=archive&forensic=false&includeScreenshotValidationStatus=false&order=desc(created)&showDeleted=0&storageType=online&type=image&resourceId=6782e594-781d-4ad2-b8ca-25a0c40f9938',
'rel': 'DR_CLOUD_SERVER_RECOVERY_POINTS',
'type': 'application/json'},
{'href': 'https://dev.acronis.cloud/bc/login?tenant_id=46&return_url=/api/2/idp/authorize?client_id=21098572-c62e-5220-8537-c7cf8050d97f&response_type=code&redirect_uri=/bc/api/gateway/cb&scope=offline_access+openid+profile+email&state=%252Fui%252F#/dr-server-remote-console',
'rel': 'DR_CLOUD_SERVER_REMOTE_CONSOLE_PAGE',
'type': 'text/html'}],
'created_at': '2018-11-11T20:20:39+00:00',
'description': 'This is a very important MS SQL server.',
'name': 'Primary Server',
'primary': {'vault_id': '0F8CA93A-E22D-40F2-9D29-49E2FB88BE2E'},
'public_ip': '8.9.10.11',
'site_uuid': '06bad843-569b-4f7a-bc6b-741aab5be247',
'status': 'STAND_BY',
'type': 'PRIMARY',
'uuid': '6782e594-781d-4ad2-b8ca-25a0c40f9938',
'vm': {'cpu': 1,
'os': 'some OS',
'ram_mb': 2048,
'status': 'STARTED',
'storage': [{'id': 'storageID5', 'protected': True, 'size_gb': 2},
{'id': 'storageID6', 'protected': False, 'size_gb': 5}]}}