---
title: "Download a PDF invoice"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/download-invoice.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:52.102886"
---

# Download a PDF invoice

Download a PDF invoice

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch an invoice ID as described in Fetch a list of invoices and assign it to the id variable:
>>> id = "e96e60a2-3fec-44f7-86b7-050a8103b431"



Define a variable named params, and then assign an object with the parameters for the request to this variable:
>>> params = {
...     "id": id
... }



Send a GET request to the /DownloadInvoice endpoint:
>>> response = requests.get(f'{base_url}/DownloadInvoice', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful and a stream with the resulting PDF invoice is returned.