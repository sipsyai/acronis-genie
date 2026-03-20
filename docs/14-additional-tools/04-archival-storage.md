---
title: "Archival Storage"
section: "Additional Cyber Protection Tools"
subsection: "Archival Storage"
page_range: "1489-1496"
tags: [archival-storage, s3-compatible, object-storage, versioning, object-locking, worm, retention-policy, lifecycle-policy, buckets, access-keys]
acronis_version: "26.02"
---

# Archival Storage

Archival storage is secure, scalable, and cost-efficient object storage for long-term data retention. You can use it for data that must meet compliance requirements or for data that is rarely accessed but must be retained.

> **Note:** You cannot use archival storage as a backup destination in a protection plan or a cloud-to-cloud backup plan.

To use archival storage, you must create one or more buckets in the Cyber Protect console. To access the buckets, view and manage their contents, or transfer data, you must use an S3-compatible client. Archival storage requires that the **Archival storage** quota is enabled in Management Portal.

## S3-Compatible Features

Archival storage is S3-compatible and supports standard S3 features.

### Versioning

You can enable versioning at the bucket level:

- In a **versioned bucket**, multiple versions of an object can exist. A new version is created when an object is uploaded, overwritten, or deleted. For example, when an object is deleted, it is not physically removed from the storage. Instead, a delete marker is added to the current object version, and the previous version remains accessible.
- In an **unversioned bucket**, each object has only one version at a time. Overwrites and deletions are permanent.

Versioning prevents accidental or malicious deletion, or overwriting of objects, but it results in increased storage space. To trim a versioned bucket, you can use a lifecycle policy. Versioning is automatically enabled when you enable object locking.

### Access Mode

In archival storage, you can control data access and security by configuring buckets as public or private:

- **Public mode** makes a bucket and its contents available to anyone who has the correct URL. You can use this mode to share non-sensitive files.
- **Private mode** restricts bucket access to authorized users. You can use this mode for sensitive or business-critical data.

### Object Locking

Object locking enables Write-Once Read-Many (WORM) capabilities for buckets. With it, you can configure a bucket where data can be written and read, but it cannot be deleted or overwritten. Object locking is only available for versioned buckets.

You can configure the object locking setting only when you create a bucket, and it cannot be changed it later.

To achieve object immutability, you must add a retention policy (retention mode and retention period) to the object locking capabilities. In the Cyber Protect console, you can configure a retention policy at the bucket level, so that all objects in that bucket use the same retention mode and period. Configuring a retention policy at the bucket level is optional.

### Retention Policy

A retention policy ensures object immutability by preventing object versions from being deleted during a specified period. This feature is commonly used to meet regulatory compliance requirements, or to protect critical data from accidental or unauthorized deletion.

In the Cyber Protect console, you can configure a retention policy at the bucket level. The policy applies to all objects placed in the bucket. You can configure a retention policy during bucket creation or later, when you edit a bucket.

> **Note:** Configuring a retention policy requires that object locking is enabled for the bucket.

A retention policy consists of:

- **Retention period** -- A fixed duration of between 1 day to 100 years, during which an object version remains locked. The retention period applies to individual object versions -- different versions of the same object can have different retention durations.
- **Retention mode**:
  - **Governance mode** -- Object versions are protected from deletion or modification by most users. However, users with special permissions can override retention settings, if necessary. This mode is useful for testing retention policies before enforcing them under compliance mode.
  - **Compliance mode** -- Object versions cannot be deleted or overwritten by any user, including administrators. Retention mode cannot be changed, and retention period cannot be shortened. This mode is used to enforce strict regulatory compliance.

### Lifecycle Policy

A lifecycle policy automatically deletes objects that you no longer need. You can configure a lifecycle policy at the bucket level for the following types of objects:

- **Current versions of objects** -- In a versioned bucket, the current version of the object is marked as deleted after the specified period. Previous (non-current) versions remain available. In a non-versioned bucket, the object is permanently deleted after the specified period.
- **Non-current versions of objects** -- After the specified period, these versions are permanently deleted. This option provides efficient management of the used storage space.

> **Note:** Lifecycle policies cannot override retention policies. If an object is protected by a retention period, it cannot be deleted until that period expires. However, you can configure a lifecycle policy with a duration longer than the retention period, ensuring that objects are automatically deleted after they are no longer protected.

## Managing Buckets in Archival Storage

You can manage your buckets in the Cyber Protect console.

### Generating an Access Key Pair

An access key pair is used to authenticate third-party applications that can access the archival storage. For example, you need a key pair to configure an S3-compatible client.

