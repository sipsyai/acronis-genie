---
title: "Fetch taxes"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-customers-clients/fetch-taxes.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:22.473027"
---

# Fetch taxes

Fetch taxes

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named params, and then assign the object with the parameters for the request to this variable:
>>> params = {
...     "Page": 1,
...     "PageSize": 50,
...     "Active": True
... }



Send a GET request to the /Taxes endpoint:
>>> response = requests.get(f'{base_url}/Taxes', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of taxes formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"taxes": [
{
"Id": "bc814c40-9114-4329-8eb5-5b1e89270afb",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Default tax",
"Value": 0.0,
"Active": true,
"Code": "TAX",
"AllowInactive": false,
"IsDefault": true,
"CustomFields": null
}
]
}