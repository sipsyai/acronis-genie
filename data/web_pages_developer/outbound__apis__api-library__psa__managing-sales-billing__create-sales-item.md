---
title: "Create a sales item"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-sales-billing/create-sales-item.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:47.869799"
---

# Create a sales item

Create a sales item

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Fetch a customer for which you would like to create a ticket by following the Fetch a list of customers procedure
and fetch their billing address by following the Fetch customer details procedure.
As a result, you should have a customer object that you will use in the following steps:
>>> customer
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
...


}

Fetch a list of products that you would like to sell to the customer by following the Fetch a list of products procedure.
As a result, you should have a list of product IDs that you will use in the following steps:
>>> products
[
{
"Id": "777e8e6d-c4e6-443b-ba2a-49bd107e0ce0",
"Name": "Test-Product-API-Documentation",
"Price": 100.0000,
"Cost": 20.0000,
"Active": true,
"ViewInContract": true,
"Ledger": null,
"Description": "Test-Product-API-Documentation-Description",
"ExternalIdNumber": null,
"LastChangeDate": "2024-10-10T00:00:00",
"AcronisId": null
}
]



Make an empty list that will contain the products you want to sell to the customer:
>>> sales_item_products = []



For each product in the list, specify the following information:

Quantity and a price for the product:
>>> quantity = 5
>>> price = product['Price']



Note
You may specify a different quantity and price for each product.
Total price will be computed by Acronis PSA.


[Optional] Specify a discount for the product:
>>> discount = 0



Add the product to the list of products:
>>> sales_item_products.append(
...     {
...         "Product": product['Id'],
...         "Quantity": quantity,
...         "Price": price,
...         "Discount": discount
...     }
... )



[Optional] Add a line note item to the list of products:
>>> sales_item_products.append(
...     {
...         "Description": "Line note Description",
...         "Price": 0,
...         "Quantity": 0,
...         "Product": product['Id'],
...         "IsItemNote": True
...     }
... )





Fetch a billing entity that will be issuing the invoice by following the Fetch information about billing entities procedure.
As a result, you should have a billing entity ID that you will use in the following steps:
>>> billing_entity_id
'c4666cb7-ca5f-401d-8ebc-bf58a142b9f1'



Define a variable named sales_item, and then assign an object with information about the sales item to this variable:
>>> sales_item = {
"Customer": customer_id,
"SalesItemProducts": sales_item_products,
"BillingEntity": billing_entity_id,
"SendByEmail": true, # Whether to send the invoice for this sales item by email
"StartDate": "2024-10-30", # Date when the sales item starts
"Active": True,
...
# Customer billing address
"Zipcode": customer['Zipcode'],
"City": customer['City'],
"Street": customer['Street'],
"HouseNo": customer['HouseNo'],
"HouseNoAdd": customer['HouseNoAdd'],
"Country": customer['Country'],
"StateCountry": customer['StateCountry'],
"PhoneNumber": customer['PhoneNumber'],
"EmailAddress": customer['Email'],
}



Note
For the simplicity’s sake, customer’s billing address is re-used from the customer object.
You may specify a different billing address if needed.


Convert the sales_item object to a JSON text:
>>> sales_item = json.dumps(sales_item, indent=4)



Send a PUT request with the JSON text to the /SalesItem endpoint:
>>> response = requests.put(
...     f'{base_url}/SalesItem',
...     headers={'Content-Type': 'application/json', **auth},
...     data=sales_item,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains an object with an ID of the sales item formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"InventoryItemsWithAmountNegative": [],
"InsertedSaleId": "f9b48a93-922d-4b08-9365-26570ac61f5d"
}