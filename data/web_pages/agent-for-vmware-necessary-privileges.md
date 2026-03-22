# Required privileges for Agent for VMware

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Required privileges for Agent for VMware
Required privileges for Agent for VMware
To enable backups of virtual machines, install vStorage APIs on the ESXi host. For more information, see this knowledge base article.

Agent for VMware authenticates to vCenter or the ESXi host by a user account that is specified during the agent deployment. The user account must have a role that includes the privileges listed in the table below. We recommend that you use a dedicated account and role, instead of using an existing account that has the Administrator role.

The user account must be granted permission to access all levels of the vSphere infrastructure, such as vCenter, datacenters, clusters, ESXi hosts, resource pools, and virtual machines. To learn how to add a permission on the vCenter level and propagate it to the other levels, see Granting access permission to the user account.

You can change the user account that is used by Agent for VMware without redeploying the agent. To learn how to change the account, see Changing the user account for Agent for VMware.

Object	Privilege	Operation
Back up a VM	Recover to a new VM	Recover to an existing VM	Run VM from backup


Cryptographic operations

(starting with vSphere 6.5)




Add disk



+*




Direct Access



+*




Datastore




Allocate space



+



+



+




Browse datastore



+




Configure datastore



+



+



+



+




Low level file operations



+




Global




Disable methods



+



+



+




Enable methods



+



+



+




Licenses



+



+



+



+




Manage custom attributes



+



+



+




Set custom attribute



+



+



+




Host > Configuration




Storage partition configuration



+


Modify cluster


Host > Local operations




Create virtual machine



+




Delete virtual machine



+




Reconfigure virtual machine



+




Network




Assign network



+



+



+




Resource




Assign virtual machine to resource pool



+



+



+




Virtual machine > Change Configuration




Acquire disk lease



+



+




Add existing disk



+



+



+




Add new disk



+



+



+




Add or remove device



+



+




Advanced configuration



+



+



+




Change CPU count



+




Change Memory



+




Change Settings



+



+



+


Change resource	+	+
Modify device settings	+	+


Remove disk



+



+



+



+




Rename



+




Set annotation



+




Toggle disk change tracking



+



+




Virtual machine > Guest operations




Guest operation modifications



+**




Guest Operation program execution



+**




Guest operation queries



+**




Virtual machine > Interaction




Acquire guest control ticket (in vSphere 4.1 and 5.0)



+




Configure CD media



+



+




Guest operating system management by VIX API (in vSphere 5.1 and later)



+




Power off



+



+




Power on



+



+



+




Virtual machine > Inventory




Create from existing



+



+



+




Create new



+



+



+




Register



+




Remove



+



+



+




Unregister



+




Virtual machine > Provisioning




Allow disk access



+



+



+




Allow read-only disk access



+



+




Allow virtual machine download



+



+



+



+




Virtual machine > State

Virtual machine > Snapshot management (vSphere 6.5 and later)




Create snapshot



+



+



+




Remove snapshot



+



+



+




vApp




Add virtual machine



+

* This privilege is required only for backing up encrypted machines.

** This privilege is required only for application-aware backups.

Granting access permission to the user account

Changing the user account for Agent for VMware

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.