---
title: "Fetch billable sales items"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/fetch-billable-sales-items.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:00.508727"
---

# Fetch billable sales items

Fetch billable sales items

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch a billing entity that will be issuing the invoice by following the Fetch information about billing entities procedure.
As a result, you should have a billing entity ID that you will use in the following steps:
>>> billing_entity_id
'c4666cb7-ca5f-401d-8ebc-bf58a142b9f1'



Define a variable named params, and then assign an object with the parameters for the request to this variable:
>>> params = {
...     "billingEntity": billing_entity_id,
...     "invoiceDate": "2024-09-26T14:02:31.917Z" # filters sales items that are past the specified invoice date
... }



Send a GET request to the /Billing endpoint:
>>> response = requests.get(f'{base_url}/Billing', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the list of billable sales items formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"SalesItems": [
{
"Id": "c3e238b0-dd86-4cef-9d88-17b0570f51e7",
"Customer": "cstmr_001",
"StartDate": "2024-06-28T00:00:00",
"EndDate": null,
"Description": "Workstation management - ",
"Ledger": "402"
},
{
"Id": "944184ee-0180-4fe6-80a0-961e5195be07",
"Customer": "cstmr_001",
"StartDate": "2024-06-28T00:00:00",
"EndDate": null,
"Description": "Workstation management - ",
"Ledger": "402"
},
{
"Id": "027a191d-8f96-4427-90a2-d888570a2173",
"Customer": "cstmr_001",
"StartDate": "2024-06-28T00:00:00",
"EndDate": null,
"Description": "Workstation management - ",
"Ledger": "402"
}
],
"IncassoContractTerms": [],
"NonIncassoContractTerms": []
}