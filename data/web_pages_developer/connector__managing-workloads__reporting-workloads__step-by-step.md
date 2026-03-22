---
title: "Step-by-step procedure"
source: "https://developer.acronis.com/doc/connector/managing-workloads/reporting-workloads/step-by-step.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:44.552075"
---

# Step-by-step procedure

Step-by-step procedure

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL
'https://eu8.acronis.cloud'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named workload_type, and then assign ID of the workload type registered in the Vendor Portal to this variable:
>>> workload_type = 'cti.a.p.wm.workload.v1.0~a.p.wm.aspect.v1.0~vendor.application.virtual_machine.v1.0'



Define a variable named allowed_actions, and then assign IDs of the allowed workload actions registered in the Vendor Portal to this variable:
>>> allowed_actions = [
...     'cti.a.ui.item.v1.0~a.ui.ext_p.workload_actions.action.v1.0~vendor.application.open_console.v1.0'
... ]



Define a variable named workload_data, and then assign the information about the workload to this variable:
>>> workload_data = {
...     "type": workload_type,
...     "name": "My Custom Virtual Machine",
...     "attributes": {
...         "hostname": "DESKTOP-12ABC3D",
...         "mac_address": "0a:df:7e:25:36:7e"
...     },
...     "client_id": client_id,
...     "allowed_actions": allowed_actions,
...     "tenant_id": tenant_id,
...     "enabled": True
... }



Convert the workload_data object to a JSON text:
>>> workload_data = json.dumps(workload_data, indent=4)



Send a POST request with the JSON text to the /api/workload_management/v5/workloads endpoint:
>>> response = requests.post(
...     f'{base_url}/api/workload_management/v5/workloads',
...     headers={'Content-Type': 'application/json', **auth},
...     data=workload_data,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 200 means that the workload was reported successfully and that it should appear in the Cyber Protection console.