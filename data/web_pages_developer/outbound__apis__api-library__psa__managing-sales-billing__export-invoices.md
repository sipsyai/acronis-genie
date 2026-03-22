---
title: "Export invoices"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/export-invoices.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:56.308089"
---

# Export invoices

Export invoices

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch a list of invoice IDs as described in Fetch a list of invoices and assign them to the ids variable:
>>> ids = [
...     "e96e60a2-3fec-44f7-86b7-050a8103b431",
...     "f2a3f46e-d6d8-4692-8271-4f8600fb2bb0"
... ]



Define a variable named params, and then assign an object with the parameters for the request to this variable:
>>> params = {
...     "ids": ids,
...     "exportFormat": 1  # 0 for XML, 1 for CSV
... }



Send a POST request to the /ExportInvoice endpoint:
>>> response = requests.post(f'{base_url}/ExportInvoice', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful and a stream with the resulting invoices is returned.
Additionally, invoices will be marked as exported and have their export date set or updated.