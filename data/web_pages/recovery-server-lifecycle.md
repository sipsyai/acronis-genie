# Recovery Server Lifecycle

Recovery server lifecycle

On the diagram below, you can see a recovery server lifecycle, which shows server permanent states and transitional states. Each block shows a recovery server state, a corresponding virtual machine state, and the actions that are available to a user at this stage. Each arrow is an event or user action that leads to the next state.

Failover and failback workflow
User action: Create a recovery server for the selected machine to be protected.
Standby state. The recovery server configuration is defined, but the corresponding virtual machine is not ready.
User action: The failover is initiated in the production mode and the recovery server is being created from the selected recovery point.
Finalization state. Virtual machine disks are finalized from the mounted recovery point to the high-performance storage. The recovery server is operational, though its performance is lower than normal until finalization is completed.
Event: Finalization is successful.
Failover state. The workload is switched from the original machine to the recovery server.

User actions:

Initiate a failback. As a result, the recovery server is turned off and backed up to the cloud storage.

OR

If a user cancels the failover, then the workload is switched back to the original machine and the recovery server returns back to the Standby state.
Ready for failback state. The recovery server backup is created. You must recover your local server from this backup by using the regular recovery process.

User actions:

Confirm failback. As a result, cloud resources that were allocated to the recovery server are released.

OR

Cancel failback. The failback is canceled by your request. The recovery server returns to the Failover state.
Test failover workflow
User action: Create a recovery server for the selected machine to be protected.
Standby state. The recovery server configuration is defined, but the respective virtual machine is not ready.
User action: Start testing the failover.
Testing failover state. In this state, a temporary virtual machine is created for testing purposes.
User action: Stop testing the failover.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.