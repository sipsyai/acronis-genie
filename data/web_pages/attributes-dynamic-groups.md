# Search attributes for non-cloud-to-cloud workloads

Managing workloads in the Cyber Protect console > Device groups > Creating a dynamic group > Search attributes for non-cloud-to-cloud workloads
Search attributes for non-cloud-to-cloud workloads

The following table summarizes the attributes that you can use in your search queries for non-cloud-to-cloud workloads.

To see which attributes you can use in search queries for cloud-to-cloud workloads, see Search attributes for cloud-to-cloud workloads.

Attribute	Meaning	Search query examples	Supported for group creation
General


name



Workload name, such as:

Host name for physical machines
Name for virtual machines
Database name
Email address for mailboxes


name = 'en-00'

Yes


id



Device ID.

To see the device ID, under Devices, select the device, click Details > All properties.

The ID is shown in the id field.



id != '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

Yes


resourceType



Workload type

Possible values:

'machine'
'exchange'
'mssql_server'
'mssql_instance'
'mssql_database'
'mssql_database_folder'
'msexchange_database'
'msexchange_storage_group'
'msexchange_mailbox.msexchange'
'msexchange_mailbox.office365'
'mssql_aag_group'
'mssql_aag_database'
'virtual_machine.vmww'
'virtual_machine.vmwesx'
'virtual_host.vmwesx'
'virtual_cluster.vmwesx'
'virtual_appliance.vmwesx'
'virtual_application.vmwesx'
'virtual_resource_pool.vmwesx'
'virtual_center.vmwesx'
'datastore.vmwesx'
'datastore_cluster.vmwesx'
'virtual_network.vmwesx'
'virtual_data_center.vmwesx'
'virtual_machine.vmww'
'virtual_cluster.mshyperv'
'virtual_machine.mshyperv'
'virtual_network.mshyperv'
'virtual_folder.mshyperv'
'virtual_data_center.mshyperv'
'datastore.mshyperv'
'virtual_machine.msvs'
'virtual_machine.parallelsw'
'virtual_cluster.parallelsw'
'virtual_machine.rhev'
'virtual_machine.kvm'
'virtual_machine.xen'
virtual_machine.vcd
virtual_machine.ovirt
virtual_machine.azure
virtual_machine.nutanix
'bootable_media'


resourceType = 'machine'

resourceType in ('virtual_center.vmwesx', 'machine')

Some resource types, such as MS SQL and MS Exchange, might be accounted for as resource groups. If your search or dynamic group query does not return the expected results, try adding the prefix group. at the beginning of the resource name. See Workload Group type.


Yes




Workload Group type

Possible values:

`group.computers`
`group.mssql_server`
`group.mssql_instance`
`group.mssql_system_databases`
`group.mssql_database`
`group.mssql_aag_group`
`group.mssql_aag_replica`
`group.mssql_aag_database`
`group.msexchange_cluster`
`group.msexchange_server`
`group.msexchange_cas`
`group.msexchange_online_server`
`group.msexchange_infostore`
`group.msexchange_storage_group`
`group.msexchange_database`
`group.msexchange_mailboxes`
`group.social_resources`
`group.all`
`group.all_vcd_vms`
`group.vcd`
`group.vcenter`
`group.ovirt_vengine`
`group.veil_vengine`
`group.nutanix_vengine`
`group.datacenter`
`group.hosts_and_clusters`
`group.cluster`
`group.host`
`group.virtual_application`
`group.resource_pool`
`group.virtual_folder`
`group.vms_and_templates`
`group.vms_folder`
`group.virtual_project`
`group.nas_devices`
`group.vcd_organization`
`group.vcd_organizations`
`group.azure`
`group.azure_subscriptions`
`group.azure_subscription`
`group.azure_resource_group`
`group.azure_all_devices`
`group.externalrmm`
`group.mail_servers`


resourceType = 'group.mssql_server'

resourceType in ('group.mssql_database', 'group.msexchange_database')



