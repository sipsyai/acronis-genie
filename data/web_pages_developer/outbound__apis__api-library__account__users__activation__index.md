---
title: "Activating a user account"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/users/activation/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:24.363004"
---

# Activating a user account

Activating a user account

After you create a user account on the Acronis platform, you must activate it.
There are 2 ways to activate a user account:



Send an email with the account activation link.
The user must open the activation link and set the password in order to be able to log in.



Set a password for the user account using API.
The user can then log in to the service console using the password.
This can be useful when implementing custom user account provisioning methods.




Available user account activation operations






Operation
Methods



Send activation email to a user account
POST /users/{user_id}/send-activation-email

Activate a user account by setting a password
POST /users/{user_id}/password

Check activation status of a user account
GET /users/{user_id}




In this section

Sending an activation email
Activating by setting the password
Checking activation status