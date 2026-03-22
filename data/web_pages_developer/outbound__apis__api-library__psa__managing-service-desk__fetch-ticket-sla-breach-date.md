---
title: "Fetch SLA breach date"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-service-desk/fetch-ticket-sla-breach-date.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:52.669924"
---

# Fetch SLA breach date

Fetch SLA breach date

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch a Service Level Agreement (SLA) by following the Fetch a list of Service Level Agreements (SLA) procedure.
As a result, you should have an SLA ID that you will use in the following steps:
>>> sla_id
'd154891a-87a4-48e2-8742-f685199baabe'



Define a variable named params, and then assign the object with request parameters to this variable:
>>> params = {
...     "baseDate": "1970-01-01T00:00:00Z"
...     "isPlanned": False,
...     "clientUpdate": False,
...     "serviceLevelAgreementId": sla_id
... }



Send a GET request to the /SLABreachDate endpoint:
>>> response = requests.get(f'{base_url}/SLABreachDate', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of support groups that can be assigned to a ticket formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"groups": [
{
"Id": "6fd181cf-10e7-4a99-a56f-cd143e50e368",
"Customer": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"Name": "cstmr_001Group",
"Manager": "78b7b594-f05e-4e44-9b26-c3d3b44529ee",
"ManagerName": "cstmr_001 Manager",
"ManagerDeleted": false,
"Active": true,
"Sequence": 0,
"Count": 3,
"Deleted": false,
"IsDefault": false,
"IsContinuum": false,
"Members": [],
"Alias": null
}
]
}