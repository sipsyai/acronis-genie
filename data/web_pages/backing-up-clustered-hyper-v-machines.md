# Backing up clustered Hyper-V machines

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Backing up clustered Hyper-V machines
Backing up clustered Hyper-V machines

In a Hyper-V cluster, virtual machines may migrate between cluster nodes. Follow these recommendations to set up a correct backup of clustered Hyper-V machines:

A machine must be available for backup no matter what node it migrates to. To ensure that Agent for Hyper-V can access a machine on any node, the agent service must run under a domain user account that has administrative privileges on each of the cluster nodes.

We recommend that you specify such an account for the agent service during the Agent for Hyper-V installation.

Install Agent for Hyper-V on each node of the cluster.
Register all of the agents in the Cyber Protection service.
High Availability of a recovered machine

When you recover backed-up disks to an existing Hyper-V virtual machine, the machine's High Availability property remains as is.

When you recover backed-up disks to a new Hyper-V virtual machine, the resulting machine is not highly available. It is considered as a spare machine and is normally powered off. If you need to use the machine in the production environment, you can configure it for High Availability from the Failover Cluster Management snap-in.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.