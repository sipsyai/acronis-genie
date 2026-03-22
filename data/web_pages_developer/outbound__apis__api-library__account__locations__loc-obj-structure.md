---
title: "Location object structure"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/loc-obj-structure.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:39.208405"
---

# Location object structure

Location object structure
The API represents locations as JSON objects.

JSON object structure of a location







Name
Value type
Description



id
UUID string
The UUID of the location.

owner_tenant_id
UUID string
The UUID of the tenant this location belongs to.

platform_owned
boolean
Flag, that specifies if it is platform-owned location.

name
string
The name of the location.

version
number
Revision number.

readonly
boolean
Flag, that specifies if the location can be modified.




Example location
{
"id": "8fcd353b-0a40-40f2-9a55-ef8137d48800",
"owner_tenant_id": "ede9f834-70b3-476c-83d9-736f9f8c7dae",
"platform_owned": false,
"name": "NYC Data Center",
"version": 0,
"readonly": false
}