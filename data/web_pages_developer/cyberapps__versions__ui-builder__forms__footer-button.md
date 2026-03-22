---
title: "Setting up a footer button"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/forms/footer-button.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:07:19.253750"
---

# Setting up a footer button

Setting up a footer button
Footer buttons are optional buttons located on the footer of dependent forms.

To set up a footer button

Open the dependent form.
Click + New footer button.





Enter an Action name for the button
This displays as the footer button label.



Select a Type from the dropdown list.
Each type has a different style. See examples.



Primary
Secondary
Danger
Ghost
Promo
Translucent




[Optional] Select an Icon name from the dropdown list.
This inserts an icon to the left of the Action name label. See examples.
If you select a monochrome icon, it is displayed in white. A colored icon is displayed unaltered.


In the Operations section:

This section defines operations executed when a user clicks the footer button.
You can define multiple (optional) data operations and a form operation.



[Optional] Data operations


Click + Add to define a data operation.
Select the Operation type.


Callback
Executes a callback.
You must select the callback from the dropdown list.



Set parameters
This option allows you to explicitly set form element and input parameter values if the user clicks the button. A common use for this functionality is for a reset filters button without executing a callback.
When you select this option, a JSON edit panel appears, where you must provide JSON to apply when the user clicks the button. The edit panel is interactive: it suggests element IDs and parameters as you type, highlights invalid IDs and parameters, and indicates invalid values.




Repeat the previous steps for all the data operations that you want to execute when a user clicks the button.

Note
Click the trash can icon to remove a data operation.





Form operation

Select an action from the dropdown list.


No action [default]
No form action is executed.
Select Trigger ‘form accepted’ event to pass any defined output parameters to the parent form, and trigger the data initializer callback on the parent form.



Open form
Select the child form Mode (Popup or Sidebar) and the child Form name to open.
Map any input or output parameters for the child form.



Close form
Closes the current form.
Select Trigger ‘form accepted’ event to pass any defined output parameters to the parent form, and trigger the data initializer callback on the parent form.









Click outside the popup window to save your changes.


Note

You can reorder footer buttons by clicking and dragging a footer button panel.
To delete a footer button, click its trash can icon.
Each Footer button panel provides a summary of the operations that you defined for the button.




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