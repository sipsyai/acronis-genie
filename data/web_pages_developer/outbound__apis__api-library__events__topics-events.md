---
title: "Topics and events"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/events/topics-events.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:10.725049"
---

# Topics and events

Topics and events
Event Manager API operates with topics and events, where:

Topic - a stream of events of the same or different types, sharing the same delivery, ordering, consolidation and retention rules.
Event - a message that describes a change in the system.


Tenant-related events
Tenant-related events are published to the following topic: cti.a.p.em.topic.v1.0~a.p.tenant.v1.0
Events published in this topic are persistent and have unlimited retention period.






Event ID
Description



cti.a.p.em.event.v1.0~a.p.tenant.enabled.v1.0
Event is raised when tenant is enabled.

cti.a.p.em.event.v1.0~a.p.tenant.disabled.v1.0
Event is raised when tenant is disabled.

cti.a.p.em.event.v1.0~a.p.tenant.created.v1.0
Event is raised when tenant is created.

cti.a.p.em.event.v1.0~a.p.tenant.updated.v1.0
Event is raised when tenant is updated.

cti.a.p.em.event.v1.0~a.p.tenant.auth_consent.updated.v1.0
Event is raised when tenant’s authentication consent is updated.

cti.a.p.em.event.v1.0~a.p.tenant.unlocked.v1.0
Event is raised when tenant is unlocked.