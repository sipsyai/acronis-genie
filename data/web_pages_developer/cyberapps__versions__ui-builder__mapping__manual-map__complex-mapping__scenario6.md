---
title: "Scenario 6: Left property is an array property and right properties is a single value"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/scenario6.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:48.492267"
---

# Scenario 6: Left property is an array property and right properties is a single value

Scenario 6: Left property is an array property and right properties is a single value

Availability
Multiple request mapping.
This is similar to scenario 5, but we are not mapping the entire array, but its properties.

Note
After mapping an array property to a single value, you cannot use scenario 2, scenario 3, scenario 4 or scenario 5.



Example
Similar to scenario 2, we have a table with some columns in our form, and we want to send all selected rows. However, we don’t want to send an array with all rows, but rather one request per row containing individual data for each row.

Form and mappings







Element
ID (Model property)
Mapped to



Table 1
table





Table 1 Column 1
id
id

Table 1 Column 2
username





Table 1 Column 3
age









Callback payload
{
“type”: “object”,
“properties”: {
“id”: {
“type”: “number”
}
}
}



Note
Every other scenario (except for scenario 1) is disabled, which means that no other array can be mapped.