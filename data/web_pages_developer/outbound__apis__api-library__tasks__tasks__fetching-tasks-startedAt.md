---
title: "Fetching a list of tasks started after the specified date"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/tasks/tasks/fetching-tasks-startedAt.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:27:11.636822"
---

# Fetching a list of tasks started after the specified date

Fetching a list of tasks started after the specified date

To fetch a list of tasks started after a specified date

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api/task_manager/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named filters, and then assign an object with the startedAt key containing the greater-than operator with a date in the RFC3339 format to this variable:
>>> filters = {
...     'startedAt': 'gt(2020-04-22T11:00:00Z)'
... }



Note

You can specify a date in one of the following formats: RFC3339, RFC1123, RFC850, ANSI, UnixTimestamp (integer), UnixTimestampNano (integer + “ns” postfix).
For the list of available comparison operators, see the Task Manager API reference.



Send a GET request to the /tasks endpoint:
>>> response = requests.get(f'{base_url}/tasks', headers=auth, params-filters)



Note
For the list of available query string parameters, see the Task Manager API reference.


Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes.

Also, the response body contains the items array of task objects formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'cancelRequested': False,
'cancellable': True,
'startedAt': '2020-04-22T11:34:03.290396913Z',
'completedAt': '2020-04-22T11:34:03.290396913Z',
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
'enqueuedAt': '2020-04-22T11:34:03.290396913Z',
'id': 944455285181775872,
'idString': '944455285181775872',
'issuer': {'clusterId': '', 'id': ''},
'priority': 'normal',
'queue': 'legacySync',
'result': {'code': 'ok',
'payload': 'MachineManagement::AddAgentResponse'},
'startedByUser': 'DESKTOP-GFT9S1R\\AMS User',
'state': 'completed',
'tenant': {'id': '1496265',
'locator': '/1/1496262/1496265/',
'name': 'johndoe@mysite.com'},
'type': 'A59E8BF2-39C3-42C4-B667-CB672381A214',
'updatedAt': '2020-04-22T11:34:03.294683447Z',
'uuid': '38045860-8901-426e-b51f-fc6d24d1cbe0'}]}