Yes


chassis

Chassis type.

Possible values:

laptop
desktop
server
other
unknown
chassis = 'laptop'

chassis IN ('laptop', 'desktop')

Yes


ip

IP address (only for physical machines).

ip RANGE ('10.250.176.1','10.250.176.50')

Yes


comment



Comment for a device. It can be specified automatically or manually.

Default value:

For physical machines running Windows, the computer description in Windows is automatically copied as a comment. This value is synchronized every 15 minutes.

Empty for other devices.
The automatic synchronization is disabled if there is manually added text in the comment field. To enable the synchronization again, clear this text.

To refresh the automatically synchronized comments for your workloads, restart the Managed Machine Service in Windows Services or run the following commands at the command prompt:

net stop mms
net start mms

To view a device comment, under Devices, select the device, click Details, and then locate the Comment section.

To add or change a comment manually, click Add or Edit.

For devices on which a protection agent is installed, there are two separate comment fields:

Agent comment

For physical machines running Windows, the computer description in Windows is automatically copied as a comment. This value is synchronized every 15 minutes.

Empty for other devices.
The automatic synchronization is disabled if there is manually added text in the comment field. To enable the synchronization again, clear this text.

Device comment

If the agent comment is specified automatically, it is copied as a device comment. Manually added agent comments are not copied as device comments.
Device comments are not copied as agent comments.

A device can have one or both of these comments specified, or have the both of them blank. If the both comments are specified, the device comment has priority.

To view an agent comment, under Settings > Agents, select the device with the agent, click Details, and then locate the Comment section.

To view a device comment, under Devices, select the device, click Details, and then locate the Comment section.

To add or change a comment manually, click Add or Edit.



comment = 'important machine'

comment = '' (all machines without a comment)

Yes
isOnline

Workload availability.

Possible values:

true
false
isOnline = true	No
hasAsz

Secure Zone availability.

Possible values:

true
false
hasAsz = true	Yes
tzOffset

Timezone offset from Coordinated Universal Time (UTC), in minutes.



tzOffset = 120

tzOffset > 120

tzOffset < 120

Yes
CPU, memory, disks
cpuArch

CPU architecture.

Possible values:

'x64'
'x86'
cpuArch = 'x64'	Yes
cpuName	CPU name.	cpuName LIKE '%XEON%'	Yes


memorySize

RAM size in megabytes.

memorySize < 1024

Yes
diskSize	Hard drive size in gigabytes or megabytes (only for physical machines).	diskSize < 300GB

diskSize >= 3000000MB

No
Operating system


osName

Operating system name.

osName LIKE '%Windows XP%'

Yes


osType



Operating system type.

Possible values:

'windows'
'linux'
'macosx'


osType = 'windows'

osType IN ('linux', 'macosx')

Yes
osArch

Operating system architecture.

Possible values:

'x64'
'x86'
cpuArch = 'x86'	Yes


osProductType



Operating system product type.

Possible values:

'dc'

Stands for Domain Controller.

When the domain controller role is assigned on a Windows server, the osProductType changes from server to dc. Such machines will be not included in the search results for osProductType='server'.

'server'
'workstation'


osProductType = 'server'

Yes
osSp	Service pack of the operating system.	osSp = 1	Yes
osVersionMajor	Major version of the operating system.	osVersionMajor = 1	Yes
osVersionMinor	Minor version of the operating system.	osVersionMinor > 1	Yes
Agent


agentVersion

Version of the installed protection agent.

agentVersion LIKE '12.0.*'

Yes


hostId



Internal ID of the protection agent.

To see the protection agent ID, under Devices, select the device, click Details > All properties. Check the id value of the agent property.



hostId = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

Yes
virtualType

Virtual machine type.

Possible values:

'vmwesx'

VMware virtual machines

'mshyperv'

Hyper-V virtual machines

'pcs'

Virtuozzo virtual machines

'hci'

