---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/managing-alerts/dismissing-alerts/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:43.660081"
---

# Step-by-step procedure

Step-by-step procedure

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL
'https://eu8.acronis.cloud'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named params, and then assign an object with the id parameter to dismiss one or more alerts by IDs to this variable:
>>> params = {
...     # ID of the alert(s) to remove
...     "id": "54f3318a-6e72-49d7-b94f-b9909df96d16"
... }



Send a DELETE request to the /api/alert_manager/v1/alerts endpoint:
>>> response = requests.delete(f'{base_url}/api/alert_manager/v1/alerts', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the alerts were dismissed successfully.