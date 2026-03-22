---
title: "Event Manager API"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/events/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:58.100595"
---

# Event Manager API

Event Manager API
This document covers the Event Manager application programming interface (Event Manager API).

What can I do with the Event Manager API?
This interface enables the integration developers to programmatically leverage the following functionality:

Subscribe to the events and receive notifications when the events occur in real time.
Read the history of the events that have occurred in the system.



Data format
The API uses HTTP/1.1 protocol and operates mostly with JSON-formatted messages.


Location
The Acronis Event Manager API is available at a specific URL (the base URL): <datacenter_url>/api/event_manager/v<version>, where:


<datacenter_url> is the URL of the Acronis data center where the client using the API is registered.

<version> is the API version number.
The Event Manager API is currently version 1.





In this section

Topics and events
Fetching event topics and types
Subscribing to the events
Listening for the events