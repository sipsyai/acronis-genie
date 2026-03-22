---
title: "Fetch a list of cloud servers"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/fetch-cloud-servers-list.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:15.972047"
---

# Fetch a list of cloud servers

Fetch a list of cloud servers

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



[Optional]
Define a variable named filters, and then assign an object with the request filters to this variable:
>>> filters = {
...     "type": "RECOVERY", # request only recovery servers
...     "recovery.resource_id": "75212e4b-dab6-4065-ad49-1447b65ff3e4", # request only recovery servers linked to the original resource identified by UUID
... }



Send a GET request to the /servers endpoint:
>>> response = requests.get(f'{base_url}/servers', headers=scoped_auth, params=filters)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of recovery cloud servers formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'items': [{'_issues': [{'domain': 'DisasterRecovery',
'error': {'code': 'ResourceBusy',
'context': {'resource_id': '1f100401-357b-4d04-a0c0-d1206c947473',
'task_uuids': ['5bc9464f-87b6-4ea8-aa42-050824135e63']},
'domain': 'DisasterRecovery',
'message': 'The resource is busy, another '
'task is currently in progress. '
'Try again later.'},
'link': 'DR_CLOUD_SERVER_START_FAILOVER_PROD',
'severity': 'ERROR',
'target': '1f100401-357b-4d04-a0c0-d1206c947473'},
{'domain': 'DisasterRecovery',
'error': {'code': 'ResourceBusy',
'context': {'resource_id': '1f100401-357b-4d04-a0c0-d1206c947473',
'task_uuids': ['5bc9464f-87b6-4ea8-aa42-050824135e63']},
'domain': 'DisasterRecovery',
'message': 'The resource is busy, another '
'task is currently in progress. '
'Try again later.'},
'link': 'DR_CLOUD_SERVER_START_FAILOVER_TEST',
'severity': 'ERROR',
'target': '1f100401-357b-4d04-a0c0-d1206c947473'},
{'domain': 'DisasterRecovery',
'error': {'code': 'ResourceBusy',
'context': {'resource_id': '1f100401-357b-4d04-a0c0-d1206c947473',
'task_uuids': ['5bc9464f-87b6-4ea8-aa42-050824135e63']},
'domain': 'DisasterRecovery',
'message': 'The resource is busy, another '
'task is currently in progress. '
'Try again later.'},
'link': 'DR_CLOUD_SERVER_STOP_FAILOVER',
'severity': 'ERROR',
'target': '1f100401-357b-4d04-a0c0-d1206c947473'}],
'_links': [{'href': 'https://dev.acronis.cloud/bc/login?tenant_id=46&return_url=/api/2/idp/authorize?client_id=21098572-c62e-5220-8537-c7cf8050d97f&response_type=code&redirect_uri=/bc/api/gateway/cb&scope=offline_access+openid+profile+email&state=%252Fui%252F#/dr-servers?id=1f100401-357b-4d04-a0c0-d1206c947473',
'rel': 'DR_CLOUD_SERVER_PAGE',
'type': 'text/html'},
{'href': 'https://dev.acronis.cloud/bc/api/vault_manager/v1/backups?backupType=differential&backupType=full&backupType=incremental&embed=archive&forensic=false&includeScreenshotValidationStatus=false&order=desc(created)&showDeleted=0&storageType=online&type=image&resourceId=09BBF995-0088-452E-AFC3-BDE227EBD64C&resourceId=1f100401-357b-4d04-a0c0-d1206c947473',
'rel': 'DR_CLOUD_SERVER_RECOVERY_POINTS',
'type': 'application/json'},
{'href': 'https://dev.acronis.cloud/bc/login?tenant_id=46&return_url=/api/2/idp/authorize?client_id=21098572-c62e-5220-8537-c7cf8050d97f&response_type=code&redirect_uri=/bc/api/gateway/cb&scope=offline_access+openid+profile+email&state=%252Fui%252F#/dr-server-remote-console',
'rel': 'DR_CLOUD_SERVER_REMOTE_CONSOLE_PAGE',
'type': 'text/html'},
{'href': 'https://dev.acronis.cloud/bc/api/dr/v2/servers/1f100401-357b-4d04-a0c0-d1206c947473:start_failover_prod',
'rel': 'DR_CLOUD_SERVER_START_FAILOVER_PROD',
'type': 'application/json'},
{'href': 'https://dev.acronis.cloud/bc/api/dr/v2/servers/1f100401-357b-4d04-a0c0-d1206c947473:start_failover_test',
'rel': 'DR_CLOUD_SERVER_START_FAILOVER_TEST',
'type': 'application/json'},
{'href': 'https://dev.acronis.cloud/bc/api/dr/v2/servers/1f100401-357b-4d04-a0c0-d1206c947473:stop_failover',
'rel': 'DR_CLOUD_SERVER_STOP_FAILOVER',
'type': 'application/json'}],
'created_at': '2018-11-11T20:20:39+00:00',
'description': 'This is a very important WEB server.',
'name': 'Recovery Server',
'public_ip': '8.9.10.12',
'recovery': {'active_failover': {'backup_uri': 'avfs:/online?account%3D3%26authProtoVersion%3D1%26computer%3D1%26provider%3DAcronis#arl:/4EF06ED7-6315-4C5C-9033-38F80503F544/C92236DB-8D4E-4D0C-8FCB-5FEB868B4ECC/A3C6EFF4-3089-4429-98F9-8A36BE66594B/6EBB5654-6DB3-4D95-BB10-F3638353CB34?archive_name=WIN-Q1O5K1HTE2J-2E19359B-59F2-4078-A422-E6858FDC7F04-65049BA5-FFB6-4901-B0DE-B2ACA8F84482A',
'id': '2a57484d-6d90-44e1-afcc-6ac8ae59425a',
'vault_id': '0F8CA93A-E22D-40F2-9D29-49E2FB88BE2E'},
'automated_test_failover': {'last_start': '2018-11-13T20:20:39+00:00',
'last_status': 'SUCCESS',
'last_task_uuid': '74a662f8-6fab-4003-8e84-93e6c9996846',
'next_start': '2018-11-13T20:20:39+00:00',
'recovery_point': {'archive_id': 'A6407256-5FB4-4E8D-914A-830D61292EEA',
'backup_id': 'D14BC70D-7F7F-4413-80E4-904660679B78',
'vault_id': '0F8CA93A-E22D-40F2-9D29-49E2FB88BE2E'},
'schedule': 'MONTHLY',
'screenshot_link': 'https://datacenter.com/bc/api/dr/v1/servers/6782e594-781d-4ad2-b8ca-25a0c40f9938/automatedTestFailover/screenshot?size=full',
'screenshot_preview_link': 'https://datacenter.com/bc/api/dr/v1/servers/6782e594-781d-4ad2-b8ca-25a0c40f9938/automatedTestFailover/screenshot?size=preview',
'timeout': 300},
'resource_id': '1931FAAF-692D-451F-98A3-DAF721102BEB'},
'site_uuid': '06bad843-569b-4f7a-bc6b-741aab5be247',
'status': 'POWERING_OFF',
'task_uuid': '5bc9464f-87b6-4ea8-aa42-050824135e63',
'type': 'RECOVERY',
'uuid': '1f100401-357b-4d04-a0c0-d1206c947473',
'vm': {'cpu': 1,
'os': 'some OS',
'ram_mb': 2048,
'status': 'STARTED'}},
{'_issues': [{'domain': 'DisasterRecovery',
'error': {'code': 'ResourceBusy',
'context': {'resource_id': '565cf826-5332-4fd8-9109-2b81630e486d',
'task_uuids': ['7db6f670-27db-4729-86e9-0136ea7bf28b']},
'domain': 'DisasterRecovery',
'message': 'The resource is busy, another '
'task is currently in progress. '
'Try again later.'},
'link': 'DR_CLOUD_SERVER_START_FAILOVER_PROD',
'severity': 'ERROR',
'target': '565cf826-5332-4fd8-9109-2b81630e486d'},
{'domain': 'DisasterRecovery',
'error': {'code': 'ResourceBusy',
'context': {'resource_id': '565cf826-5332-4fd8-9109-2b81630e486d',
'task_uuids': ['7db6f670-27db-4729-86e9-0136ea7bf28b']},
'domain': 'DisasterRecovery',
'message': 'The resource is busy, another '
'task is currently in progress. '
'Try again later.'},
'link': 'DR_CLOUD_SERVER_START_FAILOVER_TEST',
'severity': 'ERROR',
'target': '565cf826-5332-4fd8-9109-2b81630e486d'},
{'domain': 'DisasterRecovery',
'error': {'code': 'ResourceBusy',
'context': {'resource_id': '565cf826-5332-4fd8-9109-2b81630e486d',
'task_uuids': ['7db6f670-27db-4729-86e9-0136ea7bf28b']},
'domain': 'DisasterRecovery',
'message': 'The resource is busy, another '
'task is currently in progress. '
'Try again later.'},
'link': 'DR_CLOUD_SERVER_STOP_FAILOVER',
'severity': 'ERROR',
'target': '565cf826-5332-4fd8-9109-2b81630e486d'}],
'_links': [{'href': 'https://dev.acronis.cloud/bc/login?tenant_id=46&return_url=/api/2/idp/authorize?client_id=21098572-c62e-5220-8537-c7cf8050d97f&response_type=code&redirect_uri=/bc/api/gateway/cb&scope=offline_access+openid+profile+email&state=%252Fui%252F#/dr-servers?id=565cf826-5332-4fd8-9109-2b81630e486d',
'rel': 'DR_CLOUD_SERVER_PAGE',
'type': 'text/html'},
{'href': 'https://dev.acronis.cloud/bc/api/vault_manager/v1/backups?backupType=differential&backupType=full&backupType=incremental&embed=archive&forensic=false&includeScreenshotValidationStatus=false&order=desc(created)&showDeleted=0&storageType=online&type=image&resourceId=09BBF995-0088-452E-AFC3-BDE227EBD64C&resourceId=565cf826-5332-4fd8-9109-2b81630e486d',
'rel': 'DR_CLOUD_SERVER_RECOVERY_POINTS',
'type': 'application/json'},
{'href': 'https://dev.acronis.cloud/bc/login?tenant_id=46&return_url=/api/2/idp/authorize?client_id=21098572-c62e-5220-8537-c7cf8050d97f&response_type=code&redirect_uri=/bc/api/gateway/cb&scope=offline_access+openid+profile+email&state=%252Fui%252F#/dr-server-remote-console',
'rel': 'DR_CLOUD_SERVER_REMOTE_CONSOLE_PAGE',
'type': 'text/html'},
{'href': 'https://dev.acronis.cloud/bc/api/dr/v2/servers/565cf826-5332-4fd8-9109-2b81630e486d:start_failover_prod',
'rel': 'DR_CLOUD_SERVER_START_FAILOVER_PROD',
'type': 'application/json'},
{'href': 'https://dev.acronis.cloud/bc/api/dr/v2/servers/565cf826-5332-4fd8-9109-2b81630e486d:start_failover_test',
'rel': 'DR_CLOUD_SERVER_START_FAILOVER_TEST',
'type': 'application/json'},
{'href': 'https://dev.acronis.cloud/bc/api/dr/v2/servers/565cf826-5332-4fd8-9109-2b81630e486d:stop_failover',
'rel': 'DR_CLOUD_SERVER_STOP_FAILOVER',
'type': 'application/json'}],
'created_at': '2018-11-11T20:20:39+00:00',
'description': 'This is the most important WEB server.',
'name': 'Recovery Server',
'public_ip': '8.9.10.12',
'recovery': {'active_failover': {'archive_credentials_id': 'A6407256-5FB4-4E8D-914A-830D61292EEA@archive',
'backup_uri': 'avfs:/online?account%3D3%26authProtoVersion%3D1%26computer%3D1%26provider%3DAcronis#arl:/4EF06ED7-6315-4C5C-9033-38F80503F544/C92236DB-8D4E-4D0C-8FCB-5FEB868B4ECC/A3C6EFF4-3089-4429-98F9-8A36BE66594B/6EBB5654-6DB3-4D95-BB10-F3638353CB34?archive_name=WIN-Q1O5K1HTE2J-2E19359B-59F2-4078-A422-E6858FDC7F04-65049BA5-FFB6-4901-B0DE-B2ACA8F84482A',
'id': '0c1bfa0c-3d13-4fe2-8921-e83b9d6dcad1',
'vault_id': '0F8CA93A-E22D-40F2-9D29-49E2FB88BE2E'},
'automated_test_failover': {'last_start': '2018-11-01T20:20:39+00:00',
'last_status': 'SUCCESS',
'last_task_uuid': '74a662f8-6fab-4003-8e84-93e6c9996846',
'next_start': '2018-11-13T20:20:39+00:00',
'recovery_point': {'archive_id': 'AC16D9C3-2EA2-4280-A9CA-12576FFB22A',
'backup_id': '570BE591-1DCF-4BDF-82D7-29ABC494AA13',
'vault_id': '0F8CA93A-E22D-40F2-9D29-49E2FB88BE2'},
'schedule': 'MONTHLY',
'screenshot_link': 'https://datacenter.com/bc/api/dr/v1/servers/6871ae92-d7f0-435f-a882-8946df89f50c/automatedTestFailover/screenshot?size=full',
'screenshot_preview_link': 'https://datacenter.com/bc/api/dr/v1/servers/6871ae92-d7f0-435f-a882-8946df89f50c/automatedTestFailover/screenshot?size=preview',
'timeout': 300},
'resource_id': 'ECCA39E5-5018-4DF4-8429-F8C6FB91F2BC',
'test_failover': {'last_start': '2019-11-19T07:22:14+00:00',
'last_task_uuid': 'c005a6e9-5b01-4e68-9aaf-7182a3a5ccce',
'recovery_point': {'archive_id': 'AC16D9C3-2EA2-4280-A9CA-12576FFB22A1',
'backup_id': '570BE591-1DCF-4BDF-82D7-29ABC494AA13',
'vault_id': '0F8CA93A-E22D-40F2-9D29-49E2FB88BE2E'}}},
'site_uuid': '06bad843-569b-4f7a-bc6b-741aab5be247',
'status': 'POWERING_ON',
'task_uuid': '7db6f670-27db-4729-86e9-0136ea7bf28b',
'type': 'RECOVERY',
'uuid': '565cf826-5332-4fd8-9109-2b81630e486d',
'vm': {'cpu': 1,
'os': 'some OS',
'ram_mb': 2048,
'status': 'STOPPED'}}],
'paging': {'count': 2, 'cursors': {'after': 'eyJSJdfQ'}, 'total': 3}}