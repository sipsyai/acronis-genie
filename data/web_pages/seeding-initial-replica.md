# Seeding an initial replica

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Seeding an initial replica
Seeding an initial replica

To speed up replication to a remote location and save network bandwidth, you can perform replica seeding.

To perform replica seeding, Agent for VMware (Virtual Appliance) must be running on the target ESXi.

To seed an initial replica

Do one of the following:

If the original virtual machine can be powered off, power it off, and then skip to step 4.
If the original virtual machine cannot be powered off, continue to the next step.

Create a replication plan.

When creating the plan, in Target machine, select New replica and the ESXi that hosts the original machine.

Run the plan once.

A replica is created on the original ESXi.

Export the virtual machine (or the replica) files to an external hard drive.

Connect the external hard drive to the machine where vSphere Client is running.
Connect vSphere Client to the original vCenter\ESXi.
Select the newly created replica in the inventory.
Click File > Export > Export OVF template.
In Directory, specify the folder on the external hard drive.
Click OK.
Transfer the hard drive to the remote location.

Import the replica to the target ESXi.

Connect the external hard drive to the machine where vSphere Client is running.
Connect vSphere Client to the target vCenter\ESXi.
Click File > Deploy OVF template.
In Deploy from a file or URL, specify the template that you exported in step 4.
Complete the import procedure.
Edit the replication plan that you created in step 2. In Target machine, select Existing replica, and then select the imported replica.

As a result, the software will continue updating the replica. All replications will be incremental.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.