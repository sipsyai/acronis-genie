---
title: "Exchanging code"
source: "https://developer.acronis.com/doc/cyberapps/settings/oidc/sso/code-exchange.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:59:49.296419"
---

# Exchanging code

Exchanging code
When the user is redirected back to the URL you specified in the redirect_uri parameter:

Fetch the value of the state query string parameter, and verify it against the generated state.
Fetch the value of the code query string parameter.

To exchange the code on the access token, the API client must send a POST request to the https://acronis.cloud/api/idp/v1/token endpoint, providing:

Base64-encoded client ID and client secret provided in the Authorization header according to Basic authentication scheme.
grant_type set to authorization_code in the query string parameter.
code set to an authorization code obtained from the code query string parameter of redirect URI.
[For PKCE] code_verifier set to the base64-encoded plain value that was used in the URL’s code_challenge.

If the token request is successful, your CyberApp will receive the ID token that contains the user information and the access token that would allow the CyberApp to access Acronis API on behalf of the user.
The access token must be specified in the Authorization header according to Bearer authentication scheme.
The API will respond with a 401 status code and error details if the access token is expired or your API client is disabled, for example.

Important
For security reasons, the token expiration time is set to 2 hours. After this time, the API will respond with a 401 status code.


Previous step: Before you start.
Next step: Checking user information.