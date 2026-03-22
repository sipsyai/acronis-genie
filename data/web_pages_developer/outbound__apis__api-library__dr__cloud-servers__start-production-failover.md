---
title: "Start production failover for a specific recovery server"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/start-production-failover.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:32.829041"
---

# Start production failover for a specific recovery server

Start production failover for a specific recovery server

Important
Currently, the “failover” operation is only supported for cloud servers with “RECOVERY” type.


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
>>> start_prod_failover_link = None
...
# Check if the server has issues
>>> if len(recovery_server['_issues']) > 0:
...     for issue in recovery_server['_issues']:
...         print(f"Error: {issue['message']}")
... else:
...     # If there are no issues, check if the server has a link to stop failover
...     for i in recovery_server['_links']:
...         if i['rel'] == 'DR_CLOUD_SERVER_START_FAILOVER_TEST':
...             start_prod_failover_link = i['href']
...             break
...
>>> if start_prod_failover_link is None:
...     print('Cannot start test failover.')


If there are no issues and the link is present, the start_prod_failover_link variable will contain the URL to the Disaster Recovery API
endpoint that you may use to start the production failover.

[Optional] By default failover will be executed from the last available recovery point. To run the “failover” operation from a specific recovery point:

Fetch a list of available recovery points for the recovery server.
>>> recovery_points = response.json() # list of recovery points available for failover operation for the recovery server in question
>>> target_recovery_point = recovery_points[0]  # selecting the last created recovery point



Define a variable named recovery_point_data, and then assign with an object containing the recovery_point key with information about the recovery point to this variable:
>>> recovery_point_data = {
...     'recovery_point': {
...         'archive_id': target_recovery_point['archive_id'],
...         'backup_id': target_recovery_point['backup_id'],
...         'vault_id': target_recovery_point['vault_id'],
...     }
... }





Send a POST request to the Disaster Recovery API using the start_prod_failover_link URL and the scoped authentication token:
>>> response = requests.post(start_prod_failover_link, headers=scoped_auth, data=recovery_point_data)



Check the status code of the response:
>>> response.status_code
202


Status code 202 means that the request was successful and the production failover has been initiated.
Also, the response body contains a UUID of the task. You can monitor the progress of the task by querying Task Manager API with the provided task_uuid. Refer to the corresponding documentation for more details. When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{"task_uuid": "f1b3b3b4-4b1b-4b1b-4b1b-4b1b4b1b4b1b"}