---
title: "API error codes"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/error-codes.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:45.475023"
---

# API error codes

API error codes
The API errors are split into several domains that allow to identify the source of the error. The following table provides the description of the domains:






Domain
Description



DisasterRecovery
The error occurred in the Disaster Recovery service.

RunVMAgent
The error occurred in the agent running on the virtual machine.

RunVMAgentGateway
The error occurred in the gateway service that serves the agent’s requests.



Additionally, Disaster Recovery may provide an information about the error that occurred for the resource in the _issues key of the response body. For example:
HTTP/1.1 400 Bad Request
<...>

{"items":[{...,"_issues":[{"domain":"DisasterRecovery","target":"75c45087-0ba7-4580-8de8-1be489b7591d","severity":"WARNING","error":{"code":"VPNS2SApplianceNotRegistered","domain":"DisasterRecovery","message":"The VPN appliance is not registered."}}],"_links":[...]}],"paging":{...}}
The following table provides the description of error codes returned by Disaster Recovery in the error.code key:







Domain
Error code
Description



RunVMAgentGateway
ArchiveNotFound
The backup was not found. To check if the backup exists, open the Backup storage tab, select the cloud storage location, and then click Refresh.

RunVMAgentGateway
BadRequest
REST request is not correct.

RunVMAgentGateway
Conflict
REST request conflicts with object state.

RunVMAgentGateway
CredentialNotFound
The credentials were not found in the credentials store.

RunVMAgentGateway
InternalError
Internal error. Please try again later or contact support.

RunVMAgentGateway
NotAllowed
Method specified in REST request is not allowed.

RunVMAgentGateway
ObjectMissing
Object specified in REST request is missing.

RunVMAgentGateway
OperationTimeout
Operation timeout.

RunVMAgentGateway
TenantNotFound
The tenant was not found in the account server.

RunVMAgent
4KSectorDiskUnsupportedAsOSDisk
Your backup contains a 4K sector OS disk, which is not supported by Microsoft Azure.

RunVMAgent
4KSectorDiskUnsupportedInRegion
Your backup contains 4K sector hard disks, but Premium SSD v2, which supports 4K sector disks, is not available in the selected Azure region.

RunVMAgent
ArchiveCorrupted
The backup is corrupt. Create a new backup to the cloud storage or contact the Support team.

RunVMAgent
ArchiveEncrypted
Failover from encrypted backup failed. The encryption password in the recovery server settings is either missing or incorrect. Enter the correct encryption password and perform a failover again. Automated test failover will start according to its schedule.

RunVMAgent
ArchiveNotFound
The backup was not found. To check if the backup exists, open the Backup storage tab, select the cloud storage location, and then click Refresh.

RunVMAgent
ArchivePasswordNotFound
Missing credentials for encrypted backups. Please edit the recovery server settings and enter the backup encryption password.

RunVMAgent
BackupBlockedForAccount
The storage quota is exceeded.

RunVMAgent
BadTaskWorkload
Error while parsing the input data.

RunVMAgent
CertificateExpired
Internal error. Please try again later or contact support.

RunVMAgent
InvalidCertificate
Internal error. Please try again later or contact support.

RunVMAgent
CertificatePeerRejected
Internal error. Please try again later or contact support.

RunVMAgent
CertificateRevoked
Internal error. Please try again later or contact support.

RunVMAgent
CertificateUnknownCA
Internal error. Please try again later or contact support.

RunVMAgent
FilesystemCorrupted
The operation failed because the backup contains a corrupted file system. If you started the operation manually, try using another backup. If the operation was started automatically, wait for the system to retry. If this error persists, fix the file system on the source machine, create a new backup and retry the operation.

RunVMAgent
FilesystemIsUnsupported
The backup contains an unsupported file system or a file system cannot be detected. To check the supported file systems, see the documentation.

RunVMAgent
InputOutputError
Internal error. Please try again later or contact support.

RunVMAgent
MountFailed
Internal error. Please try again later or contact support.

RunVMAgent
NetworkError
Internal error. Please try again later or contact support.

RunVMAgent
NotEnoughFreeSpace
There is not enough free space on the System volume.

RunVMAgent
OperationCanceled
Internal error. Please try again later or contact support.

RunVMAgent
NoOperatingSystem
An operating system was not found in the backup. This might happen if the disk-level backup does not contain the boot partition or the operating system files are excluded in the backup settings.

RunVMAgent
OperatingSystemIsUnsupported
The backup contains an unsupported operating system or an operating system cannot be found. To check the supported operating systems and limitations, see the documentation.

RunVMAgent
UnsupportedVersionOfOSWindows
An unsupported version of Microsoft Windows is detected.

RunVMAgent
PartitionStructureIsUnsupported
The backup contains the unsupported volume type.

