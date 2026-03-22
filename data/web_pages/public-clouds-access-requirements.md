# Access requirements needed to backup to public cloud storage

Managing the backup and recovery of workloads and files > Backing up workloads to public clouds > Managing public cloud account access > Access requirements needed to backup to public cloud storage
Access requirements needed to backup to public cloud storage

When directly backing up to public cloud storage services, there are a number of access requirements to consider for each platform:

Microsoft Azure
Amazon S3
S3 compatible storage (includes Wasabi, IONOS Cloud, and Impossible Cloud)
Backing up to Microsoft Azure

To connect to a Microsoft Azure subscription, you must have several permissions. For more information about them, see article Microsoft Azure connection security and audit (72684).

You must be assigned with one of the following roles in Microsoft Azure AD in order to complete the connection to the subscription: Cloud Application Administrator, Application Administrator, or Global Administrator. You must also be assigned the Owner role for each selected subscription.
Backing up to Amazon S3

When you back up to Amazon S3, there are several requirements when defining Amazon S3 backup locations:

Supported storage classes
Policy permissions
Access keys
Bucket settings
Supported storage classes

The following Amazon S3 storage classes are currently supported:

S3 Standard

Standard - Infrequent Access (S3 Standard-IA)

One Zone - Infrequent Access (S3 One Zone-IA)

S3 Intelligent Tiering

Policy permissions

When you back up to Amazon S3, your Amazon account must have the minimum permissions applied to ensure Cyber Protect Cloud can back up the relevant workloads to Amazon S3. This means that the relevant users should have access to the AWS Management Console, and have the relevant policy applied to the group(s) they are assigned to.

The policy permissions specified for Amazon S3 can be re-used by other S3 compatible storage services. For more information, see Backing up to S3 compatible storage (includes Wasabi, IONOS Cloud, and Impossible Cloud).

Examples

The following example policy shows the minimum set of permissions for a wide scope of resources, when backing up and recovering to/from a specific bucket (indicated by [BUCKETNAME]). Note that * indicates all resources.

{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"s3:ListAllMyBuckets",
"s3:GetBucketLocation",
"s3:GetBucketObjectLockConfiguration",
"s3:GetBucketVersioning"
],
"Resource": "arn:aws:s3:::*"
},
{
"Effect": "Allow",
"Action": [
"s3:ListBucket",
"s3:ListBucketVersions"
],
"Resource": "arn:aws:s3:::[BUCKETNAME]"
},
{
"Effect": "Allow",
"Action": "sts:GetFederationToken",
"Resource": "*"
},
{
"Effect": "Allow",
"Action": [
"s3:PutObject",
"s3:GetObject",
"s3:DeleteObject",
"s3:GetObjectVersion",
"s3:GetObjectRetention",
"s3:PutObjectRetention"
],
"Resource": "arn:aws:s3:::[BUCKETNAME]/*"
}
]
}

The following example policy shows the minimum permissions for any bucket in the account. Note that [BUCKETNAME] should be replaced with the name of the bucket.

{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"s3:ListAllMyBuckets",
"s3:GetBucketLocation",
"s3:GetBucketObjectLockConfiguration",
"s3:GetBucketVersioning"
],
"Resource": "arn:aws:s3:::*"
},
{
"Effect": "Allow",
"Action": [
"s3:ListBucket",
"s3:ListBucketVersions"
],
"Resource": "arn:aws:s3:::*"
},
{
"Effect": "Allow",
"Action": "sts:GetFederationToken",
"Resource": "*"
},
{
"Effect": "Allow",
"Action": [
"s3:PutObject",
"s3:GetObject",
"s3:DeleteObject",
"s3:GetObjectVersion",
"s3:GetObjectRetention",
"s3:PutObjectRetention"
],
"Resource": "arn:aws:s3:::*"
}
]
}
Access keys

Access keys are required for each Amazon S3 connection, and are used when defining the Amazon S3 connection. For more information about generating access keys and access key IDs, see the Amazon S3 documentation.

Bucket settings

When using Amazon S3 buckets as the backup location, ensure that the bucket is configured with the default settings, including the blocking of all public access (by default this is set to On). For more information about working with buckets, see the Amazon S3 documentation.

The examples in Policy permissions include a full set of permissions. If you do not need immutability on a bucket, you can exclude the related permissions, such as the s3:GetBucketObjectLockConfiguration (which is used to create and edit the backup location) and s3:GetObjectRetention (which is used to detect the need to update the object lock for a reduced period) permissions.
Backing up to S3 compatible storage (includes Wasabi, IONOS Cloud, and Impossible Cloud)

