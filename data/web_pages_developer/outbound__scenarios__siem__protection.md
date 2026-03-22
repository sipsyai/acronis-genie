---
title: "Protection status"
source: "https://developer.acronis.com/doc/outbound/scenarios/siem/protection.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:00.016157"
---

# Protection status

Protection status
The MSP wants to see Acronis protection status data in the SIEM.

Available data

Device status (protected/unprotected)

Antimalware scan
Last successful antimalware scan date & time
Next scheduled antimalware scan





Patch management
Patch status
Update status




Vulnerabilities
Backup status (successful/unsuccessful)
Last successful backup date & time (per server, per endpoint, per VM, etc)
Next backup date & time
Backup size
Backup size by storage location



API endpoints
Blog article

Protection status report for Acronis Cyber Protect Cloud protected workloads.

Example with alerts monitoring and protection status

Advanced monitoring automation with Acronis Cyber Protect Cloud.

Various data

Note

The following information is fetched using a single API:
Protection plan name and status
Last successful backup date & time
Next backup date & time
Last successful antimalware scan date & time (an additional item under the same call)
Next scheduled antimalware scan (same item)






Fetch the protection status of resources.
Suggested with parameter/s:



GET /api/resource_management/v4/resource_statuses?type=resource.machine





Note
#Cyberfit score is fetched with the same API endpoint, but suggested with one additional parameter:
* GET /api/resource_management/v4/resource_statuses?type=resource.machine&include_attributes=true

Backup size (in bytes)

Fetch archives.
Fetch backups.