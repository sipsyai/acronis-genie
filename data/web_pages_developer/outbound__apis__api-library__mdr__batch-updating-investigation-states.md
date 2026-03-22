---
title: "Updating a batch of investigation states"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/mdr/batch-updating-investigation-states.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:36.014347"
---

# Updating a batch of investigation states

Updating a batch of investigation states

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/mdr/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch the list of incidents which investigation states you want to update by following the Fetching incidents procedure.
As a result, you should have a list of incident IDs and customer IDs that you will use in the following steps:
>>> incidents
[
{
'incident_id': '41e19c11-2606-475d-b459-56a5509494ee',
'customer_id': '64b40fe0-2051-4f11-8913-ecd9652e221c'
},
{
'incident_id': '7560c5a0-d748-467b-807f-f794c322bbe4',
'customer_id': 'f1065685-e276-484e-9527-e109e06ec236'
}
]



Define a variable named investigation_state, and then assign a dictionary with the investigation state to this variable:
>>> investigation_state = {
...     "customer_incident_ids": incidents,
...     "update": {
...         "state": "CLOSED",
...         "comment": "Remediation actions completed."
...     }
... }



Convert the investigation_state object to a JSON text:
>>> investigation_state = json.dumps(investigation_state, indent=4)



Send a POST request with the JSON text to the /incidents/investigation_state endpoint:
>>> response = requests.post(
...     f'{base_url}/incidents/investigation_state',
...     headers={'Content-Type': 'application/json', **auth},
...     data=investigation_state,
... )



Check the status code of the response:
>>> response.status_code
207


Status code 207 means that the request contains multiple statuses.
Also, the response body contains the information about processed incident status updates formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'failure_items': 0, 'items': null, 'success_items': 2, 'total_items': 2}


In case the update of some investigation states fails, the response will contain the details about the failed items:
>>> pprint.pprint(response.json())
{'failure_items': 1,
'items': [{'item': {'incident_id': '41e19c11-2606-475d-b459-56a5509494ef'},
'status': 404}],
'success_items': 1,
'total_items': 2}


Information provided with the investigation state will be reflected in the incident details and
can be obtained by following both Fetching incident details and response actions and Fetching incidents procedures.