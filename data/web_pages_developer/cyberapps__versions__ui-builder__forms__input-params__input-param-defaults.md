---
title: "Using Acronis variables in default value strings"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/forms/input-params/input-param-defaults.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:07:49.437163"
---

# Using Acronis variables in default value strings

Using Acronis variables in default value strings

You can use generic Acronis variables (formatted as {{ $.variable }} ) as part of the default value string.
The available generic Acronis variables are:



tenant_id - the Acronis tenant ID.
origin - the URL of the Acronis DC.
locale - the user language setting.



For input parameters on open pop-up workloads action forms, you can also use dynamic (context-specific) variables:


Workloads reported by you

client_id - the workload id.
name      - the workload name.

Acronis workloads

id          - the workload id.
name        - the workload name.
type        - the workload type.
displayName - the workload display name.
tenant.id   - the workload tenant id (this might be different from the current tenant in the case of a Partner).
tenant.name - the workload tenant name.
createdAt   - when the workload was created.
updatedAt   - when the workload was last updated.

Agent details

agent.id
agent.name
agent.details.os.name
agent.details.os.arch
agent.details.os.family
agent.details.os.productType
agent.details.os.servicePack
agent.details.os.versionMajor
agent.details.os.versionMinor
agent.details.hardware.macAddesses
agent.details.ipAddresses