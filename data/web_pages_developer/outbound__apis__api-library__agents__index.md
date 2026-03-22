---
title: "Agent Management"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/agents/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:11.049712"
---

# Agent Management

Agent Management

Introduction
You can use the Acronis Agent Management API to view information about installed agents and the host where an agent is installed. You can also force agent updates.

Note
Some operations might not be covered in this API guide. For a list of all public endpoints and full technical details, see the Agent Manager API reference.



Data format
The API uses the secure HTTP/1.1 over TLS 1.2 protocol, and operates mostly with JSON-formatted messages.


Location
The Acronis Agent Management API is available at a specific URL (the base URL): <datacenter_url>/api/agent_manager/v<version>, where:


<datacenter_url> is the URL of the Acronis data center where the client using the API is registered.

<version> is the API version number.
The Agent Management API is currently version 2.





In this section

Fetching agent information