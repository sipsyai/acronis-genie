---
title: "Licensing model"
source: "https://developer.acronis.com/doc/introduction/licensing.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:11:15.077234"
---

# Licensing model

Licensing model

Acronis Cyber Platform products represent a logically isolated subset of functionality, physically present in the cloud or on the agent side.
A single technical capability (such as the ability to back up virtual machines) can be included in different products, and can have different licensing terms and prices, depending on distribution channel and product type.
For example, one product could provide some capability for free, while another one may require extra charges for the same functionality.


Typical distribution channel
For Acronis partners, Acronis Cyber Platform enables product distribution via the partners Channel.
According to the Acronis distribution model, Acronis has relations with distributors and service providers, and does not communicate with end customers directly.
Acronis allows distributors to register MSPs and then, in turn, MSPs can register end customers using an API or UI.




Billing works in a similar way: Acronis bills direct partners (distributors/MSPs), and never bills end customers.
However, Acronis provides a usage reports API for direct partners to let them bill end customers.
The typical payment model is pay-as-you-go, but the prepaid payment model can be used as an alternative.



Features

A feature is a single technical capability, provided by the platform or a CyberApp.





A feature can be tenant-wide or workload-specific.


Tenant-wide features can be enabled/disabled globally for a tenant.
Examples of tenant-wide features include:


User role management.
Workload autodiscovery from Active Directory.
User actions audit.


Workload-specific features are agent-bound, and are applicable to a certain type of workload only.
Examples of workload-specific features include:


Microsoft 365 mailbox anti-malware scan is allowed.
Patch management for Windows is allowed.
Remote desktop is allowed.



Workloads

Workload is an umbrella term for an entity that is being protected, monitored or managed by Acronis Cyber Platform.
Typical examples of protected entities are user workstations, virtual machines, cloud services, mailboxes, etc.


Note
In the API documentation, workloads are also known as resources.



Offering items
An offering item is a combination of some logically grouped features, which can be applied to specific tenants and workloads.
Offering items aggregate similar granular functionality, applicable to some similar types of workloads, and are a primary licensable entity used in all the key licensing scenarios.
Offering items allow available functionality to be controlled down the distribution model hierarchy.
Initially, Acronis staff enables offering items for distributors. Distributors may select from their enabled offering items and, in turn, enable offering items for MSPs, who use
them to configure available features for their end customers.
Once the offering item is provisioned to an end customer, its features become available to its tenant, user accounts, and API clients.

Note
End customers do not have any underlying customers, and therefore do not need to configure offering items.



Quotas
An offering item itself defines only a valid combination of features applicable to specific workloads.

With the pay-as-you-go payment model, partners sell the offering items to their end customers, then track and bill usage of every offering item.
However, for the prepaid payment model, Acronis Cyber Platform’s licensing engine enforces offering item usage quotas, which prevent MSPs or end customers from overusing the offering items.