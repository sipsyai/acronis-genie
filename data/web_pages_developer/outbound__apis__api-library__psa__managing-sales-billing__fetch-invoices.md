---
title: "Fetch a list of invoices"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/fetch-invoices.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:08.919288"
---

# Fetch a list of invoices

Fetch a list of invoices

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
...     "PaymentStatusNotConfirmed": True,
... }



Note
For a complete list of possible filters, refer to the API reference.


Send a GET request to the /InvoiceOverview endpoint:
>>> response = requests.get(f'{base_url}/InvoiceOverview', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of invoices formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"Invoices": [
{
"Id": "e96e60a2-3fec-44f7-86b7-050a8103b431",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Customer": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"CustomerName": "cstmr_001",
"BillingEntityName": "Default billing entity",
"CreationDate": "2024-10-10T07:55:09.3546699+00:00",
"ScheduledAt": "2024-10-10T00:00:00",
"SendByEmail": false,
"InvoiceNumber": "1-20241010-0-11111-4",
"BatchNumber": "1",
"Exported": false,
"ExportedDate": "0001-01-01T00:00:00+00:00",
"PaymentSent": false,
"PaymentStatus": false,
"InvoicedBy": "Partner Administrator",
"InvoicerDeleted": false,
"PaymentType": 3,
"PaymentDate": "0001-01-01T00:00:00",
"Incasso": true,
"Total": 123.75,
"InvoiceXml": null,
"InvoiceQueueId": "00000000-0000-0000-0000-000000000000",
"InvoiceQueueStatus": 0,
"InvoiceQueueLastUpdateTime": "0001-01-01T00:00:00",
"InvoiceQueueErrorCount": 0,
"InvoiceQueueErrorMessage": null,
"InvoiceQueueExternalInvoiceStatus": 0,
"IsConsolidateBillingStructure": true,
"PaymentMethod": null
},
{
"Id": "f2a3f46e-d6d8-4692-8271-4f8600fb2bb0",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Customer": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"CustomerName": "cstmr_001",
"BillingEntityName": "Default billing entity",
"CreationDate": "2024-10-10T10:08:19.6948387+00:00",
"ScheduledAt": "2024-10-10T00:00:00",
"SendByEmail": false,
"InvoiceNumber": "2-20241010-0-11111-6",
"BatchNumber": "2",
"Exported": false,
"ExportedDate": "0001-01-01T00:00:00+00:00",
"PaymentSent": false,
"PaymentStatus": false,
"InvoicedBy": "Partner Administrator",
"InvoicerDeleted": false,
"PaymentType": 3,
"PaymentDate": "0001-01-01T00:00:00",
"Incasso": false,
"Total": 100.16,
"InvoiceXml": null,
"InvoiceQueueId": "00000000-0000-0000-0000-000000000000",
"InvoiceQueueStatus": 0,
"InvoiceQueueLastUpdateTime": "0001-01-01T00:00:00",
"InvoiceQueueErrorCount": 0,
"InvoiceQueueErrorMessage": null,
"InvoiceQueueExternalInvoiceStatus": 0,
"IsConsolidateBillingStructure": true,
"PaymentMethod": null
},
{
"Id": "de4fcff3-cba7-40e4-8bb2-f5decf8f9246",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Customer": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"CustomerName": "cstmr_001",
"BillingEntityName": "Default billing entity",
"CreationDate": "2024-10-10T10:08:19.6948387+00:00",
"ScheduledAt": "2024-10-10T00:00:00",
"SendByEmail": false,
"InvoiceNumber": "2-20241010-0-11111-5",
"BatchNumber": "2",
"Exported": false,
"ExportedDate": "0001-01-01T00:00:00+00:00",
"PaymentSent": false,
"PaymentStatus": false,
"InvoicedBy": "Partner Administrator",
"InvoicerDeleted": false,
"PaymentType": 3,
"PaymentDate": "0001-01-01T00:00:00",
"Incasso": false,
"Total": 18.90,
"InvoiceXml": null,
"InvoiceQueueId": "00000000-0000-0000-0000-000000000000",
"InvoiceQueueStatus": 0,
"InvoiceQueueLastUpdateTime": "0001-01-01T00:00:00",
"InvoiceQueueErrorCount": 0,
"InvoiceQueueErrorMessage": null,
"InvoiceQueueExternalInvoiceStatus": 0,
"IsConsolidateBillingStructure": true,
"PaymentMethod": null
}
],
"Paging": {
"AmountTotalItems": 3,
"AmountRecordsFound": 3,
"AmountOfPages": 1
},
"Batches": [
{
"BatchNumber": "1",
"BatchLength": 1
},
{
"BatchNumber": "2",
"BatchLength": 2
}
]
}