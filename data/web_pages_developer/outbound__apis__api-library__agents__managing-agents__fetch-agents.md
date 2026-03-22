---
title: "Fetching all registered agents"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/agents/managing-agents/fetch-agents.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:23.731100"
---

# Fetching all registered agents

Fetching all registered agents

Fetches all registered agents seen from a specified tenant.
Result includes all agents registered in the tenant and in all its child tenants that don’t block parent access using visibility barrier.


To fetch all registered agents

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api/agent_manager/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Send a GET request to the /agents endpoint:
>>> response = requests.get(f'{base_url}/agents', headers=auth)



Note
For a list of available query string parameters, see the Agent Manager API reference.


Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes.

Also, the response body contains the items array of agent objects formatted as a JSON text. When converted to an object, it looks like this:
>>> pprint.pprint(response.json())
{'items': [{'auto_update': False,
'core_version': {'current': {'build': '179',
'release_id': '1.2.8'}},
'enabled': True,
'host_id': 'b66fc4a7-69d4-4507-a229-0c38c58f626f',
'hostname': 'DESKTOP-JRPTA4A',
'id': '23effcf6-2798-4631-9a52-5785bf3af657',
'meta': {'atp': {'components': [{'name': 'ANTIVIRUS_ENGINE',
'update_time': 'Mon, 06 Jul 2020 '
'15:01:10 +0300',
'version': '80985'},
{'name': 'ACTIVE_PROTECTION',
'update_time': 'Mon, 06 Jul 2020 '
'15:02:12 +0300',
'version': '1.0.0.566'},
{'name': 'VULNERABILITY_ASSESSMENT',
'update_time': 'Mon, 06 Jul 2020 '
'15:02:12 +0300',
'version': '979.0.0.0'}]}},
'name': '',
'online': True,
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
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'meta': {'format': 'json',
'meta': 'eyJjb21wb25lbnRzIjpbeyJuYW1lIjoiQU5USVZJUlVTX0VOR0lORSIsInVwZGF0ZV90aW1lIjoiTW9uLCAwNiBKdWwgMjAyMCAxNTowMToxMCArMDMwMCIsInZlcnNpb24iOiI4MDk4NSJ9LHsibmFtZSI6IkFDVElWRV9QUk9URUNUSU9OIiwidXBkYXRlX3RpbWUiOiJNb24sIDA2IEp1bCAyMDIwIDE1OjAyOjEyICswMzAwIiwidmVyc2lvbiI6IjEuMC4wLjU2NiJ9LHsibmFtZSI6IlZVTE5FUkFCSUxJVFlfQVNTRVNTTUVOVCIsInVwZGF0ZV90aW1lIjoiTW9uLCAwNiBKdWwgMjAyMCAxNTowMjoxMiArMDMwMCIsInZlcnNpb24iOiI5NzkuMC4wLjAifV19',
'schema_ver': 1},
'name': 'atp-agent',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'atp-downloader',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'cyber-protect-service',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'mms',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'sync-unit',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'task-manager',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}}]},
{'auto_update': False,
'core_version': {'current': {'build': '174',
'release_id': '1.2.8'}},
'enabled': True,
'host_id': '6943307a-e523-40d3-9668-04f8d3374326',
'hostname': 'DESKTOP-GFT9S1R',
'id': 'f7358a00-8469-45ae-a0c3-22952e9ed12f',
'meta': {'atp': {'components': [{'name': 'ACTIVE_PROTECTION',
'update_time': 'Wed, 31 Dec 1969 '
'16:00:00 -0800',
'version': '1.0.0.377'},
{'name': 'ANTIVIRUS_ENGINE',
'update_time': 'Wed, 22 Apr 2020 '
'04:50:22 -0700',
'version': '0.0.0.0'},
{'name': 'VULNERABILITY_ASSESSMENT',
'update_time': 'Wed, 22 Apr 2020 '
'06:00:27 -0700',
'version': '912.0.0.0'}]}},
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
'registration_date': 'Wed, 22 Apr 2020 11:34:03 +0000',
'tenant': {'id': '1496265', 'name': 'JohnDoe@mysite.com'},
'units': [{'name': 'active_protection',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'meta': {'format': 'json',
'meta': 'eyJjb21wb25lbnRzIjpbeyJuYW1lIjoiQUNUSVZFX1BST1RFQ1RJT04iLCJ1cGRhdGVfdGltZSI6IldlZCwgMzEgRGVjIDE5NjkgMTY6MDA6MDAgLTA4MDAiLCJ2ZXJzaW9uIjoiMS4wLjAuMzc3In0seyJuYW1lIjoiQU5USVZJUlVTX0VOR0lORSIsInVwZGF0ZV90aW1lIjoiV2VkLCAyMiBBcHIgMjAyMCAwNDo1MDoyMiAtMDcwMCIsInZlcnNpb24iOiIwLjAuMC4wIn0seyJuYW1lIjoiVlVMTkVSQUJJTElUWV9BU1NFU1NNRU5UIiwidXBkYXRlX3RpbWUiOiJXZWQsIDIyIEFwciAyMDIwIDA2OjAwOjI3IC0wNzAwIiwidmVyc2lvbiI6IjkxMi4wLjAuMCJ9XX0=',
'schema_ver': 1},
'name': 'atp-agent',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'atp-downloader',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'cyber-protect-service',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'mms',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'sync-unit',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}},
{'name': 'task-manager',
'version': {'current': {'build': '1',
'release_id': '0.0.0'}}}]}]}