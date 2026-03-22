---
title: "Stop failover for a specific recovery server"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/stop-failover.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:41.261228"
---

# Stop failover for a specific recovery server

Stop failover for a specific recovery server

Warning
Failover stop is a destructive operation that leads to a permanent loss of the data located on the running virtual machine.
Ensure that all the essential cloud server data is backed up before stopping failover.
Note that cloud servers are not protected by backup policies in states related to failover testing.


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
>>> stop_failover_link = None
...
# Check if the server has issues
>>> if len(recovery_server['_issues']) > 0:
...     for issue in recovery_server['_issues']:
...         print(f"Error: {issue['message']}")
... else:
...     # If there are no issues, check if the server has a link to stop failover
...     for i in recovery_server['_links']:
...         if i['rel'] == 'DR_CLOUD_SERVER_STOP_FAILOVER':
...             stop_failover_link = i['href']
...             break
...
>>> if stop_failover_link is None:
...     print('Failover cannot be stopped.')


If there are no issues and the link is present, the stop_failover_link variable will contain the URL to the Disaster Recovery API
endpoint that you may use to stop the failover.

Send a POST request to the Disaster Recovery API using the stop_failover_link URL and the scoped authentication token:
>>> response = requests.post(stop_failover_link, headers=scoped_auth)



Check the status code of the response:
>>> response.status_code
202


Status code 202 means that the request was successful and the failover stop has been initiated.
Also, the response body contains a UUID of the task. You can monitor the progress of the task by querying Task Manager API with the provided task_uuid. Refer to the corresponding documentation for more details. When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{"task_uuid": "f1b3b3b4-4b1b-4b1b-4b1b-4b1b4b1b4b1b"}