---
title: "How to log in to service consoles on behalf of another user"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/advanced/ott/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:06.564843"
---

# How to log in to service consoles on behalf of another user

How to log in to service consoles on behalf of another user
The platform provides a way to log in to a service on behalf of another user account without entering its login credentials, using a one-time token.
The /idp/ott endpoint allows you to generate a one-time token containing encrypted login-specific data and use it either to log in on behalf of a user account, or to make an external login URL.

Restrictions
The platform enforces the following rules for the /idp/ott endpoint:

Only API clients can access this endpoint.
A one-time token can be generated for a user account located within the same
tenant or its sub-tenants.
A one-time token cannot be generated for a user account located in a sub-tenant
that has Support access disabled.


Available one-time-token operations






Operation
Methods and endpoints used



Generate an external login URL

GET /idp/external-login
POST /idp/ott



Log in using a one-time token

POST /idp/ott
POST /idp/ott/login






In this section

Generating an external login URL
Logging in using a one-time token