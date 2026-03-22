---
title: "Storage object structure"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/store-obj-structure.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:51.836079"
---

# Storage object structure

Storage object structure
The API represents storages as JSON objects.

JSON object structure of a storage







Name
Value type
Description



id
UUID string
The UUID of the storage.

owner_tenant_id
UUID string
The UUID of the tenant this storage belongs to.

location_id
UUID string
The UUID of the location this storage belongs to.

platform_owned
boolean
Flag, that specifies if it is platform-owned storage.

name
string
A name of the storage.

url
string
The URL of the storage. See storage url formatting rules

capabilities
array of strings
A list of services this storage can be used in. See the list of available storage capabilities.

content_url
string
The URL to the web interface of the restore server.

content_mobile_url
string
The URL to the archive server used by mobile backup apps to access the cloud storage.

backend_type
string
The backend type of the storage. Once the storage has been created, the backend_type can be changed only by root admin. See the list of available backend types

version
number
Revision number.

readonly
boolean
Flag, that specifies if the location can be modified.




Example storage
{
"id": "8fcd353b-0a40-40f2-9a55-ef8137d48800",
"owner_tenant_id": "0bb386ae-e66d-4e7b-84fb-cddcf60002de",
"location_id": "f79546d7-d051-4e19-96f3-4cc68c2c5575",
"platform_owned": true,
"name": "Azure Backup Storage",
"url": "acronis+fes://storage20.corp.acronis.com:44445",
"capabilities": [
"backup",
"disaster_recovery",
"files_cloud"
],
"content_url": "https://browse.storage20.corp.acronis.com/",
"content_mobile_url": "https://browse.storage20.corp.acronis.com/mobile/",
"backend_type": "azure",
"version": 3,
"readonly": false
}





Available storage types and required credentials
Acronis S3 Storage or other S3-compatible storage

s3 access key id
s3 secret access key
storage address
bucket name
encryption type (AES-128, AES-256) you want to use (optional)

Amazon S3

s3 access key id
s3 secret access key
bucket name
region (optional)
encryption type (AES-128, AES-256) you want to use (optional)

Microsoft Azure

azure account name
azure access key
azure blob container name
encryption type (AES-128, AES-256) you want to use (optional)



Storage URL formatting rules
The storage URL must comply with RFC 1738 and use the following storage URL schemes:






Value
Description



abgw
Acronis Storage

ssfs
Acronis File Sync & Share Storage

s3
Acronis S3 Storage or other S3-compatible storage

amazon+s3
Amazon S3 Storage

microsoft+azure
Microsoft Azure Storage



Below are listed the URL formats for different storage types (see the list of required credentials for reference):

Acronis S3 Storage or other S3-compatible storages:

s3://<s3-access-key-id>:<s3-secret-access-key>@<storage-address>/<bucket-name>?encryption=<aes128|aes256>&use_ssl=<true|false>


Amazon S3:

amazon+s3://<s3-access-key-id>:<s3-secret-access-key>@s3-<region>.amazonaws.com/<bucket-name>?encryption=<aes128|aes256>&use_ssl=<true|false>

Note
<region> is optional, for default region use s3.amazonaws.com address.



Microsoft Azure Storage:

microsoft+azure://<azure-account-name>:<azure-access-key>@blob.core.windows.net/<azure-blob-container-name>?encryption=<aes128|aes256>





Available storage backends






Value
Description



acronis
Acronis backend type.

google
Google backend type.

azure
Microsoft Azure backend type.

amazon_s3
Amazon S3 backend type.





Available storage capabilities






Value
Description



backup
Allows this storage to be used in “Backup” service.

disaster_recovery
Allows this storage to be used in “Disaster Recovery” service.

files_cloud
Allows this storage to be used in “File Sync & Share” service.