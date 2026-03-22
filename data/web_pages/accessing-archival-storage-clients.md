# Accessing archival storage via third-party clients

Additional Cyber Protection tools > Archival storage > Accessing archival storage via third-party clients
Accessing archival storage via third-party clients

You can manage the objects in archival storage by using an S3-compatible client. Popular options include:

Cyberduck
S3 Browser
Mountain Duck
Rclone

With an S3-compatible client, you can perform the following actions:

Upload files to a bucket
Create folders in a bucket
Download files or folders to local storage
Delete files and folders from a bucket
Archival storage supports object names that include alphanumeric and special characters. Check the documentation of your S3-compatible client for any restrictions on object naming.

To access archival storage, you must provide:

Access key ID
Secret access key

Object Storage S3 endpoint

For example: s3-us-central-2.acronis.storage

[If not automatically populated] Port

Archival storage supports port 443 with TLS v1.2 or later.

The access key ID, secret access key, and the endpoint URL are displayed only when you create a new access key pair. Copy or download these items as a CSV file. If you lose them, create a new key pair and reconfigure your S3-compatible client. For more information, see Generating an access key pair.

S3-compatible clients must use path-style URLs. For example:

https://s3-eu-central-1.acronis.storage/mybucket/myfolder/file.txt

Virtual-hosted-style URLs are not supported. For example:

https://mybucket.s3-eu-central-1.acronis.storage/myfolder/file.txt

For detailed information on configuring an S3-compatible client, see the client's documentation.

For example:

Cyberduck: https://docs.cyberduck.io/cyberduck
S3 Browser: https://s3browser.com/help.aspx
Mountain Duck: https://docs.cyberduck.io/mountainduck
Rclone: https://rclone.org/docs
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.