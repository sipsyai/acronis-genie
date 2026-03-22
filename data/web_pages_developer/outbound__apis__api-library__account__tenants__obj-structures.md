---
title: "JSON object structures"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/obj-structures.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:08.329801"
---

# JSON object structures

JSON object structures
The API represents tenants and tenant contacts as JSON objects.

Tenant object structure







Name
Value type
Description



id
UUID string
The universally unique identifier (UUID) of the tenant. This UUID is used for accessing the tenant via the API.

ancestral_access
true or false
If true, sets the Managed by service provider mode that allows access for parent tenant administrators. Otherwise, sets the Self-service management mode that restricts access to this tenant for parent tenant administrators.

brand_id
number
API v1 ID of the tenant’s brand.

brand_uuid
UUID string
The UUID of the tenant’s brand. If the tenant has branding active, it will contain a brand UUID generated for this tenant. Otherwise, it will contain UUID of the brand of higher-level tenant.

contact
contact object
The legal contact information of the organization.

contacts
array of user contact objects
An array of user contact objects that were created in the tenant. Only returned in GET /tenants endpoint.

customer_id
string
An internal value.

customer_type
string
An internal value.

default_idp_id
UUID string
An internal value.

enabled
true or false
Specifies if the tenant is enabled or disabled.

has_children
true or false
Specifies if the tenant has child tenants.

internal_tag
string
Any value that must be no longer than 256 characters. The platform does not use this value. A third-party application can use the value for its own purposes.

kind
string
The tenant type. The value can be partner, folder, customer, or unit. Set to unit for personal tenants.

language
string
The default language of notifications, reports, and the software that is used within the tenant. For the list of supported values, see Supported language codes.

name
string
The tenant name.

owner_id
UUID string
Set to user account UUID if it is a personal tenant. Otherwise set to null.

parent_id
UUID string
The UUID of a tenant where this tenant is created.

mfa_status
string
MFA status of the tenant. May be one of the following values: enabled, disabled, disable_in_progress.

pricing_mode
string
The current pricing mode of the tenant. May be one of the following: trial, production.

created_at
string
An RFC3339 date and time when the tenant was created.

deleted_at
string
An RFC3339 date and time when the tenant was deleted.

updated_at
string
An RFC3339 date and time when the tenant was updated.

external_operation_status
string
Status of an external operation that is performed on the tenant. May be one of the following values: no_operation, deleting, recovering.

update_lock
object
An internal value.

version
number
The revision number of the tenant. Each update of the tenant increases this number.





Tenant contact object structure







Name
Value type
Description



id
string
UUID of the contact.

created_at
string
An RFC3339 date and time when the contact was created.

updated_at
string
An RFC3339 date and time when the contact was updated.

email
string
An email address that will be used for account activation and service notifications.

address1
string
Address line 1.

address2
string
Address line 2.

country
string
Organization’s country.

state
string
Organization’s state.

zipcode
string
Organization’s zip code.

city
string
Organization’s city.

phone
string
Organization’s phone number.

firstname
string
The first name of the organization’s representative.

lastname
string
The last name of the organization’s representative.

title
string
A job title of the organization’s representative.

website
string
A URL of the organization’s website.

industry
string
The name of the industry that identifies the primary business activities of the organization.

organization_site
string
Total number of employees in the organization. May be one of the following values: 1-10, 11-100, 101-500, 501-1000, 5000+.

email_confirmed
boolean
Email confirmation status.

aan
string
Acronis Account Number (AAN). The value of this field is set only by Acronis.

types
array of string
Types of the contact. May be one of the following values: legal, primary, billing, technical, management.





Sample JSON object of a tenant
{
"ancestral_access": true,
"brand_id": 3579,
"brand_uuid": "14dc11ca-2b16-43bb-8ba4-2a3545c214a0",
"contact": {
"firstname": "",
"lastname": "",
"email": "foo.bar@example.com",
"email_confirmed": null,
"address1": "366 5th Ave",
"address2": "",
"city": "",
"country": "",
"phone": "1-541-754-3010",
"state": "",
"zipcode": "",
"title": null,
"website": null,
"industry": null,
"organization_size": "11-100",
"aan": null,
"id": "1ac28e13-b8b6-11ea-a31d-001c426f0f58",
"created_at": "2015-04-14T00:00:00Z",
"updated_at": "2023-12-01T11:07:50Z",
"types": [
"legal"
]
},
"customer_id": null,
"customer_type": "default",
"default_idp_id": "11111111-1111-1111-1111-111111111111",
"enabled": true,
"has_children": false,
"id": "0fcd4a69-8a40-4de8-b711-d9c83dc000f7",
"internal_tag": "some.unique.tag.value",
"kind": "customer",
"language": "en",
"name": "Foobar",
"owner_id": null,
"parent_id": "ede9f834-70b3-476c-83d9-736f9f8c7dae",
"update_lock": {
"enabled": false,
"owner_id": null
},
"version": 1
}