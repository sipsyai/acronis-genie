---
title: "Fetch products for activity-based ticket billing"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-service-desk/fetch-ticket-activity-products.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:44.271950"
---

# Fetch products for activity-based ticket billing

Fetch products for activity-based ticket billing

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /ProductsForActivityBasedTicketBilling endpoint:
>>> response = requests.get(f'{base_url}/ProductsForActivityBasedTicketBilling', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of products for activity-based ticket billing formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"ProductsForActivityBasedTicketBilling": [
{
"Id": "99bf5480-a641-46ab-a44c-76961b150a63",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Active": false,
"Taxable": false,
"Name": "Support outside of business hours",
"InternalName": null,
"Description": null,
"InternalDescription": null,
"Price": 0,
"Cost": 0,
"ViewInContract": false,
"ProductForActivityBasedTicketBilling": false,
"Ledger": null,
"CreationDate": "0001-01-01T00:00:00",
"LastChangeDate": null,
"VAR": false,
"TicketProduct": false,
"PriceAdjustable": false,
"ProjectProductPriceAdjustable": false,
"ExternalIdNumber": null,
"ProjectProduct": null,
"SKU": null,
"AcronisId": null,
"InUseInSales": false,
"InUseInTickets": false,
"InUseInContracts": false,
"InUseInProjects": false,
"InUseInTicketBilling": false,
"InUseInBundles": false,
"InUseInQuoteTemplates": false,
"InUse": false,
"LedgerNumber": null,
"IsDefault": false,
"LedgerDescription": null,
"CustomFields": null
},
{
"Id": "493a36c9-4cd2-4b89-a693-99ac067d6776",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Active": false,
"Taxable": false,
"Name": "Support per hour",
"InternalName": null,
"Description": null,
"InternalDescription": null,
"Price": 0,
"Cost": 0,
"ViewInContract": false,
"ProductForActivityBasedTicketBilling": false,
"Ledger": null,
"CreationDate": "0001-01-01T00:00:00",
"LastChangeDate": null,
"VAR": false,
"TicketProduct": false,
"PriceAdjustable": false,
"ProjectProductPriceAdjustable": false,
"ExternalIdNumber": null,
"ProjectProduct": null,
"SKU": null,
"AcronisId": null,
"InUseInSales": false,
"InUseInTickets": false,
"InUseInContracts": false,
"InUseInProjects": false,
"InUseInTicketBilling": false,
"InUseInBundles": false,
"InUseInQuoteTemplates": false,
"InUse": false,
"LedgerNumber": null,
"IsDefault": false,
"LedgerDescription": null,
"CustomFields": null
}
]
}