RunVMAgent
LDMPartitionStructureIsUnsupported
The backup contains unsupported dynamic disk volumes: LDM (Logical Disk Manager) or Storage Spaces. If this is a backup of a virtual machine, perform an agentless backup.

RunVMAgent
LVMPartitionStructureIsUnsupported
The backup contains an unsupported LVM (Logical Volume Manager) configuration. To check the supported Linux configurations and limitations, see the documentation.

RunVMAgent
MDPartitionStructureIsUnsupported
The backup contains an unsupported MD device (Linux software RAID array). To check the supported Linux configurations and limitations, see the documentation.

RunVMAgent
PortNotFound
The network port was not found.

RunVMAgent
ReachedLimitOfFileDescriptors
Internal error. Please try again later or contact support.

RunVMAgent
ServerNotFound
The virtual machine in the cloud was not found.

RunVMAgent
SliceNotFound
The backup was not found. To check if the backup exists, open the Backup storage tab, select the cloud storage location, and then click Refresh.

RunVMAgent
SNUMBD26KernelModuleNotLoaded
Internal error. Please try again later or contact support.

RunVMAgent
StorageQuotaExceeded
There is no free space on the cloud storage. Please upgrade your subscription. Otherwise, further backups will fail.

RunVMAgent
TimeoutError
Internal error. Please try again later or contact support.

RunVMAgent
UnhandledPanic
Internal error. Please try again later or contact support.

RunVMAgent
UnknownError
Internal error. Please try again later or contact support.

RunVMAgent
UnsupportedArchiveVersion
The backup version is not supported.

RunVMAgent
UnsupportedDiskSize
The backup contains VM disks with unsupported disk sizes. For details on the limitations, see the documentation.

RunVMAgent
UnsupportedSectorSize
The backup contains VM disks with unsupported sector sizes. For details on the limitations, see the documentation.

DisasterRecovery
BadRequest
The request has failed to pass validation against RAML schema.

DisasterRecovery
BaseDrNetworkLimitReached
With Disaster Recovery Standard, you can have only {{networksMaxNumber}} cloud networks. To have more cloud networks, contact your partner and activate the Disaster Recovery Advanced pack

DisasterRecovery
BaseDrTestFailoverLimitReached
With Disaster Recovery Standard, you cannot perform a test failover of more than {{testFailoverMaxNumber}} recovery servers at the same time. To perform a test failover of more than {{testFailoverMaxNumber}} recovery servers at the same time, contact your partner and activate the Disaster Recovery Advanced pack.

DisasterRecovery
CredentialNotFound
The credentials were not found in the credentials store.

DisasterRecovery
EntityNotFound
The requested entity is not found.

DisasterRecovery
FailoverCancellationAlreadyInProgress
Failover cancellation is already in progress.

DisasterRecovery
InternalError
Internal error. Please try again later or contact support.

DisasterRecovery
IpAddressAlreadyUsed
Another server already uses the specified IP {{address}}. Try another IP address.

DisasterRecovery
LogDownloadNotAllowed
You cannot download the log. ({{reason}})

DisasterRecovery
MacAddressAlreadyUsed
Another server already uses the specified MAC address: {{address}}. Try another MAC address.

DisasterRecovery
NetworkLimitReached
The maximum number ({{networksMaxNumber}}) of cloud networks is reached. To be able to add a network, remove one of the existing networks.

DisasterRecovery
NotAllowed
Method specified in REST request is not allowed.

DisasterRecovery
QuotaExceededBaseDR
There are no available compute points for testing the Disaster Recovery functionality. {{additionalComputePoints}} additional compute points will be added next month. To enable the complete functionality, contact your partner and activate the Disaster Recovery Advanced pack.

DisasterRecovery
QuotaExceededCloudServers
You have exceeded the “Cloud servers” quota. To increase the quota, contact the support team.

DisasterRecovery
QuotaExceededComputePoints
You have exceeded the “Compute points” quota. To increase the quota, contact the support team.

DisasterRecovery
QuotaExceededDrStorage
You have exceeded the “Disaster recovery storage” quota. To increase the quota, contact the support team.

DisasterRecovery
QuotaExceededPublicIp
You have exceeded the “Public IP addresses” quota. To increase the quota, contact the support team.

DisasterRecovery
QuotaReachedCloudServers
You have reached the “Cloud servers” quota. To increase the quota, contact the support team.

DisasterRecovery
QuotaReachedComputePoints
You have reached the “Compute points” quota. To increase the quota, contact the support team.

DisasterRecovery
QuotaReachedDrStorage
You have reached the “Disaster recovery storage” quota. To increase the quota, contact the support team.

DisasterRecovery
QuotaReachedPublicIp
You have reached the “Public IP addresses” quota. To increase the quota, contact the support team.

DisasterRecovery
ResourceBusy
The resource is busy, another task is currently in progress. Try again later.

DisasterRecovery
RunVmArchiveCorrupted
The backup is corrupt. Create a new backup to the cloud storage or contact the Support team.

