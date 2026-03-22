---
title: "Create a product"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/create-product.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:43.564336"
---

# Create a product

Create a product
To be able to create invoices and manage billing based on the products you offer,
you need to create a product that may be used:

As a part of the contract.
As a part of the sales item.
As a part of the project product.
In the service desk tickets as a part of support activity.

As an example, a product for support activity is created in this procedure.

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



[Optional] Fetch a ledger number that is used to track the product sales. If you do not have a ledger, create one by following the Create a ledger procedure.
>>> ledger_number
"8000"



Define a variable named product, and then assign an object with information about the product to this variable:
>>> product = {
...     "Name": "Test-Product-API-Documentation",
...     "Description": "Test-Product-API-Documentation-Description",
...     "Taxable": True, # Whether the product is taxable.
...     "Price": 100, # Price for the product in your country's currency.
...     "ViewInContract": False, # Whether the product is selectable in the contract.
...     "ProjectProduct": False, # Whether the product is selectable in projects.
...     "ProjectProductPriceAdjustable": False, # Whether the project product price is adjustable per project. Applicable only when ProjectProduct is true.
...     "TicketProduct": False, # Whether the product can be sold in service desk tickets as a part of support activity.
...     "PriceAdjustable": False, # Whether the ticket product price is adjustable by engineer Applicable only when TicketProduct is true.
...     "VAR": False, # Whether the product is a value-added reseller product.
...     "ProductForActivityBasedTicketBilling": False, # Whether the product can be used as an hourly rate for the ticket time billing.
...     "Cost": 20, # Cost of the product in your country's currency.
...     "Active": True,
...     "LedgerNumber": ledger_number,
... }



Convert the product object to a JSON text:
>>> product = json.dumps(product, indent=4)



Send a PUT request with the JSON text to the /Product endpoint:
>>> response = requests.put(
...     f'{base_url}/Product',
...     headers={'Content-Type': 'application/json', **auth},
...     data=product,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains an object with the information about created product formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'AcronisId': None,
'Active': True,
'Cost': 20.0,
'CreationDate': '2024-08-09T10:03:18.183',
'CustomFields': None,
'Description': 'Test-Product-API-Documentation-Description',
'ExternalIdNumber': None,
'Id': '25043e67-7752-405d-9d8b-ca2a30f52a34',
'InUse': False,
'InUseInBundles': False,
'InUseInContracts': False,
'InUseInProjects': False,
'InUseInQuoteTemplates': False,
'InUseInSales': False,
'InUseInTicketBilling': False,
'InUseInTickets': False,
'InternalDescription': None,
'InternalName': None,
'IsDefault': False,
'LastChangeDate': '2024-08-09T00:00:00',
'Ledger': None,
'LedgerDescription': None,
'LedgerNumber': None,
'Name': 'Test-Product-API-Documentation',
'Price': 100.0,
'PriceAdjustable': False,
'ProductForActivityBasedTicketBilling': False,
'ProjectProduct': False,
'ProjectProductPriceAdjustable': False,
'SKU': None,
'Taxable': True,
'Tenant': 'c4b9389c-4fae-44de-a5bc-7fbda064d07a',
'TicketProduct': False,
'VAR': False,
'ViewInContract': False}