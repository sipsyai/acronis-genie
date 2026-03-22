# Defining a backup location in Microsoft Azure

Managing the backup and recovery of workloads and files > Backing up workloads to public clouds > Defining a backup location in Microsoft Azure
Defining a backup location in Microsoft Azure
To configure backup locations in Microsoft Azure, you must have one of the following roles defined in the Cyber Protection service: Company administrator, User, Cyber administrator.

You can define backup locations on the Microsoft Azure Blob Storage service, under one of the following Microsoft Azure Storage account types:

Standard general purpose v2 (StorageV2)
Premium block blobs

To learn more about the Microsoft Azure Storage account types, see the Microsoft documentation.

To back up a workload to Microsoft Azure, you need to define the Microsoft Azure backup location in the Cyber Protect console, and connect to the relevant Microsoft Azure subscription. This can be done in the following ways:

When creating or editing a protection plan.
When defining and managing backup storage locations.
Both administrators and non-administrator users can back up workloads to Microsoft Azure.

Non-administrator users can add access to a Microsoft Azure subscription (see Managing access to Microsoft Azure subscriptions), but can only apply protection plans where the backup location is connected to the Microsoft Azure subscription they added themselves, and for workloads registered in the Cyber Protect console under their name.

Administrators can apply protection plans where the backup location is connected to Microsoft Azure subscriptions they added themselves or to subscriptions added by any other administrator, and for workloads registered in the Cyber Protect console under any user.

To define a backup location in Microsoft Azure

In the Cyber Protect console, do one of the following:

If you are creating or editing a protection plan, go to Devices and select the relevant workload you want to back up to Microsoft Azure. In the Backup section of the selected workload's protection plan, click the link in the Where to back up row.

For more information about working with protection plans, see Protection plans and modules.

If you are managing your backup storage locations and want to add Microsoft Azure as a new location, go to Backup storage.

For more information about managing your backup storage locations, see Backup storage.

Click Add location.

From the Public clouds drop-down list, select Microsoft Azure.

If the relevant Microsoft Azure subscription is already registered in the Cyber Protect console, select it from the list of subscriptions.

If the relevant subscription is not registered in the Cyber Protect console, click Add and in the displayed dialog, click Sign in. You are redirected to the Microsoft login page. For more information about adding and defining access to a Microsoft Azure subscription, see Adding access to a Microsoft Azure subscription.

In the Storage account field, select the relevant account.

Only Microsoft Azure storage accounts with regular endpoint suffixes that contain core.windows.net are currently supported.

The Location name and Access tier fields are automatically filled by default, according to the storage account selected. The location name displayed is microsoft_azure_[storage account] and the access tier selected is Default (Hot). Both fields can be modified, as required.

Only the Hot and Cool access tiers are currently supported (for more information about access tiers, see the Microsoft documentation).
When changing the location name, enter a unique location name (the name must be unique to the customer tenant). If the name you add already exists in the storage account, Acronis adds a suffix number to the name. For example, if Microsoft Azure Storage already exists, the name is automatically updated to Microsoft Azure Storage_01.

Click Add.

If you are creating or editing a protection plan, the Microsoft Azure backup location is set as the location in Where to back up row. When the backup is run (either manually or when scheduled), the backup is saved in the defined location.

If you are managing your backup storage locations, you can view and update the location details as required. The Microsoft Azure location is also available when defining a backup location for workloads. For more information, see Viewing and updating public cloud backup locations.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.