---
title: "Fetching the OS family of the host"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/agents/managing-agents/fetch-os.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:27.939152"
---

# Fetching the OS family of the host

Fetching the OS family of the host

To fetch the OS family of the host

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api/agent_manager/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Define a variable named agent_id, and then assign an ID of the agent to this variable:
>>> agent_id = '23effcf6-2798-4631-9a52-5785bf3af657'



Send a GET request to the /agents/{agent_id} endpoint:
>>> response = requests.get(f'{base_url}/agents/{agent_id}', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes.

Also, the response body contains an agent object formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'auto_update': False,
'core_version': {'current': {'build': '179', 'release_id': '1.2.8'}},
'enabled': True,
'host_id': 'b66fc4a7-69d4-4507-a229-0c38c58f626f',
'hostname': 'DESKTOP-JRPTA4A',
'id': '23effcf6-2798-4631-9a52-5785bf3af657',
'meta': {'atp': {'components': [{'name': 'ANTIVIRUS_ENGINE',
'update_time': 'Mon, 06 Jul 2020 15:01:10 '
'+0300',
'version': '80985'},
{'name': 'ACTIVE_PROTECTION',
'update_time': 'Mon, 06 Jul 2020 15:02:12 '
'+0300',
'version': '1.0.0.566'},
{'name': 'VULNERABILITY_ASSESSMENT',
'update_time': 'Mon, 06 Jul 2020 15:02:12 '
'+0300',
'version': '979.0.0.0'}]}},
'name': '',
'online': False,
'platform': {'arch': 'X64',
'caps': 0,
'family': 'WINDOWS',
'name': 'windows',
'product_type': 0,
'service_pack': 0,
'sku': 0,
'suite_mask': 0,
'version_major': 0,
'version_minor': 0},
'registration_date': 'Wed, 29 Apr 2020 15:18:40 +0000',
'tenant': {'id': '1496265', 'name': 'JohnDoe@mysite.com'},
'units': [{'name': 'active_protection',
'version': {'current': {'build': '1', 'release_id': '0.0.0'}}},
{'meta': {'format': 'json',
'meta': 'eyJjb21wb25lbnRzIjpbeyJuYW1lIjoiQU5USVZJUlVTX0VOR0lORSIsInVwZGF0ZV90aW1lIjoiTW9uLCAwNiBKdWwgMjAyMCAxNTowMToxMCArMDMwMCIsInZlcnNpb24iOiI4MDk4NSJ9LHsibmFtZSI6IkFDVElWRV9QUk9URUNUSU9OIiwidXBkYXRlX3RpbWUiOiJNb24sIDA2IEp1bCAyMDIwIDE1OjAyOjEyICswMzAwIiwidmVyc2lvbiI6IjEuMC4wLjU2NiJ9LHsibmFtZSI6IlZVTE5FUkFCSUxJVFlfQVNTRVNTTUVOVCIsInVwZGF0ZV90aW1lIjoiTW9uLCAwNiBKdWwgMjAyMCAxNTowMjoxMiArMDMwMCIsInZlcnNpb24iOiI5NzkuMC4wLjAifV19',
'schema_ver': 1},
'name': 'atp-agent',
'version': {'current': {'build': '1', 'release_id': '0.0.0'}}},
{'name': 'atp-downloader',
'version': {'current': {'build': '1', 'release_id': '0.0.0'}}},
{'name': 'cyber-protect-service',
'version': {'current': {'build': '1', 'release_id': '0.0.0'}}},
{'name': 'mms',
'version': {'current': {'build': '1', 'release_id': '0.0.0'}}},
{'name': 'sync-unit',
'version': {'current': {'build': '1', 'release_id': '0.0.0'}}},
{'name': 'task-manager',
'version': {'current': {'build': '1', 'release_id': '0.0.0'}}}]}



Convert the JSON text that the response body contains to an object, and then fetch the information about the host’s operation system family:
>>> host_os_family = response.json()['platform']['family']
>>> host_os_family
'WINDOWS'