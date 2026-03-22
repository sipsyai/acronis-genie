---
title: "Fetch information about billing entities"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/fetch-billing-entities.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:04.725327"
---

# Fetch information about billing entities

Fetch information about billing entities

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /BillingEntities endpoint:
>>> response = requests.get(f'{base_url}/BillingEntities', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the list of billing entities formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"entities": [
{
"Id": "c4666cb7-ca5f-401d-8ebc-bf58a142b9f1",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Default billing entity",
"BankAccountNumber": "",
"Active": true,
"FooterTextAutomaticDebit": "Automatic debit with bank account as following: [BANK_ACCOUNT_NUMBER], with customer name ->[CUSTOMER_NAME] and a vat number = [VAT_NUMBER]",
"FooterTextManualDebit": "[INVOICE_DUE_DAYS][INVOICE_NUMBER]",
"Right": false,
"MarginTop": 2.0,
"MarginTop2": 2.0,
"MarginSide": 1.0,
"InvoiceBackground": "",
"AddressBottomMargin": 2.5,
"PageBottomMargin": 1.5,
"InvoiceSerialNumber": "11111",
"InvoiceStartNumber": 4,
"ResetedInvoiceNumber": false,
"IsUsed": true,
"IsDefault": true,
"InvoiceDueDays": 14,
"PageNumberPosition": true,
"PageNumberVisibility": 0,
"HideInvoiceNumberPrefix": false,
"BillDaysInAdvance": 20,
"LastChangeDate": null,
"LastChangeDateACEP": null,
"SplitTotals": false
}
]
}