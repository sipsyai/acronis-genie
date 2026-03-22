---
title: "Scenario 4: Both left and right properties are array properties"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/scenario4.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:35.807768"
---

# Scenario 4: Both left and right properties are array properties

Scenario 4: Both left and right properties are array properties

Availability
Single request mapping and response mapping.

If we want to map an entire table, but our array object properties are named in a different way, mapping the entire table to the array, as in scenario 2, would not automatically match the properties.
In that case, we can choose how properties should be matched.
Generally speaking, any array property can be mapped to an array, given that they are type-compatible.


Note
After mapping an array property to an array:

You cannot perform Scenario 5 or :doc:`Scenario 6 <scenario6>’ mappings.
Scenario 4.1 is enabled for the array on the right side
Properties of other arrays on the left side can no longer map to properties on the right array (i.e. other arrays can’t be mapped to the right array, since it belongs to the left array)




Example
Table columns can be individually mapped to array properties in the callback request payload, given they are type-compatible.

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
data.age





Callback payload
{
"type": "object",
"properties": {
"data": {
"type": "array",
"items": {
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