# Defining a backup location in Amazon S3

Managing the backup and recovery of workloads and files > Backing up workloads to public clouds > Defining a backup location in Amazon S3
Defining a backup location in Amazon S3
To configure backup locations on Amazon S3, you must have one of the following roles defined in the Cyber Protection service: Company administrator, User, Cyber administrator.


To back up a workload to Amazon S3, you must define the Amazon S3 backup location in the Cyber Protect console, and then connect to the relevant Amazon S3 connection. You can do this in the following ways:

When creating or editing a protection plan.
When defining and managing backup storage locations.
Both administrators and non-administrator users can back up workloads to Amazon S3.

Non-administrator users can add access to an Amazon S3 connection (see Managing access to other public cloud storage services), but can only apply protection plans where the backup location is connected to the Amazon S3 connection they added themselves, and for workloads registered in the Cyber Protect console under their name.

Administrators can apply protection plans where the backup location is connected to Amazon S3 connections they added themselves or to subscriptions added by any other administrator, and for workloads registered in the Cyber Protect console under any user.

To define a backup location in Amazon S3

In the Cyber Protect console, do one of the following:

If you are creating or editing a protection plan, go to Devices, and then select the workload that you want to back up to Amazon S3. In the Backup section of the selected workload's protection plan, click the link in the Where to back up row.

For more information about working with protection plans, see Protection plans and modules.

If you are managing your backup storage locations and want to add Amazon S3 as a new location, go to Backup storage.

For more information about managing your backup storage locations, see Backup storage.

Click Add location.

From the Public clouds dropdown list, select Amazon S3.

Buckets in special Government Cloud regions (for example, us-gov-west-1) are not supported as backup locations.

If the relevant Amazon S3 connection is already registered in the Cyber Protect console, select it from the list.

If the relevant connection is not registered in the Cyber Protect console, click Add new connection. For more information about adding and defining access to an Amazon S3 connection, see Adding access to a public cloud connection. When the connection is added, continue to the next step.

Define the following:

In the Location name field, enter the name of the backup location.

The location name must be unique to the customer tenant. If the name you add already exists in the connection, Acronis adds a suffix number to the name. For example, if Amazon S3 storage already exists, the name will be automatically updated to Amazon S3 storage 1.

In the Storage Class field, select from one of the following supported storage classes:

S3 Standard
Standard - Infrequent Access (S3 Standard-IA)
One Zone - Infrequent Access (S3 One Zone-IA)

S3 Intelligent Tiering

When using the S3 Intelligent Tiering storage class, older backup objects can be automatically moved to the “Archive Access” or “Deep Archive Access” tiers (for more information about these tiers, see the Amazon S3 documentation). Objects in these tiers cannot be accessed instantly and require “rehydration”, which means that when you try to perform recovery from these old backups, recovery will fail. To successfully perform recovery from these backups, first retrieve the old objects from the relevant archive tiers. For more information about data retrieval from archive tiers, see the Amazon S3 documentation.

In the Bucket field, select the relevant Amazon S3 bucket.

If the selected bucket is enabled with the Object Lock and Object Versioning features (which are enabled in the AWS Management Console), the Backup immutability period (days) checkbox is enabled. You can then define the number of days for the immutability period, which ensures that backed up data is not deleted during this period, and is applied to all backup objects created by Acronis.

Note that when you set the immutability period as a backup location property, the default retention period defined for the bucket in the AWS Management Console is ignored. For more information about the Object Lock feature and retention periods, see the Amazon S3 documentation.

It is recommended that you configure the Lifecycle policy for the bucket if you have set the immutability option when creating the backup location. Buckets with the Object Versioning and Object Lock features enabled will store object versions forever, resulting in storage consumption growing indefinitely unless a Lifecycle policy is configured.

However, enabling the Object Versioning and Object Lock features is not recommended for buckets used by backup locations and which are configured without the immutability option. If Lifecycle policies are applied to these buckets, they can accidentally delete objects related to the backup archive chain, resulting in archive corruption.

With the immutability option configured, the issue is resolved by adjusting the immutability period for old objects, which the newer backup objects still have dependencies on. This happens automatically with each scheduled backup, where the immutability period of each object belonging to the backup chain is extended by the backup agent communicating with the cloud storage. This immutability period is never less than the immutability period days value defined during the creation of the backup location. For more information on how to configure the Lifecycle policy, refer to the Amazon S3 documentation.
Agents prior to version 24.05 can perform backups to Amazon S3, but only agents from version 24.05 or higher will apply Object Lock to objects created in Amazon S3 storage. This means that only newer agents can acknowledge the immutability period set as a backup location property, and will manage this period for all created backups. Agents prior to version 24.05 will ignore this setting and the default bucket Object Lock properties (defined in the AWS Management Console or via API) are applied to the created objects in Amazon S3.

Click Add.

If you are creating or editing a protection plan, the Amazon S3 backup location is set as the location in the Where to back up row. When the backup is run (either manually or when scheduled), the backup is saved in the defined location.

If you are managing your backup storage locations, you can view and update the location details as required. The Amazon S3 location is also available when defining a backup location for workloads. For more information, see Viewing and updating public cloud backup locations.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.