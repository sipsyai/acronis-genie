---
title: "Mapping data between forms"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/forms/form-data-mapping.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:07:23.756674"
---

# Mapping data between forms

Mapping data between forms
When you create a button element, a table action button, or a footer button with an Open form action, you can map input parameters, input control UI elements, and table array data from the current form to corresponding form model data items on the form that will open.

Note

To map form model data items, both sides of the mapping must have the same data type.
Input parameters can be Primitive type, which can map to either a String, Number, Integer, Boolean or Null data type.



To map data between forms

Open the source form and select the button.
Select Open form as the On click option.
Select the open form Mode.
Select the target form from the Form name dropdown.
In the Input parameter mapping section:



Select a data item from the Model dropdown.
This is the list of form model data items for the form model you are currently working on.



Select the corresponding data item from the Parameter dropdown.
This is the list of form model data items in the target form model.








Example
In this example, an Open form footer button is added to the User details dependent form.
User details has four form model data items:


userid
An input parameter, which is mapped to the userid form model data item of the root form when a user clicks to view a specific user’s details.
This is used to map to the request payload of the User details data initializer callback, which returns the other three form model data items.



userfirstname
An input element, which is mapped to the data initializer callback response payload.



usersecondname
An input element, which is mapped to the data initializer callback response payload.



useremail
An input element, which is mapped to the data initializer callback response payload.



The Open form footer button opens the User contact details dependent form.
User contact details requires userid to map to the data initializer callback request payload, so the developer must create an input parameter on User contact details and performs the request mapping.
The developer then maps the source form (user details) userid form model data item to this new target form (User contact details) userid input parameter.
The developer also maps the three input element data items on the source form to corresponding input element data items in the target form.
The rest of the user contact data is mapped from the data initializer callback response payload to the UI elements.