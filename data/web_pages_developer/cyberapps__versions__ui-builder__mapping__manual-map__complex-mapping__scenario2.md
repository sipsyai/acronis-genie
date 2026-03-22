---
title: "Scenario 2: Both left and right properties are arrays"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/scenario2.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:27.396657"
---

# Scenario 2: Both left and right properties are arrays

Scenario 2: Both left and right properties are arrays

Availability
This is a common scenario. An entire array can be mapped to another array. The whole array will be copied from the left side to the right side.

Note
After mapping an array to an array, you cannot perform Scenario 5 or :doc:`Scenario 6 <scenario6>’ mappings.



Example
A table can be mapped to an array of objects in the callback request payload, given the table columns and the array object properties are compatible.

Form and mappings







Element
ID (Model property)
Mapped to



Table 1
table
data

Table 1 Column 1
id





Table 1 Column 2
username





Table 1 Column 3
age









Callback payload
{
"type": "object",
"properties": {
"data": {
"type": "array",
"items": {
"type: "object",
"properties": {
"id": {
"type: "number"
},
"username": {
"type": "string"
},
"age": {
"type": "number",
}
}
}
}
}
}