---
title: "Create an invoice for a customer"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/create-invoice.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:35.117437"
---

# Create an invoice for a customer

Create an invoice for a customer

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



Fetch a list of billable sales items created for the billing entity by following the Fetch billable sales items procedure.
As a result, you should have a list of sales items that you will use in the following steps:
>>> sales_items
["c3e238b0-dd86-4cef-9d88-17b0570f51e7", "944184ee-0180-4fe6-80a0-961e5195be07", "027a191d-8f96-4427-90a2-d888570a2173"]



Create a variable named invoice_date and store the current invoice date:
>>> import datetime
>>> invoice_date = datetime.date.today().strftime('%Y-%m-%d')



Define a variable named invoice_data, and then assign an object containing invoice data to this variable:
>>> invoice_data = {
...     "IsPreview": False,
...     "InvoiceDate": invoice_date,
...     "Sales": sales_items,
...     "IncassoContracts": [],
...     "NonIncassoContracts": [],
...     "BillingEntity": billing_entity_id,
... }



Send a POST request to the /httphandlers/billing/invoices.ashx endpoint:
>>> response = requests.post(
...     f'{base_url}/httphandlers/billing/invoices.ashx',
...     headers=auth,
...     files={"request": json.dumps(invoice_data)},
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful and a stream with the resulting PDF invoice is returned.