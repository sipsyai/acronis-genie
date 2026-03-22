---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/managing-workloads/updating-workloads/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:52.952925"
---

# Step-by-step procedure

Step-by-step procedure

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL
'https://eu8.acronis.cloud'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named workload_id, and then assign ID of the workload obtained from the list of fetched workloads to this variable:
>>> workload_id = 'b369335d-fc8a-4c7f-b5bb-896448c854bd'



Define a variable named workload_data, and then assign the updated information about the workload to this variable:
>>> workload_data = {
...     "name": "New virtual machine name",
...     "attributes": {
...         "hostname": "CORP-123456",
...         "mac_address": "0a:df:7e:25:36:7e"
...     }
... }



Convert the workload_data object to a JSON text:
>>> workload_data = json.dumps(workload_data, indent=4)
>>> print(workload_data)
{
"name": "New virtual machine name",
"attributes": {
"hostname": "CORP-123456",
"mac_address": "0a:df:7e:25:36:7e"
}
}



Send a PATCH request with the JSON text to the /api/workload_management/v5/workloads/{workload_id} endpoint:
>>> response = requests.patch(
...     f'{base_url}/api/workload_management/v5/workloads/{workload_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=workload_data,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 200 means that the workload was updated successfully.