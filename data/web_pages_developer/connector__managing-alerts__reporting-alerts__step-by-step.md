---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/managing-alerts/reporting-alerts/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:04.893982"
---

# Step-by-step procedure

Step-by-step procedure

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL
'https://eu8.acronis.cloud'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named alert_data, and then assign the information about the workload to this variable:
>>> alert_data = {
...     "title": "Malware Quarantined",
...     "category": "Malware Detected",
...     "description": "Malicious file "trojan.exe" was put into quarantine.",
...     "fields": {
...         "Malware type": "Trojan:Win32/Caphaw.D!lnk",
...         "Device ID": "62aedd2b-6556-45d5-a76e-43db475068a7",
...         "Full path": "C:\Windows\System32   rojan.exe"
...     }
... }



Convert the alert_data object to a JSON text:
>>> alert_data = json.dumps(alert_data, indent=4)



Send a POST request with the JSON text to the /api/alert_manager/v1/alerts endpoint:
>>> response = requests.post(
...     f'{base_url}/api/alert_manager/v1/alerts',
...     headers={'Content-Type': 'application/json', **auth},
...     data=alert_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the alert was reported successfully and it should appear in the Cyber Protection console.
Also, the response body contains the identifier of the alert, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{
"id": "31bd814f-f8ca-4691-a81f-c1d229fe1c17"
}