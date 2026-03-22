---
title: "Fetch ticket priorities"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-service-desk/fetch-ticket-priorities.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:48.474646"
---

# Fetch ticket priorities

Fetch ticket priorities

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /Priorities endpoint:
>>> response = requests.get(f'{base_url}/Priorities', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of priorities that can be assigned to a ticket formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"priorities": [
{
"Id": "683a47ec-e57c-43a5-ba10-2ccdc03fd331",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Default Priority",
"Active": true,
"InUse": false,
"IsDefault": true,
"APIConnection": null,
"ExternalIdentifier": 0,
"Alias": null,
"LastChangeDate": null
}
]
}