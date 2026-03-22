---
title: "CyberApp SSO service account"
source: "https://developer.acronis.com/doc/cyberapps/settings/oidc/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:59:36.419175"
---

# CyberApp SSO service account

CyberApp SSO service account

OIDC is a technological standard identity authentication protocol, built as an extension to open authorization (OAuth) 2.0.
Together, they provide a standard process for authenticating and authorizing users when they sign in to access digital services.
By creating an SSO service account for your CyberApp, Acronis can act as an OpenID provider for your systems.

This means that you can use Acronis account credential authentication as the single sign-on (SSO) source for your cloud service.
So, CyberApp users (who are already signed in with their Acronis username and password) can seamlessly log in to your systems without having to provide another username and password combination, and your systems can interact with Acronis API using the OIDC tokens.


Note
For more information on OpenID, see OpenID Foundation website.

To use Acronis as an OpenID provider for your systems, you must generate an SSO service account credentials.

Note
To do this, you must specify a list of redirect URIs which will receive the OIDC authentication credentials.


When a redirect URI is selected, and the authentication is successful, Acronis returns two tokens, as specified in the OIDC standard:


id_token
access_token

These tokens can then be used to make calls to Acronis API to fetch data and interact with the Acronis system.

Note
For technical information on CyberApp SSO implementation, see CyberApp OIDC SSO authentication.


The CyberApp SSO flow

The CyberApp must offer a link to users in the Acronis UI. This is not a redirect link. It simply verifies that the tenant exists on the vendor cloud service and then starts the authentication and redirect process.

Important
Acronis recommends that you include the tenant_id Acronis system variable in the link.


The vendor must generate SSO credentials, which are used by the vendor to check Acronis and confirm that this is a legitimate, authorized call.

Note
To avoid being redirected to the wrong final landing URI,the list of final landing URIs is predefined and cannot be changed.



The vendor gets information about the user, such as which roles the user has. This can be used to show different type of functionality.
For example, if it is an admininistrator user, the vendor can show full UI.
If it is a user with read-only rights, the vendor can show UI which doesn’t allow any modification.
So, the vendor just needs to be aware of roles available on Acronis side and, based on the role Acronis returns, provide capabilities on their console.


The user is redirected to one of the URIs from the CyberApp’s SSO service account pre-defined redirect URI list.


In this section

CyberApp OIDC SSO authentication
Generating SSO service account credentials
Regenerating your SSO service account credentials
Deleting the SSO service account