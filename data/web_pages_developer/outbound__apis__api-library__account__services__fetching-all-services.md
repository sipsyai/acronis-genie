---
title: "Fetching information about all platform services"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/services/fetching-all-services.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:50.878591"
---

# Fetching information about all platform services

Fetching information about all platform services

To fetch information about all platform services

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /applications endpoint:
>>> response = requests.get(f'{base_url}/applications', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the response body text contains an encoded JSON object consisting of the items member. The items member is an array of service objects.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

>>> pprint.pprint(response.json())
[{'api_base_url': '/bc/',
'id': '6e6d758d-8e74-3ae3-ac84-50eb0dff12eb',
'name': 'Backup',
'type': 'backup',
'usages': ['workstations',
'servers',
'vms',
'mobiles',
'virtualhosts',
'win_server_essentials',
'mailboxes',
'storage',
'workstation_storage',
'server_storage',
'vm_storage',
'mobile_storage',
'virtualhost_storage',
'win_server_essentials_storage',
'mailbox_storage',
'mailbox_instance_size',
'websites',
'website_storage',
'dr_storage',
'public_ips',
'compute_points',
'assigned_compute_points',
'child_storages',
'total_storage',
'local_storage',
'universal_devices',
'universal_devices_storage',
'dr_cloud_servers',
'onedrive_storage',
'google_drive_storage',
'google_mail_storage',
'gsuite_seats',
'group_mailbox_storage',
'group_site_storage',
'site_collection_storage',
'google_team_drive_storage',
'cloud_to_cloud_backup',
'dr_internet_access',
'dr_child_storages',
'web_hosting_servers',
'web_hosting_server_storage',
'o365_mailboxes',
'o365_onedrive',
'o365_sharepoint_sites',
'google_mail',
'google_drive',
'google_team_drive',
'search_index_storage']},
{'api_base_url': '/pds/',
'id': 'b71b2c18-590a-303c-9d5a-8444fbe713ac',
'name': 'Physical Data Shipping',
'type': 'physical_data_shipping',
'usages': ['drives_shipped_to_cloud', 'drives_shipped_from_cloud']},
{'api_base_url': '/fc/',
'id': 'dfd85a5f-a464-32ab-81fd-99bcc66a070f',
'name': 'File Sync & Share',
'type': 'files_cloud',
'usages': ['fc_seats',
'fc_storage',
'fc_child_storages',
'fc_total_storage']},
{'api_base_url': '/hci/',
'id': 'cc29685d-a9ca-3e87-a83d-069f18b588f0',
'name': 'Cyber Infrastructure',
'type': 'hci',
'usages': ['hci_iscsi_storage',
'hci_s3_storage',
'hci_nfs_storage',
'hci_cifs_storage',
'hci_vm_storage',
'hci_vm_provisioned_cpu',
'hci_vm_provisioned_ram',
'hci_storage',
'hci_total_iscsi_storage',
'hci_total_s3_storage',
'hci_total_nfs_storage',
'hci_total_cifs_storage',
'hci_total_vm_storage',
'hci_total_vm_provisioned_cpu',
'hci_total_vm_provisioned_ram',
'hci_total_storage']},
{'api_base_url': '/mc/',
'id': '7459244f-68f3-3bf4-9f53-5f63ecc1d91f',
'name': 'Management Portal',
'type': 'platform',
'usages': []}]