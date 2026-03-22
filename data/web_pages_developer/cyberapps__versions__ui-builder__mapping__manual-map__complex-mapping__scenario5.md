---
title: "Scenario 5: Left property is an array and right properties is a single value"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/scenario5.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:44.266650"
---

# Scenario 5: Left property is an array and right properties is a single value

Scenario 5: Left property is an array and right properties is a single value

Availability
Multiple request mapping.

In previous scenarios, it was assumed that mapping was from one object (for example, the form model) to another object (for example, the callback request payload).
However, there are some scenarios in which we need to send more than one request. For example, when performing bulk actions in separate requests.
In this scenario, we map from a single object (our form model) to multiple objects (many callback requests). Since we need to send multiple requests, we will need different data for each, which means that we’ll need to use a collection on the left side that we can spread over many single items on the right side.


Note
After mapping an array to a single value, you cannot use :doc`scenario 2 <scenario2>`, scenario 3, scenario 4 or scenario 6.



Example
Similar to scenario 2, we have a table with some columns in our form, and we want to send all selected rows. However, we don’t want to send an array with all rows, but rather one request per row containing individual data for each row.

Form and mappings







Element
ID (Model property)
Mapped to



Table 1
table
rowData

Table 1 Column 1
id





Table 1 Column 2
username





Table 1 Column 3
age









Callback payload
{
“type”: “object”,
“properties”: {
“rowData”: {
“type”: “object”,
“items”: {
“id”: {
“type: “number”
},
“username”: {
“type”: “string”
},
“age”: {
“type”: “number”,
}
}
}
}
}



Note
There is no array in our schema, so we are spreading the values of our left array over many objects on the right side. Every other scenario (except for scenario 1) is disabled. This means that no other array can be mapped.