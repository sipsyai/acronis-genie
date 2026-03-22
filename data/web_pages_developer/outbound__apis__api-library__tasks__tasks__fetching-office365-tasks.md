---
title: "Fetching a list of tasks related to Office 365 backup and recovery"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/tasks/tasks/fetching-office365-tasks.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:27:03.200022"
---

# Fetching a list of tasks related to Office 365 backup and recovery

Fetching a list of tasks related to Office 365 backup and recovery

To fetch a list of tasks related to Office 365 backup and recovery

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api/task_manager/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named filters, and then assign an object with the type key containing the list of types related to Office 365 backup and recovery to this variable:
>>> filters = {
...     'type': [
...         'UserMailboxBackup', 'SPBackup', 'ODBackup', 'GSBackupGMail', 'GSBackupGDrive',
...         'UserMailboxRestore', 'SPRestore', 'ODRestore', 'GSRestoreGMail', 'GSRestoreGDrive'
...     ]
... }



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
'type': 'UserMailboxBackup',
...}
...]}