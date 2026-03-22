---
title: "Create a service desk ticket"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-service-desk/create-service-desk-ticket.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:35.812918"
---

# Create a service desk ticket

Create a service desk ticket

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch a customer for which you would like to create a ticket by following the Fetch a list of customers procedure.
As a result, you should have a customer ID that you will use in the following steps:
>>> customer_id
'ad3c629b-0969-4062-bb8b-6600a84565ab'



Fetch a phone number of the customer by following the Fetch customer details procedure.
As a result, you should have a phone number of the customer that you will use in the following steps:
>>> client_phone
'083 2222 588'



Fetch a customer’s client that is associated with the ticket by following the Fetch customer’s clients procedure.
As a result, you should have a client ID that you will use in the following steps:
>>> client_id
'65f61819-465d-4fb1-b124-13282aa1fb09'



Fetch the service desk configuration by following the Fetch service desk configuration procedure.
As a result, you should have a business unit ID that you will use in the following steps:
>>> sla_id # Service Level Agreement ID
'd154891a-87a4-48e2-8742-f685199baabe'
>>> priority_id # Ticket priority ID
'683a47ec-e57c-43a5-ba10-2ccdc03fd331'
>>> status_id # Ticket status ID
'd154891a-87a4-48e2-8742-f685199baabe'
>>> support_user_id # Support user ID
'83bab5c4-ded7-4a6b-a249-591e15286361'
>>> business_unit_id # Business unit ID
'aa8623e5-e765-4663-967d-2cb6a209f8e1'
>>> category_id # Ticket category ID
'7dd37156-a0d2-4fd3-82aa-607a58f6cbc6'





[If you bill for support activity] Fetch the product for activity-based ticket billing by following the Fetch products for activity-based ticket billing procedure.
As a result, you should have a billing activity type ID that you will use in the following steps:
>>> billing_activity_type_id
'99bf5480-a641-46ab-a44c-76961b150a63'



Define a variable named ticket_info, and then assign an object with the ticket information to this variable:
>>> ticket_info = {
...     "Title": "New ticket",
...     "Message": "This is a new ticket",
...     "Category": category_id,
...     "Customer": customer_id,
...     "PhoneNumber": client_phone,
...     "Client": client_id,
...     "Priority": priority_id,
...     "Status": status_id,
...     "SupportUser": support_user_id,
...     "BusinessUnit": business_unit_id,
...     "ServiceLevelAgreement": sla_id,
...     "UpdateEmailRecipients": True, # Whether to send an email to the client
...     "BillTheCustomer": True, # Whether customer will be billed for the ticket at product's hourly rate
...     "BillingActivityType": billing_activity_type_id,
...     "Planned": None, # Whether ticket is scheduled for the date specified in the PlannedTicket field
...     # "PlannedTicket": {
...     #     "PlannedDate": "2024-10-09T18:00:00.000Z",
...     #     "StartHour": "2024-10-09T18:00:00.000Z",
...     #     "StartHourstamp": 1080,
...     #     "Hours": 1,
...     #     "Minutes": None
...     # },
...     "TicketProducts": [],
... }



Convert the ticket_info object to a JSON text:
>>> ticket_info = json.dumps(ticket_info, indent=4)



Send a PUT request with the JSON text to the /Call endpoint:
>>> response = requests.put(
...     f'{base_url}/Call',
...     headers={'Content-Type': 'application/json', **auth},
...     data=ticket_info,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the information about the created ticket formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{"id":"167bab29-05cc-4b8a-8b5b-e16fde847f90"}