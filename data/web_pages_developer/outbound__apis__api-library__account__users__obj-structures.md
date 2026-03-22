---
title: "JSON object structure"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/obj-structures.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:02.579424"
---

# JSON object structure

JSON object structure
The API represents user accounts and user account contacts as a JSON objects.

JSON object structure of a user account







Name
Value type
Description



id
UUID string
The UUID of the user account.

version
number
Revision number.

tenant_id
UUID string
The UUID of the tenant where the user account was created.

login
string
A login of the user account.

contact
contact object
The contact information of the account.

activated
boolean (default false)
Activation status of the user.

enabled
boolean (default true)
Flag, that disables or enables user account in the platform.

terms_accepted
boolean (default false)
Flag, that shows if the user accepted legal terms.

created_at
string
ISO 8601 date and time when the user was created.

language
string
User’s language. For the list of supported values, see Supported language codes.

idp_id
string
External identity provider UUID.

external_id
string
User UUID in external identity provider (if the user was created through external identity provider).

personal_tenant_id
string
Personal tenant UUID (if the user was created in the customer tenant). This tenant includes user account contact information and has kind set to unit.

notifications
array of strings
User’s subscriptions for notifications.

mfa_status
string
User’s two-factor authentication (2FA) status. See available 2FA statuses.





JSON object structure of a user account contact







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

deleted_at
string
An RFC3339 date and time when the contact was deleted.

email
string
An email address that will be used for account activation and service notifications.

types
string

A type of contact:
billing - a contact that will get updates about important changes in usage reporting in the platform. There can be several Billing contacts per tenant.
management - a contact that will get updates about important business-related changes in the platform. There can be several Business contacts per tenant.
technical - a contact that will get updates about important technical changes in the platform. There can be several Technical contacts per tenant.





address1
string
Address line 1.

address2
string
Address line 2.

country
string
User’s country.

state
string
User’s state.

zipcode
string
User’s zip code.

city
string
User’s city.

phone
string
User’s phone number.

firstname
string
The first name of the user.

lastname
string
The last name of the user.

title
string
A job title of the user.

website
string
A URL of the user’s organization.

industry
string
The name of the industry that identifies the primary business activities of the user.

fax
string
Fax number.

email_confirmed
boolean
Email confirmation status.

language
string
A user’s language. For the list of supported values, see Supported language codes.

aan
string
Acronis Account Number (AAN). The value of this field is set only by Acronis.





Example user account
{
"id": "948efcf2-b740-4c40-bb2d-4e4a46adfd87",
"version": 2,
"tenant_id": "0ef03214-6e47-4e50-87f2-a5955ba6095c",
"login": "mylogin",
"contact": {
"id": "4bfe4631-b8b6-11ea-a31d-001c426f0f58",
"created_at": "2020-01-14T11:52:26Z",
"updated_at": "2023-12-01T10:34:34Z",
"email": "me@mysite.com",
"address1": "1440 River Drive #100",
"address2": "",
"country": "USA",
"state": "CA",
"zipcode": "12345",
"city": "Rivertown",
"phone": "123456789",
"firstname": "John",
"lastname": "Doe",
"types": ["billing", "management", "technical"],
"title": "Developer",
"website": "",
"industry": "",
"organization_size": "",
"email_confirmed": false,
"aan": "",
"fax": "",
"language": "",
"deleted_at": null
},
"activated": true,
"enabled": true,
"terms_accepted": false,
"created_at": "2019-07-25T07:11:02.807354+00:00",
"language": "en",
"idp_id": "e6f73a28-ff2e-4728-8f78-49eb74b20fce",
"external_id": "S-1-5-21-917267712-1342860078-1792151419-500",
"personal_tenant_id": "2f8ad2e2-28f2-11e7-aad1-5ffe2ad47151",
"business_types": [],
"notifications": [
"quota",
"reports",
"backup_error",
"backup_warning",
"backup_info",
"backup_daily_report"
],
"mfa_status": "setup_required"
}




Available user account notifications






Value
Description



quota
Notifications regarding quota overuse.

reports
Notifications regarding scheduled usage reports.

backup_error
Notifications regarding backup errors.

backup_warning
Notifications regarding backup warnings.

backup_info
Notifications regarding successful backup.

backup_daily_report
Notifications with daily recap about active alerts.





Available two-factor authentication (2FA) statuses






Value
Description



disabled
Tenant has disabled 2FA and user is not required to use it in order to log in.

setup_required
Tenant has enabled 2FA and user is required to configure it in order to log in.

enabled
Tenant has enabled 2FA and user has it configured.

forcibly_disabled
Force disables 2FA for the user account. Only used for service accounts.