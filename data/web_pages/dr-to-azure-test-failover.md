# Test failover in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failover in Microsoft Azure > Test failover in Microsoft Azure
Test failover in Microsoft Azure

A test failover is a vital part of the Disaster Recovery as a Service (DRaaS) strategy in Microsoft Azure. It enables organizations to validate recovery processes without affecting production environments. This is done by simulating the recovery of a virtual machine (VM) from a selected recovery point (backup). The process creates a temporary VM in an isolated Azure virtual network (VNet) to test recovery procedures, configurations, and applications functionality. Although they are optional, regular test failovers are highly recommended to ensure reliable and up-to-date recovery processes. You can establish a testing schedule that is based on your organization's cost and safety requirements.

You can test several recovery servers at a time and check their interaction. In the test network, the servers communicate using their production IP addresses, but they cannot initiate TCP or UDP connections to the workloads in your local network.

Test recovery network

To ensure that a test failover does not interfere with production operations, configure an isolated virtual network (VNet) in Azure for testing purposes. Confirm that the test VNet does not have routing or peering connections to the production VNet. Test the connectivity from a virtual machine in the test VNet to ensure that it cannot access production resources.

Test failover process

The test failover process consists of the following phases.

Initiation

During this phase, you select a recovery point and start the test failover.

Worker (temporary agent) deployment

During this phase, a worker that is used for the test failover operation is automatically deployed. The initial deployment of the worker for a test or production failover may take several minutes. Starting workers for subsequent failovers should be faster.

Data restoration

During this phase, data is copied from the backup storage to a temporary Azure Blob Storage container. The time that it takes to copy or restore data depends on the workload size. After the data is copied, the Azure Blob Storage content is converted into a managed disk, which is then used to start the temporary VM.

Recovery VM creation

The recovery VM is connected to the preconfigured isolated Azure VNet and subnet. By default, the VM is assigned an IP address where the last octet matches the original machine's IP address. You can modify the IP address before test failover in the recovery server's setting. During the test failover, you can do it directly in the Azure portal.

Ensure the the VNet is isolated from the production network to prevent unintended interactions.

Verification

After the VM is created, clicking the Connect button will redirect you to the specific VM in the Azure portal.

Perform all necessary tests to verify application behavior, connectivity, and recovery objectives in the isolated environment.

The test failover does not overwrite existing recovery points, thus ensuring that your backups remain intact.

Stopping the test failover

Stopping the test failover deletes the temporary VM and associated resources and the worker. If an encryption password was used, it is automatically deleted from the credential store upon stopping or completing the test failover.

You can stop the test failover at any time from the Azure portal.

Performing a test failover in Microsoft Azure

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.