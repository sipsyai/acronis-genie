---
title: "Scenario 1: Both left and right properties are single values"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/mapping/manual-map/complex-mapping/scenario1.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:08:23.192950"
---

# Scenario 1: Both left and right properties are single values

Scenario 1: Both left and right properties are single values

Availability
Single request mapping, multiple requests mapping, response mapping
If our left-side and right-side properties are single values (primitives or objects that are at root level). All primitives and objects that are not inside an array can be mapped to other primitives and objects at any time, given they are type-compatible.


Example
If the form contains two text fields, then you can map each text field to a root-level property in the callback request payload, and vice versa.

Form and mappings







Element
ID (Model property)
Mapped to



Input
user
username

Input
pw
password





Callback payload
{
"type": "object",
"properties": {
"username": {
"type": "string"
},
"password": {
"type": "string"
}
},
}