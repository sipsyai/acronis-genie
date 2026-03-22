---
title: "Create a ledger"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/create-ledger.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:39.338756"
---

# Create a ledger

Create a ledger

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named ledger_info, and then assign an object with information about ledger to this variable:
>>> ledger_info = {
...     "Number": "8000",
...     "Description": "Example ledger",
...     "Active": True,
... }



Convert the ledger_info object to a JSON text:
>>> ledger_info = json.dumps(ledger_info, indent=4)
>>> print(ledger_info)
{
"Number": "8000",
"Description": "Example ledger",
"Active": true
}



Send a PUT request with the JSON text to the /Ledger endpoint:
>>> response = requests.put(
...     f'{base_url}/Ledger',
...     headers={'Content-Type': 'application/json', **auth},
...     data=ledger_info,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains an object with the information about created ledger formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"Id": "3d5bd08d-89ee-4bd9-bc88-351f130c7126",
"Tenant": "0dc377ec-e970-42e2-9e95-7ff9d8b05c11",
"Active": true,
"Number": "8000",
"Description": "Example ledger",
"ExternalId": "",
"CreationDate": "2024-09-25T17:29:52.2261137",
"AllowInactive": false,
"LastChangeDate": null
}