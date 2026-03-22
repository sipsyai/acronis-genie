---
title: "Response mapping example"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/response-mapping-examples.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:09:05.835222"
---

# Response mapping example

Response mapping example

In the following example, a table which lists users is populated by a data initializer callback.
The table has a Get machine action button. This action button is available only when the user selects a single row.
When the user clicks Get machine, the CyberApp sends a callback named GetMachineInfo the callback handler.




The request payload of the GetMachineInfo callback supplies the callback handler with the userid from the selected table row:
{
"type": "object",
"$schema": "http://json-schema.org/draft-04/schema",
"properties": {
"userid": {
"type": "string"
}
}
}


The response payload of the GetMachineInfo callback supplies the CyberApp with user machine details from the ISV cloud service:
{
"type": "object",
"$schema": "http://json-schema.org/draft-04/schema",
"properties": {
"username": {
"type": "string"
},
"machineid": {
"type": "integer"
},
"machineos": {
"type": "string"
},
"machinemake": {
"type": "string"
},
"machinemodel": {
"type": "string"
}
}
}



The CyberApp developer maps the response payload data items to the form model in order to display them to the user.

In the following illustration, the developer has already mapped three elements on the form. However, when the developer tries to map the fourth element (MID), the mapping is not possible because the property type in the payload does not match the form element type.
The developer changes the form element type and tries again. This time, they are able to map.