---
title: "Fetch a list of products"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/fetch-products.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:13.123185"
---

# Fetch a list of products

Fetch a list of products

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named params, and then assign an object with the parameters for the request to this variable:
>>> params = {
...     "Page": 1,
...     "PageSize": 50,
...     "Active": True
... }



Send a GET request to the /Products endpoint:
>>> response = requests.get(f'{base_url}/Products', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the list of products formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"products": {
"Result": {
"Products": [
{
"Id": "777e8e6d-c4e6-443b-ba2a-49bd107e0ce0",
"Name": "Test-Product-API-Documentation",
"Price": 100.0000,
"Cost": 20.0000,
"Active": true,
"ViewInContract": true,
"Ledger": null,
"Description": "Test-Product-API-Documentation-Description",
"ExternalIdNumber": null,
"LastChangeDate": "2024-10-10T00:00:00",
"AcronisId": null
}
],
"Paging": {
"AmountTotalItems": 1,
"AmountRecordsFound": 1,
"AmountOfPages": 1
}
}
}
}