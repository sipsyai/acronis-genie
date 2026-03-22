---
title: "Managing user accounts"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:58.369802"
---

# Managing user accounts

Managing user accounts

User accounts represent the users registered on the platform.
User accounts created in a customer tenant have a personal tenant, which represents a tenant bound to a specific user account, and are only used to:


Control user account quotas.
Collect user account real usage


Operations with user accounts are located under the /users endpoint of the API.
The API represents user accounts and user account contacts as JSON objects. To find out more about the object structures, see JSON object structure.


Available user account operations






Operation
Methods and endpoints used



Create a new user account in a tenant

GET /users/check_login
POST /user



Activate a user account

GET /users/{user_id}
POST /users/{user_id}/send-activation-email
POST /users/{user_id}/password



Manage user account roles

GET /users/{user_id}/access_policies
PUT /users/{user_id}/access_policies



Fetch information about a user account
GET /users/{user_id}

Change a user account password
POST /users/{user_id}/password

Change a user account email
PUT /users/{user_id}

Change contact info of the user account
PUT /users/{user_id}

Disable a user account
PUT /users/{user_id}

Delete a user account
DELETE /users/{user_id}




In this section

JSON object structure
Creating a user account
Activating a user account
Managing user account roles
Fetching user account information
Changing a user account password
Changing a user account email
Changing a user account contact info
Disabling/enabling a user account
Deleting a user account