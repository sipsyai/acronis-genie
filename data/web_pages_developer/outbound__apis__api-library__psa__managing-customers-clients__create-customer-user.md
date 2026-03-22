---
title: "Create a user account for the customer"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-customers-clients/create-customer-user.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:23:05.644872"
---

# Create a user account for the customer

Create a user account for the customer

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Create a new user account in the Acronis customer tenant
and activate the user account with Account Management API v2.
Choose one of the following role identifiers that will be assigned to the user account:

advanced_automation_admin - Administrator
advanced_automation_director - Director
advanced_automation_engineer - Engineer
advanced_automation_finance_manager - Finance manager
advanced_automation_finance - Finance
advanced_automation_sales - Sales
advanced_automation_group_manager - Group manager
advanced_automation_hr - HR
advanced_automation_client_manager - Client manager
advanced_automation_client - Client


Note
A user account with the partner_admin automatically gets the advanced_automation_admin role.

For more details about Acronis PSA roles, refer to the product documentation.

Set the role to the created user account with Account Management API v2.