---
title: "Fetch a console link for the cloud server"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/fetch-cloud-server-console-link.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:03.339023"
---

# Fetch a console link for the cloud server

Fetch a console link for the cloud server

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
>>> remote_console_link = None
...
# Check if the server has issues
>>> if len(recovery_server['_issues']) > 0:
...     for issue in recovery_server['_issues']:
...         print(f"Error: {issue['message']}")
... else:
...     # If there are no issues, check if the server has a link to stop failover
...     for i in recovery_server['_links']:
...         if i['rel'] == 'DR_CLOUD_SERVER_REMOTE_CONSOLE_PAGE':
...             remote_console_link = i['href']
...             break
...
>>> if remote_console_link is None:
...     print('Cannot open remote console.')


If there are no issues and the link is present, the remote_console_link variable will contain the URL to the remote console
that you may open in your web browser.