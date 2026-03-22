---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/managing-alerts/fetching-alerts/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:52.059819"
---

# Step-by-step procedure

Step-by-step procedure

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL
'https://eu8.acronis.cloud'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named params, and then assign an object with the severity parameter to include only alerts with the warning severity to this variable:
>>> params = {
...     # Include alerts with the "critical" severity
...     "severity": "warning"
... }



Send a GET request to the /api/alert_manager/v1/alerts endpoint:
>>> response = requests.get(f'{base_url}/api/alert_manager/v1/alerts', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the list of alerts filtered by the warning severity, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{
"items": [
{
"id": "887E19F7-59F5-44DC-9721-64B1C48B4117",
"type": "cti.a.p.am.alert.v1.0~a.p.basic.v1.0~vendor.application.malware_detected.v1.0",
"category": "cti.a.p.am.category.v1.0~vendor.application.protection.v1.0",
"details": {
"title": "Malware Detected",
"category": "Protection",
"description": "Malicious file \"trojan.exe\" was put into quarantine.",
"fields": {
"Malware type": "Trojan:Win32/Caphaw.D!lnk",
"Device ID": "62aedd2b-6556-45d5-a76e-43db475068a7",
"Full path": "C:\\Windows\\System32\\trojan.exe"
}
},
"receivedAt": "2023-11-07T14:39:57.556577425Z",
"updatedAt": "2023-11-07T14:39:57.556577425Z",
"createdAt": "2023-11-07T14:39:57.556577425Z",
"severity": "warning",
"affinity": "",
"tenant": {
"id": "286",
"uuid": "1d1e5a08-1139-4c25-9a26-e9fc1b76460c",
"locator": "/1/281/282/285/286/"
}
},
...
],
"paging": {
"cursors": {}
}
}