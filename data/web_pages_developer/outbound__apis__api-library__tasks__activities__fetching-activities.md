---
title: "Fetching a list of all activities"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/tasks/activities/fetching-activities.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:50.599811"
---

# Fetching a list of all activities

Fetching a list of all activities

To fetch a list of all activities

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api/task_manager/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Send a GET request to the /activities endpoint:
>>> response = requests.get(f'{base_url}/activities', headers=auth)



Note
For the list of available query string parameters, see the Task Manager API reference.


Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes.


Also, the response body contains the items array of activity objects formatted as a JSON text. When converted to an object, it will look like this:

>>> pprint.pprint(response.json())
{'items': [{'completedAt': '2020-04-22T11:34:03.290396913Z',
'context': {'IsProcessRoot': True,
'Persistent': {'AgentType': 'agent',
'ID': 'f7358a00-8469-45ae-a0c3-22952e9ed12f',
'Name': 'DESKTOP-GFT9S1R',
'OwnerID': '1496265'},
'Specific': 'Business',
'UserName': 'DESKTOP-GFT9S1R\\AMS User',
'isLegacy': True,
'title': "Adding agent 'DESKTOP-GFT9S1R' to the "
'management server'},
'createdAt': '2020-04-22T11:34:03.290396913Z',
'executor': {'clusterId': '', 'id': ''},
'id': 944455285181775872,
'idString': '944455285181775872',
'result': {'code': 'ok',
'payload': 'MachineManagement::AddAgentResponse'},
'startedAt': '2020-04-22T11:34:03.290396913Z',
'startedByUser': 'DESKTOP-GFT9S1R\\AMS User',
'state': 'completed',
'taskId': 944455285181775872,
'taskIdString': '944455285181775872',
'tenant': {'id': '1496265',
'locator': '/1/1496262/1496265/',
'name': 'John Doe'},
'type': 'A59E8BF2-39C3-42C4-B667-CB672381A214',
'updatedAt': '2020-04-22T11:34:03.294683447Z',
'uuid': '38045860-8901-426e-b51f-fc6d24d1cbe0'}]}