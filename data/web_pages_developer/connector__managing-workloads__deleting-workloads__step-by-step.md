---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/managing-workloads/deleting-workloads/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:13.287442"
---

# Step-by-step procedure

Step-by-step procedure

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL
'https://eu8.acronis.cloud'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named params, and then assign an object with the workload_id parameter to delete one or more workloads by IDs to this variable:
>>> params = {
...     # Include workload attributes in the response
...     "workload_id": "54f3318a-6e72-49d7-b94f-b9909df96d16"
... }



Send a DELETE request to the /api/workload_management/v5/workloads endpoint:
>>> response = requests.delete(
...     f'{base_url}/api/workload_management/v5/workloads',
...     headers=auth,
...     params=params,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the workloads were deleted successfully.