---
title: "Managing reports"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/usage-reporting/reports/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:19:15.954070"
---

# Managing reports

Managing reports
Operations with the reports in the cloud platform are located under the /reports endpoint.
Reports allow you to have detailed statistics of the usage of your services.
The reports use binary gigabytes (GB), which are 1024^3 bytes, or gibibytes (GiB)
as measurement units for storage space.

Important
The platform enforces the following rules for the report period:

Report period must not be in the future.
If the tenant was renamed, the report will contain the latest name of the tenant within the provided period.



Report levels






Value
Description



direct_partners
The report will include direct customers and partners.

all_partners
The report will include all partners.

all_customers
The report will include all customers and partners.

accounts
The report will include all customers and partners (including user account details).





Report kinds






Value
Description



usage_daily
A kind of report that will contain the service usage metrics for each day of the specified period.

usage_summary
A kind of report that will contain the service usage metrics for the end of the specified period, and the difference between the metrics in the beginning and at the end of the specified period.

usage_current
A kind of report that will contain the current service usage metrics for the previous day. The usage metrics are calculated within each of the child tenants’ billing periods. If the tenants included in the report have different billing periods, the parent tenant’s usage may differ from the sum of the child tenants’ usages.

usage_breakdown
A kind of report that will contain the service usage metrics and their changes for each day of the specified period.





Report formats






Value
Description



csv
The report will be generated in table-formatted CSV format.

html
The report will be generated in HTML format.

json_v1
The report will be generated in API v1 compatible JSON format.

csv_v2_0
The report will be generated in CSV format.

json_v2_0
The report will be generated in API v2 compatible JSON format.





Report scheduling types






Value
Description



once
The report will be generated only once on generation_date.

monthly
The report will be generated at 23:59:59 by UTC time on the first day of a month and sent on the second day of that month to administrators of your tenant who have the reports attribute in notifications.





Report result actions






Value
Description



save
The report will be saved on the server when generated and it will be possible to download it.

send
The report will be sent by email when generated.





Available usage reports operations






Operation
Methods and endpoints used



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

Report-related JSON object structure
Creating a usage report
Fetching a usage report
Fetching a usage report from tenant reports
Updating a usage report
Disabling/enabling a usage report
Deleting a usage report
Fetching stored reports
Fetching a service usage using a stored report
Creating a billing report