When you backup to S3 compatible storage, there are a number of requirements you need to consider when defining backup locations:

Policy permissions
Access keys
Bucket settings
Policy permissions

When you define a backup location in S3 compatible storage, ensure that the relevant policies are applied to the relevant groups and users.

The policy permissions specified for Amazon S3 (see above) can be re-used by other S3 compatible storage services. Note that the sts:GetFederationToken permission is only applicable to Amazon S3 and is not required for other S3 compatible storage services.
When the connection to Wasabi is created for the first time, temporary credentials created with the AssumeRole permission are used. This results in additional access permissions, meaning that even if there are permissions in the Wasabi policy which restrict working with specific buckets, these buckets will still be shown in the available dropdown list of buckets. Backup and recovery operations will work with any bucket selected from the list.

However, the access token provided to the agent during backup/recovery operations is limited to operations to one specific bucket only - the bucket selected when creating the backup location on Wasabi in the Cyber Protect console. As a result, after the backup location is created, the system will limit agent operations to the selected bucket only.

Examples

The following example policy is for Wasabi only and shows the minimum permissions for any bucket in the account.

{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"s3:ListAllMyBuckets",
"s3:GetBucketLocation",
"s3:GetBucketObjectLockConfiguration",
"s3:GetBucketVersioning"
],
"Resource": "*"
},
{
"Effect": "Allow",
"Action": [
"s3:ListBucket",
"s3:ListBucketVersions"
],
"Resource": "*"
},
{
"Effect": "Allow",
"Action": [
"iam:CreateRole",
"iam:AttachRolePolicy",
"sts:GetCallerIdentity",
"sts:AssumeRole"
],
"Resource": "*"
},
{
"Effect": "Allow",
"Action": [
"s3:PutObject",
"s3:GetObject",
"s3:DeleteObject",
"s3:GetObjectVersion",
"s3:GetObjectRetention",
"s3:PutObjectRetention"
],
"Resource": "*"
}
]
}

The following example policy is for S3 compatible, IONOS Cloud, and Impossible Cloud storage, and shows limited permissions with a limited scope of resources. Note that [BUCKETNAME] should be replaced with the name of the bucket.

{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"s3:ListAllMyBuckets",
"s3:GetBucketLocation",
"s3:GetBucketObjectLockConfiguration",
"s3:GetBucketVersioning"
],
"Resource": "arn:aws:s3:::*"
},
{
"Effect": "Allow",
"Action": [
"s3:ListBucket",
"s3:ListBucketVersions"
],
"Resource": "arn:aws:s3:::[BUCKETNAME]"
},
{
"Effect": "Allow",
"Action": [
"s3:PutObject",
"s3:GetObject",
"s3:DeleteObject",
"s3:GetObjectVersion",
"s3:GetObjectRetention",
"s3:PutObjectRetention"
],
"Resource": "arn:aws:s3:::[BUCKETNAME]/*"
}
]
}

The following example policy is for S3 compatible, IONOS Cloud, and Impossible Cloud storage, and shows the minimum permissions for any bucket in the account.

{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"s3:ListAllMyBuckets",
"s3:GetBucketLocation",
"s3:GetBucketObjectLockConfiguration",
"s3:GetBucketVersioning"
],
"Resource": "arn:aws:s3:::*"
},
{
"Effect": "Allow",
"Action": [
"s3:ListBucket",
"s3:ListBucketVersions"
],
"Resource": "arn:aws:s3:::*"
},
{
"Effect": "Allow",
"Action": [
"s3:PutObject",
"s3:GetObject",
"s3:DeleteObject",
"s3:GetObjectVersion",
"s3:GetObjectRetention",
"s3:PutObjectRetention"
],
"Resource": "arn:aws:s3:::*"
}
]
}
Access keys

Access keys are required for each S3 compatible connection, and are used when defining the connection.

Note that access keys for root user accounts on Wasabi cannot be used because AssumeRole cannot be called by root users. You should create a separate non-root user and generate access keys for that user.

For more information about generating access keys and access key IDs, see the relevant documentation. For example, see the Wasabi documentation, IONOS Cloud documentation, and Impossible Cloud documentation.

Bucket settings

When using buckets as the backup location, ensure that the bucket is configured with the default settings. For more information about working with buckets, see the relevant documentation. For example, see the Wasabi documentation, IONOS Cloud documentation, or Impossible Cloud documentation.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.