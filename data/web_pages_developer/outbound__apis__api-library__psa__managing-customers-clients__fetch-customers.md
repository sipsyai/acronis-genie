---
title: "Fetch a list of customers"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-customers-clients/fetch-customers.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:18.269680"
---

# Fetch a list of customers

Fetch a list of customers

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named params, and then assign an object with request parameters to this variable:
>>> params = {
...     "Page": 1,
...     "PageSize": 50,
...     "Active": True,
... }



Send a POST request to the /Customer endpoint:
>>> response = requests.post(f'{base_url}/Customer', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of customers available in Acronis PSA formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"Customers": [
{
"Id": "8dcdc278-e900-458a-b245-eaca02c05939",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "cyber_prtnr_0810_1009am",
"Branch": null,
"Alias": "cyber_prtnr_0810_1009am",
"Status": 2,
"IsTier4": false,
"DeploymentStatus": 1,
"DeploymentStatusValue": "Completed",
"DeploymentId": "00000000-0000-0000-0000-000000000000",
"DeploymentErrorMessage": null,
"StatusTranslation": "Customer",
"DeploymentDate": null,
"PaidAccount": false,
"TrialAccount": false,
"TrialExpirationDate": null,
"CreationDate": "2024-10-08T07:17:40.707",
"OnTier2": false,
"ExternalTenantId": "110",
"ExternalTenantUUID": "a890cc01-544d-4185-b5a8-38eb5e22c067",
"AcronisTenantId": null
},
{
"Id": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "cstmr_001",
"Branch": null,
"Alias": "cstmr_001",
"Status": 2,
"IsTier4": true,
"DeploymentStatus": 1,
"DeploymentStatusValue": "Completed",
"DeploymentId": "00000000-0000-0000-0000-000000000000",
"DeploymentErrorMessage": null,
"StatusTranslation": "Customer",
"DeploymentDate": null,
"PaidAccount": false,
"TrialAccount": false,
"TrialExpirationDate": null,
"CreationDate": "2024-10-08T07:17:50.613",
"OnTier2": false,
"ExternalTenantId": "111",
"ExternalTenantUUID": "eb104c83-d944-4744-8287-7ba19821deb0",
"AcronisTenantId": null
}
],
"AmountRecordsFound": 2,
"AmountOfPages": 0
}