---
title: "Fetch customer details"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-customers-clients/fetch-customer-details.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:14.073833"
---

# Fetch customer details

Fetch customer details

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
...     "id": "8dcdc278-e900-458a-b245-eaca02c05939"
... }



Send a POST request to the /Customer endpoint:
>>> response = requests.post(f'{base_url}/Customer', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the details about the customer formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"Id": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "cstmr_001",
"DebtorCode": null,
"Alias": "cstmr_001",
"Status": 2,
"Language": "48d06c90-f8a4-4726-a83c-a47dbb709f25",
"TaxExempt": false,
"Tax": null,
"Country": "d46c54bd-1704-4a55-bb76-fc03073669a0",
"TicketUpdateMandatory": null,
"StateCountry": "f62da92d-73fe-4dd9-ab63-5fe51a3f694f",
"Street": "test",
"HouseNo": "1",
"HouseNoAdd": "-",
"Zipcode": "1",
"City": "test",
"Domain": "",
"Email": "cstmr_usr_0810_1014am@mailinator.com",
"FallbackInvoiceEmailAddress": "cstmr_usr_0810_1014am@mailinator.com",
"PhoneNumber": "+1234567890",
"Fax": "1",
"VATNumber": "",
"BankAccount": "",
"ADSyncID": "09cc109d-a662-4157-abc1-4a6308256772",
"DefaultSLA": "63b75905-10d4-44e9-ba1e-7aa2eff4100b",
"SupportGroup": "aa8623e5-e765-4663-967d-2cb6a209f8e1",
"DefaultBusinessUnit": "6fd181cf-10e7-4a99-a56f-cd143e50e368",
"SupportUser": "83bab5c4-ded7-4a6b-a249-591e15286361",
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
"BuildingName": "",
"PaidAccount": false,
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
"ExternalTenantId": "111",
"ExternalTenantUUID": "eb104c83-d944-4744-8287-7ba19821deb0",
"AcronisTenantId": null,
"LoginUserName": "cstmr_usr_0810_1014am",
"GroupId": null,
"StateCountryDescription": "Louisiana",
"CountryDescription": "United States",
"ExternalParentId": null,
"OccupancyRateNotificationThreshold": 85,
"CustomFields": []
}