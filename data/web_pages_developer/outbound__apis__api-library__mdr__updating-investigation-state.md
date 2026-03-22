---
title: "Updating incident investigation state"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/mdr/updating-investigation-state.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:57.179618"
---

# Updating incident investigation state

Updating incident investigation state

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
... }



Define a variable named investigation_state, and then assign a dictionary with the investigation state to this variable:
>>> investigation_state = {
...     'comment': 'Anomaly detected', # an optional comment about the incident
...     "state": "INVESTIGATING",
...     "ticket_subject": "Investigating incident #1", # a subject of the ticket associated with the incident
...     "ticket_id": "1", # an external ticket ID associated with the incident
...     "priority": "HIGH"
... }



Send a POST request to the /incidents/{incident_id}/investigation_state endpoint:
>>> response = requests.post(
...     f'{base_url}/incidents/{incident_id}/investigation_state',
...     headers={'Content-Type': 'application/json', **auth},
...     data=branding_options,
...     params=params,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the request is successful and investigation state was updated successfully.
Information provided with the investigation state will be reflected in the incident details and
can be obtained by following both Fetching incident details and response actions and Fetching incidents procedures.