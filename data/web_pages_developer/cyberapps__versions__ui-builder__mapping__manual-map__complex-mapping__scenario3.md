---
title: "Scenario 3: Both left and right properties are arrays"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/scenario3.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:31.608400"
---

# Scenario 3: Both left and right properties are arrays

Scenario 3: Both left and right properties are arrays

Availability

This scenario is strange, but interesting.
For example, with a table with three columns (ID, name, and age), we want to send the list of **ID**s (and not the other columns) and put it into an array of strings.
In this case, we can map the table ID column on the left side to the array of strings on the right side.

Generally speaking, any array property can be mapped to an array, given they are type-compatible.

Note
After mapping an array property to an array, you cannot perform Scenario 5 or :doc:`Scenario 6 <scenario6>’ mappings.



Example
A table can be mapped to an array of objects in the callback request payload, given the table columns and the array object properties are compatible.
A table is on the form. Instead of mapping the entire table as in scenario 2, we can map one of its column to an array of strings.

Form and mappings







Element
ID (Model property)
Mapped to



Table 1
table





Table 1 Column 1
id





Table 1 Column 2
username
usernames

Table 1 Column 3
age









Callback payload
{
“type”: “object”,
“properties”: {
“usernames”: {
“type”: “array”,
“items”: {
“type”: “string”
}
}
}
}