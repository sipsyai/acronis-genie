---
title: "Creating a billing report"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tutorials/creating-billing-report.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:18:25.209778"
---

# Creating a billing report

Creating a billing report
To create a usage report for billing purposes, use the POST /reports endpoint. This endpoint provides the possibility to include product SKUs.

Important
Not all partners may access to SKUs in reports.
Verify that SKUs are present in the sku field before using it.

To make the reports more convenient for billing purposes, the endpoint also provides the possibility to exclude offering items without usage from the report.

Note
To calculate Disaster Recovery compute points for the report types other than csv or html, divide the value by 3600 and round it to 2 decimal places.


To create a billing report

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named report_data, and then assign the report data to this variable:
>>> report_data = {
...     "parameters": {
...         "kind": "usage_summary",
...         "tenant_id": tenant_id,
...         "level": "direct_partners",
...         "kind": "usage_summary",
...         "period": {
...             "start": "2017-05-01",
...             "end": "2017-05-07"
...         },
...         "formats": [
...             "csv_v2_0",
...             "json_v2_0"
...         ],
...         "hide_zero_usage": True,
...         "show_skus": True
...     },
...     "schedule": {
...         "type": "once"
...     },
...     "result_action": "save"
... }










Name
Value type
Required
Description



parameters
report parameters object
Yes
An object of report parameters which allow to configure the report. The required parameters of this object are kind, tenant_id and level.

schedule
report schedule object
Yes
An object that allows to configure scheduling of the report. The required parameter of this object is type.

result_action
string
Yes
Action to be done with the report. See report result actions for the list of available report result actions.




Convert the report_data object to a JSON text:
>>> report_data = json.dumps(report_data, indent=4)



Send a POST request with the JSON text to the /reports endpoint:
>>> response = requests.post(
...     f'{base_url}/reports',
...     headers={'Content-Type': 'application/json', **auth},
...     data=report_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the report has been created and sent by email to specified recipients.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the report data, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'generation_date': '2017-05-08',
'id': '20dffb36-d77b-45c6-b2fa-39276e98d5fc',
'parameters': {'formats': ['csv_v2_0', 'json_v2_0'],
'kind': 'usage_summary',
'level': 'direct_partners',
'period': {'end': '2017-05-07', 'start': '2017-05-01'},
'tenant_id': 'ede9f834-70b3-476c-83d9-736f9f8c7dae'},
'result_action': 'save',
'version': 1}



Store the UUID and revision number of the report:
>>> report_id = response.json()['id']
>>> report_id
'20dffb36-d77b-45c6-b2fa-39276e98d5fc'



Send a GET request to the /reports/{report_id}/stored endpoint:
>>> response = requests.get(f'{base_url}/reports/{report_id}/stored', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains the items array with stored reports data, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'created_at': '2019-08-08T07:36:58+00:00',
'id': '479040dc-e18e-4136-98ce-635c3bc7dbae',
'report_format': 'csv_v2_0',
'size': 4945,
'status': 'saved'},
{'created_at': '2019-08-08T07:36:58+00:00',
'id': 'a10bd132-261d-47aa-b7c6-74d39bc2266b',
'report_format': 'json_v2_0',
'size': 5892,
'status': 'saved'}]}



Note
The stored report might take some time to generate, so it might not be available for download immediately. In most cases, it takes 1-2 minutes to generated the report. It is recommended to implement polling mechanism until all reports are saved.


Choose the report format, iterate over the items array and store the UUID of the stored report in a variable.
As an example, we will get the UUID of the last stored csv_v2_0 report:
>>> stored_reports = response.json()['items']
>>> stored_report_id = [stored_report['id'] for stored_report in stored_reports if stored_report['report_format'] == 'csv_v2_0' and stored_report['status'] == 'saved'][-1]
>>> stored_report_id
'af5946c3-7e5b-4480-8835-518efe1c3522'



Send a GET request to the /reports/{report_id}/stored/{stored_report_id} endpoint:
>>> response = requests.get(f'{base_url}/reports/{report_id}/stored/{stored_report_id}', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body contains the stored report file in specified format.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.


[Optional] Store the response body in a variable:

For CSV and HTML reports:
>>> stored_report_data = response.text



For JSON reports:

>>> stored_report_data = response.json()