---
title: "Reporting alerts"
source: "https://developer.acronis.com/doc/connector/managing-alerts/reporting-alerts/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:00.669929"
---

# Reporting alerts

Reporting alerts

You can inject alerts to Acronis Cyber Protect Cloud by sending a POST request to the /api/alert_manager/v1/alerts endpoint.
Injected alerts display in the Cyber Protection console.
See the Alert example, below.


Interaction diagram





Request structure







Parameter
Type
Description



type
string
The identifier of the alert type.

category
string
The identifier of the alert category.

details
object
An object that contains the information about the alert.

details.title
string
A human-readable title of the alert.

details.category
string
A human-readable alert category name.

details.description
string
A human-readable description of the alert.

details.fields
object

An object with arbitrary keys and values where each key-value pair represents a table row.
Key is the first column, value is the second column of the row.


Note

If the object includes a key-value of the type url: http://some_url, the URL is displayed as an active link.
If the URL is too long to fit on a single line in the alert, it is truncated and the suppressed characters are replaced with an ellipsis.






tenantID
string
The identifier of the tenant where the alert was triggered.

ResourceID and ResourceName
strings


Note
Both are required for the device/workload row to appear in the alert.


ResourceID is the UUID of the device/workload which triggered the alert.
ResourceName is the name of the device/workload which triggered the alert.




When the partner or customer opens the Alerts section of Acronis Protection Console, the alert shows ResourceName as a link.
The user can click this link to drill down to the device/workload (similar to native Acronis alerts).



When the partner or customer opens the Acronis dashboard and adds alerts widgets, the alert shows ResourceName as a link.
The user can click this link to drill down to the device/workload (similar to native Acronis alerts).



When the partner or customer opens the DEVICES section in Acronis Protection Console, and opens the device/workload for which an alert has been posted, the Alert section in the right panel contains the alert.





Note

If device/workload no longer exists, the name is displayed, but it is not clickable.








Alert example
{
"type": "cti.a.p.am.alert.v1.0~a.p.basic.v1.0~vendor.application.malware_detected.v1.0",
"category": "cti.a.p.am.category.v1.0~vendor.application.protection.v1.0",
"details": {
"title": "Malware Quarantined",
"category": "Malware Detected",
"description": "Malicious file \"trojan.exe\" was put into quarantine.",
"fields": {
"Malware type": "Trojan:Win32/Caphaw.D!lnk",
"Device ID": "62aedd2b-6556-45d5-a76e-43db475068a7",
"Full path": "C:\\Windows\\System32\\trojan.exe"
}
},
"tenantID": "f234baa2-e404-4d78-93de-4f3a77448d02"
}


Produces the following alert in the Cyber Protection console.




Response structure
The response returns status 200, with a single field payload.







Parameter
Type
Description



id
string
UUID of the reported alert.




In this section

Step-by-step procedure