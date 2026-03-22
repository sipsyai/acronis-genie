---
title: "Performing and monitoring response actions"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/mdr/performing-monitoring-actions.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:52.803419"
---

# Performing and monitoring response actions

Performing and monitoring response actions

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/mdr/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch the incident which actions you want to get by following the Fetching incidents procedure.
As a result, you should have an incident ID and a customer ID that you will use in the following steps:
>>> incident_id
'41e19c11-2606-475d-b459-56a5509494ee'
>>> customer_id
'64b40fe0-2051-4f11-8913-ecd9652e221c'



Fetch the list of available response actions by following the Fetching incident details and response actions procedure.
As a result, you should have a list of response actions that you will use in the following steps:
>>> response_actions
[
{
"action": "WORKLOAD_ISOLATE",
"uri": "https://eu8.acronis.cloud/api/mdr/v1/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/response_action?action=WORKLOAD_ISOLATE",
"description": "Isolate a specific workload from the network",
"display_name": "Isolate workload"
},
{
"action": "WORKLOAD_RESTART",
"uri": "https://eu8.acronis.cloud/api/mdr/v1/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/response_action?action=WORKLOAD_RESTART",
"query_parameters": {
"delay": {
"type": "number",
"description": "delay the restart of a system in minutes",
"minimum": 0,
"maximum": 60
}
},
"description": "Initiate a restart of a specific workload",
"display_name": "Restart workload"
},
{
"action": "WORKLOAD_SHUTDOWN",
"uri": "https://eu8.acronis.cloud/api/mdr/v1/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/response_action?action=WORKLOAD_SHUTDOWN",
"description": "Shut down a specific workload",
"display_name": "Power off workload"
}
]



Define a variable named params, and then assign an object with request parameters to this variable:
>>> params = {
...     'customer_id': customer_id,
...     'action': 'WORKLOAD_ISOLATE', # A response action from the list of available response actions
...     'comment': 'Isolating workload due to a security incident', # An optional comment
... }



Send a POST request to the /incidents/{incident_id}/response_action endpoint:
>>> response = requests.post(
...     f'{base_url}/incidents/{incident_id}/response_action',
...     headers=auth,
...     params=params,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the request is successful.
Also, the response body contains the response contains the ID of the performed action formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{"activity_id": "213e27f4-f319-4e2a-b273-f853c5d93e44"}



To monitor the created activity, store the activity ID received in the response in a variable named activity_id.
>>> activity_id = '213e27f4-f319-4e2a-b273-f853c5d93e44'



Note
Activity ID is associated with a specific customer ID. It is recommended to store
the activity ID and customer ID in a persistent storage to monitor the activity status later.
In case you don’t have the activity ID, you can fetch it from the activity details by following
the Fetching incident details and response actions procedure.


Define a variable named params, and then assign a dictionary with the query parameters to this variable:
>>> params = {
...     'activity_id': activity_id,
...     'customer_id': customer_id,
... }



Send a GET request to the /incidents/{incident_id}/response_action endpoint:
>>> response = requests.get(
...     f'{base_url}/incidents/{incident_id}/response_action',
...     headers=auth,
...     params=params,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request is successful.
Also, the response body contains the response contains the ID of the performed action formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'action': 'WORKLOAD_ISOLATE',
'activity_id': '213e27f4-f319-4e2a-b273-f853c5d93e44',
'result_details': 'Workload isolation is in progress.',
'status': 'STARTED'}