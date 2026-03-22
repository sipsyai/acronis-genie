---
title: "Managing user account roles"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/roles/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:06.851926"
---

# Managing user account roles

Managing user account roles

Operations with user account roles are located under the /users/{user_id}/access_policies endpoint of the API.
The API represents user account roles and user account contacts as JSON objects. To find out more about the object structures, see User account role object structure and available roles.

The roles are used to manage user account access to the services available in the same tenant.

Available user account role operations






Operation
Methods and endpoints used



Check current available access policies for a user account
GET /users/{user_id}/access_policies

Change access policies for a user account
PUT /users/{user_id}/access_policies




In this section

User account role object structure and available roles
Checking current user account roles
Modifying the user account roles