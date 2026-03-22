---
title: "Fetch customer’s clients"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-customers-clients/fetch-customer-clients.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:09.859800"
---

# Fetch customer’s clients

Fetch customer’s clients

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch an ID of the customer registered in Acronis PSA by following the Fetch a list of customers procedure.
As a result, you should have a customer ID that you will use in the following steps:
>>> customer_id
'ad3c629b-0969-4062-bb8b-6600a84565ab'



Define a variable named params, and then assign an object with request parameters to this variable:
>>> params = {
...     "Page": 1,
...     "PageSize": 50,
...     "Customer": customer_id
... }



Send a POST request to the /Person endpoint:
>>> response = requests.post(f'{base_url}/Person', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the list of users registered in this customer formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"Clients": [
{
"Id": "65f61819-465d-4fb1-b124-13282aa1fb09",
"Customer": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"Name": "cstmr_001 admin",
"FirstName": "cstmr_001",
"LastName": "admin",
"Email": "cstmr_usr_0810_1014am@mailinator.com",
"Username": "cstmr_usr_0810_1014am",
"Phonenumber": null,
"Enabled": true,
"Selected": false,
"Role": "ClientManager",
"IsLogin": true,
"Password": null,
"Question": null,
"Answer": null,
"DaysOffPerYear": 15,
"UseDefaultDaysOff": false,
"UserWorkingHours": {
"Monday": 8,
"Tuesday": 8,
"Wednesday": 8,
"Thursday": 8,
"Friday": 8,
"Saturday": 0,
"Sunday": 0
},
"IsTier4": false,
"PrimaryContact": false,
"NotifyPrimaryContact": false,
"Countable": false,
"Deleted": false,
"Activated": null,
"Deactivated": null,
"IsDefault": false,
"IsContinuum": false,
"IsTheLastOne": false,
"HideBilling": false,
"MFASecret": null,
"HourlyCost": 0.00,
"RemainingTimeBalance": null,
"IsContact": false
},
{
"Id": "3767cab4-56b6-4956-91c4-4053f77e8ea4",
"Customer": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"Name": "cstmr_001 Default User",
"FirstName": "cstmr_001",
"LastName": "Default User",
"Email": "Unknown_cstmr001@unknown.com",
"Username": null,
"Phonenumber": null,
"Enabled": true,
"Selected": false,
"Role": "",
"IsLogin": false,
"Password": null,
"Question": null,
"Answer": null,
"DaysOffPerYear": 0,
"UseDefaultDaysOff": false,
"UserWorkingHours": {
"Monday": 0,
"Tuesday": 0,
"Wednesday": 0,
"Thursday": 0,
"Friday": 0,
"Saturday": 0,
"Sunday": 0
},
"IsTier4": false,
"PrimaryContact": true,
"NotifyPrimaryContact": false,
"Countable": false,
"Deleted": false,
"Activated": null,
"Deactivated": null,
"IsDefault": false,
"IsContinuum": false,
"IsTheLastOne": false,
"HideBilling": false,
"MFASecret": null,
"HourlyCost": 0.00,
"RemainingTimeBalance": null,
"IsContact": false
},
{
"Id": "78b7b594-f05e-4e44-9b26-c3d3b44529ee",
"Customer": "ce570f06-f444-426b-b9b0-3aa8ef9b951e",
"Name": "cstmr_001 Manager",
"FirstName": "cstmr_001",
"LastName": "Manager",
"Email": "cstmr001Manager@dummy.com",
"Username": null,
"Phonenumber": null,
"Enabled": true,
"Selected": false,
"Role": "",
"IsLogin": false,
"Password": null,
"Question": null,
"Answer": null,
"DaysOffPerYear": 0,
"UseDefaultDaysOff": false,
"UserWorkingHours": {
"Monday": 0,
"Tuesday": 0,
"Wednesday": 0,
"Thursday": 0,
"Friday": 0,
"Saturday": 0,
"Sunday": 0
},
"IsTier4": false,
"PrimaryContact": false,
"NotifyPrimaryContact": false,
"Countable": false,
"Deleted": false,
"Activated": null,
"Deactivated": null,
"IsDefault": false,
"IsContinuum": false,
"IsTheLastOne": false,
"HideBilling": false,
"MFASecret": null,
"HourlyCost": 0.00,
"RemainingTimeBalance": null,
"IsContact": false
}
],
"Paging": {
"AmountRecordsFound": 3,
"AmountOfPages": 1
}
}