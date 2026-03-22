---
title: "Searching for tenants and user accounts"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/searching/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:29.752456"
---

# Searching for tenants and user accounts

Searching for tenants and user accounts
The /search endpoint that searches for tenants and user accounts that contain a specific text in some of their property values.

Available search operations






Operation
Methods and endpoints used



Search for a tenant by its name
GET /search

Search for a user account by its login
GET /search




Searched properties
In tenants:






Tenant name
name

Customer ID
customer_id

First name
firstname in the contact object

Last name
lastname in the contact object

Email address (not displayed in search results)
email in the contact object



In user accounts:






Account login
login

First name
firstname in the contact object

Last name
lastname in the contact object

Email address (not displayed in search results)
email in the contact object





General search logic

A search text is split into lower-case words (tokens).
The API looks through its index containing values and their tokens.
The API matches those values which tokens, in any position, start with the tokens being searched.

For example, the index contain the following value-token pairs:







Row
Value
Tokens



1
JohnSmithFirstAndSecond
johnsmithfirstandsecond

2
John SmithFirst
john, smithfirst

3
John Smith First
john, smith, first

4
John Smith Second
john, smith, second



Then:

John and joh will match all values;
Smith and smit – all except the first one;
SMITHfirst – the second one;
first, fir, and Smith fir – the third one;
mith and and – nothing.



Search parameters

A text to be searched must be specified in a text query parameter of the endpoint URL and must contain at least three characters.

To limit the search scope, the endpoint requires the UUID of a tenant where the platform will search. The administrator performing the search must have access to this tenant.

The tenant UUID must be specified in a tenant query parameter of the endpoint URL. The platform first searches data in this tenant, then in all its sub-tenants.

Data within sub-tenants to which access is limited for higher-level administrators are not searched.


The endpoint URL supports a limit query parameter that limits the number of results in a response. Its value must be between 1 and 300. If this parameter is not specified, a response will contain up to the first 10 results.



Search results
A response contains both tenants and user accounts as an array of JSON objects.
The obj_type member of an object differentiates a tenant from a user account.

In this section

Searching for a tenant by its name
Searching for a user account by its login