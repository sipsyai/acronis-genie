---
title: "JSON object structure"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/services/obj-structure.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:17.710633"
---

# JSON object structure

JSON object structure
The API represents a service as a JSON object.

JSON object structure of a service







Name
Value type
Description



id
UUID string
The universally unique identifier (UUID) of the service. This UUID is used for accessing the service via the API.

api_base_url
string
The service console endpoint. The full URL of the service console is a concatenation of, for example, {{beta-url}} and this value.

name
string
The display name of the service.

type
string
The internal name of the service.

usages
array of strings
The names of service usage metrics that are available in reports.





Sample JSON object of a service
{
"name": "Cyber Infrastructure",
"id": "cc29685d-a9ca-3e87-a83d-069f18b588f0",
"api_base_url": "/hci/",
"usages": [
"hci_cifs_storage",
"hci_iscsi_storage",
"hci_nfs_storage",
"hci_s3_storage",
"hci_storage",
"hci_total_cifs_storage",
"hci_total_iscsi_storage",
"hci_total_nfs_storage",
"hci_total_s3_storage",
"hci_total_storage",
"hci_total_vm_provisioned_cpu",
"hci_total_vm_provisioned_ram",
"hci_total_vm_storage",
"hci_vm_provisioned_cpu",
"hci_vm_provisioned_ram",
"hci_vm_storage"
],
"type": "hci"
}