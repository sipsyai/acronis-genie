---
title: "Fetching a list of resources by type"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/resources/fetching-resources-by-type.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:29.501139"
---

# Fetching a list of resources by type

Fetching a list of resources by type

To fetch a list of resources by type

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named filters, and then assign an object containing the type query string parameter to this variable:
>>> filters = {
...     'type': 'resource.machine'
... }



Note
For the list of available query string parameters, see the Resource and Policy Management API reference.


Note
To fetch resources by multiple types, provide the values in the following format:
or(resource.machine,resource.mssql_server)


Send a GET request to the /resource_management/v4/resources endpoint:
>>> response = requests.get(f'{base_url}/resource_management/v4/resources', headers=auth, params=filters)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes  and API error codes.

Also, the response body contains an object with the items key, containing an array of resource objects formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'created_at': '2021-02-03T14:57:07.293995787Z',
'external_id': '23effcf6-2798-4631-9a52-5785bf3af657@17',
'id': '23effcf6-2798-4631-9a52-5785bf3af657',
'name': 'DESKTOP-JRPTA4A',
'tenant_id': '17',
'type': 'resource.machine',
'updated_at': '2021-02-03T18:13:48.312293448Z',
'user_defined_name': 'DESKTOP-JRPTA4A'}],
'paging': {'cursors': {'total': 1}}}