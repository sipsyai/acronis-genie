---
title: "Usage and reporting"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/usage-reporting/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:07.477995"
---

# Usage and reporting

Usage and reporting
There are two ways to fetch service usage:

By fetching tenant service usage using /tenants/usages or /tenants/{tenant_id}/usages endpoint.
By creating a report via the reporting API and fetching service usage from the report.


Important

Information about tenant service usage is provided by /tenants/usages and /tenants/{tenant_id}/usages endpoints. The information is updated, on average, every 5-6 hours.
For billing purposes, use reports instead of /tenants/usages and /tenants/{tenant_id}/usages endpoints.



Available service usage and usage reports operations






Operation
Methods and endpoints used



Fetching tenants usage batch
GET /tenants/usages

Create a new usage report
POST /reports

Fetch a usage report
GET /reports/{report_id}

Fetch a usage report from tenant reports

GET /reports/{report_id}
GET /tenants/{tenant_id}/reports



Update a usage report
PUT /reports/{report_id}

Disable scheduled usage report
PUT /reports/{report_id}

Delete a usage report
DELETE /reports/{report_id}

Fetch a stored usage report

GET /reports/{report_id}/stored
GET /reports/{report_id}/stored/{stored_report_id}



Fetch a service usage using a stored report
GET /reports/{report_id}/stored/{stored_report_id}

Create a billing report

POST /reports
GET /reports/{report_id}/stored
GET /reports/{report_id}/stored/{stored_report_id}






In this section

Tenant service usage JSON object structure
Fetching tenants usage batch
Managing reports