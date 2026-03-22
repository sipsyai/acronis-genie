---
title: "Request mapping examples"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/request-mapping-examples.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:09:01.452368"
---

# Request mapping examples

Request mapping examples

Example 1

In this example, a button element has been defined to trigger the createuser callback when clicked. The createuser callback has a request payload:
{
"type": "object",
"$schema": "http://json-schema.org/draft-04/schema",
"properties": {
"name": {
"type": "string"
},
"email": {
"type": "string"
},
"login": {
"type": "string"
}
}
}


A request mapping is therefore expected to map three string elements from the model form to the createuser callback request payload schema.


Example 2

In this example, a table has an action button defined to trigger the resetpassword callback when clicked. The resetpassword callback has a request payload:
{
"type": "object",
"$schema": "http://json-schema.org/draft-04/schema",
"properties": {
"id": {
"type": "string"
}
}
}


A request mapping is therefore expected to map one of the table elements from the model form to the resetpassword callback request payload schema.