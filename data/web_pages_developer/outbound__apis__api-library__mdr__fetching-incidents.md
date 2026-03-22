---
title: "Fetching incidents"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/mdr/fetching-incidents.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:44.400436"
---

# Fetching incidents

Fetching incidents

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/mdr/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Specify a filter by customer IDs and store it in a variable named customer_id. The following options are available:

If you need to fetch incidents of a specific customer, specify stored customer ID or fetch one using Account Management API v2:
>>> customer_id = '41e19c11-2606-475d-b459-56a5509494ee'



If you need to fetch incidents for multiple customers, specify a list of customer IDs using the or operator:
>>> customer_id = 'or(41e19c11-2606-475d-b459-56a5509494ee,41e19c11-2606-475d-b459-56a5509494ef)'



If you need to fetch incidents of customers in a partner, specify one of the following filtering operators:

direct_children(<partner_id>) - includes all customers that are direct children of the specified partner tenant ID.
descendants(<partner_id>) - includes all customers that are descendants of the specified partner tenant ID.

Where <partner_id> is the ID of the partner tenant.
For example, to fetch incidents for all customers that are direct children of the partner tenant with ID ede9f834-70b3-476c-83d9-736f9f8c7dae:
>>> customer_id = 'direct_children(ede9f834-70b3-476c-83d9-736f9f8c7dae)'





Define a variable named params, and then assign a dictionary with the query parameters to this variable:
>>> params = {
...     'customer_id': customer_id,
...     'state': 'NOT_STARTED', # get all incidents that are not started
...     'is_mitigated': False, # get all incidents that are not mitigated
...     'cursor': None, # optional parameter with a cursor to the next page of the response
... }



Send a GET request to the /incidents endpoint:
>>> response = requests.get(f'{base_url}/incidents', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request is successful.
Also, the response body contains the response contains the list of incidents and a cursor to the next page formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'cursor': 'obT6tj3_TUqL8E6vqce6qA==',
'items': [{'agent_version': '1.0.272.0',
'created_at': '2024-09-19T11:11:22.115829Z',
'customer_id': 'fdd168cc-6c5b-4c0b-b908-0323895e74f3',
'host_domain': 'DESKTOP-N6BRO6A',
'host_name': 'DESKTOP-N6BRO6A',
'incident_categories': ['MALWARE_DETECTED'],
'incident_id': '8b4645f7-d742-470e-8368-9017d1156d8b',
'incident_link': 'https://eu8.acronis.cloud/ui/#/endpoint-detection/customer/116/incidents/8b4645f7-d742-470e-8368-9017d1156d8b/investigation',
'incident_short_id': 1,
'incident_time': '2024-09-19T11:11:22.115829Z',
'mitigation_state': 'NOT_MITIGATED',
'positivity': 10,
'severity': 'HIGH',
'state': 'NOT_STARTED',
'updated_at': '2024-09-24T09:41:36.39723Z',
'verdict': 'MALICIOUS'},
{'agent_version': '0.0.0.0',
'created_at': '2024-09-20T05:23:22.794725Z',
'customer_id': 'e71026a0-3676-435c-9e31-1aba91f0d63b',
'host_name': 'bogdajs-Virtual-Machine.local',
'incident_categories': ['MALWARE_DETECTED'],
'incident_id': '6796cbbd-d755-401b-8fbe-70d73a3dfb64',
'incident_link': 'https://eu8.acronis.cloud/ui/#/endpoint-detection/customer/186/incidents/6796cbbd-d755-401b-8fbe-70d73a3dfb64/investigation',
'incident_short_id': 1,
'incident_time': '2024-09-20T05:23:22.794725Z',
'mitigation_state': 'NOT_MITIGATED',
'positivity': 10,
'severity': 'HIGH',
'state': 'NOT_STARTED',
'updated_at': '2024-09-20T05:23:22.794725Z',
'verdict': 'MALICIOUS'}]}



Store the list of incident IDs and customer IDs in a variable named incidents.
>>> incidents = [{'incident_id': item['incident_id'], 'customer_id': item['customer_id']} for item in response.json()['items']]
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



Note
Each incident is associated with a specific customer ID. You must keep the pair
to be able to perform actions on the incidents later.