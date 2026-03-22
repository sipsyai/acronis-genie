---
title: "Creating or re-using protection plans"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/tasks/protection-plans.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:34.818872"
---

# Creating or re-using protection plans

Creating or re-using protection plans

Basic flow

MSP goes to RMM integration settings.
In the Default protection plan section, the partner can choose which plan to upload.
The integration can fetch the list of existing protection plans using the
GET /policy_management/{version}/policies
endpoint that needs to be displayed.

MSP chooses the type of workload this plan applies to. (For example, “Workstations” or “Servers”).
Once MSP maps an RMM customer to an Acronis customer tenant, the integration crawls through
all devices for this customer and applies the protection plan to all workloads that do not have a protection plan.
The integration can fetch the list of the workloads using
the GET /resource_management/{version}/resources
endpoint.




API endpoints

It’s good to have separate protection plans for workstations and servers.
Default folder for backups is Acronis Cloud unless specified differently in the protection plan.
You would need the following API:


Get customer tenants : Fetch Tenants Batch.
Suggested with parameter/s:


GET /api/2/tenants?parent_id=
GET /api/2/tenants?subtree_root_id=


Get protection plans: Get protection plans from console.
Create protection plan: Create policy.
Apply plan: Create an application.

See if a device is protected: Fetch the protection status of resources.
Suggested with parameter/s:



GET /api/resource_management/v4/resource_statuses?type=resource.machine





If the customer does not have a specific offering item enabled, but they are enabled in the protection plan, then the protection plan will throw an error.

Note
This could be specified in the instructions, when setting the default protection plan.