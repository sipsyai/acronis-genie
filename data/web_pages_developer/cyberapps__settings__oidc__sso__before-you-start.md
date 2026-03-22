---
title: "Before you start"
source: "https://developer.acronis.com/doc/cyberapps/settings/oidc/sso/before-you-start.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:59:45.081890"
---

# Before you start

Before you start
To authenticate the user with single sign-on, you should:


Set up an endpoint that will be used to initiate the SSO login.
The endpoint should accept a query parameter with the tenant ID from which the user attempts to initiate SSO.


Set up an endpoint to which the user will be redirected with the SSO login result.
Generate a URL to the https://acronis.cloud/api/idp/v1/authorize endpoint and redirect the user to that URL with the following data specified in its query string parameters:

A client ID in the client_id query string parameter.

A redirect URL in the redirect_uri query string parameter.
This must be an endpoint that will process the SSO login result.


Specify the following scopes in the scope query string parameter:


openid
roles to receive access roles that the user has in Acronis.
tenants to receive the list of tenants where the user is located in Acronis.



A unique random string in the state parameter.
[For PKCE] Specify the following parameters:


Specify the S256 method in the code_challenge_method query string parameter.
Specify the base64-encoded SHA-256-encrypted value in the code_challenge query string parameter. Keep the plain value for token exchange.






Next step: Exchanging code.