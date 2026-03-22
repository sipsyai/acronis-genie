# Defining a backup location in IONOS Cloud, Impossible Cloud, or S3 compatible storage

Managing the backup and recovery of workloads and files > Backing up workloads to public clouds > Defining a backup location in IONOS Cloud, Impossible Cloud, or S3 compatible storage
Defining a backup location in IONOS Cloud, Impossible Cloud, or S3 compatible storage
To configure backup locations in IONOS Cloud, Impossible Cloud, or S3 compatible storage, you must have one of the following roles defined in the Cyber Protection service: Company administrator, User, or Cyber administrator.
Buckets in special GovCloud regions (for example, https://aws.amazon.com/govcloud-us/, https://learn.microsoft.com/en-us/azure/azure-government/regions, or other endpoint URLs from storage vendors supporting the GovCloud concept) are not supported as backup locations.

To back up a workload to IONOS Cloud, Impossible Cloud, or S3 compatible storage, you must define the backup location in the Cyber Protect console. You can do this in the following ways:

When creating or editing a protection plan.
When defining and managing backup storage locations.

Both administrators and non-administrator users can back up workloads to IONOS Cloud, Impossible Cloud, or S3 compatible storage.

Non-administrator users can also apply protection plans which use the backup locations on Impossible Cloud, IONOS Cloud, or S3 compatible storage created by themselves, and for workloads registered in the Cyber Protect console under their name.

Administrators can apply protection plans which use the backup location connected to IONOS Cloud, Impossible Cloud, or S3 compatible storage connections they added themselves or by any other administrator, and for workloads registered in the Cyber Protect console under any user.

To define a backup location in IONOS Cloud, Impossible Cloud, or S3 compatible storage

In the Cyber Protect console, do one of the following:

If you are creating or editing a protection plan, go to Devices, and then select the workload that you want to back up to IONOS Cloud, Impossible Cloud, or S3 compatible storage. In the Backup section of the selected workload's protection plan, click the link in the Where to back up row.

For more information about working with protection plans, see Protection plans and modules.

If you are managing your backup storage locations and want to add IONOS Cloud, Impossible Cloud, or S3 compatible storage as a new location, go to Backup storage.

For more information about managing your backup storage locations, see Backup storage.

Click Add location.
From the Public clouds dropdown list, select one of the following:
S3 compatible
Impossible Cloud
IONOS Cloud Object Storage

Define the following:

[For S3 compatible, IONOS Cloud, or Impossible Cloud] In the Management agent field, click Browse to select the management agent from a list of suitable agents.

This agent will establish the initial communication with the S3 compatible / IONOS Cloud / Impossible Cloud storage. You can modify the parameters of the backup location at a later time, if necessary.

This management agent, which can be selected from any of the supported agent types (including Agent for Windows/Linux/VMware (Virtual Appliance)/Hyper-V/oVirt (but not Agent for Azure)), is used only during the creation or editing of the backup location. The offline/online state of the agent will not impact the backups performed by other regular agents.

In the Location name field, enter the name of the backup location.

The location name must be unique to the customer tenant. If the name you add already exists in the connection, Cyber Protect Cloud will add a suffix number to the name. For example, if 'IONOS Cloud Object Storage' already exists, the name will be automatically updated to 'IONOS Cloud Object Storage 1'.

In the Bucket field, select the relevant IONOS Cloud, Impossible Cloud, or S3 compatible storage bucket.

If the selected bucket is enabled with the Object Lock and Versioning features, the Backup immutability period (days) checkbox is enabled. You can then define the number of days for the immutability period, which ensures that backed up data is not deleted during this period, and is applied to all backup objects that are created by Cyber Protect Cloud.

Immutability period can be set for S3 compatible, Impossible Cloud, IONOS Cloud, and Amazon S3 types. See Defining a backup location in Amazon S3.

Note that when you set the immutability period as a backup location property, the default retention period defined for the bucket is ignored. For more information about the Object Lock feature and retention periods, see the relevant documentation. For example, see the Impossible Cloud documentation.

We recommend that you configure the Lifecycle policy for the bucket if you have set the immutability option when creating the backup location. Buckets with the Object Versioning and Object Lock features enabled will store object versions forever. As a result, storage consumption will grow indefinitely, unless a Lifecycle policy is configured.

However, we do not recommend you to enable the Object Versioning and Object Lock features for buckets that are used by backup locations and that are configured without the immutability option. If Lifecycle policies are applied to these buckets, they can accidentally delete objects that are related to the backup archive chain, which will result in archive corruption.

With the immutability option configured, the issue is resolved by adjusting the immutability period for old objects, on which the newer backup objects still have dependencies. This happens automatically with each scheduled backup, where the immutability period of each object belonging to the backup chain is extended by the backup agent that communicates with the cloud storage. This immutability period is never less than the immutability period days value that is defined during the creation of the backup location. For more information on how to configure the Lifecycle policy, see the Wasabi documentation (applicable when Wasabi public cloud storage is added as an 'S3 compatible' backup location type).

Agents prior to version 24.06 can perform backups to Impossible Cloud, or S3 compatible storage, but only agents from version 24.06 or higher will apply Object Lock to objects created in Impossible Cloud or S3 compatible storage. This means that only newer agents can acknowledge the immutability period set as a backup location property, and will manage this period for all created backups. Agents prior to version 24.06 will ignore this setting and the default bucket Object Lock properties are applied to the created objects in Impossible Cloud or S3 compatible storage.

[For Impossible Cloud only] The list of buckets is always retrieved from the primary endpoint URL (https://eu-central-2.storage.impossibleapi.net/), which lists the buckets in all regions. The endpoint URL used to read and write data to the bucket is calculated from the detected region of the bucket, and is in the following format: https://[REGION_NAME].storage.impossibleapi.net. For example, if you selected the eu-central-1 bucket, the endpoint URL would be https://eu-central-1.storage.impossibleapi.net/.

[For IONOS Cloud only] The list of buckets is always retrieved from the primary endpoint URL (https://s3.eu-central-4.ionoscloud.com), which lists the buckets in all regions. The endpoint URL used to read and write data to the bucket is calculated from the detected region of the bucket, and is in the following format: https://s3.[REGION_NAME].ionoscloud.com. For example, if you selected the eu-central-2 bucket, the endpoint URL would be https://s3.eu-central-2.ionoscloud.com/.

User-owned buckets in IONOS Cloud will not be listed because they require a unique endpoint URL for access. To use user-owned buckets as backup locations, you must configure an S3 compatible type of backup location, instead of IONOS Cloud Object Storage.

[For S3 compatible storage only] Select the Allow using a self-signed certificate of the endpoint (vulnerable to MITM attack, not recommended) checkbox to skip validation of the certificate chain and accept self-signed certificates for the S3 endpoint URL.

Note that this option is only available when creating the S3 compatible backup location and cannot be changed when editing the backup location.


Click Add.

If you are creating or editing a protection plan, the Impossible Cloud, IONOS Cloud, or S3 compatible storage backup location is set as the location in the Where to back up row. When the backup is run (either manually or when scheduled), the backup is saved in the defined location.

If you are managing your backup storage locations, you can view and update the location details as required. The Impossible Cloud, IONOS Cloud, or S3 compatible storage location is also available when defining a back up location for workloads. For more information, see Viewing and updating public cloud backup locations.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.