DisasterRecovery
RunVmArchiveEncrypted
Failover from encrypted backup failed. The encryption password in the recovery server settings is either missing or incorrect. Enter the correct encryption password and perform a failover again. Automated test failover will start according to its schedule.

DisasterRecovery
RunVmArchiveNotFound
The backup was not found. To check if the backup exists, open the Backup storage tab, select the cloud storage location, and then click Refresh.

DisasterRecovery
RunVmArchivePasswordNotFound
Missing credentials for encrypted backups. Please edit the recovery server settings and enter the backup encryption password.

DisasterRecovery
RunVmCredentialsNotFound
The credentials were not found in the credentials store.

DisasterRecovery
RunVmFileSystemIsUnsupported
The backup contains an unsupported file system or a file system cannot be detected. To check the supported file systems, see the documentation.

DisasterRecovery
RunVmNotEnoughFreeSpace
There is not enough free space in the system volume.

DisasterRecovery
RunVmOsMissing
An operating system was not found in the backup. This might happen if the disk-level backup does not contain the boot partition or the operating system files are excluded in the backup settings.

DisasterRecovery
RunVmOsUnsupported
The backup contains an unsupported operating system or an operating system cannot be found. To check the supported operating systems and limitations, see the documentation.

DisasterRecovery
RunVmOsWindowsUnsupported
An unsupported version of Microsoft Windows is detected.

DisasterRecovery
RunVmPartitionStructureUnsupported
The backup contains the unsupported volume type.

DisasterRecovery
RunVmLDMPartitionStructureUnsupported
The backup contains unsupported dynamic disk volumes: LDM (Logical Disk Manager) or Storage Spaces. If this is a backup of a virtual machine, perform an agentless backup.

DisasterRecovery
RunVmLVMPartitionStructureUnsupported
The backup contains an unsupported LVM (Logical Volume Manager) configuration. To check the supported Linux configurations and limitations, see the documentation.

DisasterRecovery
RunVmMDPartitionStructureUnsupported
The backup contains unsupported MD (multiple devices) - Linux software RAID array volumes.

DisasterRecovery
RunVmServerNotFound
The virtual machine in the cloud was not found.

DisasterRecovery
RunVmSliceNotFound
The backup was not found. To check if the backup exists, open the Backup storage tab, select the cloud storage location, and then click Refresh.

DisasterRecovery
RunVmTenantNotFound
The tenant was not found in the account server.

DisasterRecovery
ServerNotFound
The server was not found.

DisasterRecovery
ServerNotReady
The operation is not applicable to cloud servers in this state.

DisasterRecovery
SiteNotReady
You cannot perform any operations because the DR site is being deployed or removed.

DisasterRecovery
SubscriptionNotFoundCloudServers
Your “Cloud servers” quota is not enabled. To enable the quota, contact the support team.

DisasterRecovery
SubscriptionNotFoundComputePoints
Your “Compute points” quota is not enabled. To enable the quota, contact the support team.

DisasterRecovery
SubscriptionNotFoundComputePointsAssigned
Your “Assigned compute points” quota is not enabled. To enable the quota, contact the support team.

DisasterRecovery
SubscriptionNotFoundDrStorage
Your “Disaster recovery storage” quota is not enabled. To enable the quota, contact the support team.

DisasterRecovery
SubscriptionNotFoundInternetAccess
Your “Internet access” quota is not enabled. To enable the quota, contact the support team.

DisasterRecovery
SubscriptionNotFoundPublicIp
Your “Public IP addresses” quota is not enabled. To enable the quota, contact the support team.

DisasterRecovery
TenantHasServers
You cannot delete the DR site because there are cloud servers on it.

DisasterRecovery
TooManyRequests
Service is not able to process the request due to high load at the moment. Please try again after {{retry_after}} seconds.

DisasterRecovery
Unauthorized
Unauthorized. Invalid or missing authorization header.

DisasterRecovery
VPNGatewayUnreachable
VPN gateway error. This might happen when the last report from the VPN gateway was received too long ago or if the VPN gateway reported an error.

DisasterRecovery
VPNIPSecConnectionError
At least one of the IPSec tunnels could not be established.

DisasterRecovery
VPNIPSecNotConfigured
No IPSec tunnels are configured for the DR site with IPSec VPN connectivity.

DisasterRecovery
VPNS2SApplianceNotRegistered
No VPN appliance is registered for the DR site with Site-to-Site VPN connectivity.

DisasterRecovery
VPNS2SApplianceUnreachable
VPN appliance error. This might happen when the last report from the VPN appliance was received too long ago or if the VPN appliance reported an error.

DisasterRecovery
VPNS2SConnectionFailure
The VPN tunnel between the VPN gateway and the VPN appliance cannot be established for the DR site with Site-to-Site VPN connectivity.