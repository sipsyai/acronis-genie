---
title: "Fetch disaster recovery site status"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/fetch-dr-connectivity-status.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:20.179822"
---

# Fetch disaster recovery site status

Fetch disaster recovery site status

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



Send a GET request to the /sites endpoint:
>>> response = requests.get(f'{base_url}/sites', headers=scoped_auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of disaster recovery sites formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'items': [{'_issues': [{'domain': 'DisasterRecovery',
'error': {'code': 'SiteNotReady',
'domain': 'DisasterRecovery',
'message': 'You cannot perform any '
'operations because the DR site '
'is being deployed or removed.'},
'severity': 'ERROR',
'target': 'f3b3b3b3-3b3b-3b3b-3b3b-3b3b3b3b3b3b'}],
'_links': [{'href': 'https://example.com/dr/sites/f3b3b3b3-3b3b-3b3b-3b3b-3b3b3b3b3b3b/connectivity',
'rel': 'DR_SITE_CONNECTIVITY_PAGE',
'type': 'text/html'}],
'default': True,
'failover_readiness': 'ERROR',
'status': 'PROVISIONING',
'task_uuid': 'c108b478-2083-4097-a418-ab3d0d49b938',
'tenant_uuid': '9ca5aa60-4cdc-491c-94d5-23b747f7f914',
'uuid': 'f3b3b3b3-3b3b-3b3b-3b3b-3b3b3b3b3b3b'},
{'_issues': [{'domain': 'DisasterRecovery',
'error': {'code': 'VPNS2SApplianceNotRegistered',
'domain': 'DisasterRecovery',
'message': 'The VPN appliance is not '
'registered.'},
'severity': 'WARNING',
'target': '75c45087-0ba7-4580-8de8-1be489b7591d'}],
'_links': [{'href': 'https://example.com/dr/sites/f3b3b3b3-3b3b-3b3b-3b3b-3b3b3b3b3b3b/connectivity',
'rel': 'DR_SITE_CONNECTIVITY_PAGE',
'type': 'text/html'}],
'default': False,
'failover_readiness': 'WARNING',
'status': 'PROVISIONED',
'tenant_uuid': '9ca5aa60-4cdc-491c-94d5-23b747f7f914',
'uuid': '75c45087-0ba7-4580-8de8-1be489b7591d'}],
'paging': {'count': 2, 'cursors': {'after': 'eyJSJdfQ'}, 'total': 3}}



Store the disaster recovery sites in the sites variable:
>>> sites = response.json()['items']



In the response, check the failover_readiness and status of the site.
>>> for site in sites:
...     print(f"Site {site['uuid']} is {site['status']} and has failover readiness {site['failover_readiness']}")


The status can be one of the following values: PROVISIONING, PROVISIONED, DEPROVISIONING.
The failover readiness can be one of the following values: ERROR, WARNING, OK.

[Optional] In the response, check that the _issues list is empty:
>>> for site in sites:
...     if len(site['_issues']) > 0:
...         for issue in site['_issues']:
...             print(f"Error: {issue['message']}")


If there are no issues and the link is present, you can visit the DR site connectivity page to check the status of the site.

[Optional] Fetch a link to the DR site connectivity page that you may visit in your web browser:
>>> for site in sites:
...     for i in site['_links']:
...         if i['rel'] == 'DR_SITE_CONNECTIVITY_PAGE':
...             print(f"DR site connectivity page: {i['href']}")
...             break