---
title: "Building element visibility logic"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/visibility/build-visibility.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:03:56.424412"
---

# Building element visibility logic

Building element visibility logic
You build visibility logic on the VISIBILITY tab of the UI builder configuration pane.


To build element visibility logic

Click the element you want to control on the UI Builder canvas.
Select the VISIBILITY tab in the configuration pane.
Click New dependency.
Select the element State you want to control:


Visible
Enabled




Select the Condition block modifier:



And
Or



Note
These are equivalent to the common logical operators.


[Optional] Click New condition to add a condition to the block and select a Condition type:



Enablement state
The enablement state of the CyberApp for the partner administrator or customer administrator when they open the form. Options are Enabled and Disabled.



Note
This condition type is only available for the CyberApp enablement form, and the customer enablement form.




Model
For more information, see Setting model condition types and Model condition type examples.



Form Validation state
For more information, see Setting form-level condition types and Form-level condition type examples.



Form Dirty state
For more information, see Setting form-level condition types and Form-level condition type examples.



Form Touched state
For more information, see Setting form-level condition types and Form-level condition type examples.



Roles
The role of the user accessing the form.



Note

Currently, you must know the internal Acronis role names you are interested in using. In a later release, we will introduce a dropdown with available options.





Offering items
For more information, see Setting offering items condition types.





[Optional] Click New condition to add another condition to the current logic block and repeat from step 6.
[Optional] Click New block to create a recursive logic block and repeat from step 5.
[Optional] Click New dependency to add a new dependency and repeat from step 4.


Note

To delete a condition, click Delete condition, at the bottom of the condition.
To delete a block, click Delete block, at the bottom of the block.
To delete a dependency, click Delete, at the bottom of the dependency.