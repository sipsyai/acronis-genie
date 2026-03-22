---
title: "Creating the CyberApp enablement form"
source: "https://developer.acronis.com/doc/cyberapps/versions/enablement-form/create-connection-setup-form.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:01:33.380479"
---

# Creating the CyberApp enablement form

Creating the CyberApp enablement form

Note
CyberApp enablement form can only have a root form. You cannot create any dependent forms for the CyberApp enablement form.


To create the CyberApp enablement form

Open the Version.
Select CyberApp enablement form from the menu.
Select Connection setup.


Note
There is only one CyberApp enablement form, so nothing is editable here.



Click  to build the connection form UI.
For more information, see the UI builder chapter


Select the Width property from the dropdown.


Standard

Wide
The form is displayed with an increased width of 904px.





Build the form.

Note
Remember that the CyberApp enablement form automatically includes:

The CyberApp name as the title of the form.
A Cancel button to close the form.
A Connect button to enable the CyberApp.



Drag elements from the UI element menu onto the canvas.


To set an element’s properties, select the element on the canvas and select the PROPERTIES tab in the configuration pane.
For more information, see the details pages for the element types.



[Optional] To control an element’s visibility and enablement, select the element on the canvas and select the VISIBILITY tab in the configuration pane.
For more information on visibility, see element visibility.



Note

The CyberApp enablement form has a special visibility Condition type called Enablement state, which other forms do not have. This allows you to control whether or not to display and enable an element, depending on whether or not the CyberApp is enabled for the partner.





[Optional] To set validation criteria for certain input elements, select the element on the canvas and select the VALIDATION tab in the configuration pane.
For more information, see Defining validation logic.




[Optional] To delete an element, select it and click .
[Optional] To find out more about an element, select it and click .
[Optional] To view a preview of your form, click .

Note
At this point, you will not see the Cancel and Connect buttons. These are added automatically when deployed.




When you are finished, click Done.
Click Save changes.