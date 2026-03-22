# Response actions for individual cyber kill chain nodes

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Response actions for individual cyber kill chain nodes
Response actions for individual cyber kill chain nodes

If you need to manage the incident in more granular detail, you can apply various response actions to individual cyber kill chain nodes. These response actions enable you to quickly and easily remediate any node.

To apply global response actions to an entire incident, see Remediate an entire incident.

Response actions are divided into the following categories, although not all nodes include all of the following categories:

Remediate: Actions in this category enable you to apply an immediate response to the attack, and include managing network isolation for a workload, and the deletion and quarantining of files, processes, and registry values.
Investigate: Actions in this category (applicable to workloads only) enable you to run a forensic backup, remote desktop connection, or remote command line or Terminal for a more in-depth investigation.
Recovery: Actions in this category (applicable to workloads only) enable you to respond to intensive attacks by running a recovery from backup, or Disaster Recovery failover.
Prevent: Actions in this category enable you to prevent future threats or false positives by adding them to a protection plan allowlist or blocklist.
If an incident is closed, you cannot apply a response action to a node. However, you can reopen a closed incident by changing its investigation state to Investigating. When reopened, you can then apply response actions.

The following table describes each of the node types in the cyber kill chain, the applicable categories for each node, and the response actions available.

Node	Category	Response Actions
Workload	Remediate
Manage network isolation
Restart workload

Investigate
Forensic backup
Remote desktop connection
Run remote command line (Windows)
Run Terminal (macOS)

Recovery
Recovery from backup
Disaster Recovery failover

Prevent
Patch

Process	Remediate
Stop process
Quarantine

Prevent
Add to allowlist
Add to blocklist

File	Remediate
Delete
Quarantine

Prevent
Add to allowlist
Add to blocklist

Registry	Remediate
Delete

Network	Prevent
Add to allowlist
Add to blocklist

Define response actions for an affected workload

Manage the network isolation of a workload

Patch a workload

Restart a workload

Run an on-demand forensic backup on a workload

Remote connection to a workload

Running the remote command line

Recovery from backup

Disaster Recovery failover

Define response actions for a suspicious process

Define response actions for a suspicious file

Define response actions for a suspicious registry entry

Add or remove a process, file or network in the protection plan blocklist or allowlist

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.