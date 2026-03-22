---
title: "Display table action buttons as ellipsis dropdown menu column for each table row"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/selecting-elements/table/buttons.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:10.212452"
---

# Display table action buttons as ellipsis dropdown menu column for each table row

Table action buttons
In the Action buttons section of a table element, you can define table action buttons, which appear above the table.

You can optionally turn on the Show actions as ellipsis button options in table row toggle switch  to add a table column with an ellipsis menu button, which displays the action button labels.
It also displays the  icon, which users can click to hide or display columns.


To add a table action button


Click + New action button.



Enter an Action name for the button
This displays as the action button label.



Select a Type from the dropdown list.
Each type has a different style. See examples.


Primary
Secondary
Danger
Ghost
Promo
Translucent



Availability
This determines whether the action button is clickable or not.


Always enabled
If one row is selected
If some rows are selected
If no rows are selected



[Optional] Select an Icon name from the dropdown list.
This inserts an icon to the left of the Action name label. See examples.
If you select a monochrome icon, it is displayed in white. A colored icon is displayed unaltered.


In the Operations section:

This section defines operations executed when a user clicks the action button.
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

You can reorder table action buttons by clicking and dragging the action button panel.
To delete an action button, click its trash can icon.
Each Action button panel provides a summary of the operations that you defined for the button.




Examples

Button types