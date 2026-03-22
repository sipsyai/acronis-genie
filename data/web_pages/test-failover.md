# Test failover

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failover > Test failover
Test failover

Performing a test failover means starting a recovery server in a test VLAN that is isolated from your production network. You can test several recovery servers at a time and check their interaction. In the test network, the servers communicate using their production IP addresses, but they cannot initiate TCP or UDP connections to the workloads in your local network.

During test failover, the virtual machine (recovery server) is not finalized. The agent reads the content of the virtual disks directly from the backup and randomly accesses different parts of the backup. This might make the performance of the recovery server in the test failover state slower than its normal performance.

Performing a test failover




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.