---
title: "API Authentication"
source: "https://developer.acronis.com/doc/connector/authentication/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:18.312953"
---

# API Authentication

API Authentication
To authenticate to Acronis Cyber Platform, you must have API key credentials and use them in your connector.

Note
You create API key credentials when you create the CyberApp, and you can regenerate the API key from the CyberApp settings section.


The authentication with API key credentials follows The OAuth 2.0 Authorization Framework and uses its Client Credentials flow.
According to this flow, the connector must use the API key credentials to request an access token and specify the received access token in the Authorization header according to the Bearer Authentication scheme.

If, for example, the access token specified in the Authorization header is expired or your API client is disabled, the API will respond with a 401 status code and error details.


Important

For security reasons, the token expiration time is set to two hours. After this time, the API will respond with a 401 status code.



Additionally, your connector must maintain the list of Acronis data centers where the CyberApp is deployed.
This is required to:



Authenticate in the data centers where the CyberApp is deployed.
Make authenticated requests to the corresponding data center.



Interaction diagram




In this section

Step-by-step procedure