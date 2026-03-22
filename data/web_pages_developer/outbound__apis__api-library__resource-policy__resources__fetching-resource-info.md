---
title: "Fetching detailed information about the resource"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/resources/fetching-resource-info.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:25.298817"
---

# Fetching detailed information about the resource

Fetching detailed information about the resource

To fetch detailed information about the resource

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the resources, as described in Fetching a list of all resources.
As an example, the ID of the first resource will be taken. The following variable
should be available as the result:
>>> resource_id = fetched_resources[0]['id']
>>> resource_id
'5c350066-2ba6-4eeb-aa91-1213dd35f033'



Send a GET request to the /resource_management/v4/resources/{resource_id}/attributes endpoint:
>>> response = requests.get(f'{base_url}/resource_management/v4/resources/{resource_id}/attributes', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes  and API error codes.

Also, the response body contains an items array, containing objects with attribute namespaces as keys formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{'kvs': [{'key': 'components',
'value': ['HyperVAgent', 'x64WindowsAgent']},
{'key': 'features',
'value': ['HyperVAgent', 'x64WindowsAgent']},
{'key': 'os_family', 'value': 'Windows'},
{'key': 'os_name',
'value': 'Microsoft Windows Server 2019 Standard'},
{'key': 'os_arch', 'value': 'x64'},
{'key': 'os_family', 'value': 'Windows'},
{'key': 'os_caps', 'value': 18},
{'key': 'os_product_type', 'value': 3},
{'key': 'os_service_pack', 'value': 0},
{'key': 'os_suite_mask', 'value': 272},
{'key': 'sku', 'value': 7},
{'key': 'os_version_major', 'value': 10},
{'key': 'os_version_minor', 'value': 0},
{'key': 'mac_addresses', 'value': ['00:50:56:84:DB:B7']},
{'key': 'memory_size', 'value': 17178800128},
{'key': 'processor_frequency', 'value': 3504},
{'key': 'processor_name', 'value': 3504},
{'key': 'chassis', 'value': 'other'},
{'key': 'vm_host_type', 'value': 'vmwesx'},
{'key': 'esx_address', 'value': ''},
{'key': 'residental_addresses', 'value': ['10.34.16.186']},
{'key': 'inside_virtual', 'value': 1},
{'key': 'tz_offset', 'value': 120},
{'key': 'version', 'value': '15.0.26355'},
{'key': 'enabled', 'value': 1},
{'key': 'is_online', 'value': 0}],
'name': 'agent'},
{'details': [{'key': 'cyberfit_score_details',
'value': {'bitlocker': {'encrypted_volumes': 0,
'is_system_volume_encrypted': False,
'volumes': 2},
'os': {'name': 'Microsoft Windows Server 2019 Standard',
'version': '10.0.17763'},
'programs': {'antispyware': [{'name': 'Cyber Protect Agent',
'vendor': 'Acronis',
'version': '15.0.26355'}],
'antivirus': [{'name': 'Cyber Protect Agent',
'vendor': 'Acronis',
'version': '15.0.26355'}],
'backup': [{'name': 'Cyber Protect Agent',
'vendor': 'Acronis',
'version': '15.0.26355'}],
'disk_encryption': [],
'firewall': [],
'vpn': []},
'windows_defender': {'antispyware': {'enabled': True},
'antivirus': {'enabled': True}},
'windows_firewall': {'private_network': {'enabled': True},
'public_network': {'enabled': True}},
'windows_server_backup': {'installed': False}}},
{'key': 'cyberfit_score_value', 'value': 625},
{'key': 'cyberfit_score_server_version', 'value': 38},
{'key': 'cyberfit_score_client_version', 'value': 108},
{'key': 'cyberfit_score_assessment_date',
'value': '2021-02-03T18:13:46.9931835Z'},
{'key': 'cyberfit_score_metrics',
'value': {'antimalware': {'current': 275, 'max': 275},
'backup': {'current': 175, 'max': 175},
'disk_encryption': {'current': 0,
'max': 125},
'firewall': {'current': 175, 'max': 175},
'ntlm': {'current': 0, 'max': 25},
'vpn': {'current': 0, 'max': 75}}}],
'kvs': [{'key': 'cyberfit_score_value', 'value': '625'}],
'name': 'cyberfit'},
{'kvs': [{'key': 'ip_addresses', 'value': '10.34.16.186'},
{'key': 'ldap_status', 'value': 'ldapoff'},
{'key': 'operating_system_product_type', 'value': 3},
{'key': 'operating_system_type', 'value': 3},
{'key': 'architecture', 'value': 'x64'},
{'key': 'ip', 'value': '10.34.16.186'},
{'key': 'name', 'value': 'DESKTOP-JRPTA4A'},
{'key': 'operating_system',
'value': 'Microsoft Windows Server 2019 Standard'},
{'key': 'os_product_type', 'value': '3'},
{'key': 'residential_address_v4', 'value': '0a2210ba'}],
'name': 'default'}]}