# Protecting Database Availability Groups (DAG)

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Database backup > Protecting Database Availability Groups (DAG)
Protecting Database Availability Groups (DAG)
Exchange Server clusters overview

The main idea of Exchange clusters is to provide high database availability with fast failover and no data loss. Usually, it is achieved by having one or more copies of databases or storage groups on the members of the cluster (cluster nodes). If the cluster node hosting the active database copy or the active database copy itself fails, the other node hosting the passive copy automatically takes over the operations of the failed node and provides access to Exchange services with minimal downtime. Thus, the clusters are already serving as a disaster recovery solution themselves.

However, there might be cases when failover cluster solutions cannot provide data protection: for example, in case of a database logical corruption, or when a particular database in a cluster has no copy (replica), or when the entire cluster is down. Also cluster solutions do not protect from harmful content changes, as they usually immediately replicate to all cluster nodes.

Cluster-aware backup

With cluster-aware backup, you back up only one copy of the clustered data. If the data changes its location within the cluster (due to a switchover or a failover), the software will track all relocations of this data and safely back it up.

Supported cluster configurations

Cluster-aware backup is supported only for Database Availability Group (DAG) in Exchange Server 2010 or later. Other cluster configurations, such as Single Copy Cluster (SCC) and Cluster Continuous Replication (CCR) for Exchange 2007, are not supported.

DAG is a group of up to 16 Exchange Mailbox servers. Any node can host a copy of mailbox database from any other node. Each node can host passive and active database copies. Up to 16 copies of each database can be created.

How many agents are required for cluster-aware backup and recovery?

For successful backup and recovery of clustered databases, Agent for Exchange has to be installed on each node of the Exchange cluster.

After you install the agent on one of the nodes, the Cyber Protect console displays the DAG and its nodes under Devices > Microsoft Exchange > Databases. To install Agents for Exchange on the rest of the nodes, select the DAG, click Details, and then click Install agent next to each of the nodes.

Backing up the Exchange cluster data
When creating a protection plan, select the DAG as described in Selecting Exchange Server data.
Configure the Cluster backup mode backup option.
Specify other settings of the protection plan as appropriate.

For cluster-aware backup, ensure to select the DAG itself. If you select individual nodes or databases inside the DAG, only the selected items will be backed up and the Cluster backup mode option will be ignored.

Recovering the Exchange cluster data

Select the recovery point for the database that you want to recover. Selecting an entire cluster for recovery is not possible.

When you select a copy of a clustered database under Devices > Microsoft Exchange > Databases > <cluster name> > <node name> and click Recover, the software shows only the recovery points that correspond to the times when this copy was backed up.

The easiest way to view all recovery points of a clustered database is to select its backup on the Backup storage tab.

Follow the steps described in Recovering Exchange databases, starting from step 5.

The software automatically defines a cluster node to which the data will be recovered. The node's name is displayed in the Recover to field. You can manually change the target node.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.