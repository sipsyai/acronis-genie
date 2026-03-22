---
title: "Specifying a refresh callback"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/forms/refresh-callback.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:07:53.635307"
---

# Specifying a refresh callback

Specifying a refresh callback
Some forms need to display progress or update status without active participation from the user.
Refresh callbacks enable this behaviour by retrieving data from the ISV cloud service callback handler.
This data can then be displayed by mapping response data to UI elements and/or stored by mapping to input parameters.
A form refresh callback can be different from the data initializer callback (it can also be the same), and it can update all or only part of the form (for example, a table without filters).
Refresh callback are executed in the background (i.e., there is no loader) every 5 seconds, unless:


Parameters mapped to the refresh callback are changed (that is, if the form model has changed because the user has changed properties).
There is a table mapped to the refresh callback, and the user has made a selection in the table.


Refresh starts again after the data initializer callback is executed.
If the refresh callback fails, a warning message displays with the text: Could not retrieve updated data.

Note
Just as with data initializer callbacks, you can display and store data by creating a UI element and an input parameter with the same id.


To specify a refresh callback

Note

You must first create the callback you want to use as the refresh callback.
Ensure that it has the appropriate request and response payloads to provide the data you require for your form.



Open the form for which you want to specify a refresh callback.
Add the elements and add the input parameters necessary to display and/or store the data required and/or requested by the refresh callback.


Note
UI elements that you want to map to the callback reponse data must have an ID assigned.



Select the callback from the Refresh callback dropdown.
[If required] Specify the callback request mapping to supply the callback request payload with data.
Specify the callback response mapping to display data on the form or store data in form input parameters.