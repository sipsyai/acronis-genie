---
title: "Fetching incident details and response actions"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/mdr/fetching-incident-details.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:40.210602"
---

# Fetching incident details and response actions

Fetching incident details and response actions

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



Define a variable named params, and then assign an object with request parameters to this variable:
>>> params = {
...     'customer_id': customer_id,
...     'with_activities': False, # optional parameter to include activities in the response
...     'with_detections': False, # optional parameter to include detections in the response
...     'with_response_actions': True, # optional parameter to include response actions in the response
... }



Send a GET request to the /incidents/{incident_id} endpoint:
>>> response = requests.get(f'{base_url}/incidents/{incident_id}', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request is successful.
Also, the response body contains the response contains the incident details with available response actions formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'agent_version': '24.10.38581',
'assignee_id': '00000000-0000-0000-0000-000000000000',
'created_at': '2024-09-19T11:11:22.115829Z',
'customer_id': 'fdd168cc-6c5b-4c0b-b908-0323895e74f3',
'host_address': '10.144.1.22',
'host_domain': 'DESKTOP-N6BRO6A',
'host_name': 'DESKTOP-N6BRO6A',
'incident_categories': ['MALWARE_DETECTED'],
'incident_id': '8b4645f7-d742-470e-8368-9017d1156d8b',
'incident_link': 'https://eu8.acronis.cloud/ui/#/endpoint-detection/customer/116/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/investigation',
'incident_short_id': 1,
'incident_time': '2024-09-19T11:11:22.115829Z',
'mitigation_state': 'NOT_MITIGATED',
'positivity': 10,
'response_actions': [{'action': 'WORKLOAD_ISOLATE',
'description': 'Isolate a specific workload from the '
'network',
'display_name': 'Isolate workload',
'uri': 'https://eu8.acronis.cloud/api/mdr/v1/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/response_action?action=WORKLOAD_ISOLATE'},
{'action': 'WORKLOAD_RESTART',
'description': 'Initiate a restart of a specific '
'workload',
'display_name': 'Restart workload',
'query_parameters': {'delay': {'description': 'delay '
'the '
'restart '
'of a '
'system '
'in '
'minutes',
'maximum': 60,
'minimum': 0,
'type': 'number'}},
'uri': 'https://eu8.acronis.cloud/api/mdr/v1/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/response_action?action=WORKLOAD_RESTART'},
{'action': 'WORKLOAD_SHUTDOWN',
'description': 'Shut down a specific workload',
'display_name': 'Power off workload',
'uri': 'https://eu8.acronis.cloud/api/mdr/v1/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/response_action?action=WORKLOAD_SHUTDOWN'}],
'severity': 'HIGH',
'state': 'NOT_STARTED',
'updated_at': '2024-09-24T09:41:36.39723Z',
'verdict': 'MALICIOUS'}



Store the list of response actions in a variable named response_actions.
>>> response_actions = response.json()['response_actions']
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