An access key pair consists of:
- Access key ID
- Secret access key

You can only use the access key pair with a specific endpoint URL. For example: `s3-us-central-2.acronis.storage`. This URL depends on the data center location for your account, and you cannot change it.

> **Important:** You can see, copy, or download the access key ID, secret access key, and endpoint URL only when you generate the access key pair. If you lose or forget this data, you cannot retrieve it, and you must generate a new key pair. Generating a new key pair automatically disables the previous one.

### Creating Buckets

1. In the Cyber Protect console, go to **Backup storage** > **Archival storage**.
2. Click **Add bucket**.
3. Specify the bucket name. The bucket name must be globally unique. It must contain between 3 and 63 characters, and can include lowercase letters (a-z from the English alphabet), digits (0-9), hyphens, and dots. It cannot start with a hyphen or a dot.
4. Under **Access mode**, select **Public** or **Private**.
5. Under **Versioning**, select **Enable** or **Disable**. If you create an unversioned bucket, you can enable versioning at any time. If you create a versioned bucket, you cannot disable versioning, but you can suspend it.
6. Under **Object locking**, select **Enable** or **Disable**. You cannot change this setting later. Object locking is only available for versioned buckets and is a prerequisite for a retention policy.
7. Click **Add**.

### Viewing Buckets

1. Log in to the Cyber Protect console.
2. Go to **Backup storage** > **Archival storage**.

### Editing Buckets

You can edit a bucket to modify the following properties:
- Access mode
- [Only for versioned buckets where object locking is enabled] Retention policy
- Lifecycle policy

### Changing the Access Mode

1. In the Cyber Protect console, go to **Backup storage** > **Archival storage**.
2. Click the bucket that you want to edit.
3. On the **Bucket** tab, select the access mode.
4. Click **Save**.

### Configuring a Retention Policy

1. In the Cyber Protect console, go to **Backup storage** > **Archival storage**.
2. Click the bucket that you want to edit.
3. On the **Object locking** tab, turn on the **Retention** switch.
4. In **Retention mode**, select the mode.

   > **Warning!** In compliance mode, objects cannot be deleted during their retention period by any user, including administrators.

5. In **Retention period**, specify the period in days or years (between 1 day and 100 years).
6. Click **Save**.

### Configuring a Lifecycle Policy

1. In the Cyber Protect console, go to **Backup storage** > **Archival storage**.
2. Click the bucket that you want to edit.
3. On the **Lifecycle** tab, turn on the **Lifecycle** switch.
4. [For versioned buckets] Select the versions to which you want to apply the lifecycle policy.
5. Configure the period after which the lifecycle policy will be applied to the objects in the bucket.

   > **Note:** A lifecycle policy will not be applied to objects in retention. Configure a lifecycle period that is longer than the retention period for the objects that you want to delete.

6. Click **Save**.

### Deleting Buckets

**Prerequisites:** The bucket is empty.

> **Note:** You cannot delete an object from the bucket until the retention period for that object expires.

1. In the Cyber Protect console, go to **Backup storage** > **Archival storage**.
2. Select the checkbox for the buckets that you want to delete.
3. Click **Delete**.
4. Select the checkbox to confirm your choice.
5. Enter your login to confirm your account.
6. Click **Delete**.

## Accessing Archival Storage via Third-Party Clients

You can manage the objects in archival storage by using an S3-compatible client. Popular options include:

- Cyberduck
- S3 Browser
- Mountain Duck
- Rclone

With an S3-compatible client, you can perform the following actions:
- Upload files to a bucket
- Create folders in a bucket
- Download files or folders to local storage
- Delete files and folders from a bucket

> **Note:** Archival storage supports object names that include alphanumeric and special characters. Check the documentation of your S3-compatible client for any restrictions on object naming.

To access archival storage, you must provide:
- Access key ID
- Secret access key
- Object Storage S3 endpoint (e.g., `s3-us-central-2.acronis.storage`)
- [If not automatically populated] Port -- Archival storage supports port 443 with TLS v1.2 or later

> **Important:** The access key ID, secret access key, and the endpoint URL are displayed only when you create a new access key pair. Copy or download these items as a CSV file. If you lose them, create a new key pair and reconfigure your S3-compatible client.

> **Note:** S3-compatible clients must use path-style URLs. For example:
> `https://s3-eu-central-1.acronis.storage/mybucket/myfolder/file.txt`
>
> Virtual-hosted-style URLs are not supported. For example:
> `https://mybucket.s3-eu-central-1.acronis.storage/myfolder/file.txt`
