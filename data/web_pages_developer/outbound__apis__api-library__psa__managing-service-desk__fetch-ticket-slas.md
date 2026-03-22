---
title: "Fetch a list of Service Level Agreements (SLA)"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-service-desk/fetch-ticket-slas.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:56.873686"
---

# Fetch a list of Service Level Agreements (SLA)

Fetch a list of Service Level Agreements (SLA)

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
...     "Active": True,
...     "Page": 1,
...     "PageSize": 50,
... }



Send a GET request to the /SLA endpoint:
>>> response = requests.get(f'{base_url}/SLA', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of available SLAs formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"SLAs": [
{
"Id": "63b75905-10d4-44e9-ba1e-7aa2eff4100b",
"Name": "Default SLA",
"Active": true,
"ShortName": null,
"ResponseTime": 80,
"FeedbackInterval": 400,
"IsUsed": false
},
{
"Id": "d154891a-87a4-48e2-8742-f685199baabe",
"Name": "Fixed Price 24/7",
"Active": true,
"ShortName": null,
"ResponseTime": 8,
"FeedbackInterval": 48,
"IsUsed": false
},
{
"Id": "7364885a-bbc4-4566-92a5-6bee29bc1ac4",
"Name": "Fixed Price Office hours",
"Active": true,
"ShortName": null,
"ResponseTime": 8,
"FeedbackInterval": 48,
"IsUsed": false
},
{
"Id": "43dceee4-e778-45b9-96e2-7cac9ed2578a",
"Name": "Time and materials",
"Active": true,
"ShortName": null,
"ResponseTime": 8,
"FeedbackInterval": 96,
"IsUsed": false
}
],
"Paging": {
"AmountRecordsFound": 4,
"AmountOfPages": 1
}
}