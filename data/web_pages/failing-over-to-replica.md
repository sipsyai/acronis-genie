# Failing over to a replica

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Failing over to a replica
Failing over to a replica

To failover a machine to a replica

Select a replica to failover to.
Click Replica actions.
Click Failover.
Select whether to connect the powered-on replica to a network. By default, the replica will be connected to the same network as the original machine.
[Optional] If you chose to connect the replica to the network, clear the Stop original virtual machine check box to keep the original machine online.
Click Start.

While the replica is in a failover state, you can choose one of the following actions:

Stop failover

Stop failover if the original machine was fixed. The replica will be powered off. Replication will be resumed.

Perform permanent failover to the replica

This instant operation removes the 'replica' flag from the virtual machine, so that replication to it is no longer possible. If you want to resume replication, edit the replication plan to select this machine as a source.

Failback

Perform failback if you failed over to the site that is not intended for continuous operations. The replica will be recovered to the original or a new virtual machine. Once the recovery to the original machine is complete, it is powered on and replication is resumed. If you choose to recover to a new machine, edit the replication plan to select this machine as a source.

Stopping failover

Performing a permanent failover

Failing back

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.