Virtuozzo Hybrid Infrastructure virtual machines

'scale'

Scale Computing HC3 virtual machines

'ovirt'

oVirt virtual machines

'vcd'

VMware Cloud Director virtual machines

virtualType = 'vmwesx'	Yes


insideVm



Virtual machine with an agent inside.

Possible values:

true
false


insideVm = true

Yes
Location


tenant

The name of the tenant to which the device belongs.

tenant = 'Unit 1'

Yes


tenantId



The identifier of the tenant to which device belongs.

To see the tenant ID, under Devices, select the device, click Details > All properties. The ID is shown in the ownerId field.



tenantId = '3bfe6ca9-9c6a-4953-9cb2-a1323f454fc9'

Yes


ou

Devices that belong to the specified Active Directory organizational unit.

ou IN ('RnD', 'Computers')

Yes
customerUuid	Devices that belong to the specified Customer tenant ID.	customerUuid = 'd96c5dde-5466-489d-9c74-df7dbd8c2148'	No
Status


state



Device state.

Possible values:

'idle'
'interactionRequired'
'canceling'
'backup'
'recover'
'install'
'reboot'
'failback'
'testReplica'
'run_from_image'
'finalize'
'failover'
'replicate'
'createAsz'
'deleteAsz'
'resizeAsz'


state = 'backup'

No
status

Protection status.

Possible values:

ok
warning
error
critical
protected
notProtected


status = 'ok'

status IN ('error', 'warning')

No


protectedByPlan



Devices that are protected by a protection plan with a given ID.

To see the plan ID, in Management > Protection plans, select a plan, click the bar in the Status column, and then click the status name. A new search with the plan ID will be created.



protectedByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

No


okByPlan

Devices that are protected by a protection plan with a given ID and have an OK status.

okByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

No


errorByPlan

Devices that are protected by a protection plan with a given ID and have an Error status.

errorByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

No


warningByPlan

Devices that are protected by a protection plan with a given ID and have a Warning status.

warningByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

No


runningByPlan

Devices that are protected by a protection plan with a given ID and have a Running status.

runningByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

No


interactionByPlan

Devices that are protected by a protection plan with a given ID and have an Interaction Required status.

interactionByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'

No


lastBackupTime*



The date and time of the last successful backup.

The format is 'YYYY-MM-DD HH:MM'.



lastBackupTime > '2023-03-11'

lastBackupTime <= '2023-03-11 00:15'

lastBackupTime is null

No


lastBackupTryTime*



The time of the last backup attempt.

The format is 'YYYY-MM-DD HH:MM'.



lastBackupTryTime >= '2023-03-11'

No


nextBackupTime*



The time of the next backup.

The format is 'YYYY-MM-DD HH:MM'.



nextBackupTime >= '2023-08-11'

No
lastVAScanTime*

The date and time of the last successful vulnerability assessment.

The format is 'YYYY-MM-DD HH:MM'.

lastVAScanTime > '2023-03-11'

lastVAScanTime <= '2023-03-11 00:15'

lastVAScanTime is null

Yes
lastVAScanTryTime*

The time of the last vulnerability assessment attempt.

The format is 'YYYY-MM-DD HH:MM'.

lastVAScanTimeTryTime >= '2022-03-11'	Yes
nextVAScanTime*

The time of the next vulnerability assessment.

The format is 'YYYY-MM-DD HH:MM'.

nextVAScanTime <= '2023-08-11'	Yes
network_status

Network isolation status for Endpoint detection and response (EDR).

Possible values:

connected

isolated

network_status= 'connected'	Yes

If you skip the hour and minutes value, the start time is considered to be YYYY-MM-DD 00:00, and the end time is considered to be YYYY-MM-DD 23:59:59. For example, lastBackupTime = 2023-01-20, means that the search results will include all backups from the interval
lastBackupTime >= 2023-01-20 00:00 and lastBackupTime <= 2023-01-20 23:59:59.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.