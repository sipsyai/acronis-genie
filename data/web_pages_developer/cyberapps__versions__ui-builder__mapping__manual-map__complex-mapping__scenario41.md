---
title: "Scenario 4.1: Left property is a primitive or an object at root level, and right property is an array property"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/scenario41.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:40.037351"
---

# Scenario 4.1: Left property is a primitive or an object at root level, and right property is an array property

Scenario 4.1: Left property is a primitive or an object at root level, and right property is an array property

Availability
Single request mapping and response mapping.
This is a special case that is only enabled for arrays whose properties have been mapped previously. In some cases, it is useful to copy a single value over all items of an array.


Example
To map some data from a table to an array, but to also add some fixed data for every row, because we want to bulk-edit some rows.
We can map some table columns to some array properties, and map some singular values to other properties in the array, which will be copied for every row.

Form and mappings







Element
ID (Model property)
Mapped to



Table 1
table





Table 1 Column 1
id
data.id

Table 1 Column 2
username
data.username

Table 1 Column 3
age





Input 1
newAge
data.age





Callback payload
{
“type”: “object”,
“properties”: {
“data”: {
“type”: “array”,
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