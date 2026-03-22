---
title: "Specifying a data initializer callback"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/forms/data-init-callback.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:57.739138"
---

# Specifying a data initializer callback

Specifying a data initializer callback
A Data initializer callback retrieves data from the ISV cloud service callback handler when a form is first loaded. This data can be displayed by mapping response data to UI elements and/or stored by mapping to input parameters.

Note
You can display and store data by creating a UI element and an input parameter with the same id.


To specify a data initializer callback

Note

You must first create the callback you want to use as the data initializer callback.
Ensure that it has the appropriate request and response payloads to provide the data you require for your form.



Open the form you want to specify a data initializer callback for.
Add the elements and add the input parameters necessary to display and/or store the data required and/or requested by the data initializer callback.


Note
UI elements that you want to map to the callback reponse data must have an ID assigned.



Select the callback from the Data initializer callback dropdown.
[If required] Specify the callback request mapping to supply the callback request payload with data.
Specify the callback response mapping to display data on the form or store data in form input parameters.



Example

In this example, a callback named getusers is chosen as the Data initializer callback.

The request payload includes the Acronis tenant ID and a variable called usergroup as data filters.
The developer created two input parameters to use in the mapping, as illustrated in Adding input parameters.

The callback response payload is an array of user names.
This array is mapped to a UI table to display the list of user names.



Example callback request payload
{
"type": "object",
"$schema": "http://json-schema.org/draft-04/schema",
"properties": {
"items": {
"type": "object",
"properties": {
"tenantid": {
"type": "string"
},
"usergroup": {
"type": "string"
}
}
}
}
}




Example callback response payload
{
"type": "object",
"$schema": "http://json-schema.org/draft-04/schema",
"properties": {
"items": {
"type": "array",
"items": {
"type": "object",
"properties": {
"id": {
"type": "string"
},
"firstname": {
"type": "string"
},
"secondname": {
"type": "string"
}
}
}
}
}
}