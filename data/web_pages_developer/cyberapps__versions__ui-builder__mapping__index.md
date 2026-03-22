---
title: "Callback mapping"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:14.619126"
---

# Callback mapping

Callback mapping

Note
If you are not familiar with the concepts of ‘form model’ and ‘model properties’, please read The form model before you proceed.

CyberApps exchange data with your service using callbacks. Callbacks send data to or request data from your service in a callback request. They receive data from your service in a callback response.

For a CyberApp to display data received from your service in a form, you must map the callback response payload structure to the form model.
To send to your service data which a CyberApp user has entered, edited or selected in a form, you must map form model elements to the callback request payload structure.


UI builder uses JSON schema as the mechanism to define the mapping between:




Form model
You define this in the UI builder. It includes the UI elements and input parameters.



Callback payload (request or response)
You specify these when you create a callback.





The UI builder provide a visual representation of the form model and the callback payload, which you use to map values.
For more information about CyberApp callback payload, see the Payload JSON schema technical reference.

You can manually map individual model properties to callback payload data items, or you can use the auto-mapping feature to map model properties to callback data items which have the same name and compatible data types.

In this section

Callback mapping types
Manually mapping a callback payload
Auto-mapping a callback payload
Request mapping examples
Response mapping example
Deleting mappings