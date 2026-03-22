# Replication of virtual machines

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Replication of virtual machines
Replication of virtual machines

Replication is available only for VMware ESXi virtual machines.

Replication is the process of creating an exact copy (replica) of a virtual machine, and then maintaining the replica in sync with the original machine. By replicating a critical virtual machine, you will always have a copy of this machine in a ready-to-start state.

The replication can be started manually or on the schedule you specify. The first replication is full (copies the entire machine). All subsequent replications are incremental and are performed with Changed Block Tracking, unless this option is disabled.

Replication vs. backing up

Unlike scheduled backups, a replica keeps only the latest state of the virtual machine. A replica consumes datastore space, while backups can be kept on a cheaper storage.

However, powering on a replica is much faster than a recovery and faster than running a virtual machine from a backup. When powered on, a replica works faster than a VM running from a backup and does not load the Agent for VMware.

Usage examples

Replicate virtual machines to a remote site.

Replication enables you to withstand partial or complete datacenter failures, by cloning the virtual machines from a primary site to a secondary site. The secondary site is usually located in a remote facility that is unlikely to be affected by environmental, infrastructure, or other factors that might cause the primary site failure.

Replicate virtual machines within a single site (from one host/datastore to another).

Onsite replication can be used for high availability and disaster recovery scenarios.

What you can do with a replica

Test a replica

The replica will be powered on for testing. Use vSphere Client or other tools to check if the replica works correctly. Replication is suspended while testing is in progress.

Failover to a replica

Failover is a transition of the workload from the original virtual machine to its replica. Replication is suspended while a failover is in progress.

Back up the replica

Both backup and replication require access to virtual disks, and thus impact the performance of the host where the virtual machine is running. If you want to have both a replica and backups of a virtual machine, but don't want to put additional load on the production host, replicate the machine to a different host, and set up backups of the replica.

Limitations

The following types of virtual machines cannot be replicated:

Fault-tolerant machines running on ESXi 5.5 and lower.
Machines running from backups.
Replicas of virtual machines.
Some hardware changes, such as adding a network interface card (NIC) to the ESXi host or removing a NIC from it, result in changing the internal IDs of the host. This change affects the VM replication plans. After such a change, you must recreate the VM replication plans in which the ESXi host is selected as a source or target. Otherwise, the VM replication plans will fail.

Creating a replication plan

Testing a replica

Failing over to a replica

Replication options

Failback options

Seeding an initial replica

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.