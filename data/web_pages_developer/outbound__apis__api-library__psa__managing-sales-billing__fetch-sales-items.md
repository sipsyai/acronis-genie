---
title: "Fetch a list of sales items"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/fetch-sales-items.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:27.344024"
---

# Fetch a list of sales items

Fetch a list of sales items

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
...     "SortColumn": "InvoiceDate",
...     "SortDirection": "Desc",
... }



Send a GET request to the /SalesItems endpoint:
>>> response = requests.get(f'{base_url}/SalesItems', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the list of sales items formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"sales": {
"SalesItems": [
{
"Id": "c3e238b0-dd86-4cef-9d88-17b0570f51e7",
"Customer": "cstmr_001",
"InvoiceDate": "2024-06-28T00:00:00",
"HasBeenBilled": false,
"TotalAmount": 6.600000,
"Age": 0
},
{
"Id": "944184ee-0180-4fe6-80a0-961e5195be07",
"Customer": "cstmr_001",
"InvoiceDate": "2024-06-28T00:00:00",
"HasBeenBilled": false,
"TotalAmount": 10.000000,
"Age": 0
},
{
"Id": "027a191d-8f96-4427-90a2-d888570a2173",
"Customer": "cstmr_001",
"InvoiceDate": "2024-06-28T00:00:00",
"HasBeenBilled": false,
"TotalAmount": 3.300000,
"Age": 0
},
{
"Id": "d8b01952-054f-42b4-9a9f-b002e3bd0c05",
"Customer": "cstmr_001",
"InvoiceDate": "2024-10-09T00:00:00",
"HasBeenBilled": false,
"TotalAmount": 100.000000,
"Age": 1
},
{
"Id": "7a48a73c-7ec5-4ea7-9c9c-7f41fd207e19",
"Customer": "cstmr_001",
"InvoiceDate": "2024-10-10T00:00:00",
"HasBeenBilled": true,
"TotalAmount": 123.750000,
"Age": 0
},
{
"Id": "e4469386-e8fc-4a17-902c-b2729c9d0b38",
"Customer": "cstmr_001",
"InvoiceDate": "2024-10-10T00:00:00",
"HasBeenBilled": false,
"TotalAmount": 0.160000,
"Age": 0
}
],
"AmountRecordsFound": 6,
"AmountOfPages": 0,
"AmountTotalItems": 8
}
}