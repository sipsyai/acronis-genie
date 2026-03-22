---
title: "Tenant service usage JSON object structure"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/usage-reporting/obj-structure.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:11.726177"
---

# Tenant service usage JSON object structure

Tenant service usage JSON object structure
The API represents tenant service usage as JSON objects.







Name
Value type
Description



tenant_uuid
UUID string
The UUID of the tenant related to this usage.

application_id
UUID string
The UUID of the service this usage belongs to.

edition
string
The edition of the usage.

infra_id
UUID string
The UUID of the storage related to this offering item. Present only if type is infra.

measurement_unit
string
The measurement unit. See list of available measurement units

name
string
The name of the usage with edition prefix.

offering_item
offering item object
An object that contains quota and status of the offering item. Present only if the usage has related offering item.

range_start
string
ISO 8601 date and time since the usage collection has been started. By default, it is the first day of current month.

usage_name
string
A name of the usage without edition prefix.

value
number
Current value of the usage.

absolute_value
number
Accumulated value of the usage.

tenant_id
number
API v1 ID of the tenant.

type
string
Type of the usage. Since the usages share the types with offering items, see the list of available offering item types.




Example tenant service usage object
{
"absolute_value": 0,
"application_id": "6e6d758d-8e74-3ae3-ac84-50eb0dff12eb",
"edition": "standard",
"infra_id": "019097a6-114f-4418-bd54-e01ef049f209",
"measurement_unit": "bytes",
"name": "storage",
"usage_name": "storage",
"offering_item": {
"quota": {
"overage": null,
"value": null,
"version": 0
},
"status": 1
},
"range_start": "2019-08-01T00:00:00",
"tenant_id": 1326401,
"type": "infra",
"value": 0
}