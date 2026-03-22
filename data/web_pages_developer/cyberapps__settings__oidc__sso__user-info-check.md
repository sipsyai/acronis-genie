---
title: "Checking user information"
source: "https://developer.acronis.com/doc/cyberapps/settings/oidc/sso/user-info-check.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:59:57.831503"
---

# Checking user information

Checking user information

The CyberApp must check the information about the authenticated user by sending a GET request to the https://acronis.cloud/api/idp/v1/userinfo endpoint with the access token.
The endpoint will respond with:

{
"sub": "<user_id>",
// `profile` claim
"name": "",
"family_name": "",
"given_name": "",
"locale": "",
"updated_at": "",
"preferred_username": "",
"website": "",
// `email` claim
"email": "",
"email_verified": false,
// `address` claim
"address": "",
// `phone` claim
"phone_number": "",
"phone_number_verified": false,
// `roles` claim
"roles": [
{
"role_id": "<role>"
"rn": "<rn>"
"rp": "<rp>"
},
"..."
]
// `tenants` claim
// Outputs the list of parent tenant UUIDs up the hierarchy, including only those tenants that have the CyberApp enabled.
// Excludes tenants with kind 'unit' and 'folder'.
"tenants": [
"<parent_tenant_uuid>",
"<parent_of_parent_tenant_uuid>",
]
"..."
}


Previous step: Exchanging code.