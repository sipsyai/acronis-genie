---
title: "Monitoring"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/monitoring.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:05.323840"
---

# Monitoring

Monitoring
The MSP wants to monitor the state of Acronis agents and their actions.

Preconditions

The MSP has enabled the CyberApp.
The MSP has mapped customer tenants.



Basic flow
The CyberApp should fetch information about the protected workloads for all mapped customer tenants. The update must be done at
regular intervals via Acronis API and the information must be stored locally.
The information about the protected workloads should include:

Agent version (fetched with GET /agents).
Protection plan name (fetched with GET /resource_management/v4/resource_statuses?type=resource.machine).
Protection status (fetched with GET /resource_management/v4/resource_statuses?type=resource.machine).
#Cyberfit score (fetched with GET /resource_management/v4/resource_statuses?type=resource.machine&include_attributes=true)
Last successful backup date & time.
Next backup date & time.
Backup size (in GB) (fetched with GET /backups).
Last successful antimalware scan date & time.
Next scheduled antimalware scan.



API endpoints
Agent version

Fetch agents.

Various information


Note

The following information is fetched using this single API:



Protection plan name and status.



Last successful backup date & time.



Next backup date & time.



Last successful antimalware scan date & time (an additional item under the same call).



Next scheduled antimalware scan (same item).







Fetch the protection status of resources.
Suggested with parameter/s:



GET /api/resource_management/v4/resource_statuses?type=resource.machine





Note
#Cyberfit score is also fetched with the same API endpoint but suggested with one additional parameter:

GET /api/resource_management/v4/resource_statuses?type=resource.machine&include_attributes=true


Backup size (in bytes)

Fetch archives.
Fetch backups.

Blog article

Protection status report for Acronis Cyber Protect Cloud Protected workloads.

Example with alerts monitoring and protection status

Advanced monitoring automation with Acronis Cyber Protect Cloud.