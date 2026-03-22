---
title: "Managing protection plans and policies"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:51.620055"
---

# Managing protection plans and policies

Managing protection plans and policies

Note
To find out more about plans, see the Working with plans chapter of the Acronis Cyber Protection User Guide.


Available protection plan and policy operations






Operation
Methods and endpoints used



Create a protection plan
POST /policy_management/v4/policies

Fetch a list of policies and protection plans
GET /policy_management/v4/policies

Update a policy or protection plan

GET /policy_management/v4/policies
PATCH /policy_management/v4/policies/{policy_id}



Make a protection plan a favorite

GET /policy_management/v4/policies
PATCH /policy_management/v4/policies/{policy_id}



Delete a protection plan

GET /policy_management/v4/policies
DELETE /policy_management/v4/policies/{policy_id}



Delete all protection plans for a tenant
DELETE /policy_management/v4/policies

Fetch a list of policies applicable for a resource
GET /policy_management/v4/policies

Apply a protection plan to resources

GET /resource_management/v4/resources
GET /policy_management/v4/policies
POST /policy_management/v4/applications



Revoke protection plans from resources

GET /resource_management/v4/resources
GET /policy_management/v4/policies
DELETE /policy_management/v4/applications



Start execution of a policy

GET /resource_management/v4/resources
GET /policy_management/v4/policies
PUT /policy_management/v4/applications/run



Fetch policy execution statuses of resources
GET /policy_management/v4/policy_statuses

Track the execution progress of the policy

GET /resource_management/v4/resources
GET /policy_management/v4/policies
GET /policy_management/v4/applications






In this section

Protection policy settings
Creating a protection plan
Fetching a list of policies and protection plans
Updating a policy or protection plan
Making a protection plan a favorite
Deleting a protection plan
Deleting all protection plans for a tenant
Fetching a list of plans applicable for a resource
Applying a protection plan to resources
Revoking protection plans from resources
Start execution of a policy
Fetching policy execution statuses of resources
Tracking the execution progress of a policy