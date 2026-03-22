---
title: "Generating SSO service account credentials"
source: "https://developer.acronis.com/doc/cyberapps/settings/oidc/generate.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:59:32.207785"
---

# Generating SSO service account credentials

Generating SSO service account credentials
Acronis uses OpenID Connect (OIDC) to pass user authentication to one or more Uniform Resource Identifiers (URI) on the vendor cloud service.
When you create an SSO service account on Acronis, to avoid scams, user data theft, etc., you must must define in advance the list of URIs to which Acronis will allow SSO redirects.
These URIs might depend on the region, or they might depend on different scenarios, and for each scenario you want to redirect the user to a specific part of the vendor console.

Important
If you need to update the list of redirect URIs on the vendor cloud service, you must regenerate the SSO service account credentials.


To generate SSO service account credentials

Open the CyberApp settings tab.
Click .
Specify at least one redirect URI.
[Optional] Click  to add another URI or  to delete a URI.
[When your list of redirect URIs is ready] Click Generate.
Click Copy.
Paste the information in a file, and store the file somewhere safe.


Important

The secret is not stored by Acronis, so it cannot be retrieved.
If you lose your SSO service account credentials, you will have to regenerate them.