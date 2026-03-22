---
title: "Architecture"
source: "https://developer.acronis.com/doc/introduction/architecture.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:11:06.667724"
---

# Architecture

Architecture
Acronis Cyber Platform architecture can be represented by five independent layers, providing a secure and efficient control plane for endpoint protection management.


Products
The product configuration layer is where Acronis Product Management (together with partners) can define new products with specific licensing rules, allowed functionality scope, deployment schemas, appropriate documentation, legal terms, and guidelines.





CyberApps
The platform extension layer introduces additional protection, management, automation, and other services which provide value to customers.
Similar to other industry-standard application concepts, CyberApps can be developed and integrated dynamically by both Acronis and third-party ISVs (independent service vendors).





System Core
The system core layer is a skeleton of the whole Acronis Cyber Platform.
It is responsible for other platform services and CyberApp lifecycle management, isolation, communication, integration, and configuration.





Management Platform
A generic components layer, which offers CyberApp vendors various pre-defined building blocks, such as workflow management, task management, event system, alerting system, etc., available through public APIs.
It helps vendors focus on service-specific business logic (For example, backup or security engines).





Infrastructure
The infrastructure layer is physically deployed in every data center, providing storage, compute and network abstractions for the rest of the platform, and also building an efficient communication layer between various infrastructure sites (such as data centers or Acronis agents).