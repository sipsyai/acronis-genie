---
title: "Set billing information for a customer"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-customers-clients/set-customer-billing-info.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:30.909404"
---

# Set billing information for a customer

Set billing information for a customer

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



[If no customers created] Create a new customer tenant
with Account Management API v2.
As a result, you will get a tenant ID that you will use in the following steps.
>>> tenant
{
'name': 'Foobar',
'kind': 'customer',
'parent_id': tenant_id,
'language': 'en',
'contact': {
'address1': '24',
'address2': 'Esenni motivi',
'email': 'foo.bar@example.com',
'phone': '083 2222 588',
'zipcode': '1330',
'city': 'Sofia',
'country': 'Bulgaria',
},
}
>>> customer_tenant_id
'41e19c11-2606-475d-b459-56a5509494ee'



Choose a sales tax for your customer:

If a customer is subject to sales tax exemption, set the tax_exempt field to true.
>>> tax_exempt = True
>>> sales_tax_id = ""



If a customer is not subject to sales tax exemption, fetch a tax that you would like to apply by following the Fetch taxes procedure.
As a result, you should have an ID of the tax that you will use in the following steps:
>>> sales_tax_id
'bc814c40-9114-4329-8eb5-5b1e89270afb'
>>> tax_exempt = False





Fetch a list of countries and languages available in Acronis PSA by following the Fetch service desk configuration procedure
and choose a corresponding country and language for the customer.
As a result, you should have a country ID and a language that you will use in the following steps:
>>> country_id
'b28c162b-007a-42a1-ba97-d798e9e26909'
>>> language_id
'48d06c90-f8a4-4726-a83c-a47dbb709f25'



Define a variable named billing_info, and then assign an object with customer’s billing info to this variable:
>>> billing_info = {
...     "Tenant": tenant_id,
...     "Name": "New Customer",
...     "TaxExempt": tax_exempt,
...     "Tax": sales_tax_id,
...     "Language": language_id,
...     "Country": country_id,
...     "BankAccount": "AL35202111090000000001234567",
...     "VATNumber": "A23456789B",
...     "TrialAccount": False,
...     "DaysOffPerYear": 15,
...     "TimeRegistrationRoundupTime": 10, # in minutes
...     "PaymentTerms": 14, # in days
...     "LoginUserName": tenant['contact']['email'],
...     "SubtotalsOnInvoice": false, # Whether to create subtotals on invoices
...     "DirectDebit": false, # Whether to use direct debit
...     "SendInvoiceByEmail": false, # Whether to send invoices by email
...     "HouseNo": tenant['contact']['address1'],
...     "Street": tenant['contact']['address2'],
...     "Zipcode": tenant['contact']['zipcode'],
...     "City": tenant['contact']['city'],
...     "PhoneNumber": tenant['contact']['phone'],
...     "Email": tenant['contact']['email'],
... }



Note
For simplicity’s sake, the customer’s address re-uses the same contact information that was used to create a tenant.
You may specify different values if needed.


Convert the billing_info object to a JSON text:
>>> billing_info = json.dumps(billing_info, indent=4)



Send a PUT request with the JSON text to the /Customers endpoint:
>>> response = requests.put(
...     f'{base_url}/Customers',
...     headers={'Content-Type': 'application/json', **auth},
...     data=billing_info,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the information about the created customer formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"Id": "6074cc51-98d1-4f9d-b380-95d3277b5e98",
"Tenant": "0dc377ec-e970-42e2-9e95-7ff9d8b05c11",
"Name": "New Customer",
"DebtorCode": null,
"Alias": "New Customer",
"Status": 2,
"Language": "48d06c90-f8a4-4726-a83c-a47dbb709f25",
"TaxExempt": true,
"Tax": "bc814c40-9114-4329-8eb5-5b1e89270afb",
"Country": "d46c54bd-1704-4a55-bb76-fc03073669a0",
"TicketUpdateMandatory": null,
"StateCountry": "b4c87080-7c8c-45e0-8867-a714ffc79b7d",
"Street": "test",
"HouseNo": "test",
"HouseNoAdd": "test",
"Zipcode": "test",
"City": "test",
"Domain": "",
"Email": "yury.palyanitsa@acronis.com",
"FallbackInvoiceEmailAddress": "yury.palyanitsa@acronis.com",
"PhoneNumber": "test",
"Fax": "test",
"VATNumber": "",
"BankAccount": "",
"ADSyncID": "c2a53309-56e5-4640-b433-2154c4d41970",
"DefaultSLA": "63b75905-10d4-44e9-ba1e-7aa2eff4100b",
"SupportGroup": "2e4eea65-b277-4ec4-a777-07c71d622c44",
"DefaultBusinessUnit": "90c26810-e310-49e4-a1b5-0fd56c6f1655",
"SupportUser": "256b0fd2-9a50-4a73-9d08-5f11e2d104d7",
"CompanyType": "-",
"SendInvoiceByEmail": false,
"Addresses": [],
"InvoiceRecipients": [],
"TimeRegistrationRoundupTime": "10",
"Category": "7f8320eb-d653-40ae-9d57-1257bead1a29",
"Priority": "683a47ec-e57c-43a5-ba10-2ccdc03fd331",
"DaysOffPerYear": 15,
"IsTier4": true,
"Tier": "Tier 4",
"ShowPersons": true,
"TenantData": null,
"ParentCustomer": null,
"DefaultBillingEntity": null,
"ClientDocumentation": "",
"AutoPause": null,
"BuildingName": null,
"PaidAccount": true,
"TrialAccount": false,
"TrialExpirationDate": null,
"CreationDate": null,
"TrialAccountExpired": false,
"Tier3Id": "00000000-0000-0000-0000-000000000000",
"PaymentTerms": 14,
"InvoiceNotes": "",
"TierCulture": "en-US",
"DirectDebit": false,
"ConsolidateBilling": false,
"IsSetAsMainCustomer": false,
"OldParentId": "00000000-0000-0000-0000-000000000000",
"SubtotalsOnInvoice": false,
"GroupLinkedToCustomer": false,
"ExternalTenantId": "2360",
"ExternalTenantUUID": "41e19c11-2606-475d-b459-56a5509494ee",
"AcronisTenantId": null,
"LoginUserName": "yury.palyanitsa@acronis.com",
"GroupId": null,
"StateCountryDescription": "Alabama",
"CountryDescription": "United States",
"ExternalParentId": null,
"OccupancyRateNotificationThreshold": 85,
"CustomFields": []
}