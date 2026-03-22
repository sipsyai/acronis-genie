---
title: "Account Management"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:05.523920"
---

# Account Management

Account Management

Introduction
You can use the Acronis Account Management API to:

Manage all types of platform resources:

Tenants and their users
Services and their offering items
User quotas
Locations and storages they contain


Search for tenants and user accounts
Collect immediate service usage by tenants and manage usage reports
Log in to the platform on behalf of another user


Note
Some operations might not be covered in this API guide. For a list of all public endpoints and full technical details, see the Account Management API reference.



Data format
The API uses the secure HTTP/1.1 over TLS 1.2 protocol, and operates mostly with JSON-formatted messages.


Location
The Acronis Account Management API is available at a specific URL (the base URL): <datacenter_url>/api/<version>, where:


<datacenter_url> is the URL of the Acronis data center where the client using the API is registered.

<version> is the API version number.
Currently, the API has two versions.
This guide covers the API version 2, which is the preferable version to work with.


Important
The API version 1 is discontinued and its users must migrate to API version 2 by June 30, 2023.





In this section

API error codes
Tutorials
Managing tenants
Managing services
Managing offering items and quotas
Managing branding options
Managing user accounts
Managing locations and storages
Managing upsell
Managing billing settings
Searching for tenants and user accounts
Usage and reporting
Advanced operations
Supported language codes